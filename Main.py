from tkinter import *
from Tree import AVL
from graphviz import Digraph

def make_table(column,root):
    o =0
    root.destroy()
    table_trees = []
    rows = []
    f_states_list = []
    current_state = 0
    current_states = []
    for i in range(column):
        cols = []
        for j in range(column):
            e = Entry(relief=RIDGE, width=5)
            e.grid(row=i, column=j, sticky=NSEW)
            if i == j and i == 0:
                e.delete(0, END)
                e.insert(END, 'States')
                e.config(state=DISABLED)
            elif i == 0:
                e.insert(END,j-1)
            elif j == 0:
                e.insert(END,i-1)
            cols.append(e)
        rows.append(cols)
    dot = Digraph(comment='The Round Table')

    def new_graph():
        global dot
        dot = Digraph(comment='The Round Table')
        w=0
        for row in table_trees:
            dot.node(w.__str__(), w.__str__(),shape = 'doublecircle')
            z = 0
            for vertix in row:
                def draw_ver(node_to_draw):
                    if node_to_draw:
                        dot.edge(w.__str__(), z.__str__(), label=node_to_draw.word)
                        draw_ver(node_to_draw.leftChild)
                        draw_ver(node_to_draw.rightChild)
                draw_ver(vertix.root)
                z = z + 1
            w = w+1
        dot.render('test-output/round-table.gv', view=True)

    def check_string(inputString,label):
        global current_states
        current_states = []
        current_state = int(initial_state.get())
        print(current_state.__str__() + ' cur_state')
        current_states.append(current_state)
        for i in inputString:
            new_current_states = []
            for cur_state in current_states:
                z = 0
                for j in table_trees[cur_state]:
                    if j.get(i) and z not in new_current_states:
                        new_current_states.append(z)
                    z = z + 1
            current_states = new_current_states
        for final_state in new_current_states:
            if final_state.__str__() in f_states_list:
                label.config(text='True')
                return True
        label.config(text='False')
        return False

    visited = [0] * (rows.__len__() - 1)
    def DFS(node):
        visited[node] = 1
        z = 0
        for i in table_trees[node]:
            if i.root:
                if visited[z] == 1:
                    print('true')
                    return True
                elif visited[z] != 2:
                    if DFS(z):
                        print('true')
                        return True
            z = z + 1
        visited[node] = 2

    def cycle_DFS(node, j=[]):
        visited[node] = 1
        z = 0
        for i in table_trees[node]:
            if i.root:
                if visited[z] == 1:
                    table_trees[node][z].root = None
                elif visited[z] == 0:
                    j.append([node, z])
                    cycle_DFS(node=z, j=j)
            z = z + 1
        visited[node] = 2
    def onPress():
        global current_state
        current_state = int(initial_state.get())
        global dot
        dot = Digraph(comment='The Round Table')
        w=0
        visited = [0]*(rows.__len__()-1)
        for row in rows[1:]:
            dot.node(w.__str__(), row[0].get())
            row_trees=[]
            z=0
            for col in row[1:]:
                row_trees.append(AVL())
                for entry in col.get().split(','):
                    if not entry=='' and not entry=='-':
                        dot.edge(w.__str__(), z.__str__(), label=entry)
                        row_trees[-1].add(entry.strip())
                z = z + 1
            table_trees.append(row_trees)
            w = w+1
        dot.render('test-output/round-table.gv',view=True)

        def make_initial_visited():
            for i in range(visited.__len__()):
                visited[i] = 0

        for final_state in final_states.get().split(','):
            f_states_list.append(final_state)


    def check_dfs(label , initial):
        if DFS(node=initial):
            label.config(text='True')
        else:
            label.config(text='False')

    def cycle_remove(initial):
        cycle_DFS(node = initial)
        new_graph()

    def ADJ():
        result_string = ''
        for row in rows[1:]:
            result_string = result_string + row[0].get() + ' : '
            z = 0
            for col in row[1:]:
                for entry in col.get().split(','):
                    if not entry == '' and not entry == '-':
                        result_string = result_string + '('+ z.__str__()+' , '+entry+') '
                z = z + 1
            result_string = result_string + '\n'
        print(result_string)

    Label(text='Initial State : ', width=10).grid(row=rows.__len__(), column=0)
    initial_state = Entry(relief=RIDGE, width=5)
    initial_state.grid(row=rows.__len__(), column=1)
    Label(text='Final States : ',width=10).grid(row=rows.__len__()+1,column=0)
    final_states = Entry(relief=RIDGE, width=5)
    final_states.grid(row=rows.__len__()+1,column=1)
    Button(text='Make Graph', command=onPress).grid(row=rows.__len__()+2,column=0)
    cycle = Label(text='cycle')
    Button(text='Adj', command=lambda : ADJ()).grid(row=rows.__len__()+2,column=1)
    Button(text='Cycle', command=lambda : check_dfs(cycle,int(initial_state.get()))).grid(row=rows.__len__()+2,column=2)
    Button(text='unDFS', command=lambda : cycle_remove(int(initial_state.get()))).grid(row=rows.__len__()+2,column=3)
    cycle.grid(row=rows.__len__()+2,column=4)
    # Button(text='Show', command=show).grid(row=rows.__len__() + 2, column=1)
    string_checking = Entry(width=5)
    string_checking.grid(row=rows.__len__()+3,column=1)
    string_result = Label(text='Result',width=5)
    string_result.grid(row=rows.__len__() + 3, column=2)
    Button(text='Check Str',width=6,command=lambda :check_string(string_checking.get(),string_result)).grid(row=rows.__len__()+3,column=0)
    mainloop()

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root)
    frame.pack()
    labelDir = Label(frame, text='Num of States : ')
    labelDir.pack(side="left")
    coulmn_num = Entry(frame, width=5)
    coulmn_num.pack(side="left")
    frame1 = Frame(root)
    frame1.pack()
    MakeTableButton =Button(root, text="Make Table", command = lambda : make_table(int(coulmn_num.get())+1, root))
    MakeTableButton.pack()
    mainloop()
