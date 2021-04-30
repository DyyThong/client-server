from client import client_send
from tkinter import *
from client2 import client_send2

window=Tk()
window.geometry("300x300")
window.title("Computer Stats")

def exit1():
    exit()


label1 = Label(window,text = "Computer Statistic",fg = 'blue', relief = 'solid', font = ("arial",16,"bold")).pack()

label2 = Label(window,text = "Look at the terminal!!!",fg='black',font = ("arial",14,"bold"))
label2.place(x=50,y=50)

b1=Button(text="Client connect",bg='blue',fg='black',relief="solid",width=10,height=3,command=client_send)
b1.place(x=5,y=150)

b2=Button(text="New Client",bg='blue',fg='black',relief="solid",width=10,height=3,command=client_send2)
b2.place(x=105,y=150)

b3=Button(window,text="Quit",bg='brown',fg='black',relief="solid",width=10,height=3,command=exit1)
b3.place(x=205,y=150)

window.mainloop()