import tkinter

root = tkinter.Tk()
root.title('calculator')

e = tkinter.Entry(root, width=20, borderwidth=5, bg='grey', font=("Helvetica", 14))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def Button_Click(number):
    # e.delete(0, tkinter.END)
    current = e.get()
    e.delete(0, tkinter.END)
    e.insert(0, str(current) + str(number))


# clear field
def Button_Clear():
    e.delete(0, tkinter.END)


# addition
def Button_Add():
    FirstNumber = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(FirstNumber)
    e.delete(0, tkinter.END)


# divide
def Button_divide():
    FirstNumber = e.get()
    global f_num
    global math
    math = 'divide'
    f_num = int(FirstNumber)
    e.delete(0, tkinter.END)


# multiply
def Button_multiply():
    FirstNumber = e.get()
    global f_num
    global math
    math = 'multiply'
    f_num = int(FirstNumber)
    e.delete(0, tkinter.END)


def Button_subtract():
    FirstNumber = e.get()
    global f_num
    global math
    math = 'subtract'
    f_num = int(FirstNumber)
    e.delete(0, tkinter.END)


# equal
def Button_Equal():

    second_number = e.get()
    e.delete(0, tkinter.END)

    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    elif math == 'subtract':
        e.insert(0, f_num - int(second_number))
    elif math == 'multiply':
        e.insert(0, f_num * int(second_number))
    elif math == 'divide':
        e.insert(0, f_num / int(second_number))


# Define buttons
button_1 = tkinter.Button(root, text='1', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(1))
button_2 = tkinter.Button(root, text='2', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(2))
button_3 = tkinter.Button(root, text='3', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(3))
button_4 = tkinter.Button(root, text='4', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(4))
button_5 = tkinter.Button(root, text='5', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(5))
button_6 = tkinter.Button(root, text='6', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(6))
button_7 = tkinter.Button(root, text='7', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(7))
button_8 = tkinter.Button(root, text='8', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(8))
button_9 = tkinter.Button(root, text='9', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(9))
button_0 = tkinter.Button(root, text='0', padx=40, pady=20, bg='grey', font=("Helvetica", 18),
                          command=lambda: Button_Click(0))

button_add = tkinter.Button(root, text='+', padx=39, pady=20, bg='grey', font=("Helvetica", 18),
                            command=Button_Add)
button_multiply = tkinter.Button(root, text='x', padx=42, pady=20, bg='grey', font=("Helvetica", 18),
                                 command=Button_multiply)
button_divide = tkinter.Button(root, text='/', padx=42, pady=20, bg='grey', font=("Helvetica", 18),
                               command=Button_divide)
button_subtract = tkinter.Button(root, text='-', padx=42, pady=20, bg='grey', font=("Helvetica", 18),
                                 command=Button_subtract)

button_equal = tkinter.Button(root, text='=', padx=96, pady=20, bg='grey', font=("Helvetica", 18),
                              command=Button_Equal)
button_clear = tkinter.Button(root, text='Clear', padx=74, pady=20, bg='grey', font=("Helvetica", 18),
                              command=Button_Clear)

# buttons on screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1, columnspan=3)
button_clear.grid(row=4, column=1, columnspan=3)

root.mainloop()
