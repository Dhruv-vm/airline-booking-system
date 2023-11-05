from tkinter import *
from PIL import ImageTk



#function
def connect_database ():
    print ('hello')
def login_paged():
    signup_window.destroy()
    with open("loginsystem.py") as f:
        exec(f.read())

global signup_window        
signup_window=Tk()
#bk image
signup_window.title('Signup page')
signup_window.resizable(0,0)
background=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(signup_window,image=background)
bgLabel.grid()


frame=Frame(signup_window)
frame.place(x=580, y=110)
#text
heading=Label (frame, text='CREATE AN ACCOUNT', font=('Microsoft Yahei UI Light', 23,'bold'),bg='White',fg='firebrick1')
heading.grid(row=0,column=0)
#email
emailLabel=Label(frame,text='Email',font=('Microsoft Yahei UI Light', 10, 'bold'),bg="White",fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=20,pady=(20, 0))
#email entry
emailEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),fg="White",bg="firebrick1")
emailEntry.grid(row=2,column=0,sticky='w',padx=20)



#username
usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei UI Light', 10, 'bold'),bg="White",fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=20,pady=(20 , 0))
#username  entry
usernameEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),fg="White",bg="firebrick1")
usernameEntry.grid(row=4,column=0,sticky='w',padx=20)


#password
passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei UI Light', 10, 'bold'),bg="White",fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=20,pady=(20, 0))
#username  entry
passwordEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),fg="White",bg="firebrick1")
passwordEntry.grid(row=6,column=0,sticky='w',padx=20)

#confirm password
confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light', 10, 'bold'),bg="White",fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=20,pady=(20, 0))
#username  entry
confirmpasswordEntry=Entry(frame, width=30, font=('Microsoft Yahei UI Light', 10, 'bold'),fg="White",bg="firebrick1")
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=20)

#terms and conditions
termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light', 10, 'bold'),
                               fg="firebrick1",bg="white",activebackground="white",activeforeground="firebrick1",cursor="hand2")
termsandconditions.grid(row=9,column=0,padx=20,pady=(20, 0))

#sign up button

signupButton=Button (frame, text= 'Signup', font=('Microsoft Yahei UI Light', 16, 'bold'),bd=0,bg="firebrick1",fg="firebrick1",
                     activebackground="white",activeforeground="firebrick1",width=17,command=connect_database)
signupButton.grid(row=10,column=0,padx=20,pady=(20, 0))

#already account
alreadyaccount=Label (frame, text="Don't have an account?", font=('Open Sans', '9', 'bold'),
                      bg='white', fg='firebrick1')
alreadyaccount.grid(row=11, column=0, sticky='w' ,padx=25,pady=10)

#login button
LoginButton=Button (frame, text='Log in', font=('Open Sans', 9,'bold underline'),
                    bg='white', fg='blue', bd=0, cursor= 'hand2', activebackground='white' , activeforeground= 'blue',command=login_paged)
LoginButton.place(x=150,y=375)

signup_window.mainloop ()
