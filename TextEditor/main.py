from menu import *
from tkinter import *


root = Tk()
root.title("Editor")


m = Menu(root)
root.config(menu=m)


scroll = Scrollbar(root)
editArea = Text(root,width=140,height=39,yscrollcommand=scroll.set)
t = editArea.get("1.0","1.10")


filemenu = Menu(m)
FILE = File(filemenu)
m.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=FILE.New)
filemenu.add_command(label='Open',command=FILE.Open)
filemenu.add_command(label='Save',command=FILE.Save)
filemenu.add_command(label='Save as',command=FILE.SaveAs)
filemenu.add_command(label='Close',command=FILE.Close)
filemenu.add_command(label='Exit',command=FILE.Exit)


editmenu = Menu(m)
EDIT = Edit(filemenu)
m.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Cut',command=EDIT.Cut)
editmenu.add_command(label='Copy',command=EDIT.Copy)
editmenu.add_command(label='Paste',command=EDIT.Paste)
editmenu.add_command(label='Undo',command=EDIT.Undo)
editmenu.add_command(label='Redo',command=EDIT.Redo)
editmenu.add_command(label='Find',command=EDIT.Find)
editmenu.add_command(label='Replace',command=EDIT.Replace)
editmenu.add_command(label='Select All',command=EDIT.SelectAll)
editmenu.add_command(label='Comment Region',command=EDIT.CommentRegion)
editmenu.add_command(label='Uncomment Region',command=EDIT.UnCommentRegion)


editArea.grid(row=0,column=4,sticky=(N,E,W,S))
scroll.grid(row=0,column=5, sticky=(N,S))
scroll.config(command=editArea.yview)


root.mainloop()
