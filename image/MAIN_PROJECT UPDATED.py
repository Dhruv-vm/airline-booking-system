
#cs practicles grade 12

#guipart
#objet for tkinter
#functions
DATA_FILE = "bookings.csv"
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
    return ''.join(random.choice(letters_and_digits) for i in range(5)) +"baggage" ".png"

# Function to get user input for name and phone number
def get_user_input23():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter passport Number:")
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
            p=(row["flight_number"])
            
            
    else:
        print("Record not found in CSV.")
    pir_output(f,g,h,i,j,k,l,m,n,o,p)

  

def pir_output(f,g,h,i,j,k,l,m,n,o,p):
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
    elif airline1=="ETIHAD AIRWAYS":
        # Load the existing image and convert it to RGB mode
        image = Image.open("etihad-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="SINGAPORE AIRLINES":
        # Load the existing image and convert it to RGB mode
        image = Image.open("singapore-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="THAI AIRWAYS":
        # Load the existing image and convert it to RGB mode
        image = Image.open("thai-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="JAPAN AIRLINES":
        # Load the existing image and convert it to RGB mode
        image = Image.open("japan-bag.png").convert("RGB")
        draw = ImageDraw.Draw(image)
    elif airline1=="OMAN AIR":
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
    flightnono=p
    
    

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
    draw.text((280, 90), f" {flightnono}".upper(), fill=col, font=font3)
    draw.text((260, 110), f" {seat}".upper(), fill=col, font=font3)
    draw.text((287, 130), f" {departure_t}".upper(), fill=col, font=font3)
    draw.text((270, 690), f"{from2}", fill=col, font=font1)
    draw.text((270, 760), f"{departure_tt}", fill=col, font=font1)
    

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



#_______________________________________________________________________________________________________________________________________________








def barcode_digit():
    global barcode,random_gate_number,seat_number
    # Define the characters to choose from
    characters = string.digits + string.ascii_letters  # Digits + Uppercase/Lowercase Letters
    # Generate a 10-digit barcode
    barcode_length = 10
    barcode = ''.join(random.choice(characters) for _ in range(barcode_length))
    random_gate_number = random.randint(1, 19)
    print("Generated Barcode:", barcode)
    random_alphabet = random.choice(string.ascii_uppercase)
    random_digit = random.randint(1,23)
    # Combine the random alphabet and digit to create the seat number
    seat_number = random_alphabet + "-" + str(random_digit)

    
    
# Generate a random 10-digit filename
def generate_random_filename():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(5)) +"boarding_pass"+ ".png"


#["INDIGO", "EMIRATES", "QATAR","VISTARA"]
#["INDIGO", "EMIRATES", "QATAR","ETIHAD AIRWAYS"]
#["INDIGO", "EMIRATES","VISTARA","SINGAPORE AIRLINES"]
# ["THAI AIRWAYS", "SINGAPORE AIRLINES", "JAPAN AIRLINES","VISTARA"]
#["THAI AIRWAYS", "SINGAPORE AIRLINES", "QATAR","VISTARA"]
#["ETIHAD AIRWAYS", "EMIRATES", "QATAR","OMAN AIR"]
#["DUBAI", "SINGAPORE", "JAPAN","KOREA","SAUDI ARABIA","SWIZTERLAND"]
def por_output(b,c,e):
    global image,draw,airline
    code=c
    if code=="DUBAI":
        d="DXB"
        
    elif code=="SINGAPORE":
        d="SIN"
        
    elif code=="TOKYO":
        d="TYO"
        
    elif code=="KOREA":
        d="KOR"
        
    elif code=="SAUDI ARABIA":
        d="HAS"
    elif code=="SWIZTERLAND":
        d="ZRH"
        
    
    airline =b
    if airline=="INDIGO":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#ING-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("indigo.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
        
    elif airline=="EMIRATES":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#EAM-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("emirates.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
    elif airline=="QATAR":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#QAT-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("qatar.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
    elif airline=="VISTARA":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#VIS-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("vistara.png").convert("RGB")
        draw = ImageDraw.Draw(image)

    elif airline=="ETIHAD AIRWAYS":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#ETI-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("etihad.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
    elif airline=="SINGAPORE AIRLINES":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#SIG-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("singapore-airlines.png").convert("RGB")
        draw = ImageDraw.Draw(image)

    elif airline=="THAI AIRWAYS":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#THA-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("thai-aiways.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
    elif airline=="JAPAN AIRLINES":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#JAP-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("japan-airlines.png").convert("RGB")
        draw = ImageDraw.Draw(image)

    elif airline=="OMAN AIR":
        four_digit_number = random.randint(1000, 9999)
        plane_number = f"#OMA-{four_digit_number}"
        flight_number=plane_number
        # Load the existing image and convert it to RGB mode
        image = Image.open("oman-airways.png").convert("RGB")
        draw = ImageDraw.Draw(image)
        
   
    # Get user input
    barcode_digit()
    phoneno=e
    passenger_name =a
    departure_t =c
    departure_tt=d
    gate =random_gate_number
    bar=barcode
    from1="BANGLORE"
    from2="BLR"
    seat=seat_number
    airline1=b

    #saveing data to csv:
    DATA_FILE3="boarding pass details.csv"
    with open(DATA_FILE3, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([passenger_name, departure_t, departure_tt, gate, bar, phoneno,seat,from1,from2,airline1,flight_number])
    
    # Load a font for the text
    try:
        font1 = ImageFont.truetype("Raleway-ExtraBold.ttf", 21)
        font2 = ImageFont.truetype("Raleway-ExtraBold.ttf", 16)
        font3 = ImageFont.truetype("Raleway-ExtraBold.ttf", 13)
    except IOError:
        font = ImageFont.load_default()
    col="#434343"
    # Draw the boarding pass information
    draw.text((65, 280), f"{passenger_name}".upper(), fill=col, font=font1)
    draw.text((450, 280), f" {flight_number}".upper(), fill=col, font=font2)
    draw.text((65, 440), f"{departure_t}".upper(), fill=col, font=font1)
    draw.text((365, 280), f"{gate}", fill=col, font=font1)
    draw.text((65, 510), f"{bar}", fill=col, font=font3)
    draw.text((65, 370), f"{from1}", fill=col, font=font1)
    draw.text((580, 280), f"{seat}", fill=col, font=font2)
    #rightside of the boarding pass
    draw.text((750, 280), f"{passenger_name}".upper(), fill=col, font=font3)
    draw.text((785, 320), f" {flight_number}".upper(), fill=col, font=font3)
    draw.text((735, 320), f"{gate}", fill=col, font=font3)
    draw.text((885, 320), f"{seat}", fill=col, font=font3)
    draw.text((750, 365), f"{from2}", fill=col, font=font2)
    draw.text((750, 415), f"{departure_tt}".upper(), fill=col, font=font2)
    # Generate a random filename and save the image with the modified content
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    output_filename = os.path.join(downloads_dir, generate_random_filename())
    image.save(output_filename)
    print(f"Boarding pass saved as {output_filename}")
    messagebox.showinfo("boarding pass", f"Boarding pass saved as {output_filename}")

# Function to open and read the CSV file
def fetch_data(name, phone):
    try:
        with open('bookings.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'] == name and row['phone_no'] == phone:
                    return row
    except FileNotFoundError:
        print("CSV file 'bookings.csv' not found.")

    return None

# Function to get user input for name and phone number
def get_user_input():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter passport Number:")
    return name, phone

# Function to display fetched data
def display_data(row):
    global a,b,c
    if row:
        print("Data from CSV:")
        for key, value in row.items():
            a=(row["name"])
            b=(row["flight no"])
            c=(row["place"])
            e=(row["phone_no"])
            
    else:
        print("Record not found in CSV.")

    por_output(b,c,e)

def window78():
    # Create the main application window
    root = tk.Tk()
    root.withdraw()  # Hide the tkinter main window
    # Get user input for name and phone number
    name_input, phone_input = get_user_input()
    # Fetch and display data
    data_row = fetch_data(name_input, phone_input)
    display_data(data_row)
#_____________________________________________________________________________________________________________________________________  
    

def trial():
    print("successful")
def immik():
    immi= tk.Toplevel(in_window)
    immi.title("E-immigration")
    immi.geometry("990x660+50+50")

    tk.Label(immi, text="Name:").pack()
    global name_entry
    name_entry = tk.Entry(immi)
    name_entry.pack()

    tk.Label(immi, text="passportno:").pack()
    global phone_entry
    phone_entry = tk.Entry(immi)
    phone_entry.pack()

    tk.Label(immi, text="Gender:").pack()
    global gender_var
    gender_var = tk.StringVar()
    gender_var.set("Male")
    gender_option = tk.OptionMenu(immi, gender_var, "Male", "Female", "Other")
    gender_option.pack()

    nationality_options = ["Australia","Brazil","Cambodia","Canada","Denmark","England","Germany","India","Jamaica","Madagascar"]
    tk.Label(immi, text="Nationality:").pack()
    global nationality_var
    nationality_var = tk.StringVar()
    nationality_var.set(nationality_options[0])
    nationality_option = tk.OptionMenu(immi, nationality_var, *nationality_options)
    nationality_option.pack()

    tk.Label(immi, text="Today's Date:DD-MM-YYYY").pack()
    global date_entry
    date_entry = tk.Entry(immi)
    date_entry.pack()

    place_of_visit_options = ["DUBAI", "SINGAPORE", "TOKYO","KOREA","SAUDI ARABIA","SWIZTERLAND"]
    tk.Label(immi, text="Place of Visit:").pack()
    global place_of_visit_var
    place_of_visit_var = tk.StringVar()
    place_of_visit_var.set(place_of_visit_options[0])
    place_of_visit_option = tk.OptionMenu(immi, place_of_visit_var, *place_of_visit_options)
    place_of_visit_option.pack()

    tk.Button(immi, text="Submit", command=check_immigration).pack()

def output_123(phone):
    a=phone
    # Load the existing image and convert it to RGB mode
    image1 = Image.open("report_emmi.png").convert("RGB")
    draw1 = ImageDraw.Draw(image1)
    # Load a font for the text
    try:
        font1 = ImageFont.truetype("Raleway-ExtraBold.ttf", 21)
        font2 = ImageFont.truetype("Raleway-ExtraBold.ttf", 16)
        font3 = ImageFont.truetype("Raleway-ExtraBold.ttf", 13)
    except IOError:
        font = ImageFont.load_default()
    col="#434343"
    # Draw the boarding pass information
    draw1.text((65,420), f"{a}".upper(), fill=col, font=font2)
    # Generate a random filename and save the image with the modified content
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    output_filename = os.path.join(downloads_dir, generate_random_filename12334())
    image1.save(output_filename)
    print(f"emmigration status saved as {output_filename}")
    messagebox.showinfo("emmigartion status", f"emmigration saved as {output_filename}")
# Generate a random 10-digit filename
def generate_random_filename12334():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(5)) +"Emmigration status"+ ".png"  


def check_immigration():
    name = name_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    nationality = nationality_var.get()
    date = date_entry.get()
    place_of_visit = place_of_visit_var.get()
    today_date = datetime.now().strftime("%d-%m-%Y")
    if date != today_date:
        messagebox.showerror("E-Immigration", "Entered date is not today's date.")
        return
    
    if os.path.exists("bookings.csv"):
        with open("bookings.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == place_of_visit and row[0]== name and row[5]== phone:
                    messagebox.showinfo("E-Immigration", "E-Immigration successful!")
                    save_immigration_details(name, phone, gender, nationality, date, place_of_visit)
                    break
            else:
                messagebox.showerror("E-Immigration", "Place of visit does not match with bookings.csv.")
    else:
        messagebox.showerror("E-Immigration", "bookings.csv does not exist.")

def save_immigration_details(name, phone, gender, nationality, date, place_of_visit):
    with open("E-immigration.csv", "a", newline="") as e_immigration_file:
        writer = csv.writer(e_immigration_file)
        writer.writerow([name, phone, gender, nationality, date, place_of_visit])
    output_123(phone)


#--------------------------------------------------------------------------------------------------------------------------------------------

def admin_login():
    #admin window
    admin_login = tk.Toplevel(in_window)
    admin_login.title("Admin credentials")
    admin_login.geometry("990x660+50+50")
    bkImage=ImageTk.PhotoImage(file="book-page.jpg")
    bkLabel=Label(admin_login,image=bkImage)
    bkLabel.place(x=0,y=0)
    
    username_label = tk.Label(admin_login, text="username:")
    username_label.pack(pady=10)
    username_entry = tk.Entry(admin_login)
    username_entry.pack(pady=5)

    password_label = tk.Label(admin_login, text="password:")
    password_label.pack(pady=10)
    password_entry = tk.Entry(admin_login)
    password_entry.pack(pady=5)

    exit_button =Button(admin_login, text="Exit", command=admin_login.destroy)
    exit_button.pack(pady=20) 

    save_button3 =Button(admin_login, text="check credentilas", command=lambda:check_admin(username_entry,password_entry))
    save_button3.pack(pady=10)


    

def check_admin(username_entry,password_entry):
    user=username_entry.get()
    passw=password_entry.get()
    if (user=="admin")and (passw=="12345"):
        admin_window()
        
    else:
        messagebox.showerror("Login Failed", "you must have have entered wrong credentials")


        

    
def admin_window():
    global E_plane
    print("enter 1 to create your new passanger booking")
    print("enter 2 to modify the details of your passannger booking")
    print("enter 3 to just see your details")
    chociew=int(input("eneter your choice:"))
    if(chociew==1):
        E_name=input("enter passangers name:")
        E_pass=int(input("enter passport no:"))
        chi=["DUBAI", "SINGAPORE", "TOKYO","KOREA","SAUDI ARABIA","SWIZTERLAND"]
        print(chi)
        print("enter 1 for option1")
        print("enter 2 for option2")
        print("enter 3 for option3")
        print("enter 4 for option4")
        print("enter 5 for option5")
        print("enter 6 for option6")
        E_chico=int(input("enter your choice:"))
        if E_chico==1:
            E_destination=chi[0]
            pl1=["INDIGO", "EMIRATES", "QATAR","ETIHAD AIRWAYS"]
            print(pl1)
            co=int(input("enter 1-3 to choose your option:"))
            if co==1:
                E_plane=pl1[0]
            elif co==2:
                E_plane=pl1[1]
            else:
                E_plane==pl1[2]

                
        elif E_chico==2:
            E_destination=chi[1]
            pl2=["INDIGO", "EMIRATES","VISTARA","SINGAPORE AIRLINES"]
            print(pl2)
            co=int(input("enter 1-3 to choose your option:"))
            if co==1:
                E_plane=pl2[0]
            elif co==2:
                E_plane=pl2[1]
            else:
                E_plane=pl2[2]

                
        elif E_chico==3:
            E_destination=chi[2]
            pl3=["INDIGO", "EMIRATES","VISTARA","SINGAPORE AIRLINES"]
            print(pl3)

            co=int(input("enter 1-3 to choose your option:"))
            if co==1:
                E_plane=pl3[0]
            elif co==2:
                E_plane=pl3[1]
            else:
                E_plane=pl3[2]
        elif E_chico==4:
            E_destination=chi[3]
            pl4=["THAI AIRWAYS", "SINGAPORE AIRLINES", "JAPAN AIRLINES","VISTARA"]
            print(pl4)

            co=int(input("enter 1-4 to choose your option:"))
            if co==1:
                E_plane=pl4[0]
            elif co==2:
                E_plane=pl4[1]
            elif co==3:
                E_plane=pl4[2]
            else:
                E_plane=pl4[3]
                
        elif E_chico==5:
            E_destination=chi[4]
            pl5=["ETIHAD AIRWAYS", "EMIRATES", "QATAR","OMAN AIR"]
            print(pl5)

            co=int(input("enter 1-4 to choose your option:"))
            if co==1:
                E_plane=pl5[0]
            elif co==2:
                E_plane=pl5[1]
            elif co==3:
                E_plane=pl5[2]
            else:
                E_plane=pl5[3]
            



            
        elif E_chico==6:
            E_destination=chi[5]
            pl6=["LUFTHANSA", "EMIRATES", "QATAR","ETIHAD AIRWAYS"]
            print(pl6)

            co=int(input("enter 1-4 to choose your option:"))
            if co==1:
                E_plane=pl6[0]
            elif co==2:
                E_plane=pl6[1]
            elif co==3:
                E_plane=pl6[2]
            else:
                E_plane=pl6[3]



            co=int(input("enter 1-3 to choose your option:"))
            if co==1:
                E_plane=pl6[0]
            elif co==2:
                E_plane=pl6[1]
            elif co==3:
                E_plane=pl6[2]
            else:
                E_plane=pl16[3]
        else:
            print("you have entered wrong choice!!")
        E_seats=int(input("enter no of passangers travelling:"))
        E_cost=4000*E_seats
        E_total=print("$",E_cost)
        print("total amount for the booking=$",E_cost)
        import csv
        with open('bookings.csv', 'a', newline="") as file:
            myFile =csv.writer(file)
            myFile.writerow([E_name,E_plane,E_seats,E_destination,E_cost,E_pass])
        
    elif(chociew==2):
        global row
        #update details in booking.csv
        import csv
        # Ask the user for their phone number
        passo = input("Enter your passport number: ")
        # Open the CSV file for reading
        with open('bookings.csv', 'r') as file:
            # Create a CSV reader object
            reader = csv.reader(file)
            # Read the data into a list
            data = list(reader)
        for i, row in enumerate(data):
            # Check if the phone number is in the row
            if passo in row:
                # Ask the user for the new information
                print("to modify data of passanger name enter:a")
                print("to modify data of ailine enter:b")
                print("to modify data of no of passangers enter:c")
                print("to modify data of cost enter:d")
                print("to modify data of passport no enter:e")
                choice_make=input("enter your choice").lower()
                if(choice_make=="a"):
                    sur1=input("enter your surname:")
                    # Update the row with the new information
                    data[i][0] = sur1
                    print(row)
                    print("the changes in the surname is sucessfully updated")
                elif(choice_make=="b"):
                    nam1=input("enter new airline:").upper()
                    # Update the row with the new information
                    data[i][1] =nam1
                    print(row)
                elif(choice_make=="c"):
                    gen1=int(input("enter no of passangers:"))
                    # Update the row with the new information
                    data[i][2] =gen1
                elif(choice_make=="d"):
                    gen2=int(input("enter cost:"))
                    # Update the row with the new information
                    data[i][3] =gen2
                elif(choice_make=="e"):
                    gen3=int(input("enter passportno:"))
                    # Update the row with the new information
                    data[i][5] =gen3
                else:
                    print("go to the opened program thankyou for your patience!!")
                #now the entered information will be changed in the excel sheet
                with open('booking.csv', 'w', newline='') as afile:
                    # Create a CSV writer object
                    writer = csv.writer(afile)
                    # Write the data back to the file
                    print("worked till here")
                    writer.writerows(row)
    elif(chociew==3):
        #to just display details
        import csv
        # Ask the user for their phone number
        phone_number = input("Enter your phone number: ")
        # Open the CSV file for reading
        with open('bookings.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)
        for i, row in enumerate(data):
            # Check if the phone number is in the row
            if phone_number in row:
                # Print the row
                print(row)
                print("------------------PRINTING DETAILS-----------------")
                print("passanger name:",data[i][0])
                print("airline:",data[i][1])
                print("no of passangers:",data[i][2])
                print("cost:",data[i][3])
                print("passportno:",data[i][5])
                print("----------------------------------------------------")
    else:
        print("you have entered wrong choice")
        print("go to the software")



        
        
      
                
    
#----------------------------------------------------------------------------------------------------------------------------------------------------
    
    
#booking form part-1     
def place_booking(name_entry,place_var,phone_entry):
    global name,place,seat_entry,phoneno,email
    name= name_entry.get()
    place=place_var.get()
    phoneno=phone_entry.get()
    #["DUBAI", "SINGAPORE", "JAPAN","KOREA","SAUDI ARABIA","SWIZTERLAND"]
    if place=="DUBAI":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["INDIGO", "EMIRATES", "QATAR","ETIHAD AIRWAYS"]
        flight_combobox.pack(pady=5)
        calculate_label()

        
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)

           
    elif place=="SINGAPORE":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["INDIGO", "EMIRATES","VISTARA","SINGAPORE AIRLINES"]
        flight_combobox.pack(pady=5)
        calculate_label()
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)

    elif place=="TOKYO":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["THAI AIRWAYS", "SINGAPORE AIRLINES", "JAPAN AIRLINES","VISTARA"]
        flight_combobox.pack(pady=5)
        calculate_label()
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)
        
    elif place=="KOREA":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["THAI AIRWAYS", "SINGAPORE AIRLINES", "QATAR","VISTARA"]
        flight_combobox.pack(pady=5)
        calculate_label()
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)
        
    elif place=="SAUDI ARABIA":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["ETIHAD AIRWAYS", "EMIRATES", "QATAR","OMAN AIR"]
        flight_combobox.pack(pady=5)
        calculate_label()
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)
        
    elif place=="SWIZTERLAND":
        flight_label = tk.Label(booking_window, text="Flight:")
        flight_label.pack(pady=5)
        flight_var = tk.StringVar()
        flight_combobox = ttk.Combobox(booking_window, textvariable=flight_var)
        flight_combobox['values'] = ["LUFTHANSA", "EMIRATES", "QATAR","ETIHAD AIRWAYS"]
        flight_combobox.pack(pady=5)
        calculate_label()
        
        save_button3 = tk.Button(booking_window, text="Save Booking", command=lambda:save_booking(name,place,flight_var,seats_entry,phoneno,))
        save_button3.pack(pady=5)
        
        


        
#to calculate price and show it        
def calculate_label():
    global seats_entry
    instructions_label = tk.Label(booking_window, text="Enter the number of seats:")
    instructions_label.pack(pady=5)
    seats_entry = tk.Entry(booking_window)
    seats_entry.pack()
    calculate_button = tk.Button(booking_window, text="Calculate Total", command=update_label)
    calculate_button.pack()
 #to calculate price and show it part-2   
def update_label():
    global total_price
    price = tk.StringVar()
    label = tk.Label(booking_window, text="", font=("Arial", 16))
    label.pack(pady=5)
    price.set("3000.00")
    try:
        num_seats = int(seats_entry.get())
        total_price = num_seats * float(price.get())
        label.config(text=f"Total Price: ${total_price:.2f}")
    except ValueError:
        label.config(text="Invalid input. Enter a valid number of seats.")

        
        
#save all the enetered data into csv(booking deatils)        
def save_booking(name,place,flight_var,seats_entry,phoneno):
    flight = flight_var.get()
    seat = seats_entry.get()
    total=total_price
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, flight, seat, place, total, phoneno])
    
    messagebox.showinfo("Success", "Booking saved successfully")
   

    exit_button = Button(booking_window, text="Exit", command=booking_window.destroy)
    exit_button.pack(pady=10)
#---------------------------------------------------------------------------------------------------------------------------------------------
#booking form part-1    
def create_booking_window():
    global booking_window
    booking_window = tk.Toplevel(in_window)
    booking_window.title("Book a Flight")
    booking_window.geometry("990x660+50+50")
    bkImage=ImageTk.PhotoImage(file="mainpage.jpg")
    bkLabel=Label(booking_window,image=bkImage)
    bkLabel.place(x=0,y=0)
   
    # Booking form
    name_label = tk.Label(booking_window, text="Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(booking_window)
    name_entry.pack(pady=5)

    place_label = tk.Label(booking_window, text="Destination:")
    place_label.pack(pady=5)

    place_var = tk.StringVar()
    place_combobox = ttk.Combobox(booking_window, textvariable=place_var)
    place_combobox['values'] = ["DUBAI", "SINGAPORE", "TOKYO","KOREA","SAUDI ARABIA","SWIZTERLAND"]
    place_combobox.pack(pady=5)

    phone_label = tk.Label(booking_window, text="passport no:")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(booking_window)
    phone_entry.pack(pady=5)
        

    if not name_entry or not place_var or not phone_entry :
        messagebox.showerror("Error", "Please fill in all fields")
        return

    save_button1 = tk.Button(booking_window, text="confirm destination", command=lambda:place_booking(name_entry,place_var,phone_entry))
    save_button1.pack(pady=5)

#--------------------------------------------------------------------------------------------------------------------------------------------
def paymet_page():
    with open("payment_updated.py") as f:
        exec(f.read())



#--------------------------------------------------------------------------------------------------------------------------------------------

def exit_now():
    exit()

    
#window1
in_window=tk.Tk()
in_window.geometry("990x660+50+50")
in_window.resizable(0,0)
in_window.title("NAVI GO")
in_window.iconbitmap('onlylogo')

inImage=ImageTk.PhotoImage(file="mainpage.jpg")
inLabel=Label(in_window,image=inImage)
inLabel.place(x=0,y=0)


#text in window-1
#heading
heading=Label(in_window,text="WELCOME TO",font=("Adobe Clean UX",30,"bold"),bg="White",fg="black")
heading.place(x=100,y=170)
heading=Label(in_window,text="NAVI GO",font=("Adobe Clean UX",30,"bold"),bg="White",fg="black")
heading.place(x=120,y=205)
#createing buttons
bookButton=Button(in_window,text="BOOK TICKETS",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=45,pady=5,command=create_booking_window)
bookButton.place(x=200,y=340)
adminButton=Button(in_window,text="ADMIN LOGIN",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=15,pady=5,command=admin_login)
adminButton.place(x=750,y=35)

emmiButton=Button(in_window,text="IMMIGRATION",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=45,pady=5,command=immik)
emmiButton.place(x=200,y=430)

boardButton=Button(in_window,text="E-BOARDING PASS",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=35,pady=5,command=window78)
boardButton.place(x=200,y=390)
bagButton=Button(in_window,text="BAGGAGE PASS",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=40,pady=5,command=window89)
bagButton.place(x=200,y=480)
saButton=Button(in_window,text="PAYMENT",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=55,pady=5,command=paymet_page)
saButton.place(x=200,y=520)
eaButton=Button(in_window,text="EXIT",bd=0,bg="Black",activebackground="black",cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1',padx=70,pady=5,command=exit_now)
eaButton.place(x=200,y=560)





in_window.mainloop()



