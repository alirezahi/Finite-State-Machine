from tkinter import *
from Tree import AVL
from graphviz import Digraph

def make_table(column,root):
    root.destroy()
    rows = []
    for i in range(column):
        cols = []
        for j in range(column):
            e = Entry(relief=RIDGE, width=5)
            e.grid(row=i, column=j, sticky=NSEW)
            # e.insert(END, '%d.%d' % (i, j))
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

    def onPress():
        w=0
        visited = [0]*(rows.__len__()-1)
        table_trees = []
        for row in rows[1:]:
            dot.node(w.__str__(), row[0].get())
            row_trees=[]
            z=0
            for col in row[1:]:
                new_tree = AVL()
                for entry in col.get().split(','):
                    if not entry=='' and not entry=='-':
                        dot.edge(w.__str__(), z.__str__(), label=entry)
                        new_tree.add(entry.strip())
                row_trees.append(new_tree)
                z = z + 1
            table_trees.append(row_trees)
            w = w+1
        dot.render('test-output/round-table.gv', view=True)
        current_state = 0
        current_states = []
        current_states.append(current_state)
        for i in 'ab':
            new_current_states = []
            for cur_state in current_states:
                z = 0
                for j in table_trees[cur_state]:
                    if j.get(i)and z not in new_current_states:
                        new_current_states.append(z)
                    z = z+1
            current_states = new_current_states
        print(current_states)
        def DFS(node=0):
            visited[node]=1
            z=0
            for i in table_trees[node]:
                if i.root:
                    if visited[z]==1:
                        return True
                    elif visited[z] != 2:
                        if DFS(z):
                            return True
                z = z+1
            visited[node] = 2





    # dot.edges(['AB','AA','BB','CC','BA', 'CB','BC','DB','EB','BD','BE'])
    # dot.edge('A', 'B', label='001XX')
    # print(dot.source)

    Label(text='Initial State : ', width=10).grid(row=rows.__len__(), column=0)
    initial_state = Entry(relief=RIDGE, width=5)
    initial_state.grid(row=rows.__len__(), column=1)
    Label(text='Final States : ',width=10).grid(row=rows.__len__()+1,column=0)
    final_states = Entry(relief=RIDGE, width=5)
    final_states.grid(row=rows.__len__()+1,column=1)
    Button(text='Fetch', command=onPress).grid()
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
    labelDir1 = Label(frame1, text='Set States Automatically')
    labelDir1.pack(side="right")
    automate_state = Checkbutton(frame1)
    automate_state.pack(side="right")
    frame1.pack()
    MakeTableButton =Button(root, text="Make Table", command = lambda : make_table(int(coulmn_num.get())+1, root))
    MakeTableButton.pack()
    mainloop()
