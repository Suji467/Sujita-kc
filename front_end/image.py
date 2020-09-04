from tkinter import *
from PIL import ImageTk,Image
from back_end.connection import DbConnection
from tkinter import ttk
from model.model_class import Student
from tkinter import messagebox
def linear_search( record, Name):
    for i in record:
        print(i)
        if i == Name:
            return True
    return False
class Shyam():
    def __init__(self,image):
        self.wn=window
        self.wn.title("Animal")
        self.wn.geometry("1500x700")
        self.wn.canvas=Canvas (self.wn,width=5000,height=1000)
def Home():
    class Home():
        def __init__(self,image):
            self.wn=window
            self.wn.title("Home Page")
            self.wn.geometry("1500x700")
            self.wn.canvas=Canvas (self.wn,width=5000,height=1000)

    window = Toplevel()
    Home(window)
    canvas = Canvas(window, width=5000, height=1000)
    lbl_heading = Label(window, text='𝓦𝓔𝓛𝓒𝓞𝓜𝓔 𝓣𝓞 𝓑𝓔 𝓣𝓗𝓔 𝓥𝓞𝓘𝓒𝓔 𝓕𝓞𝓡 𝓣𝓗𝓔 𝓥𝓞𝓘𝓒𝓔𝓛𝓔𝓢𝓢',
                        bd=5, bg="pink",
                        font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='𝙰𝚁𝙴 𝚈𝙾𝚄 𝚆𝙸𝚃𝙷 𝚄𝚂? ', bd=5, bg='sky blue', font=('arial', 24, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\ma.png"))

    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()

def Registration():
    class Khatiwoda():
        def __init__(self,image):
            self.wn=window
            self.wn.title("Registration Page")
            self.wn.geometry("1500x700")
            self.wn.canvas=Canvas (self.wn,width=5000,height=1000)


    def Sundar():
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
                btn_add = Button(btn_frame, text='Add', font=('arial', 12, 'bold'), width=8, bg='#1C86EE',
                                 command=self.add)
                btn_add.pack(side=LEFT, padx=10, pady=10)

                btn_clear = Button(btn_frame, text='Clear', font=('arial', 12, 'bold'), width=8, bg='#1C86EE',
                                   command=self.clear)
                btn_clear.pack(side=RIGHT, padx=10, pady=10)

            def add(self):
                stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Residence.get(), self.ent_DOB.get(),
                                  self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                query = 'insert into computer values(%s,%s,%s,%s,%s,%s,%s);'
                values = (int(stu_ref.get_ID()), stu_ref.get_Name(), stu_ref.get_Residence(), stu_ref.get_DOB(),
                          stu_ref.get_Gender(), stu_ref.get_Contact(), stu_ref.get_Email())
                self.dbconnect.insert(query, values)
                messagebox.showinfo("Success", "Your data Inserted Successfully")

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

    def saumya():
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
                        heading = Label(self.wn, text=' New Registration Page', bd=5, bg='#33A1C9',
                                        font=('arial', 15, 'bold'))
                        heading.pack(side=TOP, fill=X)
                        lbl_heading = Label(root, text='Add Citizenship ID Number/Institution ID ', bd=5,
                                            bg="light pink",
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
                        lbl_Residence = Label(main_frame, text='Residence', font=('arial', 15, 'bold'), width=8,
                                              bg='#F08080')
                        lbl_Residence.grid(row=2, column=0, padx=10, pady=10)
                        self.ent_Residence = Entry(main_frame)
                        self.ent_Residence.grid(row=2, column=1, padx=10, pady=10)
                        lbl_DOB = Label(main_frame, text='DOB', font=('arial', 15, 'bold'), width=8, bg='#F08080')
                        lbl_DOB.grid(row=3, column=0, padx=10, pady=10)
                        self.ent_DOB = Entry(main_frame)
                        self.ent_DOB.grid(row=3, column=1, padx=10, pady=10)
                        lbl_Gender = Label(main_frame, text='Gender', font=('arial', 15, 'bold'), width=8, bg='#F08080')
                        lbl_Gender.grid(row=4, column=0, padx=10, pady=10)
                        self.combo_Gender = ttk.Combobox(main_frame, font=('arial', 15, 'bold'), width=12,
                                                         state='readonly')
                        self.combo_Gender['values'] = ('Male', 'Female', 'Others')
                        self.combo_Gender.grid(row=4, column=1, padx=20)
                        lbl_Contact = Label(main_frame, text='Contact', font=('arial', 15, 'bold'), width=8,
                                            bg='#F08080')
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
                        stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Residence.get(),
                                          self.ent_DOB.get(),
                                          self.combo_Gender.get(), self.ent_Contact.get(), self.ent_Email.get())
                        query = 'update computer set Name=%s,Residence=%s,DOB=%s,Gender=%s,Contact=%s,Email=%s where ID=%s;'
                        values = (stu_ref.get_Name(), stu_ref.get_Residence(), stu_ref.get_DOB(), stu_ref.get_Gender(),
                                  stu_ref.get_Contact(), stu_ref.get_Email(), int(stu_ref.get_ID()))
                        self.dbconnect.update(query, values)
                        messagebox.showinfo("Success", " Your data updated Successfully")

                    def delete(self):
                        stu_ref = Student(self.ent_ID.get(), self.ent_Name.get(), self.ent_Residence.get(),
                                          self.ent_DOB.get(),
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

    window = Toplevel()
    Khatiwoda(window)
    canvas = Canvas(window, width=1565, height=1000)
    lbl_heading = Label(window,
                        text=' 𝓡𝓔𝓖𝓘𝓢𝓣𝓔𝓡  𝓕𝓞𝓡  𝓐  𝓑𝓔𝓣𝓣𝓔𝓡  𝓣𝓞𝓜𝓞𝓡𝓡𝓞𝓦',
                        bd=5, bg="#528B8B", font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='(っ◔◡◔)っ ♥ JOIN US ♥', bd=5,
                        bg="#68838B", font=('arial', 20, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    btn_frame = Frame(window, width=1565, bd=5, bg="white", height=50)
    btn_frame.place(y=200, x=500)
    btn_Registration = Button(btn_frame, text='Registration', font=('arial', 20, 'bold'), width=20, bg="white",
                              command=Sundar)
    btn_Registration.pack(side=TOP)
    btn_signup = Button(btn_frame, text='Records', font=('arial', 20, 'bold'), width=20, bg="white", command=saumya)
    btn_signup.pack(side=TOP, pady=5)
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\USER\\Desktop\\4.JPG"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()
def Service():
    class Service():
        def __init__(self,image):
            self.wn=window
            self.wn.title("Information Page")
            self.wn.geometry("1500x700")
            self.wn.canvas=Canvas (self.wn,width=5000,height=1000)
    window = Toplevel()
    canvas = Canvas(window, width=5000, height=1000)
    lbl_heading = Label(window, text='𝓐𝓑𝓞𝓤𝓣 𝓤𝓢', bd=5,
                        bg="light blue",
                        font=('arial', 35, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='🎀  𝐿💙𝒱𝐸 𝒜𝒩𝐼𝑀𝒜𝐿𝒮  🎀 🐯👺', bd=5, bg='#7FFF00',
                        font=('arial', 24, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\sh.jpg"))

    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()

    window.mainloop()

def Contact():
    class Contact():
        def __init__(self,image):
            self.wn=window
            self.wn.title("Contact")
            self.wn.geometry("1500x700")
            self.wn.canvas=Canvas (self.wn,width=5000,height=1000)

    window = Toplevel()
    canvas = Canvas(window, width=5000, height=1000)
    lbl_heading = Label(window, text='𝓞𝓤𝓡 𝓒𝓞𝓝𝓣𝓐𝓒𝓣', bd=5, bg="light blue",
                        font=('arial', 35, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)

    image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\7.jpg"))

    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()

    window.mainloop()

    window = Toplevel()
    Shyam(window)
    canvas = Canvas(window, width=1565, height=1000)
    lbl_heading = Label(window, text='⚛  🎀  𝐵𝐸 𝒯𝐻𝐸 𝒱💞𝐼𝒞𝐸 𝐹💙𝑅 𝒯𝐻𝐸 𝒱🌺𝐼𝒞𝐸𝐿𝐸𝒮𝒮  🎀 ', bd=5,
                        bg="pink",
                        font=('arial', 30, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    lbl_heading = Label(window, text='𝒦𝒶𝓉𝒽𝓂𝒶𝓃𝒹𝓊,𝒩𝑒𝓅𝒶𝓁 ', bd=5, bg='sky blue', font=('arial', 24, 'bold'))
    lbl_heading.pack(side=TOP, fill=X)
    btn_frame = Frame(window, width=1565, bd=5, bg="pink", height=50)
    btn_frame.place(y=200,x=500)
    btn_registration = Button(btn_frame, text='Registration', font=('arial', 20, 'bold'), width=20, bg="pink", command=Sundar)
    btn_registration.pack(side=TOP)
    btn_ContactUs = Button(btn_frame, text='Records', font=('arial', 20, 'bold'), width=20, bg="pink",command=records)
    btn_ContactUs.pack(side=TOP,pady=5)
    image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\4.jpg"))
    canvas.create_image(0, 0, anchor=NW, image=image)
    canvas.pack()
    window.mainloop()


window = Tk()
Shyam(window)
canvas = Canvas(window, width=1565, height=1000)
lbl_heading = Label(window, text='⚛  🎀  𝐵𝐸 𝒯𝐻𝐸 𝒱💞𝐼𝒞𝐸 𝐹💙𝑅 𝒯𝐻𝐸 𝒱🌺𝐼𝒞𝐸𝐿𝐸𝒮𝒮  🎀 ', bd=5, bg="pink",
                    font=('arial', 30, 'bold'))
lbl_heading.pack(side=TOP, fill=X)
lbl_heading = Label(window, text='𝒦𝒶𝓉𝒽𝓂𝒶𝓃𝒹𝓊,𝒩𝑒𝓅𝒶𝓁 ', bd=5, bg='sky blue', font=('arial', 24, 'bold'))
lbl_heading.pack(side=TOP, fill=X)
btn_frame = Frame(window, width=1565, bd=5, bg="pink", height=50)
btn_frame.place(y=100)
btn_home = Button(btn_frame, text='𝓟𝓡𝓞𝓕𝓘𝓛𝓔', font=('arial', 20, 'bold'), width=20, bg="pink",command=Home)
btn_home.pack(side=LEFT)
btn_signup = Button(btn_frame, text='𝓡𝓮𝓰𝓲𝓼𝓽𝓻𝓪𝓽𝓲𝓸𝓷 𝓟𝓪𝓰𝓮', font=('arial', 20, 'bold'), width=20, bg="pink",command=Registration)
btn_signup.pack(side=LEFT)
btn_services = Button(btn_frame, text='𝓐𝓑𝓞𝓤𝓣 𝓤𝓢', font=('arial', 20, 'bold'), width=20, bg="pink",command=Service)
btn_services.pack(side=RIGHT)
btn_ContactUs = Button(btn_frame, text='𝓞𝓤𝓡 𝓒𝓞𝓝𝓣𝓐𝓒𝓣', font=('arial', 20, 'bold'), width=20, bg="pink",command=Contact)
btn_ContactUs.pack(side=RIGHT)
image = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\damii.jpg"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
window.mainloop()