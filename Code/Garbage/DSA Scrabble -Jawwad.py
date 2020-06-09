from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import time
import sys
import random
import datetime

board = Tk()
helper = Tk()
analysis =Tk()

#Changing Titlename and logo:
board.iconbitmap('Scrabble logo.ico')
board.title('Play Scrabble: Family Edition')
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

Player1 = Label(scoreframe, text = 'Player1:')
Player1.grid(row = 0, column = 0)

Player2 = Label(scoreframe, text = 'Player2:')
Player2.grid(row = 1, column = 0)

Player3 = Label(scoreframe, text = 'Player3:')
Player3.grid(row = 2, column = 0)

Player4 = Label(scoreframe, text = 'Player4:')
Player4.grid(row = 3, column = 0)

##Radio Buttons for oriantation of words:
def dirbut(value):
    if value == 0:
        dir_error = messagebox.showerror('Play Scrabble: Family Edition','You didn\'t select any direction.\n Try Again!')
    return value

direction = IntVar()
direction.set(0)

direcframe = LabelFrame(board, text = 'Select Your Prefered Direction:')
direcframe.grid(row = 5,column = 15, rowspan = 2, columnspan = 3, padx = 10, sticky = W+E)

down = Radiobutton(direcframe, text = 'Downwards', variable = direction, value = 1, command= lambda: dirbut(direction.get())).grid(row= 0, column= 0)
right = Radiobutton(direcframe, text = 'Rightwards', variable = direction, value = 2,command= lambda: dirbut(direction.get())).grid(row= 1, column= 0)

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
    return
quit_but = Button(board, text = 'Quit Game', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white', command = quit_func)
quit_but.grid(row=15, column = 15, padx = 10, sticky = W+E)

##Shuffle Button:
def shuff_func():
    for x in range(7):
        var = random.randint(0,6)
        tiles[x]['text'],tiles[var]['text'] = tiles[var]['text'],tiles[x]['text']

shuff_but = Button(board, text = 'Shuffle Tray', height = 2, width = 30, borderwidth = 5, command = shuff_func, bg= 'white')
shuff_but.grid(row=14, column = 15, padx = 10, sticky = W+E)


##Skip Turn Button and func:
skip_but = Button(board, text = 'Skip Turn' , height = 2, width = 15, borderwidth = 5, bg = 'black',fg='white')
skip_but.grid(row=13, column = 15, padx = 10,sticky = E)

##Text box for word:
word = Entry(board,width=8, font = ('DJB Letter Game Tiles',20))
word.insert(0, 'Word Here')
word.grid(row = 7, column = 15,columnspan = 10, sticky = W+E, padx = 10)

##Player Tile:
tile_frame = LabelFrame(board, text = 'Player Tiles:')
tile_frame.grid(row= 8, column = 15, padx=10,rowspan = 3, columnspan =3, sticky = W+E)
tiles = {}
for x in range (7):
    if x <=4:
        but = Button(tile_frame, text = ':)', height = 2, width = 5, borderwidth = 5, bg = 'white', fg = 'black')
        but.grid(row = 0, column = x)
        tiles[(x)] = but
    else:
        but = Button(tile_frame, text = ':(', height = 2, width = 5, borderwidth = 5, bg = 'white', fg = 'black')
        but.grid(row = 1, column = x-5)
        tiles[(x)] = but

##Player Turn:
name_frame = LabelFrame(board, text = 'Player To Turn')
name_frame.grid(row = 4,column = 15, columnspan = 3, padx = 10, sticky = W+E)
name_dispaly = Label(name_frame, text = 'Player1; It\'s your turn')
name_dispaly.grid(row =0, column = 0,sticky = W)

##Top Bar:
topbar = Label(board, text='Help', bd=1, relief=SUNKEN, anchor=W)
topbar.grid(row=0, column=0)

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
        mid = l + (r - l) // 2; 
        if arr[mid] == x: 
            return True 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1
    return False

#Submit Button Action:
TNOT = 0                                ##Total no. of turn
def Submitfunc():
    global words,TNOT
    wordtemp = []
    (s_x,s_y) = (details[0],details[1])
    (x,y)=(s_x,s_y)
    radiolen = False
    word_main = word.get().upper()
    wordlen = len(word_main)
    radio = dirbut(direction.get())
    ## Radio Button check
    if radio == 0:
        return False
    elif radio == 1:
        if wordlen <= (15-x):
            radiolen = True
    elif radio == 2:
        if wordlen <= (15-y):
            radiolen = True
    
    if radiolen == False:
        len_error = messagebox.showerror('Play Scrabble: Family Edition','Your word lenght exceeded the block available.\n Try Again!')
        return False
    else:
        dic_ans = word_challenge(word_main)
        if dic_ans and radio == 1:
            ##First word center check
            if TNOT == 0:
                if s_x < 7 and s_y == 7:
                    if (s_x + wordlen - 1) >= 7:
                        pass
                    else:
                        center_error = messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                        return False ##error
                elif s_y == s_x == 7:
                    pass
                else:
                    center_error = messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                    return False ##error

            for w in word_main:
                if grid[(x,y)].cget('state') != DISABLED:
                    wordtemp.append([x,y,grid[(x,y)].cget('text'),grid[(x,y)].cget('bg'),grid[(x,y)].cget('fg')])
                    grid[(x,y)].config(text=w)
                    grid[(x,y)].config(state= DISABLED)
                    if (x,y) != (s_x,s_y):
                        grid[(x,y)].config(bg= 'white')
                else:
                    if grid[(x,y)].cget('text') != w:
                        overwrite_error = messagebox.showerror('Play Scrabble: Family Edition','You can\' overwrite an existing word.\n Try Again!')
                        for x in wordtemp:
                            grid[(x[0],x[1])].config(text=x[2])
                            grid[(x[0],x[1])].config(state = NORMAL)
                            if (x[0],x[1]) != (s_x,s_y):
                                grid[(x[0],x[1])].config(bg=x[3])
                                grid[(x[0],x[1])].config(fg=x[4])
                        return False
                x=x+1
            temp[0] = 'white'
            word.delete(0,END)
            word.insert(0, 'Word Here')
            return True

        elif dic_ans and radio == 2:
            if TNOT == 0:
                ##First word center check
                if s_y < 7 and s_x == 7:
                    if (s_y + wordlen - 1) >= 7:
                        pass
                    else:
                        center_error = messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                        return False ##error
                elif s_x == s_y == 7:
                    pass
                else:
                    center_error = messagebox.showerror('Play Scrabble: Family Edition','First word must pass through the center of the board.\n Try Again!')
                    return False ##error
            for w in word_main:
                if grid[(x,y)].cget('state') != DISABLED:
                    wordtemp.append([x,y,grid[(x,y)].cget('text'),grid[(x,y)].cget('bg'),grid[(x,y)].cget('fg')])
                    grid[(x,y)].config(text=w)
                    grid[(x,y)].config(state= DISABLED)
                    if (x,y) != (s_x,s_y):
                        grid[(x,y)].config(bg= 'white')
                else:
                    if grid[(x,y)].cget('text') != w:
                        overwrite_error = messagebox.showerror('Play Scrabble: Family Edition','You can\' overwrite an existing word.\n Try Again!')
                        for x in wordtemp:
                            grid[(x[0],x[1])].config(text=x[2])
                            grid[(x[0],x[1])].config(state = NORMAL)
                            if (x[0],x[1]) != (s_x,s_y):
                                grid[(x[0],x[1])].config(bg=x[3])
                                grid[(x[0],x[1])].config(fg=x[4])
                        return False
                y=y+1
            temp[0] = 'white'
            word.delete(0,END)
            word.insert(0, 'Word Here')    
            return True
        else:
            no_word = messagebox.showwarning('Play Scrabble: Family Edition','Your word wasn\'t available in our dictionary.')
            return False

##Turn changing nop means no of players:
counter = 1
def change_turn(nop = 4):
    global counter, TNOT
    status = Submitfunc()
    if status == True:
        counter = counter + 1
        TNOT = TNOT + 1
        name_dispaly.config(text = 'Player'+str(counter)+'; It\'s your turn')
    if counter == nop:
        counter = 0

##Submit Button:
submit_but = Button(board, text = 'Submit Data', height = 2, width = 15, borderwidth = 5, bg = 'black',fg='white', command = change_turn)
submit_but.grid(row=13, column = 15, padx = 10,sticky = W)      




#print(details)
board.mainloop()
#click(wid[7,7].grid_info()['row'],wid[7,7].grid_info()['column'])

#Accessing button
#print(wid[(7,7)].cget('text'))

#Overwriting existing button text
#wid[(7,7)]['text'] = 'haha'
#print(wid[(7,7)].cget('text'))

#but.grid_location

#print(but.grid_info()['row'])
