#impoting module
from tkinter import *
from PIL import ImageTk


#functions
def new_account12():
    login_window.destroy()
    with open("sign up.py") as f:
        exec(f.read())
def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
    
def on_enter (event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)

def password_enter (event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)

#guipart
#objet for tkinter
global login_window
login_window=Tk()
login_window.geometry("990x660+50+50")
login_window.resizable(None,None)
login_window.title("login page")

bgImage=ImageTk.PhotoImage(file="bg.jpg")
bgLabel=Label(login_window,image=bgImage)
#to place the image from start
bgLabel.place(x=0,y=0)

#heading
heading=Label(login_window,text="USER LOGIN",font=("Adobe Clean UX",30,"bold"),bg="White",fg="firebrick1")
heading.place(x=620,y=120)

#for entering login details
usernameEntry=Entry(login_window, width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),bd=0,fg="firebrick1")
usernameEntry.place(x=600,y=200)
usernameEntry.insert(0,'Username')
#for username
usernameEntry.bind('<FocusIn>', on_enter)
frame1=Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=580,y=224)
#for password
passwordEntry=Entry(login_window,width=25, font=('Microsoft Yahei UI Light', 11, 'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=600,y=245)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=580,y=270)

#eye button
openeye=PhotoImage(file="openeye.png")
eyeButton=Button(login_window,image=openeye,bd=0,bg='White',activebackground='white',cursor="hand2",command=hide)
eyeButton.place(x=800,y=240)

#forget button
forgetButton=Button(login_window,text="Forgot password?",bd=0,bg='white',activebackground='White',cursor="hand2",font=('Microsoft Yahei UI Light', 11, 'bold'),
                    fg="firebrick1",activeforeground='firebrick1')
forgetButton.place(x=700,y=285)

#login button
loginButton=Button(login_window,text='Login',font=('Open Sans', 16, 'bold'),fg='firebrick1',bg='firebrick1',activeforeground='White',activebackground='firebrick1',cursor='hand2',bd=0,width=23)
loginButton.place(x=585,y=350)

orLabel=Label (login_window, text='- - - - - - - - - OR - - - - - - - - -', font=('Open Sans' , 16),fg="firebrick1",bg="White")
orLabel.place(x=610,y=400)

#placeing icons
facebook_Logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_Logo,bg='White')
fbLabel.place(x=630,y=440)

google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='White')
googleLabel.place(x=680, y=440)

twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='White')
twitterLabel.place(x=730, y=440)

#labels
SignupLabel=Label (login_window, text='Dont have an account?', font=('Open Sans' , 9,"bold"),fg="firebrick1",bg="White")
SignupLabel.place(x=590,y=490)

NewaccountButton=Button(login_window,text='Create new one',font=('Open Sans', 9, 'bold underline'),fg="blue",bg="White",activebackground="blue",cursor='hand2',bd=0,width=23,command=new_account12)
NewaccountButton.place(x=690,y=490)



login_window.mainloop()
