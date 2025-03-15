from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        #=========variables==========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stu_id=StringVar()
       
        self.var_stu_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        # 1st image
        img = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face16.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)  
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd image 
        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face17.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl1 = Label(self.root, image=self.photoimg1)  
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # 3rd image 
        img2 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face18.webp")
        img2 = img2.resize((500, 130), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)  

        f_lbl2 = Label(self.root, image=self.photoimg2)  
        f_lbl2.place(x=1000, y=0, width=500, height=130)


        # bg img
        img3 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\bgg.png")
        img3 = img3.resize((1520, 750), Image.LANCZOS)  
        self.photoimg3 = ImageTk.PhotoImage(img3)  

        bg_img = Label(self.root, image=self.photoimg3)  
        bg_img.place(x=0, y=130, width=1520, height=750)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times to roman",34,"bold"),bg="White",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1500,height=620)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=600)

        img_left = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face19.jpg")
        img_left = img_left.resize((680, 130), Image.LANCZOS)  
        self.photoimg_left = ImageTk.PhotoImage(img_left) 

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)  
        f_lbl_left.place(x=0, y=0, width=680, height=130)

        #current course
        curernt_course_frame=LabelFrame(Left_frame,bd=2, bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        curernt_course_frame.place(x=0,y=135,width=675,height=150)
        
        #Department
        dep_label=Label(curernt_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(curernt_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","CSE","IT","AI&DS","ECE","ECC","EE","EEE","Mechanical","Civil","Mining","Petroleum","Production" )
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Course 
        course_label=Label(curernt_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(curernt_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"]=("Select Course","BE","ME","B.ARCH")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(curernt_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(curernt_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Semester
        semester_label=Label(curernt_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(curernt_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4","Semester-5","Semester-6","Semester-7","Semester-8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2, bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=0,y=290,width=675,height=285)

        #student ID
        studentId_label=Label(class_student_frame,text="StudentID:",font=("times new roman",12,"bold"),bg="white")
        studentId_label.grid(row=0,column=0,padx=10,sticky=W)

        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=20,font=("times new roman",12,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name 
        studentName_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=20,font=("times new roman",12,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",12,"bold"),state="readonly",width=18)
        div_combo["values"]=("Select Division","A","B","C","D","E","F","G","H")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Roll NO
        roll_no_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Select Gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone No
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name:",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Button
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=5,column=0)

        
        radionbtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=5,column=1)
        
        #Button Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=670,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=230,width=670,height=35)

        take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo Smaple",width=36,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame,text="Update Photo Smaple",width=36,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        update_photo_btn.grid(row=0,column=1)


        #right frame
        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=707,height=600)

        img_right = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face20.webp")
        img_right = img_right.resize((704, 130), Image.LANCZOS)  
        self.photoimg_right = ImageTk.PhotoImage(img_right) 

        f_lbl_right = Label(Right_frame,image=self.photoimg_right)  
        f_lbl_right.place(x=0, y=0, width=704, height=130)


        # ****** SEARCH SYSTEM *******

        search_frame=LabelFrame(Right_frame,bd=2, bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=695,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",13,"bold"),bg="green",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"]=("Select", "Roll_No","Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        search_entry = ttk.Entry(search_frame, width=15, font=("times new roman", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=15, pady=8, sticky=W)


        search_btn=Button(search_frame,text="Search",command=self.search_data,width=13,height=0,font=("times new roman",10,"bold"),bg="Blue",fg="white")
        search_btn.grid(row=0,column=3,padx=5)

        showAll_btn=Button(search_frame,text="Show All",width=13,height=0,font=("times new roman",10,"bold"),bg="Blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=5)

        #========Table Frame=======

        table_frame=Frame(Right_frame,bd=2, bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=695,height=365)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=115)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
       #========function decration=========
       
    def add_data(self):
        if (self.var_dep.get()=="Department" or self.var_stu_name.get()=="Name" or self.var_stu_id.get()=="StudentID" or self.var_address.get()=="Address" or self.var_course.get()=="Course" or self.var_year.get()=="Year" or self.var_semester.get()=="Semester" or self.var_roll.get()=="Roll" or self.var_div.get()=="Division" or self.var_gender.get()=="Gender" or self.var_dob.get()=="DOB"  or self.var_email.get()=="Email" or self.var_phone.get()=="Phone" or self.var_teacher.get()=="Teacher" or self.var_radio1.get()==""):
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
               conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_stu_id.get(),
                                                                                                            self.var_stu_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_teacher.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                                                   ))
                                                                                                            
                                                                                                            
                                                                                                                                       
               conn.commit()
               self.fetch_data()
               conn.close()
               messagebox.showinfo("Sucess","Student details has been added Sucessfully",parent=self.root)
            except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
          
          #=========fetch data===================
    def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            data=my_cursor.fetchall()

            if len(data)!=0:
                self.student_table.delete(* self.student_table.get_children())
                for i in data:
                    self.student_table.insert("",END,values=i)
                conn.commit()
            conn.close()   
                
         # ==get cursor=================
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        date=content["values"]

        self.var_dep.set(date[0]),
        self.var_course.set(date[1]),
        self.var_year.set(date[2]),
        self.var_semester.set(date[3]),
        self.var_stu_id.set(date[4]),
        self.var_stu_name.set(date[5]),
        self.var_div.set(date[6]),
        self.var_roll.set(date[7]),
        self.var_gender.set(date[8]),
        self.var_dob.set(date[9]),
        self.var_email.set(date[10]),
        self.var_phone.set(date[11]),
        self.var_address.set(date[12]),
        self.var_teacher.set(date[13]),
        self.var_radio1.set(date[14]),

         #upadte function
    def update_data(self):
        if self.var_dep.get()=="Department" or self.var_stu_name.get()=="Name" or self.var_stu_id.get()=="StudentID" or self.var_address.get()=="Address" or self.var_course.get()=="Course" or self.var_year.get()=="Year" or self.var_semester.get()=="Semester" or self.var_roll.get()=="Roll " or self.var_div.get()=="Division" or self.var_dob.get()=="DOB" or self.var_gender.get()=="Gender" or self.var_email.get()=="Email" or self.var_phone.get()=="Phone " or self.var_teacher.get()=="Teacher" or self.var_radio1.get()=="":         
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s, Roll=%s, Gender=%s, DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentID=%s",(
                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                            self.var_semester.get(),
                                                                                                                                                                                                                                            self.var_stu_name.get(),
                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                            self.var_stu_id.get()
                                                                                                                                                                                                                                         ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Sucess","Student details sucessfully update completed",parent=self.root)
                conn.commit()    
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)

              # delete function==========
    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                   conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
                   my_cursor=conn.cursor()
                   sql="delete from student where StudentID=%s"
                   val=(self.var_stu_id.get(),)
                   my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Sucessfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f" Due to:{str(es)}",parent=self.root)    

               #========reset===========
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_stu_id.set(" ")
        self.var_stu_name.set(" ")
        self.var_div.set("Select Division")
        self.var_roll.set(" ")
        self.var_gender.set("Selct Gender")
        self.var_dob.set(" ")
        self.var_email.set(" ")
        self.var_phone.set(" ")
        self.var_address.set(" ")
        self.var_teacher.set("")
        self.var_radio1.set(" ")

        #====generate data set or take photo samples=====

    def generate_dataset(self):
        if self.var_dep.get() == "Department" or self.var_stu_name.get() == "Name" or self.var_stu_id.get() == "StudentID" or self.var_address.get() == "Address" or self.var_course.get() == "Course" or self.var_year.get() == "Year" or self.var_semester.get() == "Semester" or self.var_roll.get() == "Roll " or self.var_div.get() == "Division" or self.var_gender.get() == "Gender" or self.var_dob.get() == "DOB" or self.var_email.get() == "Email" or self.var_phone.get() == "Phone " or self.var_teacher.get() == "Teacher" or self.var_radio1.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="Rkb@2005", database="face_recognised")
                    my_cursor = conn.cursor()
                    my_cursor.execute("Select * from student")
                    myresult = my_cursor.fetchall()
                    id = 0
                    for x in myresult:
                        id += 1
                    my_cursor.execute("update student set Department=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Division=%s, Roll=%s, Gender=%s,DOB=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where StudentID=%s", (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_stu_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_stu_id.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    conn.close()

                    #=========Load predefined data on face frontals from opencv=======
                    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def face_cropped(img):
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                        # scaling factor=1.3
                        # minimum neighbor=5

                        for (x, y, w, h) in faces:
                            face_cropped = img[y:y + h, x:x + w]
                            return face_cropped
                        return None

                    cap = cv2.VideoCapture(0)
                    img_id = 0
                    while True:
                        ret, my_frame = cap.read()
                        if not ret:
                            break
                        cropped_face = face_cropped(my_frame)
                        if cropped_face is not None:
                            img_id += 1
                            face = cv2.resize(cropped_face, (450, 450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                            cv2.imwrite(file_name_path, face)
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 10:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                    messagebox.showinfo("Result", "Generating data sets completed!!!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    def search_data(self):
        if self.search_combo.get() == "Select":
            messagebox.showerror("Error", "Select a search criteria", parent=self.root)
        elif self.search_entry.get() == "":
            messagebox.showerror("Error", "Please enter a value to search", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Rkb@2005", database="face_recognised")
                my_cursor = conn.cursor()
                if self.search_combo.get() == "Roll_No":
                    query = "select * from student where Roll=%s"
                    value = (self.search_entry.get(),)
                elif self.search_combo.get() == "Phone_No":
                    query = "select * from student where Phone=%s"
                    value = (self.search_entry.get(),)
                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for row in rows:
                        self.student_table.insert("", END, values=row)
                else:
                    messagebox.showerror("Error", "No record found", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                                                                                                                                                                                                                                           


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)  
    root.mainloop()