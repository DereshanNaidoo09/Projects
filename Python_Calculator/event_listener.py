#controller
#
import tkinter as tk
import calculator_logic as cl

equation_string = ""

#updates input field after button click
def update_equation_string(myentry, text):
    global equation_string
    equation_string += text
    myentry.delete(0,tk.END)
    myentry.insert(0,equation_string)

def button0click(myentry):
	update_equation_string(myentry, "0")

def button1click(myentry):
	update_equation_string(myentry, "1")

def button2click(myentry):
    update_equation_string(myentry, "2")

def button3click(myentry):
    update_equation_string(myentry, "3")

def button4click(myentry):
    update_equation_string(myentry, "4")

def button5click(myentry):
    update_equation_string(myentry, "5")

def button6click(myentry):
    update_equation_string(myentry, "6")

def button7click(myentry):
    update_equation_string(myentry, "7")

def button8click(myentry):
    update_equation_string(myentry, "8")

def button9click(myentry):
    update_equation_string(myentry, "9")
	
def Additionclick(myentry):
    update_equation_string(myentry, "+")

def Multiplicationclick(myentry):
    update_equation_string(myentry, "*")

def Subtractionclick(myentry):
    update_equation_string(myentry,"-")

def Divisionclick(myentry):
    update_equation_string(myentry,"/")
		
#clears input field    
def Deleteclick(myentry):
    global equation_string
    myentry.delete(0,tk.END)
    equation_string = ""

#solves equation and displays it on the input field
def Equalclick(myentry):
    global equation_string
    myentry.delete(0,tk.END)
    answer = cl.calculate(equation_string)
    myentry.insert(0,answer)
    equation_string = ""

   