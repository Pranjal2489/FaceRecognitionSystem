from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        img_top=Image.open(r"images\deve.webp")
        img_top = img_top.resize((1364, 700), Image.BILINEAR)  

        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1364,height=700)

        # frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=800,y=0,width=500,height=600)
        
        # imge in frame

        img_side=Image.open(r"images\developy.jpeg")
        img_side = img_side.resize((200,200), Image.BILINEAR)  

        self.photoimg_side=ImageTk.PhotoImage(img_side)

        f_lbl=Label(main_frame,image=self.photoimg_side)
        f_lbl.place(x=300,y=0,width=200,height=200)

        # Developer info
        
        dev_label=Label(main_frame,text='Hello ! My name is Pranjal',font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=0,y=5) 

        dev_label=Label(main_frame,text='I am a full stack developer',font=("times new roman",17,"bold"),bg="white")
        dev_label.place(x=0,y=40) 

        # third image

        img2=Image.open("images\devel.webp")
        img2 = img2.resize((500, 400), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(main_frame,image=self.photoimg2)
        f_lbl.place(x=0,y=200,width=500,height=400)





if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()