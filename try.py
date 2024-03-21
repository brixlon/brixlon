import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + symbol)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Clear', 5, 0)
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Add clear button
clear_button = tk.Button(root, text='Clear', padx=30, pady=20, command=clear)
clear_button.grid(row=5, column=1, padx=5, pady=5)

# Add equal button
equal_button = tk.Button(root, text='=', padx=30, pady=20, command=calculate)
equal_button.grid(row=5, column=2, padx=5, pady=5)

root.mainloop()
