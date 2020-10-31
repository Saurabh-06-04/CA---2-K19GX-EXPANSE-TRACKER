#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PROGRAM TO MAKE EXPANSE TRACKER CALCULATOR.
# I HAVE TAKEN IDEA OF GENRAL FACTORY IN WHICH EXPENDITURE IN MAINLY ON LABOUR COST AND ELEC. CONSUME
# AND MADE THE BELOW EXPANSE TRACKER CALCULTOR

# CA 2

# Saurabh Singh   11905713  
# Aman Rana       11903877
# Utkarsh Sarkari 11903902

from tkinter import *
from functools import partial
from tkinter import messagebox


def clear_record():
    owner_invest.delete(0, END)
    owner_name.delete(0, END)
    company_name.delete(0, END)
    project_name.delete(0, END)
    unitelec_consume.delete(0, END)
    labour_cost.delete(0, END)


def calculate(net_profit, invest, elec, labour):
    invest = float(owner_invest.get())
    elec = float(unitelec_consume.get())
    labour = float(labour_cost.get())

    a = 9 * elec
    b = 400 * labour
    expenditure = float(a) + float(b)
    gross = invest - expenditure

    if gross < 100000:
        tax = 0

    elif gross < 500000:
        tax = gross * 0.10

    elif gross < 1000000:
        tax = gross * 0.15

    else:
        tax = gross * 0.20

    profit = gross - tax

    net_profit.config(text="NET_PROFIT= %f" % profit)
    if profit < 0:
        messagebox.showwarning(title='Warning', message='Your business is in loss!')
    return


window = Tk()

number1 = StringVar()
number2 = StringVar()
number3 = StringVar()

window.geometry("600x450")

window.title("Expanse tracker calculator")

label1 = Label(window, text="Owner name", fg='black', bg='green')

label2 = Label(window, text="company name", fg='black', bg='green')

label3 = Label(window, text="project name", fg='black', bg='green')

label4 = Label(window, text="total investment", fg='black', bg='green')

label5 = Label(window, text="elec. uint", fg='black', bg='green')

label6 = Label(window, text="worker and other expanse", fg='black', bg='green')

labelResult = Label(window)

labelResult.grid(row=7, column=2)

label1.grid(row=1, column=0, padx=10, pady=10)
label2.grid(row=2, column=0, padx=10, pady=10)
label3.grid(row=3, column=0, padx=10, pady=10)
label4.grid(row=4, column=0, padx=10, pady=10)
label5.grid(row=5, column=0, padx=10, pady=10)
label6.grid(row=6, column=0, padx=10, pady=10)

owner_name = Entry(window)
company_name = Entry(window)
project_name = Entry(window)
owner_invest = Entry(window, textvariable=number1)
unitelec_consume = Entry(window, textvariable=number2)
labour_cost = Entry(window, textvariable=number3)

owner_name.grid(row=1, column=1, padx=10, pady=10)
company_name.grid(row=2, column=1, padx=10, pady=10)
project_name.grid(row=3, column=1, padx=10, pady=10)
owner_invest.grid(row=4, column=1, padx=10, pady=10)
unitelec_consume.grid(row=5, column=1, padx=10, pady=10)
labour_cost.grid(row=6, column=1, padx=10, pady=10)

calculate = partial(calculate, labelResult, number1, number2, number3)

button1 = Button(window, text="calculate", bg="red",
                 fg="black", command=calculate)

button2 = Button(window, text="clear record", bg="red",
                 fg="black", command=clear_record)

button1.grid(row=8, column=1, pady=10)
button2.grid(row=8, column=3, pady=10)

window.mainloop()


# In[ ]:




