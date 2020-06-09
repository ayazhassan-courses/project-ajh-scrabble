def titlescreen():          ##TopLevel Window(not main)
    title = Toplevel()
    title.title('Play Scrabble: Family Edition')
    title.iconbitmap('Scrabble logo.ico')

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
        #print(np, one, two, three, four,sep = '\n')
        if np == 1:
            if one == '':
                messagebox.showerror('Play Scrabble: Family Edition','Player 1: Sahi name likho')
                return
            nop = np
            pname.append([one,0])

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

        print(nop, pname,sep = '\n')
        ##Closes Title (Top level window)
        title.quit()
        title.destroy()


    Button(title, text = 'On-Screen Keyboard',height = 2, width = 17, borderwidth = 5, bg = 'white', fg = 'black', command = open_osk).place(x = 294, y = 170)
    Button(title, text = 'Start Game',height = 2, width = 10, borderwidth = 5, bg = 'white', fg = 'black',command = lambda: startfunc(np.get(),P1.get(),P2.get(),P3.get(),P4.get())).place(x = 430, y = 170)
    title.protocol('WM_DELETE_WINDOW', quit_func)

    title.mainloop()

def home():                 ##Home Screen(Top Level)
    home = Toplevel()           
    global nop, pname
    home.title('Play Scrabble: Family Edition')
    home.iconbitmap('Scrabble logo.ico')

    ##When new game is selected, this function gets triggered and closes current window as well as call the titlescreen function
    def call_title():
        titlescreen()
        home.quit()
        home.destroy()

    ##Generating Button with their our commands
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

    if grid[(x,y)].cget('state') == DISABLED:
        word.insert(END,grid[(x,y)].cget('text'))

def shuff_func(event = None):       ##Shuffle rack
    for x in range(7):
        var = random.randint(0,6)
        tiles[x]['text'],tiles[var]['text'] = tiles[var]['text'],tiles[x]['text']

def wordfunc(event):        ##Clears the writing space for word play, used with keybinding
    word.delete(0,END)
    word.focus()

def tilefunc(event):        ##Triggers OSK when '#' Tile is selected
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

    ##POCL = POC(local)
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

    ##A function that will quit and destroy select (Toplevel)
    def closefunc():
        select.quit()
        select.destroy()

    done = Button(select, text = 'Done', height = 2, width = 30, borderwidth = 5, bg = 'black',fg='white',command = closefunc)
    done.grid(row=10, column = 1, padx = 10,pady = 10, sticky = W+E)
    
    ##The button of the player whos playing the turn will be disabled
    if counter == 1:
        R1.config(state = DISABLED)
    elif counter == 2:
        R2.config(state = DISABLED)
    elif counter == 3:
        R3.config(state = DISABLED)
    elif counter == 4:
        R4.config(state = DISABLED)

    select.mainloop()

def finish(pname):          ##Create a new window to annouce the winner
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
                scoring(word,counter)       ##A valid word is made and sent for score calculation
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
                scoring(word,counter)       ##A valid word is made and sent for score calculation
                return 'True'
            else:
                messagebox.showerror('Play Scrabble: Family Edition','Error occured while word crossing.\nAn invalid word was created: '+word+'.')
                return 'Error'
    return 'False'

def Submitfunc():           ##The Brains of the game:
    global words,TNOT, POC, skip, nop, counter, crossflag, racktemp, dl, dw, tl, tw, blank, tempscore
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
                    ##If the box is disabled, which means that it already contains a letter. 
                    # If the new letter is not same as the existing one it will pop-up un error.
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

def change_turn(skipt, nop,event = None):       ##When you end your turn, this function is called and if all checks and validations are cleared, turn is changed
    global counter, TNOT, skip, racktemp, pname, tempscore, dl, dw, tl, tw, blank, maxscore
    ##Same function is called when one either plays his turn or skips it because the consequent is same. 
    #The turn gets changed.
    if counter == skipt:
        ##First it checks for skiping of the turn.
        skip = 0
        if counter == nop:
            counter = 0
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
        counter = counter + 1
        name_dispaly.config(text = pname[counter][0]+'; It\'s your turn')
        inserting_letters_into_player_tiles(all_tiles[counter-1])
        word.delete(0,END)
        word.insert(0, 'Word Here')
        direction.set(0)

