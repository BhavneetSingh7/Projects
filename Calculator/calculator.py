from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry('422x320')

e = Entry(root, width = 40, borderwidth = 5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def Ins(num):
    current = e.get()
    e.delete(0,END)
    e.insert(0,current + num)

def C():
    e.delete(0,END)
    e.insert(0,"")

def EVAL():
    val = list(e.get())
    value = e.get()

    first = value[0]
    if first == 'x' or first == '-' or first == '+' or first == '':
        e.delete(0,END)
        return e.insert(0,value)
    last = value[-1]
    if last == 'x' or last == '-' or last == '+' or last == '':
        e.delete(0,END)
        return e.insert(0,value)
    
    if val != []:
        temp = ""
        for i in val:
            if i=="x":
                i = "*"
            temp = temp + i
        val = temp
    else :
        return e.insert(0,"")
    x = eval(val)
    e.delete(0,END)
    e.insert(0,str(x))

btn_1 = Button(root, text="1", padx=40, pady=20, command=lambda : Ins("1"))
btn_2 = Button(root, text="2", padx=40, pady=20, command=lambda : Ins("2"))
btn_3 = Button(root, text="3", padx=40, pady=20, command=lambda : Ins("3"))
btn_4 = Button(root, text="4", padx=40, pady=20, command=lambda : Ins("4"))
btn_5 = Button(root, text="5", padx=40, pady=20, command=lambda : Ins("5"))
btn_6 = Button(root, text="6", padx=40, pady=20, command=lambda : Ins("6"))
btn_7 = Button(root, text="7", padx=40, pady=20, command=lambda : Ins("7"))
btn_8 = Button(root, text="8", padx=40, pady=20, command=lambda : Ins("8"))
btn_9 = Button(root, text="9", padx=40, pady=20, command=lambda : Ins("9"))
btn_0 = Button(root, text="0", padx=40, pady=20, command=lambda : Ins("0"))

btn_dot = Button(root, text=".", padx=40, pady=20, command=lambda : Ins("."))
btn_add = Button(root, text="+", padx=40, pady=20, command=lambda : Ins("+"))
btn_sub = Button(root, text="-", padx=60, pady=20, command=lambda : Ins("-"))
btn_mul = Button(root, text="x", padx=60, pady=20, command=lambda : Ins("x"))
btn_div = Button(root, text="/", padx=60, pady=20, command=lambda : Ins("/"))
btn_equal = Button(root, text="=", padx=60, pady=20, command=EVAL)
btn_clear = Button(root, text="C", padx=60, pady=20, command=C)

btn_0.grid(row=4,column=1)
btn_1.grid(row=3,column=0)
btn_2.grid(row=3,column=1)
btn_3.grid(row=3,column=2)
btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)
btn_7.grid(row=1,column=0)
btn_8.grid(row=1,column=1)
btn_9.grid(row=1,column=2)

btn_add.grid(row=4,column=2)
btn_dot.grid(row=4,column=0)
btn_clear.grid(row=0,column=4)
btn_equal.grid(row=1,column=4)
btn_sub.grid(row=2,column=4)
btn_mul.grid(row=3,column=4)
btn_div.grid(row=4,column=4)

root.mainloop()
