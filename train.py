from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        img_top=Image.open(r"images\facialrecognition.webp")
        img_top = img_top.resize((1364, 325), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1364,height=325)
        # Button
        b1_1=Button(self.root,text="Train Data",cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1364,height=60)


        img_bottom=Image.open(r"images\train.jpg")
        img_bottom = img_bottom.resize((1364, 325), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1364,height=325)


        








if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()