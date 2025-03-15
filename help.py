from tkinter import *
from tkinter import ttk
from turtle import update
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK",font=("times to roman",34,"bold"),bg="White",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=40)

        img_top = Image.open(r"C:\Users\Rohit Kumar Bansal\OneDrive\Face Recognised\college_images\help0.jpg")
        img_top = img_top.resize((1530, 750), Image.LANCZOS)  
        self.photoimg_top = ImageTk.PhotoImage(img_top) 

        f_lbl = Label(self.root, image=self.photoimg_top)  
        f_lbl.place(x=0, y=55, width=1530, height=750)

        help_label=Label(f_lbl,text="Email: rohitkumarbansal23@gmail.com ",font=("times new roman",20,"bold"),fg="blue",bg="white")
        help_label.place(x=500,y=300)






                
if __name__ == "__main__":
    root = Tk()
    obj = Help(root)  
    root.mainloop()