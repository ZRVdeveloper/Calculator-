#! Калькулятор
from tkinter import *
from tkinter import messagebox
window = Tk()
one = IntVar() #StringVar()
two = IntVar() #IntVar()
photo1 = PhotoImage(file = "plus.png").subsample(2) #only *.PNG
photo2 = PhotoImage(file = "minus.png").subsample(2) #only *.PNG
photo3 = PhotoImage(file = "dobutok.png").subsample(2) #only *.PNG
photo4 = PhotoImage(file = "btn4.png").subsample(2) #only *.PNG
def click(c):
    try:
        a = one.get()
        b = two.get()
    except TclError:
        messagebox.showerror('Помилка','Вводити можна лише числа')
        a = 0
        b = 0        
    if c == 1: title.config(text = "Отримаємо: {} + {} = {}".format(a,b,a+b))
    if c == 2: title.config(text = "Отримаємо: {} - {} = {}".format(a,b,a-b))
    if c == 3: title.config(text = "Отримаємо: {} * {} = {}".format(a,b,a*b))
    if c == 4:
        try:
            title.config(text = "Отримаємо: {} : {} = {}".format(a,b,round((a/b),3)))
        except ZeroDivisionError:
            messagebox.showerror('Помилка нуля','Неможна ділити на нуль')        
first = Entry(textvariable=one, font = 40)

first.grid(row = 0, columnspan=2)
second = Entry(textvariable=two, font = 40)
second.grid(row = 1, columnspan=2)
title = Label(text = "",font=16)
title.grid(row = 2, columnspan=2)
plus = Button(window, image = photo1,  command = lambda: click(1))
plus.grid(row = 3, column=0)
minus = Button(window, image = photo2, command = lambda: click(2))
minus.grid(row = 3, column=1)
dobutok = Button(window, image = photo3, command = lambda: click(3))
dobutok.grid(row = 4, column=0)
btn4 = Button(window, image = photo4, command = lambda: click(4))
btn4.grid(row = 4, column=1)
window.mainloop()
input()
