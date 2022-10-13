from tkinter import *
from math import pi

def solve():
    try:
        answer.delete(0, END)
        r = int(radius.get())
        area = pi*(r**2)
        answer.insert(END, round(area, 2))

    except:
        answer.delete(0, END)
        d = int(diameter.get())
        area = (pi*(d**2))/4
        answer.insert(END, round(area, 2))

window = Tk()
window.geometry("400x150")
window.title("Area of Circle")

radius = Entry(window)
radius.place(x=100, y=7)
radtxt = Label(window, text="Radius")
radtxt.place(x=30, y=7)
diatxt = Label(window, text="Diameter")
diatxt.place(x=30, y= 37)
diameter = Entry(window)
diameter.place(x=100, y=37)
answer = Entry(window)
answer.place(x=135, y=100)
answertxt = Label(window, text="The area is")
answertxt.place(x=70, y=100)


compute = Button(window, text="Solve", command=solve)
compute.place(x=175, y=67)



window.mainloop()
