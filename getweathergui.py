#!/usr/local/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 8/28/2019                                             #
#############################################################################################

# Importing system module

import tkinter
import tkinter.messagebox


def callback():
	outvar.set("This is new text")
	root.update()
	tkinter.messagebox.showinfo("This is my title information", "this is the popup information.")
	outvar.set("This is the next new text")


root = tkinter.Tk()
root.title("The Weather Reporter")
# root.lift()
# root.minsize(500,500)
root.configure(width=500, height=500, bg="blue")

labelinfo = tkinter.Label(root, text="sample text")
labelinfo.grid(row=0, column=0, sticky="nsew")

invar = tkinter.StringVar()
inbox = tkinter.Entry(root, textvariable=invar)
inbox.grid(row=1, column=0, sticky="nsew")

outvar = tkinter.StringVar()
outvar.set("This is my sample output text")
outbox = tkinter.Message(root, textvariable=outvar)
outbox.grid(row=2, column=0, sticky="nsew")

doit = tkinter.Button(root, text="Hit Me", command=callback)
doit.grid(row=3, column=0, sticky="nsew")


root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=2)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=1)

root.mainloop()

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
