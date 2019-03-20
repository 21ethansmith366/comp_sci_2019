from tkinter import*
import turtle
t = turtle.Pen()
t.speed(100)
master=Tk()

def left_spiral():
    for x in range (200):
    
        t.forward(x)
        t.left(300)
        
def square():
    for x in range (200):
    
        t.forward(x)
        t.left(90)
        
def triangle():
    for x in range (200):
    
        t.forward(x)
        t.left(120)

def make_it_red():
    t.pencolor("red")
    
def make_it_purple():
    t.pencolor("purple")


    
button1=Button(master,text="spiral", command=left_spiral)
button1.grid(row=1,column=0)

button2=Button(master, text="square", command=square)
button2.grid(row=1,column=1)

button3=Button(master,text="triangle", command=triangle)
button3.grid(row=1,column=2)

button4=Button(master,text="red", command=make_it_red)
button4.grid(row=2,column=0)

button5=Button(master,text="purple", command=make_it_purple)
button5.grid(row=2,column=1)

master.mainloop()
