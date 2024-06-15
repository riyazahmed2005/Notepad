import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os
from datetime import datetime
w=tk.Tk()
def window():
    w.title('untitled-Notepad')
    w.geometry('1200x700+0+0')
    w.resizable(False,False)
    w.configure(bg="black")
    photo=tk.PhotoImage(file="ico.png")
    w.iconphoto(False,photo)
def exit():
    w.destroy()
def about():
    messagebox.showinfo(title="Notepad",message="""Welcome to  Notepad App – your simple, elegant, and efficient solution for all your note-taking needs. Whether you need to jot down quick ideas, write detailed notes, or keep a daily journal, our app is designed to provide a seamless experience.

FEATURES

User-Friendly Interface: Clean and intuitive design to enhance your note-taking experience.
Organized Notes: Create, edit, and organize notes effortlessly.
Customizable Themes: Personalize your notepad with various themes and fonts.

HOW TO USE

Create a New Note: Click on the "New Note" button to start writing.
Edit Notes: Select a note from the list to edit or update.
Delete Notes: Swipe left or right on a note to delete it.
Search Notes: Use the search bar at the top to find specific notes.

ABOUT THE DEVELOPER

This Notepad App is developed by Riyaz Ahmed, a passionate software developer committed to creating simple and efficient applications that make your life easier.

CONTACT

For support, feedback, or inquiries, please contact Riyaz Ahmed at riyazahmed08@gmail.com.

© 2024 Riyaz Ahmed. All rights reserved.

Unauthorized duplication or distribution of this software is prohibited.""")
def save_as():
    file=filedialog.asksaveasfile(defaultextension='.txt',filetypes=[("Text file",".txt"),("python file",".py"),("all files",".*")])
    filetext=str(area.get('1.0',END))
    file.write(filetext)
    file.close()
    #to get a file name
    file_name=file.name
    if file_name is not None:
        w.title(os.path.basename(file_name))
def open_file():
    file_path=filedialog.askopenfile(defaultextension=".txt", filetypes=[("Text file",".txt"),("python file",".py"),("all files",".*")])
    file_name=file_path.name
    if file_name==None:
        file_name=None
    else:
        w.title(os.path.basename(file_name))
        area.delete("1.0",END)
        open_file=open(file_name,"r")
        content=open_file.read()
        area.insert("1.0",content)
        open_file.close()
def new_file():
    w.title("untitled-notpad")
    area.delete("1.0",END)
def cut():
    area.event_generate("<<Cut>>")
def copy():
    area.event_generate("<<Copy>>")
def paste():
    area.event_generate("<<Paste>>")
def Dark():
    area.configure(bg="black",fg="white")
def Light():
    area.configure(bg="white",fg="black")
def date_time():
    dt=str(datetime.now())
    area.insert("1.0",dt)
def body():
    #text area
    global area
    area = Text(w,bd=0,font=('times new roman',14),width=1200,height=700)
    area.pack()
    menubar=tk.Menu(w)
    fmenu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=fmenu)
    fmenu.add_command(label="New",command=new_file)
    fmenu.add_command(label="Open",command=open_file)
    fmenu.add_command(label="Save as",command=save_as)
    fmenu.add_separator()
    fmenu.add_command(label="Exit",command=exit)
    #create a edit menu
    edit_menu=tk.Menu(menubar,tearoff=False)
    menubar.add_cascade(label="Edit",menu=edit_menu)
    edit_menu.add_command(label="Cut",command=cut)
    edit_menu.add_command(label="Paste",command=copy)
    edit_menu.add_command(label="Copy",command=paste)
    edit_menu.add_separator()
    theam=tk.Menu(edit_menu,tearoff=0)
    edit_menu.add_cascade(label="Theam",menu=theam)
    theam.add_command(label="Dark",command=Dark)
    theam.add_command(label="Light",command=Light)
    edit_menu.add_command(label="Date and time",command=date_time)
    #Help menu
    help_menu=tk.Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=help_menu)
    help_menu.add_command(label="About app",command=about)
    help_menu.add_command(label="Exit",command=exit)
    w.config(menu=menubar)
    w.mainloop()
window()
body()