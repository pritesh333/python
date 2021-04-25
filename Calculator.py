from tkinter import *

root=Tk()
root.title("Caclculator")
root.geometry("550x400")

e=Entry(root,borderwidth=10,width=50)
root.iconbitmap("calculator.ico")

e.grid(column=0,row=0,columnspan=3,padx=20,pady=10)

def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def add():
    first_number=e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)



def button_Equal():
    second_number=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0, f_num + int(second_number))

    elif math=="subtraction":
        e.insert(0, f_num - int(second_number))

    elif math=="multiplication":
        e.insert(0, f_num * int(second_number))

    elif math=="division":
        e.insert(0, f_num / int(second_number))


#Make Buttons
button1=Button(root,text="1",padx=15,pady=15,borderwidth=3,command=lambda: button_click(1))
button2=Button(root,text="2",padx=15,pady=15,borderwidth=3,command=lambda: button_click(2))
button3=Button(root,text="3",padx=15,pady=15,borderwidth=3,command=lambda: button_click(3))
button4=Button(root,text="4",padx=15,pady=15,borderwidth=3,command=lambda: button_click(4))
button5=Button(root,text="5",padx=15,pady=15,borderwidth=3,command=lambda: button_click(5))
button6=Button(root,text="6",padx=15,pady=15,borderwidth=3,command=lambda: button_click(6))
button7=Button(root,text="7",padx=15,pady=15,borderwidth=3,command=lambda: button_click(7))
button8=Button(root,text="8",padx=15,pady=15,borderwidth=3,command=lambda: button_click(8))
button9=Button(root,text="9",padx=15,pady=15,borderwidth=3,command=lambda: button_click(9))
button0=Button(root,text="0",padx=15,pady=15,borderwidth=3,command=lambda: button_click(0))
button_ac=Button(root,text="AC",padx=9,pady=15,borderwidth=3,command=button_clear)
button_equal=Button(root,text="=",padx=14,pady=15,borderwidth=3,command=button_Equal)

button_add=Button(root,text="+",padx=15,pady=15,borderwidth=5,command=add)
button_subtract=Button(root,text="-",padx=16,pady=15,borderwidth=5,command=sub)
button_multiply=Button(root,text="x",padx=16,pady=15,borderwidth=5,command=mult)
button_division=Button(root,text="÷",padx=14,pady=15,borderwidth=5,command=div)


#Place Buttons
button1.place(x=60,y=100)
button2.place(x=105,y=100)
button3.place(x=150,y=100)
button4.place(x=60,y=155)
button5.place(x=105,y=155)
button6.place(x=150,y=155)
button7.place(x=60,y=210)
button8.place(x=105,y=210)
button9.place(x=150,y=210)
button0.place(x=105,y=265)
button_ac.place(x=60,y=265)
button_equal.place(x=150,y=265)

button_add.place(x=290,y=80)
button_subtract.place(x=290,y=140)
button_multiply.place(x=290,y=200)
button_division.place(x=290,y=260)

root.mainloop()
