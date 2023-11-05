from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import tkinter as tk
from tkinter import simpledialog
import csv
import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime


def fetch_data1(name1, phone1):
    try:
        with open('boarding pass details.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['passenger_name'] == name1 and row['phoneno'] == phone1:
                    return row
    except FileNotFoundError:
        print("CSV file 'bookings.csv' not found.")

    return None
# Generate a random 10-digit filename
def generate_random_filename1():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(10)) + ".png"

# Function to get user input for name and phone number
def get_user_input23():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    return name, phone

# Function to display fetched data
def display_data1(row):
    global f,g,h,i,j,k,l,m,n,o,p
    if row:
        print("Data from CSV:")
        for key, value in row.items():
            f=(row["passenger_name"])
            g=(row["departure_t"])
            h=(row["departure_tt"])
            i=(row["gate"])
            j=(row["bar"])
            k=(row["phoneno"])
            l=(row["seat"])
            m=(row["from1"])
            n=(row["from2"])
            o=(row["airline1"])
            
            
    else:
        print("Record not found in CSV.")
    pir_output(f,g,h,i,j,k,l,m,n,o)

  

def pir_output(f,g,h,i,j,k,l,m,n,o):
    global image,draw
    airline1=o
    if airline1=="INDIGO":
        # Load the existing image and convert it to RGB mode
        image = Image.open("indigo-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="EMIRATES":
        # Load the existing image and convert it to RGB mode
        image = Image.open("emirates-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="QATAR":
        # Load the existing image and convert it to RGB mode
        image = Image.open("qatar-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="VISTARA":
        # Load the existing image and convert it to RGB mode
        image = Image.open("vistara-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline=="ETIHAD AIRWAYS":
        # Load the existing image and convert it to RGB mode
        image = Image.open("etihad-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline=="SINGAPORE AIRLINES":
        # Load the existing image and convert it to RGB mode
        image = Image.open("singapore-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline=="THAI AIRWAYS":
        # Load the existing image and convert it to RGB mode
        image = Image.open("thai-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline=="JAPAN AIRLINES":
        # Load the existing image and convert it to RGB mode
        image = Image.open("japan-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline=="OMAN AIR":
        # Load the existing image and convert it to RGB mode
        image = Image.open("oman-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
    #value stored in variables
    passenger_name=f
    departure_t=g
    departure_tt=h
    gate=i
    bar=j
    phoneno=k
    seat=l
    from1=m
    from2=n
    
    

    # Load a font for the text
    try:
        font1 = ImageFont.truetype("Raleway-ExtraBold.ttf", 21)
        font2 = ImageFont.truetype("Raleway-ExtraBold.ttf", 16)
        font3 = ImageFont.truetype("Raleway-ExtraBold.ttf", 10)
    except IOError:
        font = ImageFont.load_default()
    col="#434343"

    # Draw the boarding pass information
    draw.text((270, 70), f"{passenger_name}".upper(), fill=col, font=font3)
    draw.text((450, 280), f" {departure_tt}".upper(), fill=col, font=font3)
    draw.text((280, 85), f"{departure_t}".upper(), fill=col, font=font3)
    draw.text((365, 280), f"{from2}", fill=col, font=font3)
    draw.text((65, 510), f"{bar}", fill=col, font=font3)
    draw.text((65, 370), f"{from1}", fill=col, font=font3)
    draw.text((580, 280), f"{seat}", fill=col, font=font3)

    # Generate a random filename and save the image with the modified content
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    output_filename = os.path.join(downloads_dir, generate_random_filename1())
    image.save(output_filename)
    print(f"Baggage pass saved as {output_filename}")
    messagebox.showinfo("BAGGAGE PAS", f"Baggae pass saved as {output_filename}")
        
    

def window89():
    # Create the main application window
    bagg = tk.Tk()
    bagg.withdraw()  # Hide the tkinter main window
    # Get user input for name and phone number
    name_input, phone_input = get_user_input23()
    # Fetch and display data
    data_row = fetch_data1(name_input, phone_input)
    display_data1(data_row)
window89()
