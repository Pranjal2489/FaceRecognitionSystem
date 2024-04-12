from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from sys import path

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x790+0+0")
        self.root.title("Face Recognition System")



        title_lbl=Label(self.root,text="TRAIN DATASET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        img_top=Image.open(r"images\facialrecognition.webp")
        img_top = img_top.resize((1364, 325), Image.BILINEAR)  

        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1364,height=325)

        # Button
        b1_1=Button(self.root,text="TRAIN DATA",command=self.train_classifier,cursor="hand2",font=("times new roman",30,"bold"),bg="red",fg="white")
        b1_1.place(x=0,y=380,width=1364,height=60)


        img_bottom=Image.open(r"images\train.jpg")
        img_bottom = img_bottom.resize((1364, 325), Image.BILINEAR)  

        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1364,height=325)

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')#grayscale image
            imageNP=np.array(img,'uint8')#datatype
            id=int(os.path.split(image)[1].split('.')[1])
            

            faces.append(imageNP)
            ids.append(id)
            cv2.imshow("Training",imageNP)
            cv2.waitKey(1)==13
        ids=np.array(ids)
    # def train_classifier(self):
        # data_dir = "data"
        # if not os.path.exists(data_dir):
        #     print("Error: 'data' directory not found!")
        #     return

        # path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        # print("Image paths:", path)

        # faces = []
        # ids = []
        # for image in path:
        #     img = Image.open(image).convert('L')  # grayscale image
        #     imageNP = np.array(img, 'uint8')  # datatype
        #     id = int(os.path.split(image)[1].split('.')[1])

        #     faces.append(imageNP)
        #     ids.append(id)

        #     cv2.imshow("Training", imageNP)
        #     cv2.waitKey(1) == 13

        # ids = np.array(ids)
        # print("IDs:", ids)

        # ============= train the classifier and save===========
        # clf=cv2.face.LBPHFaceRecognizer_create()
        # clf.train(faces, ids)
        # clf_file = "classifier.xml"
        # clf.write(clf_file)
        # print("Classifier saved to:", clf_file)
        # cv2.destroyAllWindows()
        # messagebox.showinfo("RESULT", "Training Datasets completed!!!!")



        # # ============= train the classifier and save===========
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("RESULT","Training Datasets completed!!!!")


if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()