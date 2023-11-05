#impoting module
from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql


#functions
def forget_pass():
    def change_password():
        if user_entry.get()=="" or newpass_entry.get()=="" or confirmpass_entry.get()=="":
            messagebox.showerror("Error","All fields must be enetred",parent=window73)
        elif newpass_entry.get()!= confirmpass_entry.get():
            messagebox.showerror("Error","Password and Confirm password do not match!",parent=window73)
        else:
            con=pymysql.connect(host="localhost",user="root",password="root",database="userdata")
            mycursor=con.cursor()
            query="select * from data where username=%s"
            mycursor.execute(query,(user_entry.get()))
            row=mycursor.fetchone()
            if row == None:
                messagebox.showerror("Error","Incorrect username",parent=window73)
            else:
                query="update data set password =%s where username=%s"
                mycursor.execute(query,(newpass_entry.get(),user_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("success","Password Changed Successfuly ,Now Login With New Password",parent=window73)
                window73.destroy()
                    
    window73=Toplevel()
    window73.title("change password")
    #for background image of the window
    bgPic=Image.Tk(file="background.jpg")
    bglabel= Label(window73,image=bgPic)
    bgabel.grid()
    #heading
    heading_label = Label(windwo73, text='RESET PASSWORD', font=('arial', '18', 'bold'),
                      bg= 'White', fg='magenta2')
    heading_label. place(x=480, y=60)
    
    #username
    userLabel = Label(window73, text='Username', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    userLabel.place (x=470,y=130)

    user_entry = Entry(window73, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    user_entry.place(x=470,y=160)

    Frame (window73, width=250, height=2, bg='orchid1'). place(x=470, y=260)
    #password
    passwordLabel = Label(window73, text='New Password', font=('arial', 12, 'bold'), bg='white', fg= 'orchid1' )
    passwordLabel. place (x=470, =210)

    newpass_entry = Entry(window73, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    newpass_entry. place (x=470, y=240)

    Frame (window73, width=250, height=2, bg='orchid1'). place(x=470, y=260)

    
    #confirm password
    confirmpassLabel = Label(window73, text='Confirm Password', font=('arial', 12, 'bold'), bg='white', fg='orchid1')
    confirmpassLabel.place(x=470,y=290)

    confirmpass_entry = Entry(window73, width=25, fg='magenta2', font=('arial', 11, 'bold'), bd=0)
    confirmpass_entry.place(x=470, y=320)

    Frame (window73, width=250, height=2, bg= 'orchid1'). place(x=470, y=340)

    #submit button
    submitButton = Button(window, text='Submit', bd=0, bg='magenta2', fg='white',font=('Open Sans', '16', 'bold'),width=19, cursor='hand2', activebackground='magenta2',
                          activeforeground= 'white',command=change_password)
    submitButton.place (x=470, y=390)
    



    window73.mainloop()



def login_user():
    if usernameEntry.get()=="" or passwordEntry.get()=="":
        messagebox.showerror("Error","All Fields Are Required")
    else:
        try:
            con=pymysql.connect(host="localhost",user="root",password="root")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error","connection failed")
            return
        query="use userdata"
        mycursor.execute(query)
        query="select * from data where username=%s and password=%s"
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror("Error","Invalid username or password")
        else:
            messagebox.showinfo("Welcome","Login successful")
            #main program file name
            with open("MAIN_PROJECT UPDATED.py") as f:
                exec(f.read())
        


        
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
                    fg="firebrick1",activeforeground='firebrick1',command=forget_pass)
forgetButton.place(x=700,y=285)

#login button
loginButton=Button(login_window,text='Login',font=('Open Sans', 16, 'bold'),fg='firebrick1',bg='firebrick1',activeforeground='White',activebackground='firebrick1',cursor='hand2',bd=0,width=23,
                   command=login_user)
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
