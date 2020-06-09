from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import sys
import random
import datetime
import os
from random import shuffle

pname = ['', ['Player 1', 75], ['Player 2', 26], ['Player 3', 37], ['Player 4', 120]]

def finish():
    global pname, TNOT, bag
    winner = Tk()
    pname.pop(0)
    for i in range(1, len(pname)): 
        key = pname[i]
        j = i-1
        while j >=0 and key[1] > pname[j][1] : 
                pname[j+1] = pname[j] 
                j -= 1
        pname[j+1] = key
    print(pname)

    leader = LabelFrame(winner, text = 'LeaderBoard:')
    leader.grid(row = 1, column = 1,padx = 10, pady = 10,sticky = W+E)
    for x in range(len(pname)):
        Label(leader, text = str(x+1)+'.     '+pname[x][0]+':   '+str(pname[x][1])).grid(row = x,padx = 10, pady = 3, column = 1,sticky = W+E)

    stats = LabelFrame(winner, text= 'Statistics:')
    leader.grid(row = 1, column = 5,padx = 10, pady = 10,sticky = W+E)
    Label(stats, text= 'No. of Turns Played: '+str(TNOT)).grid(row = 1,padx = 10, pady = 3, column = 1,sticky = W+E)
    Label(stats, text= 'No. of Titles Played: '+str(100-len(bag))).grid(row = 2,padx = 10, pady = 3, column = 1,sticky = W+E)

    winner.mainloop()
finish()
