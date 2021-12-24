from tkinter import *
import tkinter.font as f

root = Tk()
root.title("Calculator")

# Fonts
font = f.Font(family="Helvetica", size=20)


# Global variables
button_width = 3
button_height = 2

num1 = 0
num2 = 0

adding = False
substracting = False
multiplying = False
dividing = False


# Functions
def clear():
    global num1, num2, ent_display
    ent_display.delete(0, END)
    num1 = 0
    num2 = 0


def number_pressed(number):
    global num1, num2, adding, substracting, multiplying, dividing, ent_display
    
    if adding is False and substracting is False and multiplying is False and dividing is False:
        ent_display.insert(END, number)
        num1 = int(ent_display.get())

    elif adding is True or substracting is True or multiplying is True or dividing is True:
        ent_display.insert(END, number)
        num2 = int(ent_display.get())


    


def add():
    global adding, substracting, multiplying, dividing, ent_display
    
    adding = True
    substracting = False
    multiplying = False
    dividing = False

    ent_display.delete(0, END)


def substract():
    global adding, substracting, multiplying, dividing, ent_display

    substracting = True
    adding = False
    multiplying = False
    dividing = False

    ent_display.delete(0, END)


def multiply():
    global adding, substracting, multiplying, dividing, ent_display

    multiplying = True 
    adding = False
    substracting = False
    dividing = False

    ent_display.delete(0, END)


def divide():
    global adding, substracting, multiplying, dividing, ent_display

    dividing = True 
    adding = False
    substracting = False
    multiplying = False

    ent_display.delete(0, END)


def equal():
    global num1, num2, adding, substracting, multiplying, dividing, ent_display
    
    if adding is True:
        result = num1 + num2
    if substracting is True:
        result = num1 - num2
    if multiplying is True:
        result = num1 * num2
    if dividing is True:
        result = num1 / num2

    ent_display.delete(0, END)
    ent_display.insert(0, result)

    adding = False
    substracting = False
    multiplying = False
    dividing = False

    num1 = result
    num2 = 0

    



# Body

# Initialize all buttons
ent_display = Entry(root, font=font)

btn_7 = Button(root, text="7", width=button_width, height=button_height, command=lambda: number_pressed(7))
btn_8 = Button(root, text="8", width=button_width, height=button_height, command=lambda: number_pressed(8))
btn_9 = Button(root, text="9", width=button_width, height=button_height, command=lambda: number_pressed(9))

btn_4 = Button(root, text="4", width=button_width, height=button_height, command=lambda: number_pressed(4))
btn_5 = Button(root, text="5", width=button_width, height=button_height, command=lambda: number_pressed(5))
btn_6 = Button(root, text="6", width=button_width, height=button_height, command=lambda: number_pressed(6))

btn_1 = Button(root, text="1", width=button_width, height=button_height, command=lambda: number_pressed(1))
btn_2 = Button(root, text="2", width=button_width, height=button_height, command=lambda: number_pressed(2))
btn_3 = Button(root, text="3", width=button_width, height=button_height, command=lambda: number_pressed(3))

btn_0 = Button(root, text="0", width=button_width, height=button_height, command=lambda: number_pressed(0))
btn_clear = Button(root, text="CLR", width=button_width, height=button_height, command=clear)
btn_equal = Button(root, text="=", width=button_width, height=button_height, command=equal)

btn_add = Button(root, text="+", width=button_width, height=button_height, command=add)
btn_substract = Button(root, text="-", width=button_width, height=button_height, command=substract)
btn_multiply = Button(root, text="*", width=button_width, height=button_height,command=multiply)
btn_divide = Button(root, text="/", width=button_width, height=button_height, command=divide)

# Grid system of buttons
ent_display.grid(row=0, column=0, columnspan=4, sticky=EW)

btn_7.grid(row=1, column=0, sticky=EW)
btn_8.grid(row=1, column=1, sticky=EW)
btn_9.grid(row=1, column=2, sticky=EW)

btn_4.grid(row=2, column=0, sticky=EW)
btn_5.grid(row=2, column=1, sticky=EW)
btn_6.grid(row=2, column=2, sticky=EW)

btn_1.grid(row=3, column=0, sticky=EW)
btn_2.grid(row=3, column=1, sticky=EW)
btn_3.grid(row=3, column=2, sticky=EW)

btn_0.grid(row=4, column=0, sticky=EW)
btn_clear.grid(row=4, column=1, sticky=EW)
btn_equal.grid(row=4, column=2, sticky=EW)

btn_add.grid(row=1, column=3, sticky=EW)
btn_substract.grid(row=2, column=3, sticky=EW)
btn_multiply.grid(row=3, column=3, sticky=EW)
btn_divide.grid(row=4, column=3, sticky=EW)

root.mainloop()




