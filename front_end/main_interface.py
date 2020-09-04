from tkinter import*
from back_end.connection import DbConnection
from tkinter import ttk
from model.model_class import Student
from tkinter import messagebox
class Main_Interface():
    def __init__(self,root):
        self.wn=root
        self.wn.geometry('400x500')
        self.wn.configure(bg='#D8BFD8')
        self.wn.title('Help Application')
        heading=Label(self.wn,text=' New Registration Page',bd=5,bg='#33A1C9',font=('arial',15,'bold'))
        heading.pack(side=TOP,fill=X)
        lbl_heading = Label(root, text='Add Citizenship ID Number/Institution ID ', bd=5, bg="light pink",
                            font=('arial', 15))
        lbl_heading.pack(side=TOP, fill=X)
        #==========making the object of the connection===========================
        self.dbconnect=DbConnection()
        #=================main frame================
        main_frame=Frame(self.wn,bg='#54FF9F')
        main_frame.place(x=30,y=71,width=330,height=350)
        btn_frame=Frame(self.wn,bg='#EE7AE9',bd=5)
        btn_frame.place(x=30,y=420,width=330,height=50)
        #=================widget in main frame=============
        lbl_ID = Label(main_frame, text='ID', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_ID.grid(row=0, column=0, padx=10, pady=10)
        self.ent_ID = Entry(main_frame)
        self.ent_ID.grid(row=0, column=1, padx=10, pady=10)
        lbl_Name = Label(main_frame, text='Name', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_Name.grid(row=1, column=0, padx=10, pady=10)
        self.ent_Name = Entry(main_frame)
        self.ent_Name.grid(row=1, column=1, padx=10, pady=10)
        lbl_Residence = Label(main_frame, text='Residence', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_Residence.grid(row=2, column=0, padx=10, pady=10)
        self.ent_Residence = Entry(main_frame)
        self.ent_Residence.grid(row=2, column=1, padx=10, pady=10)
        lbl_DOB = Label(main_frame, text='DOB', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_DOB.grid(row=3, column=0, padx=10, pady=10)
        self.ent_DOB = Entry(main_frame)
        self.ent_DOB.grid(row=3, column=1, padx=10, pady=10)
        lbl_Gender = Label(main_frame, text='Gender', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_Gender.grid(row=4, column=0, padx=10, pady=10)
        self.combo_Gender=ttk.Combobox(main_frame,font=('arial',15,'bold'),width=12,state='readonly')
        self.combo_Gender['values']=('Male','Female','Others')
        self.combo_Gender.grid(row=4,column=1,padx=20)
        lbl_Contact = Label(main_frame, text='Contact', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_Contact.grid(row=5, column=0, padx=10, pady=10)
        self.ent_Contact = Entry(main_frame)
        self.ent_Contact.grid(row=5, column=1, padx=10, pady=10)
        lbl_Email = Label(main_frame, text='Email', font=('arial', 15, 'bold'), width=8, bg='#F08080')
        lbl_Email.grid(row=6, column=0, padx=10, pady=10)
        self.ent_Email = Entry(main_frame)
        self.ent_Email.grid(row=6, column=1, padx=10, pady=10)
        #=================button in mainframe=========================
        btn_add = Button(btn_frame, text='Add', font=('arial', 12, 'bold'),width=8, bg='#1C86EE',command=self.add)
        btn_add.pack(side=LEFT, padx=10, pady=10)

        btn_clear = Button(btn_frame, text='Clear', font=('arial', 12, 'bold'),width=8, bg='#1C86EE',command=self.clear)
        btn_clear.pack(side=RIGHT, padx=10, pady=10)

    def add(self):
        stu_ref=Student(self.ent_ID.get(),self.ent_Name.get(),self.ent_Residence.get(),self.ent_DOB.get(),
                        self.combo_Gender.get(),self.ent_Contact.get(),self.ent_Email.get())
        query='insert into computer values(%s,%s,%s,%s,%s,%s,%s);'
        values=(int(stu_ref.get_ID()),stu_ref.get_Name(),stu_ref.get_Residence(),stu_ref.get_DOB(),
                stu_ref.get_Gender(),stu_ref.get_Contact(),stu_ref.get_Email())
        self.dbconnect.insert(query,values)
        messagebox.showinfo("Success","Your data Inserted Successfully")



    def clear(self):
        self.ent_ID.delete(0,END)
        self.ent_Name.delete(0, END)
        self.ent_Residence.delete(0, END)
        self.ent_DOB.delete(0, END)
        self.combo_Gender.delete(0, END)
        self.ent_Contact.delete(0, END)
        self.ent_Email.delete(0, END)
























race=Tk()
Main_Interface(race)
race.mainloop()