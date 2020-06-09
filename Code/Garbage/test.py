from tkinter import *
from tkinter import messagebox


def createselect():
    select = Toplevel()

    POC = IntVar()
    POC.set(0)

    pselect = LabelFrame(select, text = 'Select the Player Challanging the word:',pady = 10)
    pselect.grid(row =1, column = 1, padx = 10, rowspan = 3, columnspan = 3, sticky = W+E)

    Radiobutton(pselect, text = 'Player 1', variable = POC, value = 1).grid(row = 1, column = 1)
    Radiobutton(pselect, text = 'Player 2', variable = POC, value = 2).grid(row = 2, column = 1)
    Radiobutton(pselect, text = 'Player 3', variable = POC, value = 3).grid(row = 3, column = 1)
    Radiobutton(pselect, text = 'Player 4', variable = POC, value = 4).grid(row = 4, column = 1)

    done = Button(select, text = 'Done', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white')
    done.grid(row=10, column = 1, padx = 10,pady = 10, sticky = W+E)
    select.mainloop()
