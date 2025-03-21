from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
from PIL import Image, ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help


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
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()

