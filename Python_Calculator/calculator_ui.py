#view
#Generates the user interface of the calculator
import tkinter as tk
import event_listener as e

def calculatorUI() :
    #window
    window = tk.Tk()
    window.geometry('240x360')
    window.title("Calculator")
    window.rowconfigure((0,1,2,3,4), weight=1)
    window.columnconfigure((0,1,2,3), weight=1)

    #input field
    myentry = tk.Entry(window, font=('Ariel', 20))
    myentry.grid(columnspan=4, sticky="nsew")

    #buttons
    #row1
    button1 = tk.Button(window, text="1", command= lambda: e.button1click(myentry))                 
    button1.grid(row=1, column=0, sticky="nsew")

    button2 = tk.Button(window, text="2", command= lambda: e.button2click(myentry))
    button2.grid(row=1, column=1, sticky="nsew")

    button3 = tk.Button(window, text="3", command= lambda: e.button3click(myentry))
    button3.grid(row=1, column=2, sticky="nsew")

    buttonAddition = tk.Button(window, text="+", command= lambda: e.Additionclick(myentry))
    buttonAddition.grid(row=1, column=3, sticky="nsew")

    #row2
    button4 = tk.Button(window, text="4", command= lambda: e.button4click(myentry))
    button4.grid(row=2, column=0, sticky="nsew")

    button5 = tk.Button(window, text="5", command= lambda: e.button5click(myentry))
    button5.grid(row=2, column=1, sticky="nsew")

    button6 = tk.Button(window, text="6", command= lambda: e.button6click(myentry))
    button6.grid(row=2, column=2, sticky="nsew")

    buttonSubtraction = tk.Button(window, text="-", command= lambda: e.Subtractionclick(myentry))
    buttonSubtraction.grid(row=2, column=3, sticky="nsew")

    #row3
    button7 = tk.Button(window, text="7", command= lambda: e.button7click(myentry))
    button7.grid(row=3, column=0, sticky="nsew")

    button8 = tk.Button(window, text="8", command= lambda: e.button8click(myentry))
    button8.grid(row=3, column=1, sticky="nsew")

    button9 = tk.Button(window, text="9", command= lambda: e.button9click(myentry))
    button9.grid(row=3, column=2, sticky="nsew")

    buttonMultiplication = tk.Button(window, text="*", command= lambda: e.Multiplicationclick(myentry))
    buttonMultiplication.grid(row=3, column=3, sticky="nsew")

    #row4
    buttonDelete = tk.Button(window, text="DEL", command= lambda: e.Deleteclick(myentry))
    buttonDelete.grid(row=4, column=0, sticky="nsew")

    button0 = tk.Button(window, text="0", command= lambda: e.button0click(myentry))
    button0.grid(row=4, column=1, sticky="nsew")

    buttonEqual = tk.Button(window, text="=", command= lambda: e.Equalclick(myentry))
    buttonEqual.grid(row=4, column=2, sticky="nsew")

    buttonDivison = tk.Button(window, text="/", command= lambda: e.Divisionclick(myentry))
    buttonDivison.grid(row=4, column=3, sticky="nsew")

    window.mainloop()
