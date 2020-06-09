from tkinter import *

root = Tk()
root.iconbitmap('Scrabble logo.ico')
root.title('Play Scrabble: Family Edition')

frame = LabelFrame(root, text='Hello World!').pack()

lab = Label(frame, text='Bye World!').pack()

root.mainloop()
