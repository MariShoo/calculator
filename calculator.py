import tkinter as tk  # Importing the tkinter library for GUI development

calculation = ""  # Global variable to store the current calculation

def add_to_calculation(symbol):
    global calculation 
    calculation += str(symbol)  # Append the symbol to the current calculation
    text_result.delete(1.0, "end")  # Clear the text widget
    text_result.insert(1.0, calculation)  # Insert the updated calculation into the text widget
    


# we are going to use eval funstion for evaluation of math empreshen but its only for educational
# and not recomended to use it in production becouse with this eval function the actual code can be
# evaluated and it can be leading to bad results
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))  # Evaluate the calculation string and convert the result to a string
        text_result.delete(1.0, "end")  # Clear the text widget
        text_result.insert(1.0, calculation)  # Insert the result into the text widget
    except:
        clear_field()  # Clear the field if there is an error
        text_result.insert(1.0, "Error")  # Display an error message



def clear_field():  
    global calculation
    calculation = ""  # Reset the calculation string
    text_result.delete(1.0, "end")  # Clear the text widget

root = tk.Tk()  # Create the main application window
root.geometry("300x275")  # Set the dimensions of the window
root.title("Calculator")  # Set the title of the window

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))  # Create a text widget for displaying the calculation
text_result.grid(columnspan=5)  # Place the text widget in the grid layout

# Creating buttons for numbers and placing them in the grid layout
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Areal", 14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Areal", 14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Areal", 14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Areal", 14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Areal", 14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Areal", 14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Areal", 14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Areal", 14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Areal", 14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Areal", 14))
btn_0.grid(row=5, column=2)

# Creating buttons for operators and placing them in the grid layout
btn_pluse = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Areal", 14))
btn_pluse.grid(row=2, column=4)

btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Areal", 14))
btn_minus.grid(row=3, column=4)

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Areal", 14))
btn_div.grid(row=4, column=4)

btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Areal", 14))
btn_mult.grid(row=5, column=4)

# Creating buttons for parentheses and placing them in the grid layout
btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Areal", 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Areal", 14))
btn_close.grid(row=5, column=3)

# Creating buttons for equals and clear, and placing them in the grid layout
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Areal", 14))
btn_equals.grid(row=6, column=1, columnspan=2)

btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Areal", 14))
btn_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()  # Start the main event loop to make the application run
