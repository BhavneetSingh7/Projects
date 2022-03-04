from menu import *
from tkinter import *

root = Tk()
root.title("Editor")
root.config(background="#424242")


m = Menu(root)
root.config(menu=m)


scroll = Scrollbar(root)
editArea = Text(root,width=151,height=40,foreground="#00CD00",fg="#00CD00",highlightcolor="#00CD00",highlightbackground="#00CD00",inactiveselectbackground="#00CD00",selectbackground="#00CD00",selectforeground="#00CD00",background="black",insertbackground="#00CD00",yscrollcommand=scroll.set)
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


Tab = Frame(root,height=20)
Tab.grid(row=0,column=1)

w=0
SideBar = Frame(root,width=w,height=1000,bg="#404040")
def chg():
    global w,SideBar,editArea
    if w==0:
        w = 150
        editArea.config(width=132)
        SideBar.config(width=w)
    else:
        w=0
        editArea.config(width=151)
        SideBar.config(width=w)
    return w

SidebarButton = Button(root,width=5,background="gray",command=chg)
SideBar.grid(row = 1,column=1)
SidebarButton.grid(row=1,column=0)

editArea.grid(row=1,column=4,sticky=(N,E,W,S))
scroll.grid(row=1,column=5, sticky=(N,S))
scroll.config(command=editArea.yview)


root.mainloop()
