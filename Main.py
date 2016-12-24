from tkinter import *


def make_table(column,row,root):
    root.destroy()
    rows = []
    for i in range(row):
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


    def onPress():
        for row in rows:
            for col in row:
                print(col.get(), )
            print()


    Button(text='Fetch', command=onPress).grid()
    mainloop()

if __name__ == '__main__':
    root = Tk()
    frame = Frame(root)
    frame.pack()
    labelDir = Label(frame, text='Columns')
    labelDir.pack(side="left")
    coulmn_num = Entry(frame, width=5)
    coulmn_num.pack(side="left")
    labelDir1 = Label(frame, text='Rows')
    labelDir1.pack(side="left")
    row_num = Entry(frame, width=5)
    row_num.pack(side="left")
    frame1 = Frame(root)
    labelDir1 = Label(frame1, text='Set States Automatically')
    labelDir1.pack(side="right")
    automate_state = Checkbutton(frame1)
    automate_state.pack(side="right")
    frame1.pack()
    MakeTableButton =Button(root, text="Make Table", command = lambda : make_table(int(coulmn_num.get())+1, int(row_num.get())+1, root))
    MakeTableButton.pack()
    mainloop()
