from tkinter import *
import tkinter.font as f

root = Tk()
root.title("Calculator")

# Fonts
font = f.Font(family="Helvetica", size=20)



class Calculator:
    def __init__(self):
        self.button_width = 3
        self.button_height = 2

        self.num1 = 0
        self.num2 = 0

        self.adding = False
        self.substracting = False
        self.multiplying = False
        self.dividing = False

    def display(self):
        # Initialize all buttons
        self.ent_display = Entry(root, font=font)

        self.btn_7 = Button(root, text="7", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(7))
        self.btn_8 = Button(root, text="8", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(8))
        self.btn_9 = Button(root, text="9", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(9))

        self.btn_4 = Button(root, text="4", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(4))
        self.btn_5 = Button(root, text="5", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(5))
        self.btn_6 = Button(root, text="6", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(6))

        self.btn_1 = Button(root, text="1", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(1))
        self.btn_2 = Button(root, text="2", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(2))
        self.btn_3 = Button(root, text="3", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(3))

        self.btn_0 = Button(root, text="0", width=self.button_width, height=self.button_height, command=lambda: self.number_pressed(0))
        self.btn_clear = Button(root, text="CLR", width=self.button_width, height=self.button_height, command=self.clear)
        self.btn_equal = Button(root, text="=", width=self.button_width, height=self.button_height, command=self.equal)

        self.btn_add = Button(root, text="+", width=self.button_width, height=self.button_height, command=self.add)
        self.btn_substract = Button(root, text="-", width=self.button_width, height=self.button_height, command=self.substract)
        self.btn_multiply = Button(root, text="*", width=self.button_width, height=self.button_height, command=self.multiply)
        self.btn_divide = Button(root, text="/", width=self.button_width, height=self.button_height, command=self.divide)

        # Grid system of buttons
        self.ent_display.grid(row=0, column=0, columnspan=4, sticky=EW)

        self.btn_7.grid(row=1, column=0, sticky=EW)
        self.btn_8.grid(row=1, column=1, sticky=EW)
        self.btn_9.grid(row=1, column=2, sticky=EW)

        self.btn_4.grid(row=2, column=0, sticky=EW)
        self.btn_5.grid(row=2, column=1, sticky=EW)
        self.btn_6.grid(row=2, column=2, sticky=EW)

        self.btn_1.grid(row=3, column=0, sticky=EW)
        self.btn_2.grid(row=3, column=1, sticky=EW)
        self.btn_3.grid(row=3, column=2, sticky=EW)

        self.btn_0.grid(row=4, column=0, sticky=EW)
        self.btn_clear.grid(row=4, column=1, sticky=EW)
        self.btn_equal.grid(row=4, column=2, sticky=EW)

        self.btn_add.grid(row=1, column=3, sticky=EW)
        self.btn_substract.grid(row=2, column=3, sticky=EW)
        self.btn_multiply.grid(row=3, column=3, sticky=EW)
        self.btn_divide.grid(row=4, column=3, sticky=EW)

    
    def clear(self):
        self.ent_display.delete(0, END)
        self.num1 = 0
        self.num2 = 0


    def number_pressed(self, number):
        if self.adding is False and self.substracting is False and self.multiplying is False and self.dividing is False:
            self.ent_display.insert(END, number)
            self.num1 = int(self.ent_display.get())

        elif self.adding is True or self.substracting is True or self.multiplying is True or self.dividing is True:
            self.ent_display.insert(END, number)
            self.num2 = int(self.ent_display.get())


    def add(self):
        self.adding = True
        self.substracting = False
        self.multiplying = False
        self.dividing = False

        self.ent_display.delete(0, END)


    def substract(self):
        self.substracting = True
        self.adding = False
        self.multiplying = False
        self.dividing = False

        self.ent_display.delete(0, END)


    def multiply(self):
        self.multiplying = True 
        self.adding = False
        self.substracting = False
        self.dividing = False

        self.ent_display.delete(0, END)


    def divide(self):
        self.dividing = True 
        self.adding = False
        self.substracting = False
        self.multiplying = False

        self.ent_display.delete(0, END)


    def equal(self):       
        if self.adding is True:
            result = self.num1 + self.num2
        if self.substracting is True:
            result = self.num1 - self.num2
        if self.multiplying is True:
            result = self.num1 * self.num2
        if self.dividing is True:
            result = self.num1 / self.num2

        self.ent_display.delete(0, END)
        self.ent_display.insert(0, result)

        self.adding = False
        self.substracting = False
        self.multiplying = False
        self.dividing = False

        self.num1 = result
        self.num2 = 0


if __name__ == "__main__":
    calc = Calculator()
    calc.display()
    mainloop()
