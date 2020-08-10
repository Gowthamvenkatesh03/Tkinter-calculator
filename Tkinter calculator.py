# Python program to  create a simple GUI  
# calculator using Tkinter 
  
# import everything from tkinter module
import tkinter as tk
from tkinter import *
import time
import datetime

  
# globally declare the expression variable 
expression = "" 
  
  
# Function to update expressiom 
# in the text entry box 
def press(num): 
    # point out the global expression variable 
    global expression 
  
    # concatenation of string 
    expression = expression + str(num) 
  
    # update the expression by using set method 
    equation.set(expression)

def tick(time1=''):
    # get the current time from the PC
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
 
    clock.after(1,tick)
  
  
# Function to evaluate the final expression 
def equalpress(): 
    # Try and except statement is used 
    # for handling the errors like zero 
    # division error etc. 
  
    # Put that code inside the try block 
    # which may generate the error 
    try: 
  
        global expression 
  
        # eval function evaluate the expression 
        # and str function convert the result 
        # into string 
        total = str(eval(expression)) 
  
        equation.set(total) 
  
        # initialze the expression variable 
        # by empty string 
        expression = "" 
  
    # if error is generate then handle 
    # by the except block 
    except: 
  
        equation.set(" error ") 
        expression = "" 
  
  
# Function to clear the contents 
# of text entry box 
def clear(): 
    global expression 
    expression = "" 
    equation.set("") 
  
  
# Driver code 
if __name__ == "__main__": 
    # create a GUI window 
    gui = Tk() 
  
    # set the background colour of GUI window 
    gui.configure(background="Black") 
  
    # set the title of GUI window 
    gui.title("Tkinter Calculator") 
  
    # set the configuration of GUI window 
    gui.geometry("365x420") 
  
    # StringVar() is the variable class 
    # we create an instance of this class 
    equation = StringVar()
   
    clock=tk.Label(gui,font=('arial', 20, 'bold'))
    #clock.grid()
    tick()


  
    # create the text entry box for 
    # showing the expression .
    clock.grid(columnspan=4,ipadx=24,ipady=0)
    expression_field = Entry(gui,font=('arial',20,'bold'),bd=10,insertwidth=600,bg="white",fg="black",textvariable=equation)
    
  
    # grid method is used for placing 
    # the widgets at respective positions 
    # in table like structure . 
    expression_field.grid(columnspan=4, ipadx=24,ipady=0) 
  
    equation.set('')

    
  
    # create a Buttons and place at a particular 
    # location inside the root window . 
    # when user press the button, the command or 
    # function affiliated to that button is executed . 
    button1 = Button(gui,font=("arial"),bd=10, text=' 1 ', fg='black', bg='white', 
                     command=lambda: press(1), height=2, width=7) 
    button1.grid(row=2, column=0) 
  
    button2 = Button(gui,font=("arial"),bd=10, text=' 2 ', fg='black', bg='white', 
                     command=lambda: press(2), height=2, width=7) 
    button2.grid(row=2, column=1) 
  
    button3 = Button(gui,font=("arial"),bd=10, text=' 3 ', fg='black', bg='white', 
                     command=lambda: press(3), height=2, width=7) 
    button3.grid(row=2, column=2) 
  
    button4 = Button(gui,font=("arial"),bd=10, text=' 4 ', fg='black', bg='white', 
                     command=lambda: press(4), height=2, width=7) 
    button4.grid(row=3, column=0) 
  
    button5 = Button(gui,font=("arial"),bd=10, text=' 5 ', fg='black', bg='white', 
                     command=lambda: press(5), height=2, width=7) 
    button5.grid(row=3, column=1) 
  
    button6 = Button(gui,font=("arial"),bd=10, text=' 6 ', fg='black', bg='white', 
                     command=lambda: press(6), height=2, width=7) 
    button6.grid(row=3, column=2) 
  
    button7 = Button(gui,font=("arial"),bd=10, text=' 7 ', fg='black', bg='white', 
                     command=lambda: press(7), height=2, width=7) 
    button7.grid(row=4, column=0) 
  
    button8 = Button(gui,font=("arial"),bd=10, text=' 8 ', fg='black', bg='white', 
                     command=lambda: press(8), height=2, width=7) 
    button8.grid(row=4, column=1) 
  
    button9 = Button(gui,font=("arial"),bd=10, text=' 9 ', fg='black', bg='white', 
                     command=lambda: press(9), height=2, width=7) 
    button9.grid(row=4, column=2) 
  
    button0 = Button(gui,font=("arial"),bd=10, text=' 0 ', fg='black', bg='white', 
                     command=lambda: press(0), height=2, width=7) 
    button0.grid(row=5, column=0) 
  
    plus = Button(gui,font=("arial"),bd=10, text=' + ', fg='black', bg='white', 
                  command=lambda: press("+"), height=2, width=7) 
    plus.grid(row=2, column=3) 
  
    minus = Button(gui,font=("arial"),bd=10, text=' - ', fg='black', bg='white', 
                   command=lambda: press("-"), height=2, width=7) 
    minus.grid(row=3, column=3) 
  
    multiply = Button(gui,font=("arial"),bd=10, text=' * ', fg='black', bg='white', 
                      command=lambda: press("*"), height=2, width=7) 
    multiply.grid(row=4, column=3) 
  
    divide = Button(gui,font=("arial"),bd=10, text=' / ', fg='black', bg='white', 
                    command=lambda: press("/"), height=2, width=7) 
    divide.grid(row=5, column=3) 
  
    equal = Button(gui,font=("arial"),bd=10, text=' = ', fg='black', bg='white', 
                   command=equalpress, height=2, width=7) 
    equal.grid(row=6, column=2) 
  
    clear = Button(gui,font=("arial"),bd=10, text='Clear', fg='black', bg='white', 
                   command=clear, height=2, width=7) 
    clear.grid(row=6, column=3) 
  
    Decimal= Button(gui,font=("arial"),bd=10,text='.', fg='black', bg='white', 
                    command=lambda: press('.'),height=2, width=7) 
    Decimal.grid(row=6, column=0)

    pi= Button(gui,font=("arial"),bd=10,text='pi', fg='black', bg='white', 
                    command=lambda: press(3.14),height=2, width=7) 
    pi.grid(row=5, column=2)

    percent= Button(gui,font=("arial"),bd=10,text='%', fg='black', bg='white', 
                    command=lambda: press("*0.01"),height=2, width=7) 
    percent.grid(row=6, column=1)

    double= Button(gui,font=("arial"),bd=10,text='00', fg='black', bg='white', 
                    command=lambda: press("00"),height=2, width=7) 
    double.grid(row=5, column=1)
    # start the GUI 
gui.mainloop()
