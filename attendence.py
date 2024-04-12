from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open("images\s4.jpeg")
        img = img.resize((500, 200), Image.BILINEAR) 

        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1=Image.open("images\s5.jpeg")
        img1 = img1.resize((500, 130), Image.BILINEAR) 

        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

if __name__=="__main__":
    root=Tk()
    obj=attendence(root)
    root.mainloop()