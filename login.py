from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

# for login functionality
def login():
    if username_entry.get()=='' or pswd_entry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif username_entry.get()=='Vedant' and pswd_entry.get()=='12345':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms

    else:
        messagebox.showerror('Error','Please enter correct credentials')


window=Tk()

window.state('zoomed')
window.resizable(False,False)
window.title('Login System of Student Management System')

 # importing background image
bg_img=ImageTk.PhotoImage(file='bg.jpg')

# creating label for adding background image
bg_label=Label(window,image=bg_img)
bg_label.place(x=0,y=0)

# creating frame
login_frame=Frame(window,bg='white')
login_frame.place(x=400,y=150)

# adding logo image inside a frame
logo_img=PhotoImage(file='logo.png')
logo_label=Label(login_frame,image=logo_img)
logo_label.grid(row=0,column=0,columnspan=2,pady=20)

username_img=PhotoImage(file='user.png')
# creating labels for username and password
username_label=Label(login_frame,image=username_img,text='USERNAME',compound=LEFT
                     ,font=('times new roman',20,'bold'),bg='white')
# here compound is used in order to display both text and image whereas LEFT is used to keep image on which side
username_label.grid(row=1,column=0,pady=20,padx=20)

# creating entry field for username
username_entry=Entry(login_frame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
username_entry.grid(row=1,column=1,pady=20,padx=20)

pswd_img=PhotoImage(file='password.png')

pswd_label=Label(login_frame,image=pswd_img,text='PASSWORD',compound=LEFT
                     ,font=('times new roman',20,'bold'),bg='white')
# here compound is used in order to display both text and image whereas LEFT is used to keep image on which side
pswd_label.grid(row=2,column=0,pady=20,padx=20)

# creating entry field for username
pswd_entry=Entry(login_frame,font=('times new roman',20,'bold'),bd=5,fg='royalblue')
pswd_entry.grid(row=2,column=1,pady=20,padx=20)

# creating button

login_btn=Button(login_frame,text="LOGIN",font=('times new roman',14,'bold'),width=15
                 ,fg='white',bg='blue',activebackground='blue',
                 activeforeground='white',cursor='hand2',command=login)
login_btn.grid(row=3,column=1,pady=20)

window.mainloop()