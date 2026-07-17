import tkinter as tk
def calculate_label():
    global seats_entry,root
    root = tk.Tk()
    root.title("Price Calculator")
    instructions_label = tk.Label(root, text="Enter the number of seats:")
    instructions_label.pack(pady=10)
    seats_entry = tk.Entry(root)
    seats_entry.pack()
    calculate_button = tk.Button(root, text="Calculate Total", command=update_label)
    calculate_button.pack()
def update_label():
    price = tk.StringVar()
    label = tk.Label(root, text="", font=("Arial", 16))
    label.pack(pady=20)
    price.set("10.00")
    try:
        num_seats = int(seats_entry.get())
        total_price = num_seats * float(price.get())
        label.config(text=f"Total Price: ${total_price:.2f}")
    except ValueError:
        label.config(text="Invalid input. Enter a valid number of seats.")
    
calculate_label()
