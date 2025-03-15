from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()




class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1550x800+0+0")  
        self.root.title("Login")

        self.bg=ImageTk.PhotoImage(file=r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\fr.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\lo.jpg")
        img = img.resize((100, 100), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(image=self.photoimg,bg="black",borderwidth=0)  
        f_lbl.place(x=730, y=175, width=100, height=100)

        title_lbl=Label(frame,text="Get Started",font=("Helvetica",20),bg="black",fg="white")
        title_lbl.place(x=95,y=100)

        username=lbl=Label(frame,text="Username",font=("Helvetica",16),bg="black",fg="white")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Times", "16", "bold italic"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="Password",font=("Helvetica",16),bg="black",fg="white")
        password.place(x=70,y=225)

        self.txtpass=ttk.Entry(frame,font=("Times", "16", "bold italic"))
        self.txtpass.place(x=40,y=250,width=270)

        #=======icon button======

        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\lo.jpg")
        img1 = img1.resize((25, 25), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(image=self.photoimg1,bg="black",borderwidth=0)  
        f_lbl.place(x=650, y=325, width=25, height=25)

        img2 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\2.jpg")
        img2 = img2.resize((25, 25), Image.LANCZOS)  
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(image=self.photoimg2,bg="black",borderwidth=0)  
        f_lbl.place(x=650, y=395, width=25, height=25)

         #login button
        loginbtn = Button(frame,text="Login",command=self.login,relief=RIDGE,bd=3 ,font=("times to roman", 15, "bold"), bg="red", fg="white",activebackground="red",activeforeground="white")
        loginbtn.place(x=110, y=300, width=120, height=35)

         #registration button
        loginbtn = Button(frame,text="New User Register",command=self.rigister_window ,font=("times to roman", 10, "bold"),borderwidth=0, bg="black", fg="white",activebackground="black",activeforeground="white")
        loginbtn.place(x=15, y=350, width=160)

         #forget pass button
        loginbtn = Button(frame,text="Forget Password",command=self.forget_password_window ,font=("times to roman", 10, "bold"),borderwidth=0, bg="black", fg="white",activebackground="black",activeforeground="white")
        loginbtn.place(x=10, y=370, width=160)

    def rigister_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)



    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","All field are required") 
        elif self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to the system ")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor()
            my_cursor.execute("Select * from register where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()
           
                                                                                              ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username & Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()

                #============Reset password========= 
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="" :
            messagebox.showerror("Error","Pls enter the answer",parent=self.root2)
        elif self.txt_new_password.get()=="" :
            messagebox.showerror("Error","Pls enter the new password ",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor()
            query=("Select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","pls enter correct answer",parent=self.root2 )
            else:
                query=("update register set password=%s where email=%s") 
                value=(self.txt_new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset, pls login new password",parent=self.root2)
                self.root2.destroy()

    
                #==========forget password===========

    def forget_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor() 
            query=("Select * from register where email=%s")
            value=(self.txtuser.get(),) 
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()


            #print(row)  
            if row==None:
                messagebox.showerror("My Error","Please enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")  
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forget Password",font=("times to roman", 20, "bold"), bg="red", fg="white")
                l.place(x=0,y=10,relwidth=1)


                security_Q=Label(self.root2,text="Select Security Question",font=("times to roman",15,"bold"),bg="lightblue")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,state="readonly",font=("times new roman",15,"bold"))
                self.combo_security_Q["values"]=("Select","Your Favourite Book","Your Favourite Teacher","Your Favourite City")
                self.combo_security_Q.current(0)
                self.combo_security_Q.place(x=50,y=110,width=250)


            
                security_A=Label(self.root2,text="Security Answer",font=("times to roman",15,"bold"),bg="lightblue")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("Times", "15", "bold italic"))
                self.txt_security.place(x=50,y=180,width=250)


                new_pass=Label(self.root2,text="New Password",font=("times to roman",15,"bold"),bg="lightblue")
                new_pass.place(x=50,y=220)

                self.txt_new_password=ttk.Entry(self.root2,font=("Times", "15", "bold italic"))
                self.txt_new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",command=self.reset_pass,font=("times to roman",15,"bold"),fg="white",bg="green")
                btn.place(x=100,y=290)






class Register:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x900+0+0")  
        self.root.title("Register")

        #======variables===========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        # bg img
        img = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\sa.jpg")
        img = img.resize((1600, 900), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)  

        bg_img = Label(self.root, image=self.photoimg)  
        bg_img.place(x=0, y=0, width=1600, height=900)

        # left img
        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\rob.jpg")
        img1 = img1.resize((470, 550), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        bg_img = Label(self.root, image=self.photoimg1)  
        bg_img.place(x=50, y=100, width=470, height=550)

        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times to roman",20,"bold"),bg="white",fg="darkgreen")
        register_lbl.place(x=20,y=20)

        fname=Label(frame,text="First Name",font=("times to roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Times", "15", "bold italic"))
        fname_entry.place(x=50,y=130,width=250)


        l_name=Label(frame,text="Last Name",font=("times to roman",15,"bold"),bg="white")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("Times", "15", "bold italic"))
        self.txt_lname.place(x=370,y=130,width=250)


        contact=Label(frame,text="Contact No",font=("times to roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("Times", "15", "bold italic"))
        self.txt_contact.place(x=50,y=200,width=250)


        email=Label(frame,text="Email",font=("times to roman",15,"bold"),bg="white")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("Times", "15", "bold italic"))
        self.txt_email.place(x=370,y=200,width=250)


        security_Q=Label(frame,text="Select Security Question",font=("times to roman",15,"bold"),bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,state="readonly",font=("times new roman",15,"bold"))
        self.combo_security_Q["values"]=("Select","Your Favourite Book","Your Favourite Teacher","Your Favourite City")
        self.combo_security_Q.current(0)
        self.combo_security_Q.place(x=50,y=270,width=250)


    
        security_A=Label(frame,text="Security Answer",font=("times to roman",15,"bold"),bg="white")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("Times", "15", "bold italic"))
        self.txt_security.place(x=370,y=270,width=250)


        pswd=Label(frame,text="Password",font=("times to roman",15,"bold"),bg="white")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("Times", "15", "bold italic"))
        self.txt_pswd.place(x=50,y=340,width=250)

        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times to roman",15,"bold"),bg="white")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("Times", "15", "bold italic"))
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

         #======check button=============
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Conditions",font=("times to roman",12,"bold"),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=400)

        #=========buttons=========

        img3=Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\regs.png")
        img3=img3.resize((200,35),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimg3,command=self.register_data,borderwidth=0,cursor="hand2",font=("Times", "5", "bold italic"),bg="white",activebackground="white")
        b1.place(x=10,y=455,width=300)

        img4=Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\logg.jpg")
        img4=img4.resize((200,50),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(frame,image=self.photoimg4,command=self.return_login,borderwidth=0,cursor="hand2",font=("Times", "5", "bold italic"),bg="white",activebackground="white")
        b1.place(x=330,y=450,width=300)

        #=========function declaration===============

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select": 
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions",parent=self.root) 
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor()
            query=("select*from register where email=%s")
            value=(self.var_email.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,pls try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                       self.var_fname.get(),
                                                                                       self.var_lname.get(),
                                                                                       self.var_contact.get(),
                                                                                       self.var_email.get(),
                                                                                       self.var_securityQ.get(),
                                                                                       self.var_securityA.get(),
                                                                                       self.var_pass.get()
                                                                                        
                                                                                     ))
                
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucess","Register Sucessfully",parent=self.root)

    def return_login(self): 
        self.root.destroy()       



class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        # 1st image
        img = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face4.jpg")
        img = img.resize((500, 130), Image.LANCZOS)  
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)  
        f_lbl.place(x=0, y=0, width=500, height=130)

        # 2nd image 
        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face3.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl1 = Label(self.root, image=self.photoimg1)  
        f_lbl1.place(x=500, y=0, width=500, height=130)

        # 3rd image 
        img2 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face5.jpg")
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times to roman",34,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1510,height=45)

        #==========time=========
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000,time)

        lbl=Label(title_lbl,font=('times new roman',15,'bold'),background='white',foreground='blue')
        lbl.place(x=0,y=0, width=110,height=50)
        time()


        #STUDENT BUTTON
        img4 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\facee1.jpg")
        img4 = img4.resize((280, 220), Image.LANCZOS)  
        self.photoimg4 = ImageTk.PhotoImage(img4) 

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2", font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)



        #Detect Face Button
        img5 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\facee.png")
        img5 = img5.resize((280,220), Image.LANCZOS)  
        self.photoimg5 = ImageTk.PhotoImage(img5) 

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_recognition, font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b2_1.place(x=500, y=300, width=220, height=40)

         # Attendance face button
        img6 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\facee2.jpg")
        img6 = img6.resize((280,220), Image.LANCZOS)  
        self.photoimg6 = ImageTk.PhotoImage(img6) 

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2",command=self.attendance_data, font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help Face Button
        img7 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face9.png")
        img7 = img7.resize((280,220), Image.LANCZOS)  
        self.photoimg7 = ImageTk.PhotoImage(img7) 

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2",command=self.help_data ,font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b4_1.place(x=1100, y=300, width=220, height=40)

        #Train Face Button
        img8 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face10.jpg")
        img8 = img8.resize((280,220), Image.LANCZOS)  
        self.photoimg8 = ImageTk.PhotoImage(img8) 

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data, font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b5_1.place(x=200, y=580, width=220, height=40)


        #Photos face button
        img9 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\facee3.webp")
        img9 = img9.resize((280,220), Image.LANCZOS)  
        self.photoimg9 = ImageTk.PhotoImage(img9) 

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2",command=self.open_img, font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b6_1.place(x=500, y=580, width=220, height=40)

         #Developer face button 
        img10 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face12.jpg")
        img10 = img10.resize((280,220), Image.LANCZOS)  
        self.photoimg10 = ImageTk.PhotoImage(img10) 

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2",command=self.developer_data ,font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b7_1.place(x=800, y=580, width=220, height=40)

         #Exit face button
        img11 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\face15.jpg")
        img11= img11.resize((280,220), Image.LANCZOS)  
        self.photoimg11 = ImageTk.PhotoImage(img11) 

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1 = Button(bg_img, text="Exit", cursor="hand2",command=self.iExit ,font=("times to roman", 15, "bold"), bg="dark blue", fg="red")
        b8_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure exit",parent=self.root)   
        if self.iExit>0:
           self.root.destroy()
        else:
            return 


#========function buttons====================
    def student_details(self):
         self.new_window = Toplevel(self.root)
         self.app = Student(self.new_window)


    def train_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Train(self.new_window)


    def face_recognition(self):
         self.new_window = Toplevel(self.root)
         self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Attendance(self.new_window)

    def developer_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Developer(self.new_window)

    def help_data(self):
         self.new_window = Toplevel(self.root)
         self.app = Help(self.new_window)




if __name__ == "__main__":
    main()