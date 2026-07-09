import tkinter as tk

# Function to add button value to screen
def press(value):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + value)

# Function to clear screen
def clear():
    screen.delete(0, tk.END)

# Function to delete last character
def delete():
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current[:-1])

# Function to calculate answer
def calculate():
    try:
        expression = screen.get()
        answer = eval(expression)
        screen.delete(0, tk.END)
        screen.insert(0, str(answer))
    except:
        screen.delete(0, tk.END)
        screen.insert(0, "Error")

# Create window
window = tk.Tk()
window.title("Standard Calculator")
window.geometry("350x450")
window.resizable(False, False)

# Screen
screen = tk.Entry(window, font=("Arial", 24), justify="right")
screen.pack(fill="both", padx=10, pady=10, ipady=10)

# Button frame
button_frame = tk.Frame(window)
button_frame.pack()

# Buttons
buttons = [
    ["C", "DEL", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "=", ""]
]

for row in buttons:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()

    for btn in row:
        if btn == "":
            continue

        if btn == "C":
            action = clear
        elif btn == "DEL":
            action = delete
        elif btn == "=":
            action = calculate
        else:
            action = lambda x=btn: press(x)

        tk.Button(
            row_frame,
            text=btn,
            width=7,
            height=2,
            font=("Arial", 14),
            command=action
        ).pack(side="left", padx=3, pady=3)

window.mainloop()