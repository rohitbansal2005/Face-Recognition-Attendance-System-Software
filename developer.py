from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times to roman",34,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img_top = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\Ai.jpg")
        img_top = img_top.resize((1530, 750), Image.LANCZOS)  
        self.photoimg_top = ImageTk.PhotoImage(img_top) 

        f_lbl = Label(self.root, image=self.photoimg_top)  
        f_lbl.place(x=0, y=55, width=1530, height=750)

        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=900,y=0,width=500,height=600)

        img_top1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\rohit.jpg")
        img_top1 = img_top1.resize((200, 200), Image.LANCZOS)  
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1) 

        f_lbl = Label(main_frame, image=self.photoimg_top1)  
        f_lbl.place(x=300, y=0, width=200, height=200)

        dev_label=Label(main_frame,text="Hello,my name is Rohit",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="I am tech enthusiast",font=("times new roman",20,"bold"),fg="blue",bg="white")
        dev_label.place(x=0,y=40)

        img1 = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\facee1.jpg")
        img1 = img1.resize((500, 390), Image.LANCZOS)  
        self.photoimg1 = ImageTk.PhotoImage(img1)  

        f_lbl1 = Label(main_frame, image=self.photoimg1)  
        f_lbl1.place(x=0, y=210, width=500, height=390)














        
if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)  
    root.mainloop()