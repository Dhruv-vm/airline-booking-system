'''

import tkinter as tk
from tkinter import messagebox
import csv

# Function to handle payment processing
def process_payment():
    card_number = entry_card_number.get()
    expiry_date = entry_expiry_date.get()
    cvv = entry_cvv.get()
    
    # Update credit card image with entered details
    updated_image = tk.PhotoImage(file="credit_card_image.png")
    canvas.itemconfig(card_image, image=updated_image)
    canvas.image = updated_image''

    with open("payment_details.csv", "a", newline='') as csvfile:
        fieldnames = ["Card Number", "Expiry Date", "CARD HOLDER"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        # Write payment details to CSV file
        writer.writerow({"Card Number": card_number, "Expiry Date": expiry_date, "CARD HOLDER": cvv})

    messagebox.showinfo("Payment Status", "Payment processed successfully!")

# Function to update the labels with real-time input
def update_label(*args):
    card_number = entry_card_number.get()
    expiry_date = entry_expiry_date.get()
    cvv = entry_cvv.get()
    label_card_output.config(text=f"{card_number}")
    label_expiry_output.config(text=f"{expiry_date}")
    label_cvv_output.config(text=f"{cvv}".upper())

# Create the main window
root = tk.Tk()
root.title("Credit Card Gateway")

# Create a canvas to display the credit card image
canvas = tk.Canvas(root, width=400, height=250)
canvas.pack()

# Display initial credit card image
credit_card_image = tk.PhotoImage(file="credit_card_image.png")
card_image = canvas.create_image(200, 125, anchor=tk.CENTER, image=credit_card_image)

# Credit Card Number
label_card_number = tk.Label(root, text="Credit Card Number(XXXX XXXX XXXX):")
label_card_number.pack()
entry_card_number = tk.Entry(root)
entry_card_number.pack()
entry_card_number.bind("<KeyRelease>", update_label)  # Update labels in real-time

# Expiry Date
label_expiry_date = tk.Label(root, text="Expiry Date (MM/YY):")
label_expiry_date.pack()
entry_expiry_date = tk.Entry(root)
entry_expiry_date.pack()
entry_expiry_date.bind("<KeyRelease>", update_label)  # Update labels in real-time

# CVV
label_cvv = tk.Label(root, text="NAME")
label_cvv.pack()
entry_cvv = tk.Entry(root, show="*")
entry_cvv.pack()
entry_cvv.bind("<KeyRelease>", update_label)  # Update labels in real-time



# Labels to display credit card details, expiry date, and CVV
label_card_output = tk.Label(root, text="", font=("credit card", 12), fg="#FFFFFF",bg="black")
label_card_output.place(x=60, y=125)  # Set position (x, y) for card number label

label_expiry_output = tk.Label(root, text="", font=("credit card", 12), fg="#FFFFFF",bg="black")
label_expiry_output.place(x=305, y=145)  # Set position (x, y) for expiry date label

label_cvv_output = tk.Label(root, text="", font=("verdana Bold", 12), fg="#FFFFFF",bg="black")
label_cvv_output.place(x=50, y=185)  # Set position (x, y) for CVV label




# Button to process payment
button_process_payment = tk.Button(root, text="Process Payment", command=process_payment)
button_process_payment.pack()

# Run the main loop
root.mainloop()'''

import tkinter as tk
from tkinter import messagebox
import csv
global root

# Define entry widgets and image globally
entry_card_number = None
entry_expiry_date = None
entry_card_holder_name = None
credit_card_image = None

# Function to handle payment processing
def process_payment():
    global entry_card_number, entry_expiry_date, entry_card_holder_name

    card_number = entry_card_number.get()
    expiry_date = entry_expiry_date.get()
    card_holder_name = entry_card_holder_name.get()

    # Update credit card image with entered details
    updated_image = tk.PhotoImage(file="credit_card_image.png")
    canvas.itemconfig(card_image, image=updated_image)
    canvas.image = updated_image

    with open("payment_details.csv", "a", newline='') as csvfile:
        fieldnames = ["Card Number", "Expiry Date", "CARD HOLDER"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # Write headers if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        # Write payment details to CSV file
        writer.writerow({"Card Number": card_number, "Expiry Date": expiry_date, "CARD HOLDER": card_holder_name})

    messagebox.showinfo("Payment Status", "Payment processed successfully!")

# Function to update the labels with real-time input
def update_label(*args):
    global entry_card_number, entry_expiry_date, entry_card_holder_name

    card_number = entry_card_number.get()
    expiry_date = entry_expiry_date.get()
    card_holder_name = entry_card_holder_name.get()
    label_card_output.config(text=f"{card_number}")
    label_expiry_output.config(text=f"{expiry_date}")
    label_cvv_output.config(text=f"{card_holder_name}".upper())

# Create main window and configure widgets
def create_widgets():
    global entry_card_number, entry_expiry_date, entry_card_holder_name, card_image, canvas, label_card_output, label_expiry_output, label_cvv_output, credit_card_image

    # Create a canvas to display the credit card image
    canvas = tk.Canvas(root, width=400, height=250)
    canvas.pack()

    # Display initial credit card image
    credit_card_image = tk.PhotoImage(file="credit_card_image.png")
    card_image = canvas.create_image(200, 125, anchor=tk.CENTER, image=credit_card_image)

    # Create labels and entry widgets for card number, expiry date, and cardholder name
    label_card_number = tk.Label(root, text="Credit Card Number(XXXX XXXX XXXX):")
    label_card_number.pack()
    entry_card_number = tk.Entry(root)
    entry_card_number.pack()
    entry_card_number.bind("<KeyRelease>", update_label)  # Update labels in real-time

    label_expiry_date = tk.Label(root, text="Expiry Date (MM/YY):")
    label_expiry_date.pack()
    entry_expiry_date = tk.Entry(root)
    entry_expiry_date.pack()
    entry_expiry_date.bind("<KeyRelease>", update_label)  # Update labels in real-time

    label_card_holder_name = tk.Label(root, text="Card Holder Name:")
    label_card_holder_name.pack()
    entry_card_holder_name = tk.Entry(root)
    entry_card_holder_name.pack()
    entry_card_holder_name.bind("<KeyRelease>", update_label)  # Update labels in real-time

    label_card_output = tk.Label(root, text="", font=("credit card", 12), fg="#FFFFFF", bg="black")
    label_card_output.place(x=60, y=125)  # Set position (x, y) for card number label

    label_expiry_output = tk.Label(root, text="", font=("credit card", 12), fg="#FFFFFF", bg="black")
    label_expiry_output.place(x=305, y=145)  # Set position (x, y) for expiry date label

    label_cvv_output = tk.Label(root, text="", font=("verdana Bold", 12), fg="#FFFFFF", bg="black")
    label_cvv_output.place(x=50, y=185)  # Set position (x, y) for Cardholder Name label

    button_process_payment = tk.Button(root, text="Process Payment", command=process_payment)
    button_process_payment.pack()

    # Update labels with real-time input
    entry_card_number.bind("<KeyRelease>", update_label)
    entry_expiry_date.bind("<KeyRelease>", update_label)
    entry_card_holder_name.bind("<KeyRelease>", update_label)

# Create the main window
root = tk.Tk()
root.title("Credit Card Gateway")

# Configure widgets
create_widgets()

# Run the main loop
root.mainloop()



