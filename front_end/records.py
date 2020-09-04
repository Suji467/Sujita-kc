from tkinter import*
from tkinter import ttk
from back_end.connection import DbConnection
from tkinter import messagebox
from model.model_class import *


def linear_search( record, Name):
    for i in record:
        print(i)
        if i == Name:
            return True
    return False
class Teacher():
    def __init__(self, root):
        self.root = root
        self.root.title("Show Record")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg='sky blue')
        title = Label(self.root, text='Records Of members ', bd=10, relief=GROOVE,
                      font=("times new roman", 40, 'bold'), bg='cyan')
        title.pack(side=TOP, fill=X)
        # ====================connection object=====================================
        self.dbconnect = DbConnection()
        self.ent_ID = StringVar()
        self.ent_Name = StringVar()
        self.ent_Residence = StringVar()
        self.ent_DOB = StringVar()
        self.combo_Gender = StringVar()
        self.ent_Contact = StringVar()
        self.ent_Email = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()
        # ====================Detail frame in window=====================================
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg='magenta')
        Detail_Frame.place(x=300, y=100, width=800, height=580)
        # ====================Widget in Detail frame=====================================
        lbl_search = Label(Detail_Frame, text="Search By Full Name", bg="magenta", fg="black",
                           font=("times new roman", 20, 'bold'))
        lbl_search.grid(row=0, column=0, pady=10, padx=5, sticky="w")
        self.txt_Search = Entry(Detail_Frame, textvariable=self.search_txt, width=15,
                                font=("times new roman", 14, 'bold'),
                                bd=5,
                                relief=GROOVE)
        self.txt_Search.grid(row=0, column=2, pady=10, padx=5, sticky="w")
        # ====================Buttons in Detail Frame=====================================
        Searchbtn = Button(Detail_Frame, text='Search', width=15, pady=5, command=self.search_data).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=1,
                                                                                                         pady=10)
        Showallbtn = Button(Detail_Frame, text='Show All', width=15, pady=5, command=self.fetch_data).grid(
            row=0,
            column=4,
            padx=1,
            pady=10)
        updatebtn = Button(Detail_Frame, text='Update', width=15, pady=5, command=self.update_delete).grid(
            row=0,
            column=5,
            padx=1,
            pady=10)

        # ====================Table frame in window=====================================
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg='magenta')
        Table_Frame.place(x=10, y=70, width=760, height=500)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Test_Table = ttk.Treeview(Table_Frame,
                                       columns=("ID", "Name", "Residence", "DOB", "Gender", "Contact", "Email"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Test_Table.xview)
        scroll_y.config(command=self.Test_Table.yview)
        self.Test_Table.heading("ID", text="ID")
        self.Test_Table.heading("Name", text="Name")
        self.Test_Table.heading("Residence", text="Residence")
        self.Test_Table.heading("DOB", text="DOB")
        self.Test_Table.heading("Gender", text="Gender")
        self.Test_Table.heading("Contact", text="Contacts")
        self.Test_Table.heading("Email", text="Email")
        self.Test_Table['show'] = 'headings'
        self.Test_Table.column("ID", width=100)
        self.Test_Table.column("Name", width=100)
        self.Test_Table.column("Residence", width=100)
        self.Test_Table.column("DOB", width=100)
        self.Test_Table.column("Gender", width=100)
        self.Test_Table.column("Contact", width=100)
        self.Test_Table.column("Email", width=150)
        self.Test_Table.pack(fill=BOTH, expand=1)
        self.fetch_data()

    def fetch_data(self):
        query = "select * from computer;"
        records = self.dbconnect.select(query)
        if len(records) != 0:
            self.Test_Table.delete(*self.Test_Table.get_children())
            for row in records:
                self.Test_Table.insert('', END, values=row)
    def search_data(self):
        if self.txt_Search.get() == "":
            messagebox.showinfo("Error", "Searching information required")
        else:
            query = "select * from computer where Name=%s;"
            values = (self.txt_Search.get(),)
            records = self.dbconnect.search(query, values)
            list = []
            for row in records:
                list.append(row[1])
            if not linear_search(list, self.txt_Search.get()):
                messagebox.showinfo("Error", "This Name doesnot exist")
            elif len(records) != 0:
                self.Test_Table.delete(*self.Test_Table.get_children())
                for row in records:
                    self.Test_Table.insert('', END, values=row)
    def update_delete(self):
        class Main_Interface():
            def __init__(self, root):
                self.wn = root
                self.wn.geometry('400x500')
                self.wn.configure(bg='#D8BFD8')
                self.wn.title('Help Application')
                heading = Label(self.wn, text=' New Registration Page', bd=5, bg='#33A1C9', font=('arial', 15, 'bold'))
                heading.pack(side=TOP, fill=X)
                lbl_heading = Label(root, text='Add Citizenship ID Number/Institution ID ', bd=5, bg="light pink",
                                    font=('arial', 15))
                lbl_heading.pack(side=TOP, fill=X)
                # ==========making the object of the connection===========================
                self.dbconnect = DbConnection()
                # =================main frame================
                main_frame = Frame(self.wn, bg='#54FF9F')
                main_frame.place(x=30, y=71, width=330, height=350)
                btn_frame = Frame(self.wn, bg='#EE7AE9', bd=5)
                btn_frame.place(x=30, y=420, width=330, height=50)
                # =================widget in main frame=============
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
                self.combo_Gender = ttk.Combobox(main_frame, font=('arial', 15, 'bold'), width=12, state='readonly')
                self.combo_Gender['values'] = ('Male', 'Female', 'Others')
                self.combo_Gender.grid(row=4, column=1, padx=20)
                lbl_Contact = Label(main_frame, text='Contact', font=('arial', 15, 'bold'), width=8, bg='#F08080')
                lbl_Contact.grid(row=5, column=0, padx=10, pady=10)
                self.ent_Contact = Entry(main_frame)
                self.ent_Contact.grid(row=5, column=1, padx=10, pady=10)
                lbl_Email = Label(main_frame, text='Email', font=('arial', 15, 'bold'), width=8, bg='#F08080')
                lbl_Email.grid(row=6, column=0, padx=10, pady=10)
                self.ent_Email = Entry(main_frame)
                self.ent_Email.grid(row=6, column=1, padx=10, pady=10)
                # =================button in mainframe=========================
                btn_update = Button(btn_frame, text='Update', font=('arial', 12, 'bold'), width=8, bg='#1C86EE',
                                 command=self.update)
                btn_update.pack(side=LEFT, padx=10, pady=10)

                btn_delete = Button(btn_frame, text='Delete', font=('arial', 12, 'bold'), width=8, bg='#1C86EE',
                                   command=self.delete)
                btn_delete.pack(side=RIGHT, padx=10, pady=10)

                btn_clear = Button(btn_frame, text='Clear', font=('arial', 12, 'bold'), width=8, bg='#1C86EE',
                                   command=self.clear)
                btn_clear.pack(side=RIGHT, padx=10, pady=10)

            def update(self):
                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Residence.get(), self.ent_DOB.get(),
                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                query = 'update computer set Name=%s,Residence=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
                values = (stu_ref.get_Name(), stu_ref.get_Residence(), stu_ref.get_DOB(), stu_ref.get_Gender(),
                          stu_ref.get_Contact(), stu_ref.get_Email(), int(stu_ref.get_ID()))
                self.dbconnect.update(query, values)
                messagebox.showinfo("Success", " Your data updated Successfully")

            def delete(self):
                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Residence.get(), self.ent_DOB.get(),
                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                query = 'delete from computer where ID=%s;'
                values = (int(stu_ref.get_ID()),)
                self.dbconnect.delete(query, values)
                messagebox.showinfo("Success", "Your data deleted Successfully")

            def clear(self):
                self.ent_ID.delete(0, END)
                self.ent_Name.delete(0, END)
                self.ent_Residence.delete(0, END)
                self.ent_DOB.delete(0, END)
                self.combo_Gender.delete(0, END)
                self.ent_Contact.delete(0, END)
                self.ent_Email.delete(0, END)

        race = Tk()
        Main_Interface(race)
        race.mainloop()

root = Tk()
Teacher(root)
root.mainloop()