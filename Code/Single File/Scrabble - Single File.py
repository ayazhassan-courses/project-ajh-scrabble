from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import time
import sys
import random
import datetime
import os
import pickle
import winsound
import pygame
from pygame import mixer
from fontTools.ttLib import TTFont
from random import shuffle
from pynput.keyboard import Key, Controller


# The line below is calling a file the contains all the required function to run this game:
# Please Enter the path:
def titlescreen():          ##TopLevel Window(not main)
    title = Toplevel()
    title.title('Play Scrabble: Family Edition')
    title.iconbitmap('Scrabble logo.ico')
    title.grab_set()
    title.bind('<Button-1>', buttonclick)
    title.after(1, lambda: title.focus_force())

    ##Generating required frames:
    frame1 = LabelFrame(title,text = 'Select Number of Players')
    frame1.grid(row=0, column = 1,padx = 10,pady=10,sticky = N+S)

    frame2 = LabelFrame(title,text = 'Name The Players')
    frame2.grid(row=0, column = 10,padx = 10,pady=10,sticky = N+S)

    frame3 = LabelFrame(title,text = 'Select Game Mode')
    frame3.grid(row=1, column = 1,padx = 10,pady=10,sticky = W)

    ##This function enables and disables writing space for required no. of players
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

    ##Generation of writing space
    def wordfunc(event):
        event.widget.delete(0,END)
        event.widget.focus()

    #No. of Players (local)
    np = IntVar()
    np.set(2)

    ##Options is a list containing menu options.
    options = [2, 3, 4]
    Label(frame1,text ='Number of Players:').grid(row=1, column = 1, padx=5, pady=10)
    drop = OptionMenu(frame1, np, *options, command=func)
    drop.grid(row= 1, column = 2, padx=5, pady=10)
    drop.bind('<Enter>', buttonhover)

    ##Initialsing each writing space to each player
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

    ##Writing space if practice mode is activated
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

    ##Players have 2 mode options, presented in Radio Buttons form
    mode = IntVar()
    mode.set(1)
    Radiobutton(frame3, text = 'Original', variable = mode, value = 1,command = lambda :pracfunc(mode.get())).grid(row= 0, column= 0)
    Radiobutton(frame3, text = 'Practice', variable = mode, value = 2, command = lambda :pracfunc(mode.get())).grid(row= 0, column= 2)
    Radiobutton(frame3, text = 'Arcade', state = DISABLED, variable = mode, value = 3).grid(row= 0, column= 3)


    ##Function triggered when startgame is selected
    def startfunc(np, one, two, three, four): 
        global nop, pname, pscore
        pname = ['',]
        #print(np, one, two, three, four,sep = '\n')
        if np == 1:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            nop = np
            pname.append([one,0])

        elif np == 2:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            nop = np
            pname.append([one,0])
            pname.append([two,0])

        elif np == 3:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if three == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 3: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            nop = np
            pname.append([one,0])
            pname.append([two,0])
            pname.append([three,0])


        elif np == 4:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if two == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 2: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if three == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 3: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            if four == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 4: Please Write Your Name')
                title.after(1, lambda: title.focus_force())
                return
            nop = np
            pname.append([one,0])
            pname.append([two,0])
            pname.append([three,0])
            pname.append([four,0])

        print(nop, pname,sep = '\n')
        ##Closes Title (Top level window)
        title.grab_release()
        title.quit()
        title.destroy()


    B1 = Button(title, text = 'On-Screen Keyboard',height = 2, width = 17, borderwidth = 5, bg = 'white', fg = 'black', command = open_osk)
    B1.place(x = 294, y = 170)
    B2 = Button(title, text = 'Start Game',height = 2, width = 10, borderwidth = 5, bg = 'white', fg = 'black',command = lambda: startfunc(np.get(),P1.get(),P2.get(),P3.get(),P4.get()))
    B2.place(x = 430, y = 170)
    
    B1.bind('<Enter>', buttonhover)
    B2.bind('<Enter>', buttonhover)
    title.bind('<Return>', lambda event:startfunc(np.get(),P1.get(),P2.get(),P3.get(),P4.get()))
    
    title.protocol('WM_DELETE_WINDOW', quit_func)

    title.mainloop()

def home():                 ##Home Screen(Top Level)
    home = Toplevel() 
    home.geometry("+%d+%d" % (825, 210))
    home.grab_set()          
    global nop, pname
    home.title('Play Scrabble: Family Edition')
    home.iconbitmap('Scrabble logo.ico')
    home.bind('<Button-1>', buttonclick)
    home.after(1, lambda: home.focus_force())

    ##When new game is selected, this function gets triggered and closes current window as well as call the titlescreen function
    def call_title():
        home.grab_release()
        titlescreen()
        home.quit()
        home.destroy()

    def call_congame():
        home.grab_release()
        congame()
        home.grab_release()
        home.quit()
        home.destroy()

    ##Generating Button with their our commands
    start = Button(home, text = 'New Game',height = 3,  width = 20, borderwidth = 10, bg = 'white', fg = 'black',command = call_title)
    start.grid(row = 0, column = 0, padx = 100, pady = 10, sticky = E+W)

    con = Button(home, text = 'Continue Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',command = call_congame)
    con.grid(row = 1, column = 0, padx = 100, pady = 10)

    #hs = Button(home, text = 'Hight Score',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',state = DISABLED)
    #hs.grid(row = 2, column = 0, padx = 100, pady = 10)

    ins = Button(home, text = 'Instructions',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black',command = call_ins)
    ins.grid(row = 3, column = 0, padx = 100, pady = 10)

    quitbut = Button(home, text = 'Quit Game',height = 3, width = 20, borderwidth = 10, bg = 'white', fg = 'black', command = quit_func)
    quitbut.grid(row = 4, column = 0, padx = 100, pady = 10)

    start.bind('<Enter>', buttonhover)
    con.bind('<Enter>', buttonhover)
    #hs.bind('<Enter>', buttonhover)
    ins.bind('<Enter>', buttonhover)
    quitbut.bind('<Enter>', buttonhover)

    home.protocol('WM_DELETE_WINDOW', quit_func)
    home.mainloop()

def open_osk():             ##On Screen Keyboard
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

def scoreboard():           ##It checks NOP and then create scoreboard
    scoreframe.config(text = 'ScoreBoard:')

    Player1.config(text = pname[1][0]+':   '+str(pname[1][1]))
    Player1.grid(row = 0, column = 0)

    if len(pname) >= 3:
        Player2.config(text = pname[2][0]+':   '+str(pname[2][1]))
        Player2.grid(row = 1, column = 0)

    if len(pname) >= 4:
        Player3.config(text = pname[3][0]+':   '+str(pname[3][1]))
        Player3.grid(row = 2, column = 0)

    if len(pname) == 5:
        Player4.config(text = pname[4][0]+':   '+str(pname[4][1]))
        Player4.grid(row = 3, column = 0)

def tick():                 ##Time Clock display
    global start
    time2 = time.time()
    rn=round(time2-start,0)
    status.config(text=str(datetime.timedelta(seconds=rn)))
    status.after(200, tick)

def click(event):           ##Preserves the default color value of a tile when selected and unselected and updates global variable details
    global details, yellow, temp
    (x,y) = (event.widget.grid_info()['row']-1,event.widget.grid_info()['column'])
    old= detail_label.cget('text').split()
    t = grid[(x,y)].cget('text')
    details = [x,y,t]
    grid[(int(old[0]),int(old[1]))]['bg'] = temp[0]
    grid[(int(old[0]),int(old[1]))]['fg'] = temp[1]

    temp[0]= grid[(details[0],details[1])]['bg']
    temp[1] = grid[(details[0],details[1])]['fg']

    grid[(details[0],details[1])]['bg'] = yellow[0]
    grid[(details[0],details[1])]['fg'] = yellow[1]
    detail_func()

def point(event):
    global details, yellow, temp
    (x,y) = (event.widget.grid_info()['row']-1,event.widget.grid_info()['column'])
    old= detail_label.cget('text').split()
    t = grid[(x,y)].cget('text')
    details = [x,y,t]
    grid[(int(old[0]),int(old[1]))]['bg'] = temp[0]
    grid[(int(old[0]),int(old[1]))]['fg'] = temp[1]

    temp[0]= grid[(details[0],details[1])]['bg']
    temp[1] = grid[(details[0],details[1])]['fg']

    grid[(details[0],details[1])]['bg'] = yellow[0]
    grid[(details[0],details[1])]['fg'] = yellow[1]
    detail_func()

    if grid[(x,y)].cget('state') == DISABLED:
        if word.get() == 'Word Here':
            word.delete(0,END)
            word.focus()
        word.insert(END,grid[(x,y)].cget('text'))

def shuff_func(event = None):       ##Shuffle rack
    for x in range(7):
        var = random.randint(0,6)
        tiles[x]['text'],tiles[var]['text'] = tiles[var]['text'],tiles[x]['text']

def wordfunc(event=None):        ##Clears the writing space for word play, used with keybinding
    word.delete(0,END)
    word.focus()

def tilefunc(event):        ##Triggers OSK when '#' Tile is selected
    temp = word.get()
    if temp == 'Word Here':
        word.delete(0,END)
        word.focus()
    temp = event.widget.cget('text')
    if temp == '#':
        open_osk()
        return
    word.insert(END,temp)

def detail_func():          ##Displays the content of global variable Details
    detail_label['text'] = details
    detail_label.grid(row = 0, column = 0, sticky = W)

def donebut(radio):         ##Updating global varibale POC(player of challange)
    global POC, pname, counter
    POC = radio

def createselect():         ##Creates a TopLevel for selection of player of challange
    global counter, pname
    select = Toplevel()

    select.iconbitmap('Scrabble logo.ico')
    select.title('Play Scrabble: Family Edition')
    select.bind('<Button-1>', buttonclick)
    select.grab_set()
    select.after(1, lambda: select.focus_force())

    ##POCL = POC(local)
    POCL = IntVar()
    POCL.set(0)
    

    pselect = LabelFrame(select, text = 'Select the Player Challanging the word:',pady = 10)
    pselect.grid(row =1, column = 1, padx = 10, rowspan = 5, columnspan = 3, sticky = W+E)

    R1 = Radiobutton(pselect, text = 'Player 1', variable = POCL, value = 1, command= lambda: donebut(POCL.get()))
    R1.grid(row = 1, column = 1)
    R1.bind('<Enter>', buttonhover)

    if len(pname) >= 3:
        R2 = Radiobutton(pselect, text = 'Player 2', variable = POCL, value = 2, command= lambda: donebut(POCL.get()))
        R2.grid(row = 2, column = 1)
        R2.bind('<Enter>', buttonhover)

    if len(pname) >= 4:
        R3 = Radiobutton(pselect, text = 'Player 3', variable = POCL, value = 3, command= lambda: donebut(POCL.get()))
        R3.grid(row = 3, column = 1)
        R3.bind('<Enter>', buttonhover)

    if len(pname) == 5:
        R4 = Radiobutton(pselect, text = 'Player 4', variable = POCL, value = 4, command= lambda: donebut(POCL.get()))
        R4.grid(row = 4, column = 1)
        R4.bind('<Enter>', buttonhover)

    ##A function that will quit and destroy select (Toplevel)
    def closefunc():
        if (POCL.get()) == 0:
            no_word = messagebox.showwarning('Play Scrabble: Family Edition','Please Select the challenging Player.')
            return
        select.grab_release()
        select.quit()
        select.destroy()

    done = Button(select, text = 'Done', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white',command = closefunc)
    done.grid(row=10, column = 1, padx = 10,pady = 10, sticky = W+E)
    done.bind('<Enter>', buttonhover)
    
    ##The button of the player whos playing the turn will be disabled
    if counter == 1:
        R1.config(state = DISABLED)
    elif counter == 2:
        R2.config(state = DISABLED)
    elif counter == 3:
        R3.config(state = DISABLED)
    elif counter == 4:
        R4.config(state = DISABLED)

    def warn():
        no_word = messagebox.showwarning('Play Scrabble: Family Edition','A player must challenge now!')
        return

    select.protocol('WM_DELETE_WINDOW', warn)
    select.mainloop()

def finish(pname):          ##Create a new window to annouce the winner
    global TNOT, bag, maxscore, nop, Tilescore
    board.quit()
    board.destroy()
    winner = Tk()
    winner.title('Play Scrabble: Family Edition')
    winner.iconbitmap('Scrabble logo.ico')
    pname.pop(0)

    cheer_sound = mixer.Sound('Cheers.wav')
    cheer_sound.play()

    for x in range(nop):
        temp = 0
        for y in all_tiles[x]:
            temp = temp + Tilescore[y]
        pname[x][1] = pname[x][1] - temp

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
    Label(stats, text= 'Best Word played was : '+maxscore[2]).grid(row = 5,padx = 10, pady = 3, column = 1,sticky = W+E)

    declare = LabelFrame(winner, text= 'Winner:')
    declare.grid(row = 3, column = 1,padx = 10, pady = 10,columnspan = 10)
    Label(declare,text = 'The Winner Is: '+pname[0][0]+' By Scoring '+str(pname[0][1])+' Points.\nCongrats!').grid(row = 1,padx = 10, pady = 3, column = 1,sticky = W)
    
    def byes():         ##Good bye msg box
        messagebox.showinfo('Play Scrabble: Family Edition','Thank You For Playing Scrabble: Family Edition.\nHope To See You Soon. Good Bye :)')
        winner.quit()
        winner.destroy()

    winner.protocol('WM_DELETE_WINDOW', byes)
    winner.mainloop()

def dirbut(value):          ##Direction Check for word if left unselected
    if value == 0:
        messagebox.showerror('Play Scrabble: Family Edition','You didn\'t select any direction.\n Try Again!')
    return value

def cross_check(radio, mx, my, w):      ##It checks if any invalid or valid words are made when new turns are played but in cross directions
    x = mx
    y = my
    word = ''
    if radio == 1:
        if y >0:
            while y > 0:
                if grid[(x,y-1)].cget('state') == DISABLED:
                    word = grid[(x,y-1)].cget('text') + word
                    y = y - 1
                    continue
                break

        word = word + w
        
        if w == grid[(mx,my)].cget('text') and grid[(mx,my)].cget('state') == DISABLED:
            return 'True'

        y = my
        if y < 14:
            while y < 14:
                if grid[(x,y+1)].cget('state') == DISABLED:
                    word = word + grid[(x,y+1)].cget('text')
                    y = y + 1
                    continue
                break

        if len(word) > 1:
            if word_challenge(word) == True:
                print(word)
                scoring(word,counter)       ##A valid word is made and sent for score calculation
                return 'True'
            else:
                messagebox.showerror('Play Scrabble: Family Edition','Error occured while word crossing.\nAn invalid word was created: '+word+'.')
                return 'Error'

    else:
        ##y axis check
        if x > 0:
            while x > 0:
                if grid[(x-1,y)].cget('state') == DISABLED:
                    word = grid[(x-1,y)].cget('text') + word
                    x = x - 1
                    continue
                break
        
        word = word + w

        if w == grid[(mx,my)].cget('text') and grid[(mx,my)].cget('state') == DISABLED:
            return 'True'

        x = mx
        if x < 14:
            while x < 14:
                if grid[(x+1,y)].cget('state') == DISABLED:
                    word = word + grid[(x+1,y)].cget('text')
                    x = x + 1
                    continue
                break

        if len(word) > 1:
            if word_challenge(word) == True:
                print(word)
                scoring(word,counter)       ##A valid word is made and sent for score calculation
                return 'True'
            else:
                messagebox.showerror('Play Scrabble: Family Edition','Error occured while word crossing.\nAn invalid word was created: '+word+'.')
                return 'Error'
    return 'False'

def Submitfunc():           ##The Brains of the game:
    global words,TNOT, POC, skip, nop, counter, crossflag, racktemp, dl, dw, tl, tw, blank, tempscore, tempword, maxscore
    wordtemp = []
    racktemp = []
    (s_x,s_y) = (details[0],details[1])     ##row, column of starting point
    (x,y)=(s_x,s_y)
    word_main = word.get().upper()      ##Upper case the input words
    wordlen = len(word_main)
    radio = dirbut(direction.get())     ##Validating that a direction is selected
    
    if radio_check(radio,wordlen,x,y) != True:  ##Validating that the word wont go beyond boards bound
        return False

    dic_ans = word_challenge(word_main)     ##Checking word from dictionary
    if dic_ans == False:
        messagebox.showwarning('Play Scrabble: Family Edition','Your word wasn\'t available in our dictionary.')
        challange_box = messagebox.askyesnocancel('Play Scrabble: Family Edition','Do other player\'s want to challange this word ?')
        
        if challange_box == True:
            createselect()      
            Challenge_success= messagebox.askyesno('Play Scrabble: Family Edition','Was challenge successful?')
            if Challenge_success == False:
                ##If challenge wan't successful then the new word will be included in our dictionary
                dic_ans = True
                f = open('dic.txt', "a")
                f.write(word_main.upper())
                words.append(word_main.upper())
                f.close()
                words = sort_dictionary(words)
                ##As a penalty, POC will have its upcoming turn skipped
                skip = POC
                
            
            if Challenge_success == True:
                ##Losing to a challenge will cause the player to loss its ongoing turn
                return change_turn(counter,nop)
        
        if challange_box == False:
            ##If no one challenges, then the word is accepted as a valid word and added to the dictionary
            dic_ans = True
            f = open('dic.txt', "a")
            f.write(word_main.upper())
            words.append(word_main.upper())
            f.close()
            words = sort_dictionary(words)

    if dic_ans and radio == 1:
        if x > 0:
            if grid[(x-1,y)].cget('state') == DISABLED:
                messagebox.showerror('Play Scrabble: Family Edition','You can\'t overwite an exisiting word')
                return False
        ##First word center check
        if TNOT == 0:
            if s_x < 7 and s_y == 7:
                if (s_x + wordlen - 1) >= 7:
                    pass
                else:
                    messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                    return False
            elif s_y == s_x == 7:
                pass
            else:
                messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                return False

        for w in word_main:
            ##Word is printed on the board letter by letter after required checks have been performed
            tempflag = cross_check(radio, x, y, w) 
            if tempflag == 'True':
                crossflag = 'True'

            elif tempflag == 'Error':
                ##If an error occurs, all values are retured to their original state
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
                ##It means their is no prior letter written on the box
                if check_if_word_in_rack(w,counter) == True:
                    wordtemp.append([x,y,grid[(x,y)].cget('text'),grid[(x,y)].cget('bg'),grid[(x,y)].cget('fg')])
                    ##Before printing the letter, the above mentioned attributes are recorded for each turn
                    ##and used when an error is occured to reset values to their original state
                    ##Then its checked that does the current box give any bonus score
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
                    ##If letter is not available in rack error is showed
                    messagebox.showerror('Play Scrabble: Family Edition',w+': is not available in your rack')
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
                    ##If the box is disabled, which means that it already contains a letter. 
                    # If the new letter is not same as the existing one it will pop-up un error.
                    messagebox.showerror('Play Scrabble: Family Edition','You can\'t overwrite an existing word.\n Try Again!')
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
        tempword = word_main
        return True

    elif dic_ans and radio == 2:
        if y > 0:
            if grid[(x,y-1)].cget('state') == DISABLED:
                messagebox.showerror('Play Scrabble: Family Edition','You can\'t overwite an exisiting word')
                return False
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
                    messagebox.showerror('Play Scrabble: Family Edition',w+': is not available in your rack')
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
                    messagebox.showerror('Play Scrabble: Family Edition','You can\'t overwrite an existing word.\n Try Again!')
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
        tempword = word_main
        return True
    else:
        return False

def change_turn(skipt, nop,event = None):       ##When you end your turn, this function is called and if all checks and validations are cleared, turn is changed
    global counter, TNOT, skip, racktemp, pname, tempscore, dl, dw, tl, tw, blank, maxscore, tempword
    ##Same function is called when one either plays his turn or skips it because the consequent is same. 
    #The turn gets changed.
    if counter == skipt:
        ##First it checks for skiping of the turn.
        skip = 0
        if counter == nop:
            counter = 0
        scoreboard()
        counter = counter + 1
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)
        #In case of changing of turn the above mentioned steps are taken:
        # 1) Turn notification bar chnages it text. 
        # 2) The rack gets changed. 
        # 3) The writing space gets it default text back. 
        # 4) The direction button is unselected
        return

    status = Submitfunc()
    ##If not skipped, then word played is checked
    if status == True:
        pname[counter][1] = pname[counter][1] + tempscore
        if TNOT == 0:
            pname[counter][1] = pname[counter][1] * 2
        scoreboard()
        if tempscore > maxscore[0]:
            maxscore[0] = tempscore
            maxscore[1] = pname[counter][0]
            maxscore[2] = tempword
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
    ##If a valid word is created above mentioned steps are taken:
    # 1) Scoreboard is updated. 
    # 2) Score related global varibales are reseted. 
    # 3) Racks are refilled. 
    # 4) Turn notification bar changes its text. 
    # 5) Rack is changed
    # 6) Lastly, its checked should the upcoming player get his turn skipped becuase of lossing a challenge

    if counter == skip:
        skip = 0
        if counter == nop:
            counter = 0
        scoreboard()
        counter = counter + 1
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)

def newgame():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def savegame(event = None):
    global counter, TNOT, nop, skip, pname, tiles, grid, maxscore, bag, all_tiles, start
    
    save = {}
    lst = []
    for a in range(15):
        for b in range(15):
            lst.append([a,b,grid[(a,b)].cget('text')])
    

    save['counter'] = counter
    save['TNOT'] = TNOT
    save['nop'] = nop
    save['skip'] = skip
    save['pname'] = pname
    save['maxscore'] = maxscore
    save['bag'] = bag
    save['all_tiles'] = all_tiles
    save['grid'] = lst
    save['time'] = start

    dbfile = filedialog.asksaveasfile(title= 'Select The Saving Directory', mode='wb', defaultextension=".bin", filetypes=(('Binary Files','*.bin'),('All Files','*.*')))
    pickle.dump(save, dbfile)                      
    dbfile.close()

def congame():
    global counter, TNOT, nop, skip, pname, tiles, grid, maxscore, bag, all_tiles, conflag, start
    ret = {}
    filename = filedialog.askopenfilename(title= 'Select a Saved File:',filetypes=(('Binary Files','*.bin'),('All Files','*.*')))
    dbfile = open(filename, 'rb')      
    db = pickle.load(dbfile) 
    dbfile.close()
    #print(db)

    counter = db['counter'] - 1
    TNOT = db['TNOT']
    nop = db['nop']
    skip = db['skip']
    pname = db['pname']
    maxscore = db['maxscore']
    bag = db['bag']
    all_tiles = db['all_tiles']
    lst = db['grid']
    start = db['time']

    if counter == 0:
        counter = len(pname) - 1

    for x in lst:
        grid[(x[0],x[1])].config(text = x[2])

    for a in range(15):
        for b in range(15):
            if grid[(a,b)].cget('text') != 'TWS' and grid[(a,b)].cget('text') != 'DWS' and grid[(a,b)].cget('text') != 'TLS' and grid[(a,b)].cget('text') != 'DLS' and grid[(a,b)].cget('text') != '':
                grid[(a,b)].config(state = DISABLED)
                grid[(a,b)].config(bg = 'white')

    conflag = True

def call_ins():
    os.startfile('Scrabble Family Edition PDF.pdf')
    return

def buttonclick(event):
    winsound.PlaySound('Mouse-Click-00.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)

def buttonhover(event):
    return
    #hover_sound = mixer.Sound('button-hover.wav')
    #hover_sound.play()
    
def down(event=None):
    direction.set(1)

def right(event = None):
    direction.set(2)

def contact():
    con = Toplevel()
    con.title('Play Scrabble: Family Edition')
    con.iconbitmap('Scrabble logo.ico')
    con.grab_set()
    con.bind('<Button-1>', buttonclick)
    con.after(1, lambda: con.focus_force())

    frame1 = LabelFrame(con,text = 'Project Participents:')
    frame1.grid(row=0, column = 1,padx = 10,pady=10,sticky = N+S)

    Label(frame1,text ='Muhammad Jawwad: mj05516@st.habib.edu.pk').grid(row=1, column = 1, padx=5, pady=10)
    Label(frame1,text ='Hussain Abbas: ha06228@st.habib.edu.pk').grid(row=2, column = 1, padx=5, pady=10)
    Label(frame1,text ='Amin Fareed: af04372@st.habib.edu.pk').grid(row=3, column = 1, padx=5, pady=10)

def stop_music():
    mixer.music.stop()

def play_music():
    mixer.music.load("Good_Starts.wav")
    mixer.music.play(-1)



def quit_func():                ##Quits and Destroys the board(main window)
    global quitflag
    quit_box = messagebox.askyesno('Play Scrabble: Family Edition','Do you want to quit ?')
    if quit_box == 1:
        board.quit()
        board.destroy()
    return

def generate_bag():             ##Generates letters and append them to bag
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

def generating_racks(number_of_players,bag):            ##Generates rack for each player
    players_racks=[]
    for i in range(number_of_players):
        tmp=[]
        for k in range(7):
            tmp.append(bag.pop())
        players_racks.append(tmp)
    return players_racks

def inserting_letters_into_player_tiles(letters_lst):   ##Overwriting tile's text with rack alphabets
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
        tiles[(y)].bind('<Enter>', buttonhover)
        y=y+1
    return

def word_challenge(word):       ##Calls a function what checks the work through the dictionary
    global words
    if check_word(words, 1, len(words), word):
        return True
    else:
        return False
        
def check_word(arr, l, r, x):   ##Binary search implementaion, searches through the dictionary for the word  
    while l <= r: 
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return True 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return False

def radio_check(radio,wordlen,x,y): ##With repect to direction selected, it checks the word should not go out of bounds of board
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

def partition(arr,low,high):    ##These 3 functions are used when a challenge is made
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

def quickSort(arr,low,high):    ##When a new word is introduced to our dictionary it gets appended
    if low < high: 
  
        # pi is partitioning index, arr[p] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

def sort_dictionary(words):     ##and then our dictionary is sorted so we can use binary search again
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

def temprefill(racktemp):       ##When an error occurs, this function restores the rack with its default letters
    tmp_rack = all_tiles[counter-1]
    for x in racktemp:
        tmp_rack.append(x)
    all_tiles[counter-1] = tmp_rack
    racktemp = []

def refilling_tray():           ##After each turn this function makes sure that players rack has 7 letters
    tmp_rack = all_tiles[counter-1]
    while len(tmp_rack) < 7:
        tmp = bag.pop()
        tmp_rack.append(tmp)
    all_tiles[counter-1] = tmp_rack

def check_if_word_in_rack(word_main,counter):   ##This functions check that are the letters required available in the rack 
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

def rack_empty(counter):    ##It checks for the lenght of the rack for scoring purpose
	if len(all_tiles[counter-1]) == 0:
		return True
	return False
 
def score_checker(word, list_of_scores):    ##Calculates indivisual tile's score
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
        
    blank = []
    return score

def scoring(word,counter):      ##It checks and applies DWS & TWS and updates the score
    global tempscore, dw, tw
    winsound.PlaySound('Score.wav', winsound.SND_FILENAME + winsound.SND_ASYNC)
    tempscore = tempscore + score_checker(word, Tilescore)
    if dw > 0:
        tempscore = tempscore*(2*dw)
        dw = 0

    if tw > 0:
        tempscore = tempscore*(3*tw)
        tw = 0

    if rack_empty(counter) == True:
        tempscore = tempscore + 50

# Titescore is a dictionary that holds the score of indivisual alphabet
Tilescore = {"A": 1, "B": 3, "C": 3, "D": 2,
             "E": 1, "F": 4, "G": 2, "H": 4,
             "I": 1, "J": 8, "K": 5, "L": 1,
             "M": 3, "N": 1, "O": 1, "P": 3,
             "Q": 10, "R": 1, "S": 1, "T": 1,
             "U": 1, "V": 4, "W": 4, "X": 8,
             "Y": 4, "Z": 10, "#": 0}

board = Tk()                    # Initialising Main Board(Window)
pygame.init()                   # Initialising pygame to use its mixer

POC = IntVar()                  # Player Of Challange
counter = 1                     # Player Of Turn
TNOT = 0                        # Total No. Of Turns
nop = 4                         # No. Of Players
skip = 0                        # Player who's turn is going to get skipped.
crossflag = 'True'              # Flag Check For Wather  the words built in cross are valid or not
direction = IntVar()            # Direction in which the word is being played
racktemp = []                   # Temp. rack of Turn Player
blank = []                      # List conatins what letters was been used to subsitute a blank tile
pname = ['', '','','','']       # List holding Player names and their respective scores
tiles = {}                      # Racks placment on GUI is handled by tiles
grid = {}                       # The whole board and its cordinates are accessed by grid dictionary
tempscore = 0                   # Temp. score calculated per turn before the turn finishes
tempword = ''
dw = 0                          # How many Double word scores has been activated in a single turn
tw = 0                          # How many Triple word scores has been activated in a single turn
dl = []                         # Which letters will be awarded Double score for a single turn
tl = []                         # Which letters will be awarded Triple score for a single turn
maxscore = [-1, "",""]          # Statistic analysis: list holds max score scored in a single turn adn its scorer
conflag = False                 # Triggers when continue game is selected
start = time.time()             #start time of the game is

# Controller function is declared over a variable Keyboards
keyboard = Controller()
# This alters the default protocol of a Windows OS default window. When click the cross, instead of closing the game it will now call a function.
board.protocol('WM_DELETE_WINDOW', quit_func)

# Key binding: Control+s will result in shuffling the rack for the player
board.bind('<Control-z>', shuff_func)

# Key binding: Control+c on word space will result in clearing it out.
board.bind('<Control-c>', wordfunc)

# Key binding: Enter key will submit your turn
board.bind('<Return>', lambda event: change_turn(skip, nop))

#click sound
board.bind('<Button-1>', buttonclick)

#Key binding: Skip turn:
board.bind('<Control-t>', lambda event: change_turn(counter, nop))

#Key binding: Direction Down
board.bind('<Control-d>',down)

#Key binding: Direction Right
board.bind('<Control-r>',right)

#Key binding: Finish game
board.bind('<Control-Return>', lambda event: finish(pname))

#key binding: savegame
board.bind('<Control-s>', savegame)

# Changing Titlename and logo:
board.iconbitmap('Scrabble logo.ico')
board.title('Play Scrabble: Family Edition')
board.state('zoomed')

# Creating Scrabble Body/Grid/Board:
for x in range(15):
    for y in range(15):
        if (x, y) == (7, 7):

            but = Button(board, text='X', height=2, width=5,
                         borderwidth=5, bg='yellow', fg='black')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but
        elif (x, y) == (0, 0) or (x, y) == (0, 7) or (x, y) == (0, 14) or (x, y) == (7, 0) or (x, y) == (7, 14) or (x, y) == (14, 0) or (x, y) == (14, 7) or (x, y) == (14, 14):

            but = Button(board, text='TWS', height=2, width=5,
                         borderwidth=5, bg='red', fg='white')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but

        elif (x, y) == (1, 1) or (x, y) == (2, 2) or (x, y) == (3, 3) or (x, y) == (4, 4) or (x, y) == (10, 10) or (x, y) == (11, 11) or (x, y) == (12, 12) or (x, y) == (13, 13) or (x, y) == (1, 13) or (x, y) == (2, 12) or (x, y) == (3, 11) or (x, y) == (4, 10) or (x, y) == (10, 4) or (x, y) == (11, 3) or (x, y) == (12, 2) or (x, y) == (13, 1):

            but = Button(board, text='DWS', height=2, width=5,
                         borderwidth=5, bg='grey', fg='white')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but

        elif (x, y) == (0, 3) or (x, y) == (0, 11) or (x, y) == (2, 6) or (x, y) == (2, 8) or (x, y) == (3, 0) or (x, y) == (3, 7) or (x, y) == (3, 14) or (x, y) == (6, 2) or (x, y) == (6, 6) or (x, y) == (6, 8) or (x, y) == (6, 12) or (x, y) == (7, 3) or (x, y) == (7, 11) or (x, y) == (14, 3) or (x, y) == (14, 11) or (x, y) == (12, 6) or (x, y) == (12, 8) or (x, y) == (11, 0) or (x, y) == (11, 7) or (x, y) == (11, 14) or (x, y) == (8, 2) or (x, y) == (8, 6) or (x, y) == (8, 8) or (x, y) == (8, 12):
            but = Button(board, text='DLS', height=2, width=5,
                         borderwidth=5, bg='blue', fg='white')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but

        elif (x, y) == (1, 5) or (x, y) == (1, 9) or (x, y) == (5, 1) or (x, y) == (5, 5) or (x, y) == (5, 9) or (x, y) == (5, 13) or (x, y) == (13, 5) or (x, y) == (13, 9) or (x, y) == (9, 1) or (x, y) == (9, 5) or (x, y) == (9, 9) or (x, y) == (9, 13):

            but = Button(board, text='TLS', height=2, width=5,
                         borderwidth=5, bg='green', fg='white')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but

        else:
            but = Button(board, text='', height=2, width=5,
                         borderwidth=5, bg='#f2c4b1', fg='white')
            but.grid(row=x+1, column=y)
            grid[(x, y)] = but


# Info updated after generation of board:
# Temp hold the bg and fg color of each tile after its been selected; 
# Its default value is setted according to position 7,7(center of the board)
temp = ['white', 'black']

# Yellow holds the color value of the pointer. 
# When a tile is selected, its color values are change to whats being hold in Yellow
yellow = ['yellow', 'black']

# Details hold the vital info thats being presented on the board, 
# the info of the selected tile. Its default value is setted according to position 7,7(center of the board)
details = [7, 7, grid[(7, 7)].cget('text')]

# Top Menu Bar:
topbar = Menu(board)
board.config(menu=topbar)

# File Option:
file = Menu(topbar, tearoff=0)
topbar.add_cascade(label='File', menu=file)
file.add_command(label='New Game', command = newgame)
file.add_separator()
file.add_command(label='Save Game           <Ctrl + S>', command = savegame)
file.add_separator()
file.add_command(label='Exit                <Alt + F4>', command = quit_func)

#Player Commands:
pcmd = Menu(topbar, tearoff = 0)
topbar.add_cascade(label = 'Player Options', menu=pcmd)
pcmd.add_command(label = 'Submit Data                               <Enter>', command = lambda: change_turn(skip, nop))
pcmd.add_separator()
pcmd.add_command(label = 'Shuffle Tray                              <Ctrl + Z>', command = shuff_func)
pcmd.add_separator()
pcmd.add_command(label = 'Skip Turn                                 <Ctrl + T>', command = lambda: change_turn(counter, nop))
pcmd.add_separator()
pcmd.add_command(label = 'Clear Writing box                     <Ctrl + C>', command = wordfunc)
pcmd.add_separator()
pcmd.add_command(label = 'Select Downwards                  <Ctrl + D>', command = down)
pcmd.add_separator()
pcmd.add_command(label = 'Select Rightwards                     <Ctrl + R>', command = right)
pcmd.add_separator()
pcmd.add_command(label = 'End Match                         <Ctrl + Enter>', command = lambda:finish(pname))

# Help Option:
helper = Menu(topbar, tearoff=0)
topbar.add_cascade(label='Help', menu=helper)
helper.add_command(label='Instructions', command = call_ins)
helper.add_separator()
helper.add_command(label='Contact', command = contact)
helper.add_separator()
helper.add_command(label='On-Screen Keyboard', command = open_osk)
helper.add_separator()
helper.add_command(label='Turn Off Background Music', command = stop_music)
helper.add_separator()
helper.add_command(label='Turn On Background Music', command = play_music)





# Score Board Frame:
scoreframe = LabelFrame(board, text='Welcome:')
scoreframe.grid(row=1, column=15, rowspan=3, columnspan=3, sticky=W+E, padx=10)

Player1 = Label(scoreframe, text = 'The minds behind the recreation of this GUI based Scrabble are:')
Player1.grid(row = 0, column = 0)

if len(pname) >= 3:
    Player2 = Label(scoreframe, text = 'Amin Fareed, Hussain Abbas and Muhammad Jawwad')
    Player2.grid(row = 1, column = 0)

if len(pname) >= 4:
    Player3 = Label(scoreframe, text = 'It\'s recommended to have a resolution of 1366*768 and \n place your taskbar to the right-side of your screen for optimal UI experience.')
    Player3.grid(row = 2, column = 0)

if len(pname) == 5:
    Player4 = Label(scoreframe, text = 'Hope you enjoy the game, and if there is any room for imporvemnt do let us know :)')
    Player4.grid(row = 3, column = 0)

# Letter bag is generated and it will contain all the tiles which will be distributed through out the game
bag = generate_bag()

# Home Screen is called; there you get many options to access as NEWGAME, HIGHSCORE, INSTRUCTIONS and etc.
mixer.music.load("Good_Starts.wav")
mixer.music.play(-1)
home()
scoreboard()

# Time Clock:
status = Label(board, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=16, column=0, columnspan = 10, sticky = W)
tick()

# Racks are being generated for all players, 7 tiles per player
if conflag == False:
    all_tiles = generating_racks(nop, bag)
print(all_tiles)

if len(pname) < 3:
    Player2.destroy()

if len(pname) < 4:
    Player3.destroy()

if len(pname) < 5:
    Player4.destroy()


# Generating Radio Buttons and its frame For Direction of the word:
direction.set(0)  # Setting default value for direction button
direcframe = LabelFrame(board, text='Select Your Prefered Direction:')
direcframe.grid(row=5, column=15, rowspan=2, columnspan=3, padx=10, sticky=W+E)

Radiobutton(direcframe, text='Downwards', variable=direction,
            value=1).grid(row=0, column=0)
Radiobutton(direcframe, text='Rightwards',
            variable=direction, value=2).grid(row=1, column=0)



# Binding Mouse left click to grid dictionary + color preserve:
for a in range(15):
    for b in range(15):
        grid[(a, b)].bind("<Button-1>", click)
        grid[(a, b)].bind("<Button-3>", point)


# End Of Match Button:
match_but = Button(board, text='End Match', height=2, width=30,
                   borderwidth=5, bg='black', fg='white', command=lambda: finish(pname))
match_but.grid(row=15, column=15, padx=10, sticky=W+E)
match_but.bind('<Enter>', buttonhover)


# Shuffle Button:
shuff_but = Button(board, text='Shuffle Tray', height=2,
                   width=13, borderwidth=5, command=shuff_func, bg='white')
shuff_but.grid(row=14, column=15, padx=10, sticky=E)
shuff_but.bind('<Enter>', buttonhover)


# Skip Turn Button and func:
skip_but = Button(board, text='Skip Turn', height=2, width=15, borderwidth=5,
                  bg='black', fg='white', command=lambda: change_turn(counter, nop))
skip_but.grid(row=13, column=15, padx=10, sticky=E)
skip_but.bind('<Enter>', buttonhover)


# On screen keyboard button
Onkey = Button(board, text='On-Screen Keyboard', height=2, width=17, borderwidth=5,
       bg='white', fg='black', command=open_osk)
Onkey.grid(row=14, column=15, padx=10, sticky=W)
Onkey.bind('<Enter>', buttonhover)


# Text box for word:
word = Entry(board, width=8, font=('DJB Letter Game Tiles', 20))
word.insert(0, 'Word Here')
word.grid(row=7, column=15, columnspan=10, sticky=W+E, padx=10)
# Key binding: Mouse left click on word space will result in clearing it out.
word.bind("<Button-3>", wordfunc)

# Player Tile:
tile_frame = LabelFrame(board, text='Player Tiles:')
tile_frame.grid(row=8, column=15, padx=10, rowspan=3, columnspan=3, sticky=W+E)
inserting_letters_into_player_tiles(all_tiles[0])

# Player Turn Alert frame and lable:
name_frame = LabelFrame(board, text='Player To Turn')
name_frame.grid(row=4, column=15, columnspan=3, padx=10, sticky=W+E)
name_dispaly = Label(name_frame, text=pname[counter][0]+'; It\'s your turn')
name_dispaly.grid(row=0, column=0, sticky=W)

# Submiting Details:
detail_frame = LabelFrame(board, text='Details of Submission:', pady=10)
detail_frame.grid(row=10, column=15, padx=10,
                  rowspan=3, columnspan=3, sticky=W+E)
detail_label = Label(detail_frame, text=details)
detail_label.grid(row=0, column=0, sticky=W)

# Submiting Details label:
detail_label2 = Label(
    detail_frame, text='--> This the cell you have selected.')
detail_label2.grid(row=0, column=1, sticky=E, padx=5)


# Writing a dictionary to a list for faster access:
words = []
f = open('dic.txt', "r")
for line in f:
    words.append(line[0:(len(line)-1)])
f.close()

# Submit Button:
submit_but = Button(board, text='Submit Data', height=2, width=15, borderwidth=5,
                    bg='black', fg='white', command=lambda: change_turn(skip, nop))
submit_but.grid(row=13, column=15, padx=10, sticky=W)
submit_but.bind('<Enter>', buttonhover)
# print(details)

# Habib logo is placed on the window:
img = ImageTk.PhotoImage(Image.open('sherpng.png'))
Label(board, image=img, anchor=E).grid(
    row=12, column=29, padx=10, rowspan=10, columnspan=10)

htp = LabelFrame(board, text='How To Play:')
htp.grid(row=1, column=30, columnspan=3,rowspan = 15, padx=5, sticky=W+N, pady = 20)
htpt = Label(htp, text='Here are some brief guidelines about the \ngame, to read complete set of instructions \nplease select "Instructions" from \ndrop down menu.\n\n1. Each Player will be notified of his/her\n turn form th alert box "Player To Turn".\n\n2. To play a turn, each player must\ncreate a word from his/her provided rack.\n\n3. The word must be typed in the\n entry box mentioning "Word Here".\n\n4. The word played must be valid or else\nother players can challenge it; losing\na challenge will result in skip turn penalty.\n\n5. Player must select the direction for\nthe word before finishing the turn.\n\n6. Clicking left mouse button on board\nwill result in change of pointers location.\n\n7. Clicking right mouse button on board\nwill result in same actions as left\nbutton click + the letter underneath\nthe cursor will be added to the entry box.\n\n8. Clicking right mouse button on text field\nwill clear it.')
htpt.grid(row=0, column=0, sticky=W)

if conflag == True:
    change_turn(counter, nop)
    conflag = False

board.mainloop()
