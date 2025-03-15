from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector




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
        b1=Button(frame,image=self.photoimg4,borderwidth=0,cursor="hand2",font=("Times", "5", "bold italic"),bg="white",activebackground="white")
        b1.place(x=330,y=450,width=300)

        #=========function declaration===============

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select": 
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and conditions") 
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Rkb@2005",database="face_recognised")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,pls try another email")
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
            messagebox.showinfo("Sucess","Register Sucessfully")


        
 












 




if __name__ == "__main__":
    root = Tk()
    obj = Register(root)  
    root.mainloop()       