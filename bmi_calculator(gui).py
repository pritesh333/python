from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

# gui
root = Tk()
root.title("BMI CALCULATOR")
root.geometry('500x500')

# bmi chart for reference
label1=Label(root,text="BMI                                Weight status")
label1.place(x=0,y=0)
label2=Label(root,text="Below 18.5	       Underweight")
label2.place(x=0,y=40)
label3=Label(root,text="18.5–24.9	       Healthy")
label3.place(x=0,y=60)
label4=Label(root,text="25.0–29.9	       Overweight")
label4.place(x=0,y=80)
label5=Label(root,text="30.0 and above	       Obese")
label5.place(x=0,y=100)


# input for height and weight
label6=Label(root, text="Enter your height in metres:")
label6.place(x=0,y=140)
e1=Entry(root,width=10,borderwidth=5)
e1.place(x=153,y=140)

label7=Label(root,text="Enter your weight in kilograms:")
label7.place(x=0,y=180)
e2=Entry(root,width=10,borderwidth=5)
e2.place(x=170,y=180)

def submit():
    height=e1.get()
    weight=e2.get()
    heightFLOAT=(float)(height)
    weightFLOAT=(float)(weight)
    bmiFLOAT=(float)(weightFLOAT/(heightFLOAT*heightFLOAT))

    bmi=(str)(bmiFLOAT)
    # printing bmi
    label8 = Label(root, text="Your BMI :"+bmi, borderwidth=20,width=25,bg='gray')
    label8.place(x=50, y=350)



# submit button
submit=tk.Button(root,text="submit",command=submit)
submit.place(x=150,y=250)

root.mainloop()
