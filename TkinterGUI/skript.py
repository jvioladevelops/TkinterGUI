from tkinter import *


window = Tk()
#name it anything you like

def km_to_miles():
    #print(e1_value.get())
    miles=float(e1_value.get())*1.606
    t1.insert(END, miles)#the place to you want to insert

b1 = Button(window, text="finish", command=km_to_miles) #command points to a function when button is pressed 
b1.grid(row=0, column=0) #display the button you can use pack() and  also use the grid(row=0, column=1) add the rowspan=2 argument to span multiplerows more control of position method 

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)

window.mainloop()
#leave this at the end of code 