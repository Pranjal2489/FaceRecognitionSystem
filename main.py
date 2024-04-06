from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # first image
        img=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\gndu.jpg")
        img = img.resize((500, 130), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)


        # second image
        img1=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\facialrecognition.webp")
        img1 = img1.resize((500, 130), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image

        img2=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\gndu.jpg")
        img2 = img2.resize((500, 130), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

         # Bg image4
        img3=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\HD-wallpaper-nature.jpg")
        img3 = img3.resize((1366, 710), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1366,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        #student button

        img4=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\studentt.webp")
        img4 = img4.resize((210, 210), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=300,width=210,height=40)

        #detect face button

        img5=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\faceDet.jpeg")
        img5 = img5.resize((210, 210), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=300,width=210,height=40)



        #attendance button

        img6=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\attendence.png")
        img6 = img6.resize((210, 210), Image.BILINEAR)  
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=300,width=210,height=40)

        #help button

        img7=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\helpdesk.jpeg")
        img7 = img7.resize((210, 210), Image.BILINEAR)  
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=210,height=210)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=300,width=210,height=40)

        #train face button

        img8=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\face.jpg")
        img8 = img8.resize((210, 210), Image.BILINEAR)  
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=350,width=210,height=210)

        b1_1=Button(bg_img,text="Train Face",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=200,y=550,width=210,height=40)


        #photos button

        img9=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\train.jpg")
        img9 = img9.resize((210, 210), Image.BILINEAR)  
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=350,width=210,height=210)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=500,y=550,width=210,height=40)


        #Developer button

        img10=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\developer.jpg")
        img10 = img10.resize((210, 210), Image.BILINEAR)  
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=350,width=210,height=210)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=800,y=550,width=210,height=40)

        #exit button

        img11=Image.open(r"C:\Users\hp\Desktop\face_recognition_system\images\exit.jpeg")
        img11 = img11.resize((210, 210), Image.BILINEAR)  
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=350,width=210,height=210)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="dark blue",fg="white")
        b1_1.place(x=1100,y=550,width=210,height=40)

        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()