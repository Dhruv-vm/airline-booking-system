
import tkinter as tk
import csv
global name_entry
global passport_entry
global total_cost
global payment_status

def get_cost():
    name = name_entry.get()
    passport_number = passport_entry.get()
    try:
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # Assuming the name is in the second column and passport number is in the third column
                # and the cost is in the fifth column of the CSV file
                if row[0] == name and row[5] == passport_number:
                    total_cost.set("Total Cost: $" + row[4])
                    return
            total_cost.set("Data not found for provided name and passport number")
    except FileNotFoundError:
        total_cost.set("File not found")
    except IndexError:
        total_cost.set("Invalid data format")

def process_payment():
    card_number = card_number_entry.get()
    cardholder_name = cardholder_name_entry.get()
    expiry_date = expiry_date_entry.get()
    cvv = cvv_entry.get()

    try:
        with open('payment_card.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name_entry.get(), passport_entry.get(), total_cost.get(), card_number, cardholder_name, expiry_date, cvv])
        payment_status.set("Payment Successful! Card ending in {}".format(card_number[-4:]))
    except Exception as e:
        payment_status.set("Error occurred while processing payment")
global root
root = tk.Tk()
root.title("Payment Interface")

total_cost = tk.StringVar()
payment_status = tk.StringVar()

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root, name="name_entry")
passport_label = tk.Label(root, text="Passport Number:")
passport_entry = tk.Entry(root, name="passport_entry")

cost_label = tk.Label(root, textvariable=total_cost)
get_cost_button = tk.Button(root, text="Get Cost", command=get_cost)

card_number_label = tk.Label(root, text="Card Number:")
card_number_entry = tk.Entry(root, show="*")
cardholder_name_label = tk.Label(root, text="Cardholder's Name:")
cardholder_name_entry = tk.Entry(root)
expiry_date_label = tk.Label(root, text="Expiry Date (MM/YY):")
expiry_date_entry = tk.Entry(root)
cvv_label = tk.Label(root, text="CVV:")
cvv_entry = tk.Entry(root, show="*")

pay_button = tk.Button(root, text="Process Payment", command=process_payment)
payment_status_label = tk.Label(root, textvariable=payment_status)

name_label.grid(row=0, column=0, sticky='w')
name_entry.grid(row=0, column=1)
passport_label.grid(row=1, column=0, sticky='w')
passport_entry.grid(row=1, column=1)

cost_label.grid(row=2, column=0, columnspan=2)
get_cost_button.grid(row=3, column=0, columnspan=2)

card_number_label.grid(row=4, column=0, sticky='w')
card_number_entry.grid(row=4, column=1)
cardholder_name_label.grid(row=5, column=0, sticky='w')
cardholder_name_entry.grid(row=5, column=1)
expiry_date_label.grid(row=6, column=0, sticky='w')
expiry_date_entry.grid(row=6, column=1)
cvv_label.grid(row=7, column=0, sticky='w')
cvv_entry.grid(row=7, column=1)

pay_button.grid(row=8, column=0, columnspan=2)
payment_status_label.grid(row=9, column=0, columnspan=2)

root.mainloop()

