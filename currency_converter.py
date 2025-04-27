import currency_data

import tkinter as tk
from tkinter import ttk

root=tk.Tk()
root.title("Currency Converter")

top_lab_frame=tk.Frame(root)
top_lab_frame.pack()
label_title=tk.Label(top_lab_frame, text="Currency Converter", font=("Times New Roman", 15, "bold"))
label_title.pack(padx=10, pady=10, side="top")

rest_frame=tk.Frame(root)
rest_frame.pack()

first_amount=tk.StringVar()
first_entry=tk.Entry(rest_frame, textvariable=first_amount, font=("Times New Roman", 15))
first_entry.grid(row=3, column=0, padx=10, pady=10)
first_currency=tk.StringVar()
first_combobox=ttk.Combobox(rest_frame, textvariable=first_currency, font=("Times New Roman", 15))
first_combobox["values"]=currency_data.currencies_data
first_combobox.grid(row=3, column=1, padx=10, pady=10)

second_amount=tk.StringVar()
second_entry=tk.Entry(rest_frame, textvariable=second_amount, state="readonly", font=("Times New Roman", 15))
second_entry.grid(row=5, column=0, padx=10, pady=10)
second_currency=tk.StringVar()
second_combobox=ttk.Combobox(rest_frame, textvariable=second_currency, font=("Times New Roman", 15))
second_combobox["values"]=currency_data.currencies_data
second_combobox.grid(row=5, column=1, padx=10, pady=10)

def is_float_int(num):
    try:
        int(num)
        return True
    except ValueError:
        try:
            float(num)
            return True
        except ValueError:
            return False

def check_conversion(*args):
    if (is_float_int(first_amount.get())==True) and ((first_currency.get() and second_currency.get()) !=""):
        base=first_currency.get()
        target=second_currency.get()
        convert=float(first_amount.get())*(currency_data.rates[target]/currency_data.rates[base])
        return second_amount.set(round(convert, 2))

first_amount.trace_add("write", check_conversion)
first_currency.trace_add("write",check_conversion)
second_currency.trace_add("write", check_conversion)

root.mainloop()