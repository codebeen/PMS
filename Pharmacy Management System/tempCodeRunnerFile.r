# import tkinter module for GUI programming
import tkinter as tk
from tkinter import messagebox

# create a parent/main window name root
root = tk.Tk()
root.title("Simple Calculator") # name of the window
root.config(bg="lightgray")
root.geometry('430x300')  # increased the height to fit the output label

# frame for operators
operator_frame = tk.LabelFrame(root, text="Operators:", bg="lightgray", padx=5, pady=5)
operator_frame.grid(column=0, row=2, padx=15, pady=10)

add_button = tk.Button(operator_frame, text="+", width=8).grid(column=0, row=10, padx=5, pady=5)
subtract_button = tk.Button(operator_frame, text="-", width=8).grid(column=1, row=10, padx=5, pady=5)
multiply_button = tk.Button(operator_frame, text="*", width=8).grid(column=0, row=11, padx=5, pady=5)
division_button = tk.Button(operator_frame, text="/", width=8).grid(column=1, row=11, padx=5, pady=5)
division_button = tk.Button(operator_frame, text="/", width=8).grid(column=1, row=11, padx=5, pady=5)
backslash_button = tk.Button(operator_frame, text="\\", width=8).grid(column=0, row=12, padx=5, pady=5)
division_button = tk.Button(operator_frame, text="/", width=8).grid(column=1, row=11, padx=5, pady=5)
exponent_button = tk.Button(operator_frame, text="^", width=8).grid(column=1, row=12, padx=5, pady=5)
mod_button = tk.Button(operator_frame, text="Mod", width=19).grid(row=13, columnspan=2, padx=5, pady=5)

# frame for operations
operation_frame = tk.LabelFrame(root, text="Operators:",  bg="lightgray", padx=5, pady=15)
operation_frame.grid(column=1, row=2, padx=15, pady=10)

# label and input for operand 1
operand1_label = tk.Label(operation_frame, text="Operand 1:", bg="lightgray").grid(column=0, row=2, padx=5, pady=5)
operand1_input = tk.Entry(operation_frame, width=17).grid(column=1, row=2, padx=5, pady=5)

# for operator
operator = tk.Entry(operation_frame, width=8, bg="lightgrey").grid(column=1, row=3, padx=5, pady=5)

# Label and input for operand 2
operand2_label = tk.Label(operation_frame, text="Operand 2:", bg="lightgray").grid(column=0, row=4, padx=5, pady=5)
operand2_input = tk.Entry(operation_frame, width=17).grid(column=1, row=4, padx=5, pady=5)

# Label and input for result
result_label = tk.Label(operation_frame, text="Result:",  bg="lightgray").grid(column=0, row=5, padx=5, pady=5, sticky="w")
result_input = tk.Entry(operation_frame, width=17, bg="lightgray").grid(column=1, row=5, padx=5, pady=5)

button_frame = tk.Frame(root, padx=5, pady=5, bg="lightgray")
button_frame.grid(column=1, row=3)

# cancel button
cancel_button = tk.Button(button_frame, text="Cancel", width=10).grid(column=0, row="10",padx=15, pady=5)

# exit button
exit_button = tk.Button(button_frame, text="Exit", width=10).grid(column=1, row="10",padx=15, pady=5)

# run the window in an inifinite loop unless terminated
root.mainloop()