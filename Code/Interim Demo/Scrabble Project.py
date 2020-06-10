from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import time
import sys
import random
import datetime
import os
from random import shuffle
from pynput.keyboard import Key, Controller
# The line below is calling a file the contains all the required function to run this game:
# Please enter the path to the scripts Manually:
execfile("<Path>//func2.0.py")
execfile("<Path>//func3.0.py")

# Titescore is a dictionary that holds the score of indivisual alphabet
Tilescore = {"A": 1, "B": 3, "C": 3, "D": 2,
             "E": 1, "F": 4, "G": 2, "H": 4,
             "I": 1, "J": 8, "K": 5, "L": 1,
             "M": 3, "N": 1, "O": 1, "P": 3,
             "Q": 10, "R": 1, "S": 1, "T": 1,
             "U": 1, "V": 4, "W": 4, "X": 8,
             "Y": 4, "Z": 10, "#": 0}

board = Tk()                    # Initialising Main Board(Window)

POC = IntVar()                  # Player Of Challange
counter = 1                     # Player Of Turn
TNOT = 0                        # Total No. Of Turns
nop = 4                         # No. Of Players
skip = 0                        # Player who's turn is going to get skipped.
crossflag = 'True'              # Flag Check For Wather  the words built in cross are valid or not
direction = IntVar()            # Direction in which the word is being played
racktemp = []                   # Temp. rack of Turn Player
blank = []                      # List conatins what letters was been used to subsitute a blank tile
pname = ['', ]                  # List holding Player names and their respective scores
tiles = {}                      # Racks placment on GUI is handled by tiles
grid = {}                       # The whole board and its cordinates are accessed by grid dictionary
tempscore = 0                   # Temp. score calculated per turn before the turn finishes
dw = 0                          # How many Double word scores has been activated in a single turn
tw = 0                          # How many Triple word scores has been activated in a single turn
dl = []                         # Which letters will be awarded Double score for a single turn
tl = []                         # Which letters will be awarded Triple score for a single turn
maxscore = [-1, ""]             # Statistic analysis: list holds max score scored in a single turn adn its scorer


# Controller function is declared over a variable Keyboards
keyboard = Controller()
# This alters the default protocol of a Windows OS default window. When click the cross, instead of closing the game it will now call a function.
board.protocol('WM_DELETE_WINDOW', quit_func)

# Key binding: Control+s will result in shuffling the rack for the player
board.bind('<Control-s>', shuff_func)

# Key binding: Control+c on word space will result in clearing it out.
board.bind('<Control-c>', wordfunc)

# Key binding: Enter key will submit your turn
board.bind('<Return>', lambda event: change_turn(skip, nop))

# Changing Titlename and logo:
board.iconbitmap('Scrabble logo.ico')
board.title('Play Scrabble: Family Edition')
board.state('zoomed')


# Home Screen is called; there you get many options to access as NEWGAME, HIGHSCORE, INSTRUCTIONS and etc.
home()

# Letter bag is generated and it will contain all the tiles which will be distributed through out the game
bag = generate_bag()
# Racks are being generated for all players, 7 tiles per player
all_tiles = generating_racks(nop, bag)
print(all_tiles)


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


# Score Board Frame:
scoreframe = LabelFrame(board, text='Score Board:')
scoreframe.grid(row=1, column=15, rowspan=3, columnspan=3, sticky=W+E, padx=10)
scoreboard()    # Scoreboard is called/generated/updated


# Generating Radio Buttons and its frame For Direction of the word:
direction.set(0)  # Setting default value for direction button
direcframe = LabelFrame(board, text='Select Your Prefered Direction:')
direcframe.grid(row=5, column=15, rowspan=2, columnspan=3, padx=10, sticky=W+E)

Radiobutton(direcframe, text='Downwards', variable=direction,
            value=1).grid(row=0, column=0)
Radiobutton(direcframe, text='Rightwards',
            variable=direction, value=2).grid(row=1, column=0)


# Time Clock:
start = time.time()
status = Label(board, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=16, column=0)
tick()

# Binding Mouse left click to grid dictionary + color preserve:
for a in range(15):
    for b in range(15):
        grid[(a, b)].bind("<Button-1>", click)


# End Of Match Button:
match_but = Button(board, text='End Match', height=2, width=30,
                   borderwidth=5, bg='black', fg='white', command=lambda: finish(pname))
match_but.grid(row=15, column=15, padx=10, sticky=W+E)


# Shuffle Button:
shuff_but = Button(board, text='Shuffle Tray', height=2,
                   width=13, borderwidth=5, command=shuff_func, bg='white')
shuff_but.grid(row=14, column=15, padx=10, sticky=E)


# Skip Turn Button and func:
skip_but = Button(board, text='Skip Turn', height=2, width=15, borderwidth=5,
                  bg='black', fg='white', command=lambda: change_turn(counter, nop))
skip_but.grid(row=13, column=15, padx=10, sticky=E)


# On screen keyboard button
Button(board, text='On-Screen Keyboard', height=2, width=17, borderwidth=5,
       bg='white', fg='black', command=open_osk).grid(row=14, column=15, padx=10, sticky=W)


# Text box for word:
word = Entry(board, width=8, font=('DJB Letter Game Tiles', 20))
word.insert(0, 'Word Here')
word.grid(row=7, column=15, columnspan=10, sticky=W+E, padx=10)
# Key binding: Mouse left click on word space will result in clearing it out.
word.bind("<Button-1>", wordfunc)

# Player Tile:
tile_frame = LabelFrame(board, text='Player Tiles:')
tile_frame.grid(row=8, column=15, padx=10, rowspan=3, columnspan=3, sticky=W+E)
inserting_letters_into_player_tiles(all_tiles[0])

# Player Turn Alert frame and lable:
name_frame = LabelFrame(board, text='Player To Turn')
name_frame.grid(row=4, column=15, columnspan=3, padx=10, sticky=W+E)
name_dispaly = Label(name_frame, text=pname[counter][0]+'; It\'s your turn')
name_dispaly.grid(row=0, column=0, sticky=W)


# Top Menu Bar:
topbar = Menu(board)
board.config(menu=topbar)

# File Option:
file = Menu(topbar, tearoff=0)
topbar.add_cascade(label='File', menu=file)
file.add_command(label='New Game')
file.add_separator()
file.add_command(label='Exit')

# Help Option:
helper = Menu(topbar, tearoff=0)
topbar.add_cascade(label='Help', menu=helper)
helper.add_command(label='Instructions')
helper.add_separator()
helper.add_command(label='Contact')


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
# print(details)

# Habib logo is placed on the window:
img = ImageTk.PhotoImage(Image.open('sherpng.png'))
Label(board, image=img, anchor=E).grid(
    row=12, column=30, padx=10, rowspan=10, columnspan=10)

board.mainloop()
