import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == 'Add':
            result = num1 + num2
        elif operation == 'Subtract':
            result = num1 - num2
        elif operation == 'Multiply':
            result = num1 * num2
        elif operation == 'Divide':
            result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        
        result_label.config(text=f"Result: {result}", foreground='green')
    except ValueError:
        result_label.config(text="Error: Invalid input", foreground='red')

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Set a minimum size for the window
root.minsize(300, 200)

# Use a stylish theme
style = ttk.Style()
style.theme_use('clam')  # You can try 'alt', 'default', 'classic', etc.

# Create and place the labels and entries with some padding
ttk.Label(root, text="First Number:", font=("Helvetica", 10)).grid(row=0, column=0, padx=10, pady=10, sticky='e')
ttk.Label(root, text="Second Number:", font=("Helvetica", 10)).grid(row=1, column=0, padx=10, pady=10, sticky='e')

entry1 = ttk.Entry(root, font=("Helvetica", 10))
entry2 = ttk.Entry(root, font=("Helvetica", 10))
entry1.grid(row=0, column=1, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

# Create a variable for storing the selected operation
operation_var = tk.StringVar()
operation_var.set('Add')  # Default value

# Create a dropdown menu for operations
operations_menu = ttk.Combobox(root, textvariable=operation_var, values=['Add', 'Subtract', 'Multiply', 'Divide'], state="readonly", font=("Helvetica", 10))
operations_menu.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the calculate button
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a label for displaying the result
result_label = ttk.Label(root, text="Result:", font=("Helvetica", 10))
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Add padding to all widgets
for widget in root.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Start the GUI event loop
root.mainloop()
