import tkinter as tk
from math import *

def button_click(value):
    entry.insert(tk.END, value)

def clear_display():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def switch_mode():
    global is_scientific
    if is_scientific:
        is_scientific = False
        show_normal()
        mode_button.config(text='Scientifique')
    else:
        is_scientific = True
        show_scientific()
        mode_button.config(text='Normal')

def show_normal():
    for widget in scientific_widgets:
        widget.grid_remove()
    for widget in normal_widgets:
        widget.grid()

def show_scientific():
    for widget in normal_widgets:
        widget.grid_remove()
    for widget in scientific_widgets:
        widget.grid()

root = tk.Tk()
root.title("Calculatrice")

is_scientific = False

entry = tk.Entry(root, width=25, font=('Arial', 12), bd=5, justify='right')
entry.grid(row=0, column=0, columnspan=5)

numbers = [
    '7', '8', '9', 
    '4', '5', '6', 
    '1', '2', '3', 
    '.', '0', '=',
]

normal_widgets = []
row_val = 1
col_val = 0

for num in numbers:
    if num != '=':
        button = tk.Button(
            root, 
            text=num, 
            width=5, 
            height=2, 
            command=lambda val=num: button_click(val)
        )
        button.grid(row=row_val, column=col_val)
        normal_widgets.append(button)
    else:
        button = tk.Button(
            root, 
            text=num, 
            width=5, 
            height=2, 
            command=calculate
        )
        button.grid(row=row_val, column=col_val)
        normal_widgets.append(button)
    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

operations = [
    ('+', lambda: button_click('+')),
    ('-', lambda: button_click('-')),
    ('*', lambda: button_click('*')),
    ('/', lambda: button_click('/')),
    ('back', lambda: entry.delete(len(entry.get()) - 1, tk.END)),
    ('clear', clear_display),
    ('exit', root.quit)
]

row_val = 1
col_val = 4

for op, cmd in operations:
    button = tk.Button(
        root, 
        text=op, 
        width=5, 
        height=2, 
        command=cmd
    )
    button.grid(row=row_val, column=col_val)
    normal_widgets.append(button)
    row_val += 1
    if row_val > 4:
        row_val = 1
        col_val += 1

scientific_functions = [
    ('sin', lambda: button_click('math.sin(')),
    ('cos', lambda: button_click('math.cos(')),
    ('tan', lambda: button_click('math.tan(')),
    ('log', lambda: button_click('math.log(')),
    ('ln', lambda: button_click('math.log(')),
    ('sqrt', lambda: button_click('math.sqrt(')),
    ('(', lambda: button_click('(')),
    (')', lambda: button_click(')')),
    ('^2', lambda: button_click('**2')),
]

scientific_widgets = []
row_val = 1
col_val = 0

for func, cmd in scientific_functions:
    button = tk.Button(
        root, 
        text=func, 
        width=5, 
        height=2, 
        command=cmd
    )
    button.grid(row=row_val, column=col_val)
    scientific_widgets.append(button)
    col_val += 1
    if col_val > 4:
        col_val = 0
        row_val += 1

mode_button = tk.Button(
    root, 
    text='Scientifique', 
    width=10, 
    height=2, 
    command=switch_mode
)
mode_button.grid(row=6, column=0, columnspan=5)

show_normal()

root.mainloop()
