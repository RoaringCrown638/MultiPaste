from concurrent.futures import thread
from tkinter.constants import ANCHOR, END, HORIZONTAL, X, Y
import pyperclip
import pyautogui as pya
import keyboard as key
import tkinter
import time
import threading
import multiprocessing

copiedList = []

def choosePaste(event):
    if pasteList.get(ANCHOR):
        selection = pasteList.get(ANCHOR)
        pasteWindow.clipboard_clear()
        pasteWindow.clipboard_append(selection[0:len(selection)-1])
        

def deleteAllButtonCom():
    open("D:\\Residual Information\\pasteList", 'w').close()
    pasteList.delete(0, tkinter.END)
    pasteList.insert(tkinter.END, "")


def deleteButtonCom():
    with open("D:\\Residual Information\\pasteList", 'r') as f:
        lines = f.readlines()
    with open("D:\\Residual Information\\pasteList", 'w') as f:
        for line in lines:
            if line == pasteList.get(ANCHOR):
                continue
            f.write(line)
    pasteList.delete(ANCHOR)
    pasteList.insert(tkinter.END, "")


def refreshButtonCom():
    pasteList.delete(0, tkinter.END)
    with open("D:\\Residual Information\\pasteList", 'r') as file:
        for pastes in file.readlines():
            pasteList.insert(tkinter.END, pastes)
            

while True:
    time.sleep(0.1)
    if key.is_pressed('ctrl') and key.is_pressed('alt') and key.is_pressed('v'):
        pasteWindow = tkinter.Tk()
        pasteWindow.attributes("-topmost", True)

        pasteWindow.title("Paste")
        pasteWindow.geometry('303x280+500+500')

        delAllButton = tkinter.Button(pasteWindow, text="Delete All", width=9, bd='3', command=deleteAllButtonCom)
        dellButton = tkinter.Button(pasteWindow, text="Delete", width=9, bd='3', command=deleteButtonCom)
        refreshButton = tkinter.Button(pasteWindow, text="Refresh", width=9, bd='3', command=refreshButtonCom)

        delAllButton.place(x=191, y=5)
        dellButton.place(x=5, y=5)
        refreshButton.place(x=98, y=5)

        pasteList = tkinter.Listbox(pasteWindow, height=13, width=39, font=("Aerial", '10'))
        pasteList.place(x=5, y=35)

        with open("D:\\Residual Information\\pasteList", 'r') as file:
            for pastes in file.readlines():
                pasteList.insert(tkinter.END, pastes)

        pasteBarY = tkinter.Scrollbar(pasteWindow)
        pasteBarY.pack(side='right', fill=Y)

        pasteBarX = tkinter.Scrollbar(pasteWindow, orient=HORIZONTAL)
        pasteBarX.pack(side='bottom', fill=X)

        pasteList.config(yscrollcommand=pasteBarY.set)
        pasteList.config(xscrollcommand=pasteBarX.set)

        pasteBarX.config(command=pasteList.xview)
        pasteBarY.config(command=pasteList.yview)

        pasteWindow.bind("<Button-1>", choosePaste)
        
        pasteWindow.mainloop()
        

               
