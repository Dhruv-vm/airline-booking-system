import csv
  # Ask the user for their phone number
  phone_number = input("Enter your phone number: ")
  # Open the CSV file for reading
  with open('Passport Details Of Clint.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
  for i, row in enumerate(data):
    # Check if the phone number is in the row
    if phone_number in row:
      # Print the row
      print(row)
      print("------------------PRINTING DETAILS-----------------")
      print("Surname:",data[i][3]).title()
      print("Name:",data[i][4]).title()
      print("Age:",data[i][14])
      print("Gender:",data[i][6])
      print("Date of birth:",data[i][7])
      print("Place of birth:",data[i][8])
      print("exipiry date of passport:",data[i][11])
      print("Phone no:",data[i][12])
      print("Aadhar card:",data[i][13])
      print("------------------------------------------------------------")
