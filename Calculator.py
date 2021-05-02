from tkinter import *
import math
import numpy as np

root = Tk()
root.title("Caclculator")
root.geometry("550x400")
root.configure(bg='gray50')

e = Entry(root, borderwidth=5, width=70)
root.iconbitmap("calculator.ico")

e.grid(column=0, row=0, columnspan=3, padx=65, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))


def button_clear():
    e.delete(0, END)


def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)


def sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)


def mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)


def div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)


def square():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, f_num * f_num)


def cube():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, f_num * f_num*f_num)


def square_root():
    first_number = e.get()
    sqrtvar =(float)(first_number)
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, math.sqrt(sqrtvar))


def cube_root():
    first_number = e.get()
    cbrtvar = (float)(first_number)
    ans=np.cbrt(cbrtvar)
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, ans)

def logarithm():
    first_number = e.get()
    logvar = (int)(first_number)
    ans=np.log10(logvar)
    global f_num
    f_num = int(first_number)
    e.delete(0, END)
    e.insert(0, ans)

def sin():
    first_number = e.get()
    sinfn = (float)(first_number)
    ans=np.sin(np.deg2rad(sinfn))
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, ans)

def cos():
    first_number = e.get()
    sinfn = (float)(first_number)
    ans=np.cos(np.deg2rad(sinfn))
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, ans)

def tan():
    first_number = e.get()
    sinfn = (float)(first_number)
    ans=np.tan(np.deg2rad(sinfn))
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
    e.insert(0, ans)

def pi():
    e.delete(0, END)
    pi=3.14
    e.insert(0,(float)(pi))

def celtofar():
    first_number = e.get()
    celtemp=(float)(first_number)
    ans=(float)((celtemp*1.8)+32)
    e.delete(0, END)
    e.insert(0, (float)(ans))

def fartocel():
    first_number = e.get()
    fartemp=(float)(first_number)
    ans=(float)((5*(fartemp-32))/9)
    e.delete(0, END)
    e.insert(0, (float)(ans))


def euler_no():
    e.delete(0, END)
    eul = 2.718
    e.insert(0, (float)(eul))


def button_Equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
        e.insert(0, f_num + float(second_number))

    elif math == "subtraction":
        e.insert(0, f_num - float(second_number))

    elif math == "multiplication":
        e.insert(0, f_num * float(second_number))

    elif math == "division":
        e.insert(0, f_num / float(second_number))


# Make Buttons
button1 = Button(root, text="1",padx=15, pady=15, borderwidth=3, command=lambda: button_click(1),bg='snow')
button2 = Button(root, text="2",padx=15, pady=15, borderwidth=3, command=lambda: button_click(2),bg='snow')
button3 = Button(root, text="3",padx=15, pady=15, borderwidth=3, command=lambda: button_click(3),bg='snow')
button4 = Button(root, text="4",padx=15, pady=15, borderwidth=3, command=lambda: button_click(4),bg='snow')
button5 = Button(root, text="5",padx=15, pady=15, borderwidth=3, command=lambda: button_click(5),bg='snow')
button6 = Button(root, text="6",padx=15, pady=15, borderwidth=3, command=lambda: button_click(6),bg='snow')
button7 = Button(root, text="7",padx=15, pady=15, borderwidth=3, command=lambda: button_click(7),bg='snow')
button8 = Button(root, text="8",padx=15, pady=15, borderwidth=3, command=lambda: button_click(8),bg='snow')
button9 = Button(root, text="9",padx=15, pady=15, borderwidth=3, command=lambda: button_click(9),bg='snow')
button0 = Button(root, text="0",padx=15, pady=15, borderwidth=3, command=lambda: button_click(0),bg='snow')
button_ac = Button(root, text="AC", padx=9, pady=15, borderwidth=3, command=button_clear,bg='misty rose')
button_equal = Button(root, text="=", padx=14, pady=15, borderwidth=3, command=button_Equal,bg='misty rose')

button_add = Button(root, text="+", padx=15, pady=15, borderwidth=5, command=add)
button_subtract = Button(root, text="-", padx=16, pady=15, borderwidth=5, command=sub)
button_multiply = Button(root, text="x", padx=16, pady=15, borderwidth=5, command=mult)
button_division = Button(root, text="÷", padx=14, pady=15, borderwidth=5, command=div)
button_sqaure = Button(root, text="x²", padx=16, pady=15, borderwidth=4, command=square)
button_cube = Button(root, text="x³", padx=16, pady=15, borderwidth=4, command=cube)
button_sqrt = Button(root, text="√", padx=17, pady=15, borderwidth=4, command=square_root)
button_cbrt = Button(root, text="³√", padx=14, pady=15, borderwidth=4, command=cube_root)
button_log = Button(root, text="log", padx=12, pady=15, borderwidth=4, command=logarithm)
button_sin = Button(root, text="sin", padx=13, pady=15, borderwidth=4, command=sin)
button_cos = Button(root, text="cos", padx=12, pady=15, borderwidth=4, command=cos)
button_tan = Button(root, text="tan", padx=12, pady=15, borderwidth=4, command=tan)
button_pi = Button(root, text="π", padx=15, pady=15, borderwidth=4, command=pi)
button_celtofar = Button(root, text="C→F", padx=7, pady=15, borderwidth=4, command=celtofar)
button_fartocel = Button(root, text="F→C", padx=7, pady=15, borderwidth=4, command=fartocel)
button_euler_no = Button(root, text="e", padx=15, pady=15, borderwidth=4, command=euler_no)


# Place Buttons
button1.place(x=60, y=100)
button2.place(x=105, y=100)
button3.place(x=150, y=100)
button4.place(x=60, y=155)
button5.place(x=105, y=155)
button6.place(x=150, y=155)
button7.place(x=60, y=210)
button8.place(x=105, y=210)
button9.place(x=150, y=210)
button0.place(x=105, y=265)
button_ac.place(x=60, y=265)
button_equal.place(x=150, y=265)

button_add.place(x=290, y=80)
button_subtract.place(x=290, y=140)
button_multiply.place(x=290, y=200)
button_division.place(x=290, y=260)
button_sqaure.place(x=345, y=80)
button_cube.place(x=345, y=140)
button_sqrt.place(x=345, y=200)
button_cbrt.place(x=345, y=260)
button_log.place(x=400, y=80)
button_sin.place(x=400, y=140)
button_cos.place(x=400, y=200)
button_tan.place(x=400, y=260)
button_pi.place(x=455, y=80)
button_celtofar.place(x=455, y=140)
button_fartocel.place(x=455, y=200)
button_euler_no.place(x=455, y=260)

root.mainloop()


