# Created an example folder with three txt files in it.
from tkinter import *
from tkinter import ttk

def encode():
    pass
def decode():
    pass

root = Tk()
root.title("Senseless")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N, W, E, S))

button_encode = ttk.Button(mainframe, text="ENCODE", command= encode)
button_encode.grid(column=0,row=0,sticky=(W))

button_decode = ttk.Button(mainframe, text="DECODE", command= decode)
button_decode.grid(column=1,row=0,sticky=(E))


root.mainloop()