from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
	host="localhost", 
    user="root", 
    password="chiucd123", 
    database="mydatabase")

mycursor = db.cursor()

login = Tk()
login.title("Employee Management System") 
login.geometry("1920x1080+0+0")
login.config(bg="#EADDCA")
login.state("zoomed")


entries_frame = Frame(login, bg="#EADDCA", highlightthickness=7, highlightbackground='black')
entries_frame.pack(side=TOP, fill=X)
title = Label(entries_frame, text="Employee Management System", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
title.grid(row= 0, column=0, padx=10, pady=20, sticky='nsew')

entries_frame.grid(row=0, column=0, sticky="NESW")
entries_frame.grid_columnconfigure(0, weight=1)
login.grid_columnconfigure(0, weight=1)

def clear():
    username1.set("")
    password1.set("")
    print()

def login1():
    user = username1.get()
    pswd = password1.get()
    
    if user == username and pswd == password:
        clear()

        root = Toplevel(login)
        root.grab_set()
        root.title("Employee Management System")
        root.geometry("1920x1080+0+0")
        root.config(bg="#EADDCA")
        root.state("zoomed")

        entries_frame = Frame(root, bg="#EADDCA")
        entries_frame.pack(side=TOP, fill=X)
        title = Label(entries_frame, text="Employee Management System", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
        title.grid(column=0, padx=10, pady=20, sticky='nsew')

        entries_frame.grid(row=0, column=0, sticky="NESW")
        entries_frame.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        # Function Declarations and Definitions

        # Add Employee Page

        def add_employee():
            win = Toplevel(root)
            win.grab_set()
            win.title("Add Employee")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def addNew():

                eid = txtEid.get()
                fname = txtfName.get()
                mname = txtmName.get()
                lname = txtlName.get()
                dob = txtDOB.get()
                age = txtAge.get()
                gender = comboGender.get()
                doj = txtDOJ.get()
                department = txtDepartment.get()
                designation = txtDesignation.get()
                salary = txtSalary.get()
                commission = txtCommission.get()
                email  = txtEmail.get()
                contact = txtContact.get()

                if fname == "" or lname == "" or mname == "" or age == "" or eid == "" or doj == "" or email == "" or gender == "" or contact == "" or dob == "" or designation == "" or department == "" or salary == "" or commission == "":
                    messagebox.showerror("Erorr in Input", "Please Fill All the Details")
                                
                if (check_employee(eid) == True):
                    messagebox.showinfo("Error", "Record already exists.")
                else:
                    sql = 'insert into emp6 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                    data = (eid, fname,  mname, lname, dob, age, gender, doj, department, designation, salary, commission, email, contact)

                    c = db.cursor()
                    c.execute(sql,data)
                    db.commit()

                    messagebox.showinfo("Success", "Record Inserted.")
                    clearAll()


            def clearAll():
                eid.set("")
                fname.set("")
                mname.set("")
                lname.set("")
                dob.set("")
                age.set("")
                gender.set("")
                doj.set("")
                department.set("")
                designation.set("")
                salary.set("")
                commission.set("")
                email.set("")
                contact.set("")
                
            def check_employee(empid):
                sql = 'select * from empd where id=%s'
                
                c = db.cursor(buffered=True)
                data = (empid,)
                
                c.execute(sql, data)
                
                r = c.rowcount
                if r == 1:
                    return True
                else:
                    return False

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()
            age = StringVar()
            doj = StringVar()
            dob = StringVar()
            gender = StringVar()
            email = StringVar()
            contact = StringVar()
            designation = StringVar()
            department = StringVar()
            salary = StringVar()
            commission = StringVar()

            # Entries Frame
            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Add Employee", font=("Calibri", 24, "bold"), bg="#EADDCA", fg="black")
            title.grid(row=0, columnspan=2, padx=10, pady=20, sticky="w")
            
            title2 = Label(entries_frame, text="Personal Information", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title2.grid(row=1, columnspan=2, padx=10, pady=20, sticky="w")

            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=2, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=2, column=1, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=4, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=4, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=4, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=4, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=4, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=4, column=5, padx=10, pady=10, sticky="w")

            lblDOB = Label(entries_frame, text="Date of Birth", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDOB.grid(row=6, column=0, padx=10, pady=10, sticky="w")
            txtDOB = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
            txtDOB.grid(row=6, column=1, padx=10, pady=10, sticky="w")

            lblAge = Label(entries_frame, text="Age", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblAge.grid(row=6, column=2, padx=10, pady=10, sticky="w")
            txtAge = Entry(entries_frame, textvariable=age, font=("Calibri", 16), width=30)
            txtAge.grid(row=6, column=3, padx=10, pady=10, sticky="w")

            lblGender = Label(entries_frame, text="Gender", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblGender.grid(row=6, column=4, padx=10, pady=10, sticky="w")
            comboGender = ttk.Combobox(entries_frame, font=("Calibri", 16), width=28, textvariable=gender, state="readonly")
            comboGender['values'] = ("Male", "Female")
            comboGender.grid(row=6, column=5, padx=10, sticky="w")
                    
            title3 = Label(entries_frame, text="Current Posting", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title3.grid(row=8, columnspan=2, padx=10, pady=20, sticky="w")

            lblDOJ = Label(entries_frame, text="Date of Joining", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDOJ.grid(row=10, column=0, padx=10, pady=10, sticky="w")
            txtDOJ = Entry(entries_frame, textvariable=doj, font=("Calibri", 16), width=30)
            txtDOJ.grid(row=10, column=1, padx=10, pady=10, sticky="w")

            lblDepartment = Label(entries_frame, text="Department", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDepartment.grid(row=10, column=2, padx=10, pady=10, sticky="w")
            txtDepartment = Entry(entries_frame, textvariable=department, font=("Calibri", 16), width=30)
            txtDepartment.grid(row=10, column=3, padx=10, pady=10, sticky="w")

            lblDesignation = Label(entries_frame, text="Designation", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDesignation.grid(row=10, column=4, padx=10, pady=10, sticky="w")
            txtDesignation = Entry(entries_frame, textvariable=designation, font=("Calibri", 16), width=30)
            txtDesignation.grid(row=10, column=5, padx=10, pady=10, sticky="w")
            
            title4 = Label(entries_frame, text="Salary Details", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title4.grid(row=12, columnspan=2, padx=10, pady=20, sticky="w")

            lblSalary = Label(entries_frame, text="Salary", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblSalary.grid(row=14, column=0, padx=10, pady=10, sticky="w")
            txtSalary = Entry(entries_frame, textvariable=salary, font=("Calibri", 16), width=30)
            txtSalary.grid(row=14, column=1, padx=10, pady=10, sticky="w")

            lblCommission = Label(entries_frame, text="Commision", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblCommission.grid(row=14, column=2, padx=10, pady=10, sticky="w")
            txtCommission = Entry(entries_frame, textvariable=commission, font=("Calibri", 16), width=30)
            txtCommission.grid(row=14, column=3, padx=10, pady=10, sticky="w")

            title5 = Label(entries_frame, text="Contact Details", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title5.grid(row=16, columnspan=2, padx=10, pady=20, sticky="w")

            lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblContact.grid(row=18, column=0, padx=10, pady=10, sticky="w")
            txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
            txtContact.grid(row=18, column=1, padx=10, sticky="w")

            lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEmail.grid(row=18, column=2, padx=10, pady=10, sticky="w")
            txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
            txtEmail.grid(row=18, column=3, padx=10, sticky="w")


            btnAdd = Button(entries_frame, command=addNew, text="Add Employee", width=15, font=("Calibri", 16, "bold"), fg="white",
                        bg="#28282B", bd=0).grid(row=20, column=3, padx=10, pady=20, sticky="w")

            btnClear = Button(entries_frame, command=clearAll, text="Clear", width=15, font=("Calibri", 16, "bold"), fg="white",
                        bg="#28282B", bd=0).grid(row=20, column=2, padx=10, pady=20, sticky="w")
            
            win.mainloop()

        # Add Employee Page Ends


        # Update Employee Page Starts

        def update_employee():
            win = Toplevel(root)
            win.grab_set()
            win.title("Update Employee Details")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def update():
                
                eid = txtEid.get()
                fname = txtfName.get()
                mname = txtmName.get()
                lname = txtlName.get()
                dob = txtDOB.get()
                department = txtDepartment.get()
                designation = txtDesignation.get()
                salary = txtSalary.get()
                email  = txtEmail.get()
                contact = txtContact.get()


                s1 = "UPDATE emp6 SET fname = %s where eid = %s"
                dt1 = (fname, mname, lname, eid)

                s2 = "UPDATE emp6 SET mname = %s where eid = %s"
                dt2 = (mname, eid)

                s3 = "UPDATE emp6 SET lname = %s where eid = %s"
                dt3 = (lname, eid)

                s4 = 'UPDATE emp6 SET dob = %s where eid = %s'
                dt4 = (dob, eid)

                s5 = "UPDATE emp6 SET department = %s where eid = %s"
                dt5 = (department, eid)

                s6 = "UPDATE emp6 SET designation = %s where eid = %s"
                dt6 = (designation, eid)

                s7 = "UPDATE emp6 SET salary = %s where eid = %s"
                dt7 = (salary, eid)

                s8 = "UPDATE emp6 SET contact = %s, email = %s where eid = %s"
                dt8 = (contact, email, eid)

                s9 = "UPDATE emp6 SET contact = %s, email = %s where eid = %s"
                dt9 = (contact, email, eid)
                
                c=db.cursor()

                if fname != "":
                    c.execute(s1,dt1)

                if mname != "":
                    c.execute(s2,dt2)

                if lname != "":
                    c.execute(s3,dt3)
                
                if dob != "":
                    c.execute(s4,dt4)
                
                if department != "":
                    c.execute(s5,dt5) 
                
                if designation != "":
                    c.execute(s6,dt6) 

                if salary != "":
                    c.execute(s7,dt7)

                if contact != "":
                    c.execute(s8,dt8)
                
                if email != "":
                    c.execute(s9,dt9)              

                db.commit()

                messagebox.showinfo("Success", "Record Updated")
                clearAll()
            
            def clearAll():
                eid.set("")
                fname.set("")
                mname.set("")
                lname.set("")
                dob.set("")
                age.set("")
                gender.set("")
                doj.set("")
                department.set("")
                designation.set("")
                salary.set("")
                commission.set("")
                email.set("")
                contact.set("")

            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Update Employee Details", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
            title.grid(column=0, columnspan=2, padx=10, pady=10, sticky='nsew')

            entries_frame.grid(row=0, column=0, sticky="nsew")
            entries_frame.grid_rowconfigure(0, weight=1)
            entries_frame.grid_columnconfigure(0, weight=1)
            win.grid_rowconfigure(0, weight=1)
            win.grid_columnconfigure(0, weight=1)

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()
            age = StringVar()
            doj = StringVar()
            dob = StringVar()
            gender = StringVar()
            email = StringVar()
            contact = StringVar()
            designation = StringVar()
            department = StringVar()
            salary = StringVar()
            commission = StringVar()
                       
            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=1, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=1, column=1, padx=10, pady=10, sticky="w")

            title1 = Label(entries_frame, text="Update Name", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title1.grid(row=3, columnspan=2, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=5, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=5, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=5, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=5, column=5, padx=10, pady=10, sticky="w")

            title2 = Label(entries_frame, text="Update Date of Birth", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title2.grid(row=7, columnspan=2, padx=10, pady=10, sticky="w")

            lblDOB = Label(entries_frame, text="Date of Birth", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDOB.grid(row=9, column=0, padx=10, pady=10, sticky="w")
            txtDOB = Entry(entries_frame, textvariable=dob, font=("Calibri", 16), width=30)
            txtDOB.grid(row=9, column=1, padx=10, pady=10, sticky="w")

            title3 = Label(entries_frame, text="Update Department and Designation", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title3.grid(row=11, columnspan=2, padx=10, pady=10, sticky="w")

            lblDepartment = Label(entries_frame, text="Department", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDepartment.grid(row=13, column=0, padx=10, pady=10, sticky="w")
            txtDepartment = Entry(entries_frame, textvariable=department, font=("Calibri", 16), width=30)
            txtDepartment.grid(row=13, column=1, padx=10, pady=10, sticky="w")

            lblDesignation = Label(entries_frame, text="Designation", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDesignation.grid(row=13, column=2, padx=10, pady=10, sticky="w")
            txtDesignation = Entry(entries_frame, textvariable=designation, font=("Calibri", 16), width=30)
            txtDesignation.grid(row=13, column=3, padx=10, pady=10, sticky="w")
            
            title5 = Label(entries_frame, text="Update Salary Details", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title5.grid(row=15, columnspan=2, padx=10, pady=10, sticky="w")

            lblSalary = Label(entries_frame, text="Salary", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblSalary.grid(row=17, column=0, padx=10, pady=10, sticky="w")
            txtSalary = Entry(entries_frame, textvariable=salary, font=("Calibri", 16), width=30)
            txtSalary.grid(row=17, column=1, padx=10, pady=10, sticky="w")

            title6 = Label(entries_frame, text="Update Contact Details", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title6.grid(row=19, columnspan=2, padx=10, pady=10, sticky="w")

            lblContact = Label(entries_frame, text="Contact No", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblContact.grid(row=21, column=0, padx=10, pady=10, sticky="w")
            txtContact = Entry(entries_frame, textvariable=contact, font=("Calibri", 16), width=30)
            txtContact.grid(row=21, column=1, padx=10, sticky="w")

            lblEmail = Label(entries_frame, text="Email", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEmail.grid(row=21, column=2, padx=10, pady=10, sticky="w")
            txtEmail = Entry(entries_frame, textvariable=email, font=("Calibri", 16), width=30)
            txtEmail.grid(row=21, column=3, padx=10, sticky="w")

            btn_frame = Frame(entries_frame, bg="#EADDCA")
            btn_frame.grid(row=23, column=0, padx=10, pady=10)

            btnEdit = Button(btn_frame, command=update, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                            fg="white", bg="#28282B", bd=0).grid(row=23, column=0, columnspan=2, pady=10, padx=10)

            win.mainloop()

        # Update Employee Page Ends


        # Delete Employee Details Page Starts

        def delete_employee():
            win = Toplevel(root)
            win.grab_set()
            win.title("Delete Employee")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def delete():
                eid = txtEid.get()
                fname = txtfName.get()
                mname = txtmName.get()
                lname = txtlName.get()
                        
                sql = 'DELETE FROM emp6 WHERE eid = %s and fname = %s'
                d = (eid, fname)
                        
                c=db.cursor()
                c.execute(sql,d)
                db.commit()

                messagebox.showinfo("Success", "Record Deleted")
                clearAll()

            def clearAll():
                eid.set("")
                fname.set("")
                mname.set("")
                lname.set("")
                dob.set("")
                age.set("")
                gender.set("")
                doj.set("")
                department.set("")
                designation.set("")
                salary.set("")
                commission.set("")
                email.set("")
                contact.set("")

            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Delete Employee Details", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
            title.grid(column=0, padx=10, pady=10, sticky='nsew')

            entries_frame.grid(row=0, column=0, sticky="nsew")
            entries_frame.grid_columnconfigure(0, weight=1)
            win.grid_columnconfigure(0, weight=1)

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()
            age = StringVar()
            doj = StringVar()
            dob = StringVar()
            gender = StringVar()
            email = StringVar()
            contact = StringVar()
            designation = StringVar()
            department = StringVar()
            salary = StringVar()
            commission = StringVar()
            
            title = Label(entries_frame, text="Delete Employee Details", font=("Calibri", 20, "bold"), bg="#EADDCA", fg="black")
            title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
            
            title1 = Label(entries_frame, text="Enter Employee ID and Name of the Employee: ", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title1.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=3, column=1, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=5, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=5, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=5, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=5, column=5, padx=10, pady=10, sticky="w")

            btn_frame = Frame(entries_frame, bg="#EADDCA")
            btn_frame.grid(row=23, column=0, padx=10, pady=10)

            btnEdit = Button(btn_frame, command=delete, text="Delete Employee", width=15, font=("Calibri", 16, "bold"),
                            fg="white", bg="#28282B", bd=0).grid(row=23, column=3, columnspan=2, pady=10, padx=10)

            win.mainloop()

        # Delete Employee Details Page Ends


        # Promote Employee Page Starts

        def promote_employee():
            win = Toplevel(root)
            win.grab_set()
            win.title("Promote Employee")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def promote():
                eid = txtEid.get()
                fname = txtfName.get()
                mname = txtmName.get()
                lname = txtlName.get()
                department = txtDepartment.get()
                designation = txtDesignation.get()
                salary = txtSalary.get()
                        
                sql = 'UPDATE emp6 SET designation = %s, department = %s , salary = %d where eid = %s'
                d = (designation, department, salary, eid)
                
                c=db.cursor()
                c.execute(sql,d)
                db.commit()

                messagebox.showinfo("Success", "Record Updated")
                clearAll()

            def clearAll():
                eid.set("")
                fname.set("")
                mname.set("")
                lname.set("")
                dob.set("")
                age.set("")
                gender.set("")
                doj.set("")
                department.set("")
                designation.set("")
                salary.set("")
                commission.set("")
                email.set("")
                contact.set("")

            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Promote Employee", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
            title.grid(column=0, padx=10, pady=10, sticky='nsew')

            entries_frame.grid(row=0, column=0, sticky="nsew")
            entries_frame.grid_columnconfigure(0, weight=1)
            win.grid_columnconfigure(0, weight=1)

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()
            age = StringVar()
            doj = StringVar()
            dob = StringVar()
            gender = StringVar()
            email = StringVar()
            contact = StringVar()
            designation = StringVar()
            department = StringVar()
            salary = StringVar()
            commission = StringVar()
        
            title = Label(entries_frame, text="Enter Employee Details to Promote Employee", font=("Calibri", 20, "bold"), bg="#EADDCA", fg="black")
            title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")

            title1 = Label(entries_frame, text="Enter Employee ID and Name of the Employee: ", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title1.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=3, column=1, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=5, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=5, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=5, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=5, column=5, padx=10, pady=10, sticky="w")

            title3 = Label(entries_frame, text="Enter new Department and Designation", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title3.grid(row=7, columnspan=2, padx=10, pady=10, sticky="w")

            lblDepartment = Label(entries_frame, text="Department", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDepartment.grid(row=9, column=0, padx=10, pady=10, sticky="w")
            txtDepartment = Entry(entries_frame, textvariable=department, font=("Calibri", 16), width=30)
            txtDepartment.grid(row=9, column=1, padx=10, pady=10, sticky="w")

            lblDesignation = Label(entries_frame, text="Designation", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblDesignation.grid(row=9, column=2, padx=10, pady=10, sticky="w")
            txtDesignation = Entry(entries_frame, textvariable=designation, font=("Calibri", 16), width=30)
            txtDesignation.grid(row=9, column=3, padx=10, pady=10, sticky="w")
            
            title5 = Label(entries_frame, text="Update Salary Details", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title5.grid(row=11, columnspan=2, padx=10, pady=10, sticky="w")

            lblSalary = Label(entries_frame, text="Salary", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblSalary.grid(row=13, column=0, padx=10, pady=10, sticky="w")
            txtSalary = Entry(entries_frame, textvariable=salary, font=("Calibri", 16), width=30)
            txtSalary.grid(row=13, column=1, padx=10, pady=10, sticky="w")

            btn_frame = Frame(entries_frame, bg="#EADDCA")
            btn_frame.grid(row=15, column=0, padx=10, pady=10)

            btnEdit = Button(btn_frame, command=promote, text="Promote Employee", width=15, font=("Calibri", 16, "bold"),
                            fg="white", bg="#28282B", bd=0).grid(row=15, column=3, columnspan=2, pady=10, padx=10)

            win.mainloop()

        # Promote Employee Page Ends


        # Search Employee Page Starts

        def searchEmployee():
            win = Toplevel(root)
            win.grab_set()
            win.title("Search Employee")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def search():
                eid = txtEid.get()
                fname = txtfName.get()
                mname = txtmName.get()
                lname = txtlName.get()
                        
                sql = 'SELECT * FROM emp6 WHERE eid = %s and fname = %s'
                d = (eid, fname)
                
                c=db.cursor()
                c.execute(sql,d)

                myresult = c.fetchall()
                
                flag = False

                for x in myresult:
                    flag = True

                db.commit()

                if flag:
                    messagebox.showinfo("Success", "Employee exists.")
                else:
                    messagebox.showinfo("Success", "Employee does not exixts.")
                
                clearAll()

            def clearAll():
                eid.set("")
                fname.set("")
                mname.set("")
                lname.set("")

            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Search Employee", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
            title.grid(column=0, padx=10, pady=10, sticky='nsew')

            entries_frame.grid(row=0, column=0, sticky="nsew")
            entries_frame.grid_columnconfigure(0, weight=1)
            win.grid_columnconfigure(0, weight=1)

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()    

            title = Label(entries_frame, text="Enter Employee Details to Search Employee", font=("Calibri", 20, "bold"), bg="#EADDCA", fg="black")
            title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
            
            title1 = Label(entries_frame, text="Enter Employee ID and Name of the Employee: ", font=("Calibri", 18, "bold"), bg="#EADDCA", fg="black")
            title1.grid(row=1, columnspan=2, padx=10, pady=10, sticky="w")

            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=3, column=1, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=5, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=5, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=5, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=5, column=5, padx=10, pady=10, sticky="w") 


            btn_frame = Frame(entries_frame, bg="#EADDCA")
            btn_frame.grid(row=7, column=0, padx=10, pady=10)

            btnEdit = Button(btn_frame, command=search, text="Search Employee", width=15, font=("Calibri", 16, "bold"),
                            fg="white", bg="#28282B", bd=0).grid(row=7, column=3, columnspan=2, pady=10, padx=10)

            win.mainloop()

        # Search Employee Page Ends


        # Display Details Page Starts

        def displayDetails():
            win = Toplevel(root)
            win.grab_set()
            win.title("Employee Details")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            def display():
                win2 = Toplevel(win)
                win2.grab_set()
                win2.geometry("1920x1080+0+0")
                win2.config(bg="#EADDCA")
                win2.state("zoomed")

                eid = txtEid.get()
                fname = txtfName.get()

                c = db.cursor()
                i=0
                c.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = Database() AND TABLE_NAME = 'emp6'")

                a=0

                for k in c:
                    e = Entry(win2, width=17, fg='black', highlightbackground='black', highlightthickness=2) 
                    e.grid(row=i, column=a) 
                    if a==0:
                        e.insert(END, "eid")
                    elif a==1:
                        e.insert(END, "First Name")
                    elif a==2:
                        e.insert(END, "Middle Name")
                    elif a==3:
                        e.insert(END, "Last Name")
                    elif a==4:
                        e.insert(END, "DOB")
                    elif a==5:
                        e.insert(END, "Age")
                    elif a==6:
                        e.insert(END, "Gender")
                    elif a==7:
                        e.insert(END, "DOJ")
                    elif a==8:
                        e.insert(END, "Department")
                    elif a==9:
                        e.insert(END, "Designation")
                    elif a==10:
                        e.insert(END, "Salary")
                    elif a==11:
                        e.insert(END, "Commission")
                    elif a==12:
                        e.insert(END, "Email")
                    elif a==13:
                        e.insert(END, "Mobile no.")
                    a+=1
                    e.config(state="disabled")

                cursor = db.cursor()
                sql_select_query = """select * from emp6 where eid = %s"""
                
                cursor.execute(sql_select_query, (eid,))
                
                record = cursor.fetchall()

                i=1
                for k in record: 
                    for j in range(len(k)):
                        e = Entry(win2, width=17, fg='black') 
                        e.grid(row=i, column=j) 
                        e.insert(END, k[j])
                        e.config(state="disabled")
                        
                    i=i+1

            

                win2.mainloop()

            entries_frame = Frame(win, bg="#EADDCA")
            entries_frame.pack(side=TOP, fill=X)
            title = Label(entries_frame, text="Display Employee Details", font=("Calibri", 28, "bold"), bg="#EADDCA", fg="black")
            title.grid(column=0, padx=10, pady=10, sticky='nsew')

            entries_frame.grid(row=0, column=0, sticky="nsew")
            entries_frame.grid_columnconfigure(0, weight=1)
            win.grid_columnconfigure(0, weight=1)

            eid = StringVar()
            fname = StringVar()
            mname = StringVar()
            lname = StringVar()    

            title = Label(entries_frame, text="Enter Employee ID and Name", font=("Calibri", 20, "bold"), bg="#EADDCA", fg="black")
            title.grid(row=0, columnspan=2, padx=10, pady=10, sticky="w")
            
            lblEid = Label(entries_frame, text="Employee ID", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblEid.grid(row=3, column=0, padx=10, pady=10, sticky="w")
            txtEid = Entry(entries_frame, textvariable=eid, font=("Calibri", 16), width=30)
            txtEid.grid(row=3, column=1, padx=10, pady=10, sticky="w")

            lblfName = Label(entries_frame, text="First Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblfName.grid(row=5, column=0, padx=10, pady=10, sticky="w")
            txtfName = Entry(entries_frame, textvariable=fname, font=("Calibri", 16), width=30)
            txtfName.grid(row=5, column=1, padx=10, pady=10, sticky="w")

            lblmName = Label(entries_frame, text="Middle Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lblmName.grid(row=5, column=2, padx=10, pady=10, sticky="w")
            txtmName = Entry(entries_frame, textvariable=mname, font=("Calibri", 16), width=30)
            txtmName.grid(row=5, column=3, padx=10, pady=10, sticky="w")

            lbllName = Label(entries_frame, text="Last Name", font=("Calibri", 16), bg="#EADDCA", fg="black")
            lbllName.grid(row=5, column=4, padx=10, pady=10, sticky="w")
            txtlName = Entry(entries_frame, textvariable=lname, font=("Calibri", 16), width=30)
            txtlName.grid(row=5, column=5, padx=10, pady=10, sticky="w") 


            btn_frame = Frame(entries_frame, bg="#EADDCA")
            btn_frame.grid(row=7, column=0, padx=10, pady=10)

            btnEdit = Button(btn_frame, command=display, text="Display Details", width=15, font=("Calibri", 16, "bold"),
                            fg="white", bg="#28282B", bd=0).grid(row=7, column=3, columnspan=2, pady=10, padx=10)

            win.mainloop()

        # Display Details Page Ends


        # Display All Records Page Starts

        def viewAll():
            win = Toplevel(root)
            win.grab_set()
            win.title("All Records")
            win.geometry("1920x1080+0+0")
            win.config(bg="#EADDCA")
            win.state("zoomed")

            c = db.cursor()
            i=0
            c.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = Database() AND TABLE_NAME = 'emp6'")

            a=0

            for k in c:
                    e = Entry(win, width=17, fg='black', highlightbackground='black', highlightthickness=2) 
                    e.grid(row=i, column=a) 
                    if a==0:
                        e.insert(END, "eid")
                    elif a==1:
                        e.insert(END, "First Name")
                    elif a==2:
                        e.insert(END, "Middle Name")
                    elif a==3:
                        e.insert(END, "Last Name")
                    elif a==4:
                        e.insert(END, "DOB")
                    elif a==5:
                        e.insert(END, "Age")
                    elif a==6:
                        e.insert(END, "Gender")
                    elif a==7:
                        e.insert(END, "DOJ")
                    elif a==8:
                        e.insert(END, "Department")
                    elif a==9:
                        e.insert(END, "Designation")
                    elif a==10:
                        e.insert(END, "Salary")
                    elif a==11:
                        e.insert(END, "Commission")
                    elif a==12:
                        e.insert(END, "Email")
                    elif a==13:
                        e.insert(END, "Mobile no.")
                    a+=1
                    e.config(state="disabled")
            
            c.execute("SELECT * FROM emp6")
            
            i=1 
            for k in c: 
                for j in range(len(k)):
                    e = Entry(win, width=17, fg='black') 
                    e.grid(row=i, column=j) 
                    e.insert(END, k[j])
                    e.config(state="disabled")
                i=i+1
            win.mainloop()

        # Display All Records Page Ends


        # Homepage Buttons Layout  

        btn_frame = Frame(entries_frame, bg="#EADDCA")
        btn_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        btn_frame.grid_rowconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(0, weight=1)
        btnAdd = Button(btn_frame, command=add_employee, text="Add Employee ", width=25, font=("Calibri", 16, "bold"), fg="white",
                        bg="#28282B", bd=0).grid(row=0, column=0, pady=10, padx=10)

        btnEdit = Button(btn_frame, command=update_employee, text="Update Employee Details", width=25, font=("Calibri", 16, "bold"),
                        fg="white", bg="#28282B", bd=0).grid(row=1, column=0, pady=10, padx=10)

        btnDelete = Button(btn_frame, command=delete_employee, text="Delete Employee Details", width=25, font=("Calibri", 16, "bold"),
                        fg="white", bg="#28282B", bd=0).grid(row=2, column=0, pady=10, padx=10)

        btnClear = Button(btn_frame, command=promote_employee, text="Promote Employee", width=25, font=("Calibri", 16, "bold"), fg="white",
                        bg="#28282B", bd=0).grid(row=3, column=0, pady=10, padx=10)

        btnAdd = Button(btn_frame, command=searchEmployee, text="Search Employee", width=25, font=("Calibri", 16, "bold"), fg="white",
                        bg="#28282B", bd=0).grid(row=4, column=0, pady=10, padx=10)

        btnEdit = Button(btn_frame, command=displayDetails, text="Display Details", width=25, font=("Calibri", 16, "bold"),
                        fg="white", bg="#28282B", bd=0).grid(row=5, column=0, pady=10, padx=10)

        btnDelete = Button(btn_frame, command=viewAll, text="View All Records", width=25, font=("Calibri", 16, "bold"),
                        fg="white", bg="#28282B", bd=0).grid(row=6, column=0, pady=10, padx=10)

        # Homepage Buttons Layout Complete

        root.mainloop()
        
    else:
        messagebox.showinfo("Error", "Invalid Credentials.")
        clear()


username = "admin"
password = "password"

username1 = StringVar()
password1 = StringVar()

title = Label(entries_frame, text="Admin Login", font=("Calibri", 24, "bold"), bg="#EADDCA", fg="black")
title.grid(row=2, columnspan=2, padx=10, pady=20, sticky="nsew")

lblUserName = Label(entries_frame, text="Username", font=("Calibri", 16), bg="#EADDCA", fg="black")
lblUserName.grid(row=4, column=0, padx=10, pady=10, sticky="w")
txtUserName = Entry(entries_frame, textvariable=username1, font=("Calibri", 16), width=30)
txtUserName.grid(row=4, column=0, padx=10, pady=10, sticky="e")

lblPassword = Label(entries_frame, text="Password",  font=("Calibri", 16), bg="#EADDCA", fg="black")
lblPassword.grid(row=6, column=0, padx=10, pady=10, sticky="w")
txtPassword = Entry(entries_frame, textvariable=password1,  show ="*", font=("Calibri", 16), width=30)
txtPassword.grid(row=6, column=0, padx=10, pady=10, sticky="e")


btn_frame = Frame(entries_frame, bg="#EADDCA")
btn_frame.grid(row=8, column=0, padx=10, pady=10, sticky="nsew")
btn_frame.grid_rowconfigure(0, weight=1)
btn_frame.grid_columnconfigure(0, weight=1)

btnlogin = Button(btn_frame, command=login1, text="Login", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="#28282B", bd=0).grid(row=8, column=1, pady=10, padx=10)

btnclear = Button(btn_frame, command=clear, text="Clear", width=15, font=("Calibri", 16, "bold"),
                fg="white", bg="#28282B", bd=0).grid(row=8, column=0, pady=10, padx=10)

entries_frame.pack(expand=True)

login.mainloop()