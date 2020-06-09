from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import sys
import random
import datetime
import os
from random import shuffle
from pynput.keyboard import Key, Controller


Tilescore = {"A": 1 , "B": 3 , "C": 3 , "D": 2 ,
         "E": 1 , "F": 4 , "G": 2 , "H": 4 ,
         "I": 1 , "J": 8 , "K": 5 , "L": 1 ,
         "M": 3 , "N": 1 , "O": 1 , "P": 3 ,
         "Q": 10, "R": 1 , "S": 1 , "T": 1 ,
         "U": 1 , "V": 4 , "W": 4 , "X": 8 ,
         "Y": 4 , "Z": 10 , "#": 0}

board = Tk()
POC = IntVar()
counter = 1
TNOT = 0
nop = 4
skip = 0
crossflag = 'True'
racktemp = []
tword = []
blank = []
pname = ['',]
tempscore = 0
dw = 0
tw = 0
dl = []
tl = []
maxscore = [-1,""]

keyboard=Controller()

#Changing Titlename and logo:
board.iconbitmap('Scrabble logo.ico')
board.title('Play Scrabble: Family Edition')
board.state('zoomed')

'''
w, h = board.winfo_screenwidth(), board.winfo_screenheight()
can = Canvas(board, width= 1300, height= 750)
my_img = ImageTk.PhotoImage(Image.open('back.png'))
can.create_image(0,0,image= my_img)
can.grid(row = 0,column = 0, rowspan = 500, columnspan = 500)
'''


'''
board.geometry("%dx%d+0+0" % (w, h))
'''
##Function to return details upone clicking a box:
'''
def click(event):
    (x,y) = (event.widget.grid_info()['row'],event.widget.grid_info()['column'])
    if grid[(x,y)].cget('state') != DISABLED:
        t = grid[(x,y)].cget('text')
        grid[(x,y)]['state'] = DISABLED
        grid[(x,y)]['text'] = ':)'
        print('x:',x,'\ny:',y,'\ntext:',t)
    else:
        print('Button Disabled')
'''
##OSK
def open_osk():
    keyboard.press(Key.cmd)
    keyboard.press('r')
    keyboard.release('r')
    keyboard.release(Key.cmd)

    time.sleep(0.5)

    keyboard.press('o')
    keyboard.release('o')
    keyboard.press('s')
    keyboard.release('s')
    keyboard.press('k')
    keyboard.release('k')

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

## Termination of game
def des_func():
    quit_box = messagebox.askyesno('Play Scrabble: Family Edition','Do you want to quit ?')
    if quit_box == 1:
        board.quit()
        board.destroy()
    return

##title screen:
def titlescreen():
    title = Toplevel()
    title.title('Play Scrabble: Family Edition')
    title.iconbitmap('Scrabble logo.ico')
    #title.geometry('400x400')


    frame1 = LabelFrame(title,text = 'Select Number of Players')
    frame1.grid(row=0, column = 1,padx = 10,pady=10,sticky = N+S)

    frame2 = LabelFrame(title,text = 'Name The Players')
    frame2.grid(row=0, column = 10,padx = 10,pady=10,sticky = N+S)

    frame3 = LabelFrame(title,text = 'Select Game Mode')
    frame3.grid(row=1, column = 1,padx = 10,pady=10,sticky = W)

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
    Label(frame1,text ='Number of Players:').grid(row=1, column = 1, padx=5, pady=10)
    drop = OptionMenu(frame1, np, *options, command=func)
    drop.grid(row= 1, column = 2, padx=5, pady=10)

    Label(frame2,text= 'Player 1:').grid(row = 1, column = 5)
    P1 = Entry(frame2,width=10,font = ('DJB Letter Game Tiles',15))
    P1.grid(row = 1, column = 6,padx = 5, pady = 1)
    P1.insert(0, 'Player 1')
    P1.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 2:').grid(row = 2, column = 5)
    P2 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles',15))
    P2.grid(row = 2, column = 6,padx = 5, pady = 1)
    P2.insert(0, 'Player 2')
    P2.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 3:').grid(row = 3, column = 5)
    P3 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles',15))
    P3.grid(row = 3, column = 6,padx = 5, pady = 1)
    P3.insert(0, 'Player 3')
    P3.bind("<Button-1>",wordfunc)

    Label(frame2,text= 'Player 4:').grid(row = 4, column = 5)
    P4 = Entry(frame2,width=10, font = ('DJB Letter Game Tiles',15))
    P4.grid(row = 4, column = 6,padx = 5, pady = 1)
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
        global nop, pname, pscore
        #print(np, one, two, three, four,sep = '\n')
        if np == 1:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            nop = np
            pname.append([one,0])
            #pscore.append(0)

        elif np == 2:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Sahi name likho')
                return
            nop = np
            pname.append([one,0])
            pname.append([two,0])
            #pscore.append(0)
            #pscore.append(0)

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
            pname.append([one,0])
            pname.append([two,0])
            pname.append([three,0])
            #pscore.append(0)
            #pscore.append(0)
            #pscore.append(0)

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
            pname.append([one,0])
            pname.append([two,0])
            pname.append([three,0])
            pname.append([four,0])
            #pscore.append(0)
            #pscore.append(0)
            #pscore.append(0)
            #pscore.append(0)
        
        print(nop, pname,sep = '\n')
        title.quit()
        title.destroy()


    Button(title, text = 'On-Screen Keyboard',height = 2, width = 17, borderwidth = 5, bg = 'white', fg = 'black', command = open_osk).place(x = 294, y = 170)
    Button(title, text = 'Start Game',height = 2, width = 10, borderwidth = 5, bg = 'white', fg = 'black',command = lambda: startfunc(np.get(),P1.get(),P2.get(),P3.get(),P4.get())).place(x = 430, y = 170)
    title.protocol('WM_DELETE_WINDOW', des_func)

    title.mainloop()

def home():
    home = Toplevel()
    global nop, pname
    home.title('Play Scrabble: Family Edition')
    home.iconbitmap('Scrabble logo.ico')

    def call_title():
        titlescreen()
        home.quit()
        home.destroy()

    start = Button(home, text = 'New Game',height = 3,  width = 20, borderwidth = 10, bg = 'white', fg = 'black',command = call_title)
    start.grid(row = 0, column = 0, padx = 100, pady = 10, sticky = E+W)

    con = Button(home, text = 'Continue Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    con.grid(row = 1, column = 0, padx = 100, pady = 10)

    hs = Button(home, text = 'Hight Score',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    hs.grid(row = 2, column = 0, padx = 100, pady = 10)

    ins = Button(home, text = 'Instructions',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    ins.grid(row = 3, column = 0, padx = 100, pady = 10)

    quitbut = Button(home, text = 'Quit Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black')
    quitbut.grid(row = 4, column = 0, padx = 100, pady = 10)
    home.mainloop()

home()

##Creating the Tiles Bag
def generate_bag():
    bag=[]
    for i in range(9):
        bag.append("A")
    for i in range(2):
        bag.append("B")
    for i in range(2):
        bag.append("C")
    for i in range(4):
        bag.append("D")
    for i in range(12):
        bag.append("E")
    for i in range(2):
        bag.append("F")
    for i in range(3):
        bag.append("G")
    for i in range(1):
        bag.append("H")
    for i in range(9):
        bag.append("I")
    for i in range(9):
        bag.append("J")
    for i in range(1):
        bag.append("K")
    for i in range(4):
        bag.append("L")
    for i in range(2):
        bag.append("M")
    for i in range(6):
        bag.append("N")
    for i in range(8):
        bag.append("O")
    for i in range(2):
        bag.append("P")
    for i in range(1):
        bag.append("Q")
    for i in range(6):
        bag.append("R")
    for i in range(4):
        bag.append("S")
    for i in range(6):
        bag.append("T")
    for i in range(4):
        bag.append("U")
    for i in range(2):
        bag.append("V")
    for i in range(2):
        bag.append("W")
    for i in range(1):
        bag.append("X")
    for i in range(2):
        bag.append("Y")
    for i in range(1):
        bag.append("Z")
    for i in range(2):
        bag.append("#")
    shuffle(bag)
    return bag

##Generating Racks of Tiles for Players
def generating_racks(number_of_players,bag):
    players_racks=[]
    for i in range(number_of_players):
        tmp=[]
        for k in range(7):
            tmp.append(bag.pop())
        players_racks.append(tmp)
    return players_racks

bag = generate_bag()
all_tiles = generating_racks(nop,bag)
print(all_tiles)


##Creating Grid/Board:
grid = {}
for x in range (15):
    for y in range(15):
        if (x,y) == (7,7):
            
            but = Button(board, text = 'X',height = 2, width = 5, borderwidth = 5, bg = 'yellow',fg='black')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but
        elif (x,y) == (0,0) or (x,y) == (0,7) or (x,y) == (0,14) or (x,y) == (7,0) or (x,y) == (7,14) or (x,y) == (14,0) or (x,y) == (14,7) or (x,y) == (14,14):
            
            but = Button(board, text = 'TWS',height = 2, width = 5, borderwidth = 5, bg = 'red',fg='white')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but

        elif (x,y) == (1,1) or (x,y) == (2,2) or (x,y) == (3,3) or (x,y) == (4,4) or (x,y) == (10,10) or (x,y) == (11,11) or (x,y) == (12,12) or (x,y) == (13,13) or (x,y) == (1,13) or (x,y) == (2,12) or (x,y) == (3,11) or (x,y) == (4,10) or (x,y) == (10,4) or (x,y) == (11,3) or (x,y) == (12,2) or (x,y) == (13,1):

            but = Button(board, text = 'DWS',height = 2, width = 5, borderwidth = 5, bg = 'grey',fg='white')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but
        
        elif (x,y) == (0,3) or (x,y) == (0,11) or (x,y) == (2,6) or (x,y) == (2,8) or (x,y) == (3,0) or (x,y) == (3,7) or (x,y) == (3,14) or (x,y) == (6,2) or (x,y) == (6,6) or (x,y) == (6,8) or (x,y) == (6,12) or (x,y) == (7,3) or (x,y) == (7,11) or (x,y) == (14,3) or (x,y) == (14,11) or (x,y) == (12,6) or (x,y) == (12,8) or (x,y) == (11,0) or (x,y) == (11,7) or (x,y) == (11,14) or (x,y) == (8,2) or (x,y) == (8,6) or (x,y) == (8,8) or (x,y) == (8,12) :
            but = Button(board, text = 'DLS',height = 2, width = 5, borderwidth = 5, bg = 'blue',fg='white')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but

        elif (x,y) == (1,5) or (x,y) == (1,9) or (x,y) == (5,1) or (x,y) == (5,5) or (x,y) == (5,9) or (x,y) == (5,13) or (x,y) == (13,5) or (x,y) == (13,9) or (x,y) == (9,1) or (x,y) == (9,5) or (x,y) == (9,9) or (x,y) == (9,13):

            but = Button(board, text = 'TLS',height = 2, width = 5, borderwidth = 5, bg = 'green',fg='white')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but

        else:
            but = Button(board, text = '', height = 2, width = 5, borderwidth = 5, bg = '#f2c4b1',fg='white')
            but.grid(row = x+1, column = y)
            grid[(x,y)] = but

##Score Board:
scoreframe = LabelFrame(board, text = 'Score Board:')
scoreframe.grid(row = 1, column = 15,rowspan = 3,columnspan = 3, sticky = W+E, padx = 10)

def scoreboard():
    Player1 = Label(scoreframe, text = pname[1][0]+':   '+str(pname[1][1]))
    Player1.grid(row = 0, column = 0)

    if len(pname) == 3:
        Player2 = Label(scoreframe, text = pname[2][0]+':   '+str(pname[2][1]))
        Player2.grid(row = 1, column = 0)


    if len(pname) == 4:
        Player2 = Label(scoreframe, text = pname[2][0]+':   '+str(pname[2][1]))
        Player2.grid(row = 1, column = 0)

        Player3 = Label(scoreframe, text = pname[3][0]+':   '+ str(pname[3][1]))
        Player3.grid(row = 2, column = 0)

    if len(pname) == 5:
        Player2 = Label(scoreframe, text = pname[2][0]+':   '+str(pname[2][1]))
        Player2.grid(row = 1, column = 0)

        Player3 = Label(scoreframe, text = pname[3][0]+':   '+ str(pname[3][1]))
        Player3.grid(row = 2, column = 0)

        Player4 = Label(scoreframe, text = pname[4][0]+':   '+ str(pname[4][1]))
        Player4.grid(row = 3, column = 0)
scoreboard()

##Radio Buttons for oriantation of words:
def dirbut(value):
    if value == 0:
        messagebox.showerror('Play Scrabble: Family Edition','You didn\'t select any direction.\n Try Again!')
    return value

direction = IntVar()
direction.set(0)

direcframe = LabelFrame(board, text = 'Select Your Prefered Direction:')
direcframe.grid(row = 5,column = 15, rowspan = 2, columnspan = 3, padx = 10, sticky = W+E)

Radiobutton(direcframe, text = 'Downwards', variable = direction, value = 1).grid(row= 0, column= 0)
Radiobutton(direcframe, text = 'Rightwards', variable = direction, value = 2).grid(row= 1, column= 0)


##Time Clock:
start = time.time()
def tick():
    global start
    time2 = time.time()
    rn=round(time2-start,0)
    status.config(text=str(datetime.timedelta(seconds=rn)))
    status.after(200, tick)

status = Label(board, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=16, column=0)
tick()

##Binding Mouse left click to grid dictionary + color preserve:
details = [7,7,grid[(7,7)].cget('text')]
yellow = ['yellow', 'black']
temp = ['white' , 'black']

def click(event):
    global details, yellow, temp
    (x,y) = (event.widget.grid_info()['row']-1,event.widget.grid_info()['column'])
    old= detail_label.cget('text').split()
    #print(old)
    t = grid[(x,y)].cget('text')
    #print('x:',x,'\ny:',y,'\ntext:',t)
    details = [x,y,t]
    grid[(int(old[0]),int(old[1]))]['bg'] = temp[0]
    grid[(int(old[0]),int(old[1]))]['fg'] = temp[1]

    temp[0]= grid[(details[0],details[1])]['bg']
    temp[1] = grid[(details[0],details[1])]['fg']

    grid[(details[0],details[1])]['bg'] = yellow[0]
    grid[(details[0],details[1])]['fg'] = yellow[1]
    detail_func()

    if grid[(x,y)].cget('state') == DISABLED:
        word.insert(END,grid[(x,y)].cget('text'))

    #print(details)

for a in range (15):
    for b in range (15):
        grid[(a,b)].bind("<Button-1>",click)




##Warning Message boxes:
#len_error = messagebox.showerror('Play Scrabble: Family Edition','Your word lenght exceeded the block available.\n Try Again!')
##center_error = messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
##dir_error = messagebox.showerror('Play Scrabble: Family Edition','You didn\'t select any direction.\n Try Again!')
##quit_box = messagebox.askyesno('Play Scrabble: Family Edition','Do you want to quit ?')
#no_word = messagebox.showwarning('Play Scrabble: Family Edition','Your word wasn\'t available in our dictionary.')
#challange_box = messagebox.askyesnocancel('Play Scrabble: Family Edition','Do other player\'s want to challange this word ?')
#Challenge_success= messagebox.askyesno('Play Scrabble: Family Edition','Was challenge successful?')

##Exit Button:
def quit_func():
    quit_box = messagebox.askyesno('Play Scrabble: Family Edition','Do you want to quit ?')
    if quit_box == 1:
        board.quit()
        board.destroy()
    return

def finish(pname):
    global TNOT, bag, maxscore
    board.quit()
    board.destroy()
    winner = Tk()
    winner.title('Play Scrabble: Family Edition')
    winner.iconbitmap('Scrabble logo.ico')
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
    stats.grid(row = 1, column = 5,padx = 10, pady = 10,sticky = W+E)
    Label(stats, text= 'No. of Turns Played: '+str(TNOT)).grid(row = 1,padx = 10, pady = 3, column = 1,sticky = W+E)
    Label(stats, text= 'No. of Titles Left In The Bag: '+str(len(bag))).grid(row = 2,padx = 10, pady = 3, column = 1,sticky = W+E)
    Label(stats, text= 'Highest Score Scored In A Single Turn : '+str(maxscore[0])).grid(row = 3,padx = 10, pady = 3, column = 1,sticky = W+E)
    Label(stats, text= 'Player Who Scored The Highest Scored Turn : '+maxscore[1]).grid(row = 4,padx = 10, pady = 3, column = 1,sticky = W+E)

    declare = LabelFrame(winner, text= 'Winner:')
    declare.grid(row = 3, column = 1,padx = 10, pady = 10,columnspan = 10)
    Label(declare,text = 'The Winner Is: '+pname[0][0]+' By Scoring '+str(pname[0][1])+' Points.\nCongrats!').grid(row = 1,padx = 10, pady = 3, column = 1,sticky = W)
    
    def byes():
        messagebox.showinfo('Play Scrabble: Family Edition','Thank You For Playing Scrabble: Family Edition.\nHope To See You Soon. Good Bye :)')
        winner.quit()
        winner.destroy()

    winner.protocol('WM_DELETE_WINDOW', byes)
    winner.mainloop()

quit_but = Button(board, text = 'End Match', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white', command = lambda: finish(pname))
quit_but.grid(row=15, column = 15, padx = 10, sticky = W+E)
board.protocol('WM_DELETE_WINDOW', quit_func)

##Shuffle Button:
def shuff_func(event = None):
    for x in range(7):
        var = random.randint(0,6)
        tiles[x]['text'],tiles[var]['text'] = tiles[var]['text'],tiles[x]['text']

shuff_but = Button(board, text = 'Shuffle Tray', height = 2, width = 13, borderwidth = 5, command = shuff_func, bg= 'white')
shuff_but.grid(row=14, column = 15, padx = 10, sticky = E)
board.bind('<Control-s>',shuff_func)

##Skip Turn Button and func:
skip_but = Button(board, text = 'Skip Turn' , height = 2, width = 15, borderwidth = 5, bg = 'black',fg='white',command = lambda: change_turn(counter,nop))
skip_but.grid(row=13, column = 15, padx = 10,sticky = E)

##On screen keyboard button
Button(board, text = 'On-Screen Keyboard',height = 2, width = 17, borderwidth = 5, bg = 'white', fg = 'black', command = open_osk).grid(row=14, column = 15, padx = 10,sticky = W)

##Text box for word:
def wordfunc(event):
    word.delete(0,END)
    word.focus()

word = Entry(board,width=8, font = ('DJB Letter Game Tiles',20))
word.insert(0, 'Word Here')
word.grid(row = 7, column = 15,columnspan = 10, sticky = W+E, padx = 10)
word.bind("<Button-1>",wordfunc)
board.bind('<Control-c>',wordfunc)

##Player Tile:
tile_frame = LabelFrame(board, text = 'Player Tiles:')
tile_frame.grid(row= 8, column = 15, padx=10,rowspan = 3, columnspan =3, sticky = W+E)
tiles = {}
'''

for x in range (7):
    if x <=4:
        but = Button(tile_frame, text = ':)', height = 2, width = 5, borderwidth = 5, bg = 'white', fg = 'black')
        but.grid(row = 0, column = x)
        tiles[(x)] = but
    else:
        but = Button(tile_frame, text = ':(', height = 2, width = 5, borderwidth = 5, bg = 'white', fg = 'black')
        but.grid(row = 1, column = x-5)
        tiles[(x)] = but
'''

def tilefunc(event):
    temp = event.widget.cget('text')
    if temp == '#':
        open_osk()
        return
    word.insert(END,temp)
    #print(temp)

def inserting_letters_into_player_tiles(letters_lst):
    global tiles
    y=0
    for x in letters_lst:
        but = Button(tile_frame, text = x, height = 2, width = 5, borderwidth = 5, bg = 'white', fg = 'black')
        if y<=4:
            but.grid(row = 0, column = y)

        else:
            but.grid(row = 1, column = y-5)
        tiles[(y)] = but
        tiles[(y)].bind("<Button-1>",tilefunc)
        y=y+1
    return
inserting_letters_into_player_tiles(all_tiles[0])
#Button(tile_frame, text = 'On-Screen Keyboard', justify="center",height = 2, width = 20, borderwidth = 5, bg = 'white', fg = 'black', command = open_osk).grid(row = 1, column = 2, columnspan = 3)


##Player Turn:
name_frame = LabelFrame(board, text = 'Player To Turn')
name_frame.grid(row = 4,column = 15, columnspan = 3, padx = 10, sticky = W+E)
name_dispaly = Label(name_frame, text = pname[counter][0]+'; It\'s your turn')
name_dispaly.grid(row =0, column = 0,sticky = W)

##Top Bar:
topbar = Menu(board)
board.config(menu = topbar)

file = Menu(topbar,tearoff=0)
topbar.add_cascade(label = 'File', menu = file)
file.add_command(label = 'New Game')
file.add_separator()
file.add_command(label = 'Exit')

helper = Menu(topbar,tearoff=0)
topbar.add_cascade(label = 'Help', menu = helper)
helper.add_command(label = 'Instructions')
helper.add_separator()
helper.add_command(label = 'Contact')


#topbar = Label(board, text='Help', bd=1, relief=SUNKEN, anchor=W)
#topbar.grid(row=0, column=0)

##Submiting Details:
def detail_func():
    detail_label['text'] = details
    detail_label.grid(row = 0, column = 0, sticky = W)
    '''
    global yellow, temp
    temp.append(grid[(details[0],details[1])].cget('bg'))
    temp.append(grid[(details[0],details[1])].cget('fg'))
    grid[(details[0],details[1])]['bg'] = yellow[0]
    grid[(details[0],details[1])]['fg'] = yellow[1]
    '''
    
detail_frame = LabelFrame(board, text = 'Details of Submission:',pady = 10)
detail_frame.grid(row =10, column = 15, padx = 10, rowspan = 3, columnspan = 3, sticky = W+E)
detail_label = Label(detail_frame, text= details)
detail_label.grid(row = 0, column = 0, sticky = W)

detail_label2 = Label(detail_frame, text= '--> This the cell you have selected.')
detail_label2.grid(row = 0, column = 1, sticky = E, padx = 5)
#detail_but = Button(detail_frame,command = detail_func,text = 'Click To Update',height = 2, width = 15 ,borderwidth = 5, bg = 'white', fg = 'black')
#detail_but.grid(row =0, column = 1,sticky = E, columnspan = 4,padx = 10)

#Word listing from dic:
words=[]
f = open('dic.txt', "r")
for line in f:
    words.append(line[0:(len(line)-1)])
f.close()

##Varification of the word consisting of next 2 functions:
def word_challenge(word):
    global words
    if check_word(words, 1, len(words), word):
        return True
    else:
        return False
        
def check_word(arr, l, r, x): 
    while l <= r: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return True 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return False

## Radio Button check
def radio_check(radio,wordlen,x,y):
    radiolen = False
    if radio == 0:
        return False
    elif radio == 1:
        if wordlen <= (15-x):
            radiolen = True
    elif radio == 2:
        if wordlen <= (15-y):
            radiolen = True
    
    if radiolen == False:
        messagebox.showerror('Play Scrabble: Family Edition','Your word lenght exceeded the block available.\n Try Again!')
        return False
    return True

def donebut(radio):
    global POC, pname, counter
    POC = radio

def createselect():
    global counter, pname
    select = Toplevel()

    select.iconbitmap('Scrabble logo.ico')
    select.title('Play Scrabble: Family Edition')

    POCL = IntVar()
    POCL.set(counter+1)
    
    if counter == nop:
        POCL.set(1)

    pselect = LabelFrame(select, text = 'Select the Player Challanging the word:',pady = 10)
    pselect.grid(row =1, column = 1, padx = 10, rowspan = 5, columnspan = 3, sticky = W+E)

    R1 = Radiobutton(pselect, text = 'Player 1', variable = POCL, value = 1, command= lambda: donebut(POCL.get()))
    R1.grid(row = 1, column = 1)

    if len(pname) == 3:
        R2 = Radiobutton(pselect, text = 'Player 2', variable = POCL, value = 2, command= lambda: donebut(POCL.get()))
        R2.grid(row = 2, column = 1)

    if len(pname) == 4:
        R2 = Radiobutton(pselect, text = 'Player 2', variable = POCL, value = 2, command= lambda: donebut(POCL.get()))
        R2.grid(row = 2, column = 1)

        R3 = Radiobutton(pselect, text = 'Player 3', variable = POCL, value = 3, command= lambda: donebut(POCL.get()))
        R3.grid(row = 3, column = 1)

    if len(pname) == 5:
        R2 = Radiobutton(pselect, text = 'Player 2', variable = POCL, value = 2, command= lambda: donebut(POCL.get()))
        R2.grid(row = 2, column = 1)

        R3 = Radiobutton(pselect, text = 'Player 3', variable = POCL, value = 3, command= lambda: donebut(POCL.get()))
        R3.grid(row = 3, column = 1)

        R4 = Radiobutton(pselect, text = 'Player 4', variable = POCL, value = 4, command= lambda: donebut(POCL.get()))
        R4.grid(row = 4, column = 1)

    def closefunc():
        select.quit()
        select.destroy()

    done = Button(select, text = 'Done', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white',command = closefunc)
    done.grid(row=10, column = 1, padx = 10,pady = 10, sticky = W+E)
    
    if counter == 1:
        R1.config(state = DISABLED)
    elif counter == 2:
        R2.config(state = DISABLED)
    elif counter == 3:
        R3.config(state = DISABLED)
    elif counter == 4:
        R4.config(state = DISABLED)

    select.mainloop()

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 

def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def sort_dictionary(words):
    #l=len(words)
    #quickSort(words,0,l-1)
    words.sort()

    #testing
    if os.path.exists("dic.txt"): 
        os.remove("dic.txt") 
    
    file = open("dic.txt", "w")
    for k in words:
        file.write(k+"\n") 
    file.close()
    return words

#words = sort_dictionary(words)

def cross_check(radio, mx, my, w):
    global tword
    x = mx
    y = my
    word = ''
    if radio == 1:
        if y >0:
            while grid[(x,y-1)].cget('state') == DISABLED and y > 0:
                word = grid[(x,y-1)].cget('text') + word
                y = y - 1

        word = word + w
        
        if w == grid[(mx,my)].cget('text') and grid[(mx,my)].cget('state') == DISABLED:
            return 'True'

        y = my
        if y < 14:
            while grid[(x,y+1)].cget('state') == DISABLED and y < 14:
                word = word + grid[(x,y+1)].cget('text')
                y = y + 1

        if len(word) > 1:
            if word_challenge(word) == True:
                print(word)
                scoring(word,counter)
                return 'True'
            else:
                messagebox.showerror('Play Scrabble: Family Edition','Error occured while word crossing.\nAn invalid word was created: '+word+'.')
                return 'Error'

    else:
        ##y axis check
        if x > 0:
            while grid[(x-1,y)].cget('state') == DISABLED and x > 0:
                word = grid[(x-1,y)].cget('text') + word
                x = x - 1
        
        word = word + w

        if w == grid[(mx,my)].cget('text') and grid[(mx,my)].cget('state') == DISABLED:
            return 'True'

        x = mx
        if x < 14:
            while grid[(x+1,y)].cget('state') == DISABLED and x < 14:
                word = word + grid[(x+1,y)].cget('text')
                x = x + 1

        if len(word) > 1:
            if word_challenge(word) == True:
                print(word)
                scoring(word,counter)
                return 'True'
            else:
                messagebox.showerror('Play Scrabble: Family Edition','Error occured while word crossing.\nAn invalid word was created: '+word+'.')
                return 'Error'
    return 'False'

#Submit Button Action:
def Submitfunc():
    global words,TNOT, POC, skip, nop, counter, crossflag, racktemp, dl, dw, tl, tw, blank, tempscore
    wordtemp = []
    racktemp = []
    (s_x,s_y) = (details[0],details[1])
    (x,y)=(s_x,s_y)
    word_main = word.get().upper()
    wordlen = len(word_main)
    radio = dirbut(direction.get())
    
    if radio_check(radio,wordlen,x,y) != True:
        return False

    dic_ans = word_challenge(word_main)
    if dic_ans == False:
        messagebox.showwarning('Play Scrabble: Family Edition','Your word wasn\'t available in our dictionary.')
        challange_box = messagebox.askyesnocancel('Play Scrabble: Family Edition','Do other player\'s want to challange this word ?')
        
        if challange_box == True:
            createselect()
            Challenge_success= messagebox.askyesno('Play Scrabble: Family Edition','Was challenge successful?')
            if Challenge_success == False:
                dic_ans = True
                f = open('dic.txt', "a")
                f.write(word_main.upper())
                words.append(word_main.upper())
                f.close()
                words = sort_dictionary(words)
                skip = POC
                #return change_turn(skip, nop)
                
            
            if Challenge_success == True:
                return change_turn(counter,nop)
        
        if challange_box == False:
            dic_ans = True
            f = open('dic.txt', "a")
            f.write(word_main.upper())
            words.append(word_main.upper())
            f.close()
            words = sort_dictionary(words)

    if dic_ans and radio == 1:
        ##First word center check
        if TNOT == 0:
            if s_x < 7 and s_y == 7:
                if (s_x + wordlen - 1) >= 7:
                    pass
                else:
                    messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                    return False ##error
            elif s_y == s_x == 7:
                pass
            else:
                messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                return False ##error

        for w in word_main:
            tempflag = cross_check(radio, x, y, w) 
            if tempflag == 'True':
                crossflag = 'True'

            elif tempflag == 'Error':
                temprefill(racktemp)
                tempscore = 0
                dw = 0
                tw = 0
                dl = []
                tl = []
                blank = []
                for x in wordtemp:
                    grid[(x[0],x[1])].config(text=x[2])
                    grid[(x[0],x[1])].config(state = NORMAL)
                    if (x[0],x[1]) != (s_x,s_y):
                        grid[(x[0],x[1])].config(bg=x[3])
                        grid[(x[0],x[1])].config(fg=x[4])
                return False
                
            if grid[(x,y)].cget('state') != DISABLED:
                if check_if_word_in_rack(w,counter) == True:
                    wordtemp.append([x,y,grid[(x,y)].cget('text'),grid[(x,y)].cget('bg'),grid[(x,y)].cget('fg')])
                    if grid[(x,y)].cget('text') == 'DWS':
                        dw = dw + 1
                    elif grid[(x,y)].cget('text') == 'TWS':
                        tw = tw + 1
                    elif grid[(x,y)].cget('text') == 'DLS':
                        dl.append(w)
                    elif grid[(x,y)].cget('text') == 'TLS':
                        tl.append(w)
                    grid[(x,y)].config(text=w)
                    grid[(x,y)].config(state= DISABLED)
                else:
                    messagebox.showerror('Play Scrabble: Family Edition','Not in rack')
                    temprefill(racktemp)
                    tempscore = 0
                    dw = 0
                    tw = 0
                    dl = []
                    tl = []
                    blank = []
                    for x in wordtemp:
                        grid[(x[0],x[1])].config(text=x[2])
                        grid[(x[0],x[1])].config(state = NORMAL)
                        if (x[0],x[1]) != (s_x,s_y):
                            grid[(x[0],x[1])].config(bg=x[3])
                            grid[(x[0],x[1])].config(fg=x[4])
                    return False
                if (x,y) != (s_x,s_y):
                    grid[(x,y)].config(bg= 'white')
            else:
                if grid[(x,y)].cget('text') != w:
                    messagebox.showerror('Play Scrabble: Family Edition','You can\' overwrite an existing word.\n Try Again!')
                    temprefill(racktemp)
                    tempscore = 0
                    dw = 0
                    tw = 0
                    dl = []
                    tl = []
                    blank = []
                    for x in wordtemp:
                        grid[(x[0],x[1])].config(text=x[2])
                        grid[(x[0],x[1])].config(state = NORMAL)
                        if (x[0],x[1]) != (s_x,s_y):
                            grid[(x[0],x[1])].config(bg=x[3])
                            grid[(x[0],x[1])].config(fg=x[4])
                    return False
            x=x+1
        if crossflag == 'False':
            messagebox.showerror('Play Scrabble: Family Edition','New words must be connected to the exisiting words')
            temprefill(racktemp)
            tempscore = 0
            dw = 0
            tw = 0
            dl = []
            tl = []
            blank = []
            for x in wordtemp:
                grid[(x[0],x[1])].config(text=x[2])
                grid[(x[0],x[1])].config(state = NORMAL)
                if (x[0],x[1]) != (s_x,s_y):
                    grid[(x[0],x[1])].config(bg=x[3])
                    grid[(x[0],x[1])].config(fg=x[4])
            return False
        crossflag = 'False'
        temp[0] = 'white'
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)
        print(word_main)
        scoring(word_main,counter)
        return True

    elif dic_ans and radio == 2:
        if TNOT == 0:
            ##First word center check
            if s_y < 7 and s_x == 7:
                if (s_y + wordlen - 1) >= 7:
                    pass
                else:
                    messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                    return False ##error
            elif s_x == s_y == 7:
                pass
            else:
                messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                return False ##error

        for w in word_main:
            tempflag = cross_check(radio, x, y, w)

            if tempflag == 'True':
                crossflag = 'True'
            elif tempflag == 'Error':
                temprefill(racktemp)
                tempscore = 0
                dw = 0
                tw = 0
                dl = []
                tl = []
                blank = []
                for x in wordtemp:
                    grid[(x[0],x[1])].config(text=x[2])
                    grid[(x[0],x[1])].config(state = NORMAL)
                    if (x[0],x[1]) != (s_x,s_y):
                        grid[(x[0],x[1])].config(bg=x[3])
                        grid[(x[0],x[1])].config(fg=x[4])
                return False
            if grid[(x,y)].cget('state') != DISABLED:
                if check_if_word_in_rack(w,counter) == True:
                    if grid[(x,y)].cget('text') == 'DWS':
                        dw = dw + 1
                    elif grid[(x,y)].cget('text') == 'TWS':
                        tw = tw + 1
                    elif grid[(x,y)].cget('text') == 'DLS':
                        dl.append(w)
                    elif grid[(x,y)].cget('text') == 'TLS':
                        tl.append(w)
                    wordtemp.append([x,y,grid[(x,y)].cget('text'),grid[(x,y)].cget('bg'),grid[(x,y)].cget('fg')])
                    grid[(x,y)].config(text=w)
                    grid[(x,y)].config(state= DISABLED)
                else:
                    messagebox.showerror('Play Scrabble: Family Edition','Not in rack')
                    temprefill(racktemp)
                    tempscore = 0
                    dw = 0
                    tw = 0
                    dl = []
                    tl = []
                    blank = []
                    for x in wordtemp:
                        grid[(x[0],x[1])].config(text=x[2])
                        grid[(x[0],x[1])].config(state = NORMAL)
                        if (x[0],x[1]) != (s_x,s_y):
                            grid[(x[0],x[1])].config(bg=x[3])
                            grid[(x[0],x[1])].config(fg=x[4])
                    return False

                if (x,y) != (s_x,s_y):
                    grid[(x,y)].config(bg= 'white')
            else:
                if grid[(x,y)].cget('text') != w:
                    messagebox.showerror('Play Scrabble: Family Edition','You can\' overwrite an existing word.\n Try Again!')
                    temprefill(racktemp)
                    tempscore = 0
                    dw = 0
                    tw = 0
                    dl = []
                    tl = []
                    blank = []
                    for x in wordtemp:
                        grid[(x[0],x[1])].config(text=x[2])
                        grid[(x[0],x[1])].config(state = NORMAL)
                        if (x[0],x[1]) != (s_x,s_y):
                            grid[(x[0],x[1])].config(bg=x[3])
                            grid[(x[0],x[1])].config(fg=x[4])
                    return False
            y=y+1
        if crossflag == 'False':
            messagebox.showerror('Play Scrabble: Family Edition','New words must be connected to the exisiting words')
            temprefill(racktemp)
            tempscore = 0
            dw = 0
            tw = 0
            dl = []
            tl = []
            blank = []
            for x in wordtemp:
                grid[(x[0],x[1])].config(text=x[2])
                grid[(x[0],x[1])].config(state = NORMAL)
                if (x[0],x[1]) != (s_x,s_y):
                    grid[(x[0],x[1])].config(bg=x[3])
                    grid[(x[0],x[1])].config(fg=x[4])
            return False
        crossflag = 'False'
        temp[0] = 'white'
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)  
        print(word_main)
        scoring(word_main,counter)
        return True
    else:
        return False

def temprefill(racktemp):
    tmp_rack = all_tiles[counter-1]
    for x in racktemp:
        tmp_rack.append(x)
    all_tiles[counter-1] = tmp_rack
    racktemp = []

def refilling_tray():
    tmp_rack = all_tiles[counter-1]
    while len(tmp_rack) < 7:
        tmp = bag.pop()
        tmp_rack.append(tmp)
    all_tiles[counter-1] = tmp_rack

def rack_empty(counter):
	if len(all_tiles[counter-1]) == 0:
		return True
	return False
 
def score_checker(word, list_of_scores):
    global dl ,tl, blank
    score = 0
    my_string = list(word)

    for i in my_string:
        if i in dl:
            score = score + (2*Tilescore[i])
            dl.pop(dl.index(i))
        elif i in tl:
            score = score + (3*Tilescore[i])
            tl.pop(tl.index(i))
        else:
            score = score + (Tilescore[i])
    
    for x in blank:
        score = score - (Tilescore[x])
        blank.pop(blank.index(x))

    return score

def scoring(word,counter):
    global tempscore, dw, tw
    tempscore = tempscore + score_checker(word, Tilescore)
    if dw > 0:
        tempscore = tempscore*(2*dw)
        dw = 0

    if tw > 0:
        tempscore = tempscore*(3*tw)
        tw = 0
'''
def refilling_tray(word_main):
    wordlen = len(word_main)
    #print("hi1")
    tmp = all_tiles[counter-1]
    #print(tmp)
    tots=7
    for w in word_main:
        for k in range(tots):
            #print(w+" "+tmp[k][0])
            if w == tmp[k][0]:
                #print(w)
                tmp.pop(k)
                tots=tots-1
                break
    for i in range(wordlen):
        tmp.append(bag.pop())

    #print(tmp)
    return
'''
def check_if_word_in_rack(word_main,counter):
    global racktemp, blank
    tmp_rack = all_tiles[counter-1]
    if word_main in tmp_rack:
        tmp_rack.remove(word_main)
        racktemp.append(word_main)
        all_tiles[counter-1] = tmp_rack
        return True
    elif '#' in tmp_rack:
        blank.append(word_main)
        tmp_rack.remove('#')
        racktemp.append('#')
        all_tiles[counter-1] = tmp_rack
        return True
    return False

'''
def check_if_word_in_rack(word_main,counter):
    print("Hi")
    tmp_lst = [char for char in word_main]
    print(tmp_lst)
    tmp_rack = all_tiles[counter-1]
    tmp_rack = [char[0] for char in tmp_rack]
    print(tmp_rack)
    fin=""
    for k in tmp_lst:
        c=0
        for i in tmp_rack:
            c=c+1
            print(c)
            if k==i[0]:
                fin+=k
                tmp_rack.remove(i)
                print(tmp_rack)
                break
    print("FIN")
    print(fin)
    print(word_main)
    if len(fin)==len(word_main):
        return True
    else:
        return False
'''
##Turn changing nop means no of players:
def change_turn(skipt, nop,event = None):
    global counter, TNOT, skip, racktemp, pname, tempscore, dl, dw, tl, tw, blank, maxscore
    if counter == skipt:
        skip = 0
        if counter == nop:
            counter = 0
        counter = counter + 1
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)
        return

    status = Submitfunc()
    if status == True:
        pname[counter][1] = pname[counter][1] + tempscore
        scoreboard()
        if tempscore > maxscore[0]:
            maxscore[0] = tempscore
            maxscore[1] = pname[counter][0]
        tempscore = 0
        dw = 0
        tw = 0
        dl = []
        tl = []
        blank = []
        print(pname)
        refilling_tray()
        if counter == nop:
            counter = 0
        counter = counter + 1
        TNOT = TNOT + 1
        for x in range(nop):
            print(x+1,' :',all_tiles[x])
        print('\n')
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])

    if counter == skip:
        skip = 0
        if counter == nop:
            counter = 0
        counter = counter + 1
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)
    

##Submit Button:
submit_but = Button(board, text = 'Submit Data', height = 2, width = 15, borderwidth = 5, bg = 'black',fg='white', command = lambda: change_turn(skip, nop))
submit_but.grid(row=13, column = 15, padx = 10,sticky = W)      
#print(details)
board.bind('<Return>', lambda event: change_turn(skip, nop))

img = ImageTk.PhotoImage(Image.open('sherpng.png'))
Label(board, image = img, anchor = E).grid(row = 12, column = 30,padx = 10, rowspan = 10, columnspan = 10)

board.mainloop()

#click(wid[7,7].grid_info()['row'],wid[7,7].grid_info()['column'])

#Accessing button
#print(wid[(7,7)].cget('text'))

#Overwriting existing button text
#wid[(7,7)]['text'] = 'haha'
#print(wid[(7,7)].cget('text'))

#but.grid_location

#print(but.grid_info()['row'])
