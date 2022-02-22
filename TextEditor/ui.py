import features
from tkinter import *

root = Tk()
root.geometry("800x500")
root.title(' '*1 + 'Editor')


########################
#        MENU

m = Menu(root)
root.config(menu=m)

filemenu = Menu(m)
m.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open')
filemenu.add_command(label='Save')

view = Menu(m)
m.add_cascade(label='View',menu=view)
view.add_command(label='Layout')
view.add_command(label='Appearance')
view.add_checkbutton(label='Word Wrap')

Help = Menu(m)
m.add_cascade(label='Help',menu=Help)
Help.add_command(label='About')



############################
#        SIDEBAR

margin = Frame(root,width=110,height=200)
margin.grid(row=0,column=3)


##################################
#          EDITING AREA

scroll = Scrollbar(root)

editArea = Text(root,width=140,height=39,yscrollcommand=scroll.set)
t = editArea.get("1.0","1.10")
editArea.grid(row=0,column=4,sticky=(N,E,W,S))

scroll.grid(row=0,column=5, sticky=(N,S))
scroll.config(command=editArea.yview)

l = Label(margin,text="b hgvferwferer42433hv"+str(t))
l.grid(row=1,column=1)

root.mainloop()
