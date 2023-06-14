from tkinter import *
import time
import ttkthemes
from tkinter import ttk
import pymysql
from tkinter import messagebox,filedialog
import pandas as pd


def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=student_table.get_children()
    newlist=[]
    for index in indexing:
        content=student_table.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pd.DataFrame(newlist,columns=['Enrollment No.','Name','Phone No.','Email','Address','Gender','D.O.B','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved successfully')

def toplevel_data(title,button_text,command):
    global identry,nameentry,phoneentry,emailentry,adddressentry,genderentry,dobentry,screen

    screen = Toplevel()
    screen.resizable(0, 0)
    screen.grab_set()
    screen.title(title)

    idlabel = Label(screen, text='Id', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    idlabel.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    identry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    identry.grid(row=0, column=1, padx=20, pady=10)

    namelabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    namelabel.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    nameentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameentry.grid(row=1, column=1, padx=20, pady=10)

    phonelabel = Label(screen, text='Phone No.', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    phonelabel.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    phoneentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneentry.grid(row=2, column=1, padx=20, pady=10)

    emaillabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    emaillabel.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    emailentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailentry.grid(row=3, column=1, padx=20, pady=10)

    adddresslabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    adddresslabel.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    adddressentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    adddressentry.grid(row=4, column=1, padx=20, pady=10)

    genderlabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    genderlabel.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    genderentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderentry.grid(row=5, column=1, padx=20, pady=10)

    doblabel = Label(screen, text='Date Of Birth', font=('times new roman', 20, 'bold'), padx=10, pady=10)
    doblabel.grid(row=6, column=0, padx=10, pady=10, sticky=W)
    dobentry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobentry.grid(row=6, column=1, padx=20, pady=10)

    student_btn = ttk.Button(screen, text=button_text, command=command)
    student_btn.grid(row=7, columnspan=2, pady=10)

    if title=='Update Student':

        indexing = student_table.focus()
        print(indexing)
        content = student_table.item(indexing)
        listdata = content['values']
        identry.insert(0, listdata[0])
        nameentry.insert(0, listdata[1])
        phoneentry.insert(0, listdata[2])
        emailentry.insert(0, listdata[3])
        adddressentry.insert(0, listdata[4])
        genderentry.insert(0, listdata[5])
        dobentry.insert(0, listdata[6])


def update_data():
    query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameentry.get(),phoneentry.get(),emailentry.get(),adddressentry.get(),genderentry.get(),dobentry.get(),
                            date,current_time,identry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {identry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()




def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        student_table.insert('', END, values=data)

def delete_student():
    indexing=student_table.focus()
    print(indexing)
    content=student_table.item(indexing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    student_table.delete(*student_table.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        student_table.insert('', END, values=data)

def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(identry.get(),nameentry.get(),emailentry.get(),phoneentry.get(),adddressentry.get(),genderentry.get(),dobentry.get()))
    student_table.delete(*student_table.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
        student_table.insert('', END, values=data)




def add_data():
    if identry.get()=='' or nameentry.get()=='' or phoneentry.get()=='' or emailentry.get()=='' or adddressentry.get()=='' or \
            genderentry.get()=='' or dobentry.get()=='':
        messagebox.showerror('Error','All Fields are required',parent=screen)

    else:
        try:
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(identry.get(),nameentry.get(),phoneentry.get(),emailentry.get(),adddressentry.get(),genderentry.get(),
                                    dobentry.get(),date,current_time))
            con.commit()
            result=messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                identry.delete(0,END)
                nameentry.delete(0,END)
                phoneentry.delete(0,END)
                emailentry.delete(0,END)
                adddressentry.delete(0,END)
                genderentry.delete(0,END)
                dobentry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Error','Id cannot be repeated',parent=screen)
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?',
                                         parent=screen)
            if result:
                identry.delete(0, END)
                nameentry.delete(0, END)
                phoneentry.delete(0, END)
                emailentry.delete(0, END)
                adddressentry.delete(0, END)
                genderentry.delete(0, END)
                dobentry.delete(0, END)
            else:
                pass

        query='select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        student_table.delete(*student_table.get_children())

        for data in fetched_data:
            student_table.insert('',END,values=data)



def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost', user='root', password='12345')
            mycursor=con.cursor()

        except:
            messagebox.showerror('Error','Invalid Details',parent=connectwindow)
            return

        try:

            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key, name varchar(30), mobile varchar(10), email varchar(30),' \
                  'address varchar(100), gender varchar(30), dob varchar(20), date varchar(50), time varchar(50))'
            mycursor.execute(query)

        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is sucessful', parent=connectwindow)
        connectwindow.destroy()

        addstudentbtn.config(state=NORMAL)
        searchstudentbtn.config(state=NORMAL)
        deletestudentbtn.config(state=NORMAL)
        updatestudentbtn.config(state=NORMAL)
        showstudentbtn.config(state=NORMAL)
        exportstudentbtn.config(state=NORMAL)
        showstudentbtn.config(state=NORMAL)


    connectwindow=Toplevel()
    connectwindow.grab_set() # used because window is getting minimized
    connectwindow.geometry('470x270+730+230')
    connectwindow.title('Database Connection')
    connectwindow.resizable(0,0)

    hostnamelabel=Label(connectwindow,text='Host Name',font=('arial',20,'bold'))
    hostnamelabel.grid(row=0,column=0,padx=20,pady=20)

    hostentry=Entry(connectwindow,font=('roman',15,'bold'),bd=2)
    hostentry.grid(row=0,column=1,padx=30,pady=20)

    usernamelabel = Label(connectwindow, text='User Name', font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0, padx=20, pady=20)

    userentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    userentry.grid(row=1, column=1, padx=30, pady=20)

    pswdlabel = Label(connectwindow, text='Password', font=('arial', 20, 'bold'))
    pswdlabel.grid(row=2, column=0, padx=20, pady=20)

    pswdentry = Entry(connectwindow, font=('roman', 15, 'bold'), bd=2)
    pswdentry.grid(row=2, column=1, padx=30, pady=20)

    connectbtn=ttk.Button(connectwindow,text='CONNECT',command=connect)
    connectbtn.grid(row=3,columnspan=2)


def clock():
    global date,current_time
    date=time.strftime('%d/%m/%Y')
    current_time=time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'   Date : {date}\nTime : {current_time}')
    datetimelabel.after(1000,clock)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text='  '
    text=text+s[count]
    sliderlabel.config(text=text)
    count+=1
    sliderlabel.after(300,slider)

root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme('radiance')

root.state('zoomed')
root.resizable(False,False)
root.title('Student Management System')

datetimelabel=Label(root,text='hello',font=('times new roman',18,'bold'))
datetimelabel.place(x=5,y=5)
clock()

s='STUDENT MANAGEMENT SYSTEM'
sliderlabel=Label(root,text=s,font=('Arial',28,'bold'),width=35)
sliderlabel.place(x=250,y=0)
slider()

connectbutton=ttk.Button(root,text='Connect Database',command=connect_database)
connectbutton.place(x=1100,y=10)

leftframe=Frame(root)
leftframe.place(x=50,y=80,width=300,height=600)

logo_img=PhotoImage(file='student1.png')
logo_label=Label(leftframe,image=logo_img)
logo_label.grid(row=0,column=0)

addstudentbtn=ttk.Button(leftframe,text='Add Student',width=25,state=DISABLED,command=lambda :toplevel_data('Add Student','Add',add_data))
addstudentbtn.grid(row=1,column=0,pady=20)

searchstudentbtn=ttk.Button(leftframe,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentbtn.grid(row=2,column=0,pady=20)

deletestudentbtn=ttk.Button(leftframe,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentbtn.grid(row=3,column=0,pady=20)

updatestudentbtn=ttk.Button(leftframe,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentbtn.grid(row=4,column=0,pady=20)

showstudentbtn=ttk.Button(leftframe,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentbtn.grid(row=5,column=0,pady=20)

exportstudentbtn=ttk.Button(leftframe,text='Export Data',width=25,state=DISABLED,command=export_data)
exportstudentbtn.grid(row=6,column=0,pady=20)

exitbtn=ttk.Button(leftframe,text='Exit',width=25,command=iexit)
exitbtn.grid(row=7,column=0,pady=20)

rightframe=Frame(root)
rightframe.place(x=450,y=80,width=820,height=600)

# adding scroll bar to right frame

scrollBarX=Scrollbar(rightframe,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightframe,orient=VERTICAL)


# tree view

student_table=ttk.Treeview(rightframe,columns=('Enrollment No.','Name','Mobile Number','Email Id','Address','Gender','DOB','Added Date',
                                               'Added Time'),xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=student_table.xview)
scrollBarY.config(command=student_table.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
student_table.pack(fill=BOTH,expand=1)

student_table.heading('Enrollment No.',text='Enrollment No.')
student_table.heading('Name',text='Name')
student_table.heading('Mobile Number',text='Mobile Number')
student_table.heading('Email Id',text='Email Id')
student_table.heading('Address',text='Address')
student_table.heading('Gender',text='Gender')
student_table.heading('DOB',text='DOB')
student_table.heading('Added Date',text='Added Date')
student_table.heading('Added Time',text='Added Time')

student_table.column('Enrollment No.',width=150,anchor=CENTER)
student_table.column('Name',width=300,anchor=CENTER)
student_table.column('Mobile Number',width=200,anchor=CENTER)
student_table.column('Email Id',width=300,anchor=CENTER)
student_table.column('Address',width=300,anchor=CENTER)
student_table.column('Gender',width=200,anchor=CENTER)
student_table.column('DOB',width=200,anchor=CENTER)
student_table.column('Added Date',width=200,anchor=CENTER)
student_table.column('Added Time',width=200,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),background='white',fieldbackground='white')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='red')

student_table.config(show='headings')


root.mainloop()