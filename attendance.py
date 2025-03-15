from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        #=========variables===========
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()



        # 1st image
        img = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face16.jpg")
        img = img.resize((800, 200), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)  
        f_lbl.place(x=0, y=0, width=800, height=200)

        # 2nd image 
        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face5.jpg")
        img1 = img1.resize((800, 200), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl1 = Label(self.root, image=self.photoimg1)  
        f_lbl1.place(x=800, y=0, width=800, height=200)

        # bg img
        img3 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\bgg.png")
        img3 = img3.resize((1520, 750), Image.LANCZOS)  
        self.photoimg3 = ImageTk.PhotoImage(img3)  

        bg_img = Label(self.root, image=self.photoimg3)  
        bg_img.place(x=0, y=200, width=1520, height=750)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times to roman",34,"bold"),bg="White",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1500,height=620)

        #left frame
        Left_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Students Attendance Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=680,height=550)

        img_left = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face19.jpg")
        img_left = img_left.resize((680, 130), Image.LANCZOS)  
        self.photoimg_left = ImageTk.PhotoImage(img_left) 

        f_lbl_left = Label(Left_frame, image=self.photoimg_left)  
        f_lbl_left.place(x=0, y=0, width=680, height=130)

        Left_inside_frame=LabelFrame(Left_frame,bd=2, bg="white",relief=RIDGE)
        Left_inside_frame.place(x=0,y=135,width=674,height=390)

        #Labeland entry
        #Attendance ID
        attendanceId_label=Label(Left_inside_frame,text="AttendanceID:",font=("times new roman",12,"bold"),bg="white")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceId_entry=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,"bold"))
        attendanceId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        
        #Roll NO
        roll_label=Label(Left_inside_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        atten_roll=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name 
        name_label=Label(Left_inside_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        atten_name=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(Left_inside_frame,text="Department:",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        atten_dep=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,"bold"))
        atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(Left_inside_frame,text="Time:",font=("times new roman",12,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        atten_time=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label=Label(Left_inside_frame,text="Date:",font=("times new roman",12,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        atten_date=ttk.Entry(Left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        
        #attendance status
        attendance_label=Label(Left_inside_frame,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        attendance_label.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(Left_inside_frame,textvariable=self.var_atten_attendance,font=("times new roman",12,"bold"),state="readonly",width=18)
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3,column=1,pady=8)

        #Button Frame
        btn_frame=Frame(Left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=300,width=670,height=35)

        emport_btn=Button(btn_frame,text="Import CSV",command=self.importCsv,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        emport_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export CSV",command=self.exportCsv,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=18,height=0,font=("times new roman",11,"bold"),bg="Blue",fg="white")
        reset_btn.grid(row=0,column=3)



        #right frame
        Right_frame=LabelFrame(main_frame,bd=2, bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=710,y=10,width=707,height=550)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=690,height=455)

        #Scroll bar and table 
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="AttendanceID")
        self.AttendanceReportTable.heading("roll",text="Roll No")
        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

        #==========Fetch Data=============

    def fetch_Data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

        # import csv
    def importCsv(self):
        global mydata  
        mydata.clear()  # Clear the existing data
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV file", "*.csv"), ("All file", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_Data(mydata)  # Corrected method name

            # export csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSv",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported To"+os.path.basename(fln)+"Sucessfully")

        except Exception as es:
               messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)  

    def get_cursor(self,event=" "):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")

         #upadte function
    def update_data(self):
        if self.var_atten_id.get()=="AttendanceID" or self.var_atten_roll.get()=="Roll No" or self.var_atten_name.get()=="Student Name" or self.var_atten_dep.get()=="Department" or self.var_atten_time.get()=="Time" or self.var_atten_date.get()=="Date" or self.var_atten_attendance.get()=="Attendance Status" :         
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("update","Do you want to update this student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set AttendanceID=%s,Roll No=%s,Student Name=%s,Department=%s,Time=%s,Date=%s, Attendance Status=%s",(
                                                                                                                                                                                                                                            self.var_atten_id.get(),
                                                                                                                                                                                                                                            self.var_atten_roll.get(),
                                                                                                                                                                                                                                            self.var_atten_name.get(),
                                                                                                                                                                                                                                            self.var_atten_dep.get(),
                                                                                                                                                                                                                                            self.var_atten_time.get(),
                                                                                                                                                                                                                                            self.var_atten_date.get(),
                                                                                                                                                                                                                                            self.var_atten_attendance.get()
                                                                                                                                                                                                                                           
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






               


        











if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)  
    root.mainloop()