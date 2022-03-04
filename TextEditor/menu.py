from tkinter import *
import tkinter.filedialog


class File:
    def __init__(self,base) -> None:
        self.base = base
    
    def New(self):
        val = Label(self.base,text="heyyyyyyyyyyy")
        val.pack()

    def Open(self):
        val = tkinter.filedialog.askopenfilename()

    def Save(self):
        pass

    def SaveAs(self):
        pass

    def Close(self):
        pass

    def Exit(self):
        pass


class Edit:
    def __init__(self,base) -> None:
        self.base = base
    
    def Cut(self):
        pass

    def Copy(self):
        pass

    def Paste(self):
        pass

    def Undo(self):
        pass

    def Redo(self):
        pass
    
    def Find(self):
        pass
    
    def Replace(self):
        pass

    def SelectAll(self):
        pass

    def CommentRegion(self):
        pass

    def UnCommentRegion(Self):
        pass


class View:
    def __init__(self,base) -> None:
        self.base = base
    # """Word Wrap
    #    Extensions
    #    Show side bar
    #    Show Menu bar
    #    Themes
    #    Full Screen
    #    Line numbers
    #    Font
    #    """
    pass


class Run:
    def __init__(self,base) -> None:
        self.base = base
    pass


class Configure:
    def __init__(self,base) -> None:
        self.base = base
    pass


class Window:
    def __init__(self,base) -> None:
        self.base = base
    pass
