from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import sys
import random
import datetime
import os
from random import shuffle

pname = ['',]
nop = 4

'''
def titlescreen():
    title = Tk()
    title.title('Play Scrabble: Family Edition')
    #title.geometry('400x400')


    frame1 = LabelFrame(title,text = 'Select Number of Players')
    frame1.grid(row=0, column = 1,padx = 10,pady=1015ticky = N+S)

    frame2 = LabelFrame(title,text = 'Name The Players')
    frame2.grid(row=0, column = 10,padx = 10,pady=1015ticky = N+S)

    frame3 = LabelFrame(title,text = 'Select Game Mode')
    frame3.grid(row=1, column = 1,padx = 10,pady=1015ticky = W)

    def func(val):
        if val == 2:
            P3.config(state = DISABLED)
            P4.config(state = DISABLED)
        elif val == 3:
            P3.config(state = NORMAL)
            P4.config(state = DISABLED)
        elif val == 4:
            P3.config(state = NORMAL)
            P4.config(state = NORMAL)    

    def wordfunc(event):
        event.widget.delete(0,END)
        event.widget.focus()

    np = IntVar()
    np.set(2)

    options = [2, 3, 4]
    Label(frame1,text ='Number of Players:').grid(row=1, column = 1, padx=3, pady=1015    drop = OptionMenu(frame1, np, *options, command=func)
    drop.grid(row= 1, column = 2, padx=3, pady=1015
    Label(frame2,text= 'Player 1:').grid(row = 1, column = 3)
    P1 = Entry(frame2,width=10,font = ('DJB Letter Game Tiles' 10))
    P1.grid(row = 1, column = 6,padx = 3, pady = 10
    P1.insert(0, 'Player 1')
    P1.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 2:').grid(row = 2, column = 3)
    P2 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles' 10))
    P2.grid(row = 2, column = 6,padx = 3, pady = 10
    P2.insert(0, 'Player 2')
    P2.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 3:').grid(row = 3, column = 3)
    P3 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles' 10))
    P3.grid(row = 3, column = 6,padx = 3, pady = 10
    P3.insert(0, 'Player 3')
    P3.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 4:').grid(row = 4, column = 3)
    P4 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles' 10))
    P4.grid(row = 4, column = 6,padx = 3, pady = 10
    P4.insert(0, 'Player 4')
    P4.bind("<Button-1>",wordfunc)

    P3.config(state = DISABLED)
    P4.config(state = DISABLED)

    def pracfunc(val):
        if val == 1:
            np.set(2)
            drop.config(state = NORMAL)
            P2.config(state = NORMAL)
            P3.config(state = DISABLED)
            P4.config(state = DISABLED)

        elif val == 2:
            np.set(1)
            drop.config(state = DISABLED)
            P2.config(state = DISABLED)
            P3.config(state = DISABLED)
            P4.config(state = DISABLED)

    mode = IntVar()
    mode.set(1)
    Radiobutton(frame3, text = 'Original', variable = mode, value = 1,command = lambda :pracfunc(mode.get())).grid(row= 0, column= 0)
    Radiobutton(frame3, text = 'Practice', variable = mode, value = 2, command = lambda :pracfunc(mode.get())).grid(row= 0, column= 2)
    Radiobutton(frame3, text = 'Arcade', state = DISABLED, variable = mode, value = 3).grid(row= 0, column= 3)

    def startfunc(np, one, two, three, four): 
        global nop, pname
        #print(np, one, two, three, four,sep = '\n')

        if np == 1:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            nop = np
            pname.append(one)

        elif np == 2:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Sahi name likho')
                return
            nop = np
            pname.append(one)
            pname.append(two)

        elif np == 3:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Sahi name likho')
                return
            if three == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 3: Sahi name likho')
                return
            nop = np
            pname.append(one)
            pname.append(two)
            pname.append(three)

        elif np == 4:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Sahi name likho')
                return
            if three == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 3: Sahi name likho')
                return
            if four == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 4: Sahi name likho')
                return
            nop = np
            pname.append(one)
            pname.append(two)
            pname.append(three)
            pname.append(four)
            
        title.quit()


    Button(title, text = 'On-Screen Keyboard',height = 2, width = 17, borderwidth = 3, bg = 'white', fg = 'black').place(x = 294, y = 170)
    Button(title, text = 'Start Game',height = 2, width = 10, borderwidth = 3, bg = 'white', fg = 'black',command = lambda: startfunc(np.get(),P1.get(),P2.get(),P3.get(),P4.get())).place(x = 430, y = 170)


    title.mainloop()


titlescreen()
'''
def home():
    home = Tk()
    home.title('Play Scrabble: Family Edition')

    start = Button(home, text = 'New Game',height = 3,  width = 20, borderwidth = 10, bg = 'white', fg = 'black',command = titlescreen)
    start.grid(row = 0, column = 0, padx = 100, pady = 10, sticky = E+W)

    start = Button(home, text = 'Continue Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    start.grid(row = 1, column = 0, padx = 100, pady = 10)

    hs = Button(home, text = 'Hight Score',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    hs.grid(row = 2, column = 0, padx = 100, pady = 10)

    ins = Button(home, text = 'Instructions',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    ins.grid(row = 3, column = 0, padx = 100, pady = 10)

    quitbut = Button(home, text = 'Quit Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black')
    quitbut.grid(row = 4, column = 0, padx = 100, pady = 10)
    home.mainloop()

home()