#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 19:28:40 2023

@author: apple
"""

from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("working on canvas using functions")
root.geometry("600x600")

colorlabel = Label(root, text="enter a color")
colorlabel.place(relx=0.4, rely=0.9, anchor = CENTER)

input_box = Entry(root)
input_box.insert(0, "black")
input_box.place(relx=0.8, rely=0.9, anchor=CENTER)

canvas = Canvas(root, width=590, height=510, bg="white", highlightbackground="gray")
canvas.pack()

img = ImageTk.PhotoImage(Image.open("start_point1.png"))
my_image = canvas.create_image(50,50, image = img)

direction = ""
oldx = 50
oldy = 50
newx = 50
newy = 50

def draw(direction, oldx, oldy, newx, newy):
    fill_color = input_box.get()

root.mainloop()