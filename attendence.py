from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class attendence:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x790+0+0")
        self.root.title("Face Recognition System")

        # ==========variables===========
        self.var_atten_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_atten_attendance=StringVar()
        

        # first image
        img=Image.open(r"images\s4.jpeg")
        img = img.resize((680, 200), Image.BILINEAR) 

        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=680,height=200)


        # second image
        img1=Image.open(r"images\s5.jpeg")
        img1 = img1.resize((680, 200), Image.BILINEAR) 

        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=680,y=0,width=680,height=200)

        # background image

        img3=Image.open(r"images\HD-wallpaper-nature.jpg")
        img3 = img3.resize((1366, 710), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=200,width=1366,height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="dark green")
        title_lbl.place(x=0,y=0,width=1366,height=45)

        # main frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=55,width=1330,height=600)

        # left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendence Details",font=("times new roman",11,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=535)

        img_left=Image.open(r"images\download.jpeg")
        img_left = img_left.resize((720, 130), Image.BILINEAR)  # or Image.BICUBIC, Image.LANCZOS, etc.

        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=640,height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=5,y=135,width=637,height=320)
        
        # Label and Entry
        #AttendenceId
        attendenceId_label=Label(left_inside_frame,text='AttendenceID:',font=("times new roman",11,"bold"),bg="white")
        attendenceId_label.grid(row=0,column=0)

        attendenceID_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_atten_id,font=("times new roman",11,"bold"))
        attendenceID_entry.grid(row=0,column=1,pady=8,sticky=W)

        # Roll
        roll_label=Label(left_inside_frame,text='Roll:',font=("times new roman",11,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=4,pady=8,sticky=W)

        roll_entry=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_roll,font=("times new roman",11,"bold"))
        roll_entry.grid(row=0,column=3,pady=8,sticky=W)

        # Name
        Name_label=Label(left_inside_frame,text='Name:',font=("times new roman",11,"bold"),bg="white")
        Name_label.grid(row=1,column=0,sticky=W)

        atten_name=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_name,font=("times new roman",11,"bold"))
        atten_name.grid(row=1,column=1,pady=8,sticky=W)

        # Department
        dep_label=Label(left_inside_frame,text='Department:',font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2,sticky=W)

        atten_dep=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_dep,font=("times new roman",11,"bold"))
        atten_dep.grid(row=1,column=3,pady=8,sticky=W)

        # Time
        time_label=Label(left_inside_frame,text='Time:',font=("times new roman",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,sticky=W)

        atten_time=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_time,font=("times new roman",11,"bold"))
        atten_time.grid(row=2,column=1,pady=8,sticky=W)

        #ate:
        date_label=Label(left_inside_frame,text='Date:',font=("times new roman",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,sticky=W) 

        atten_date=ttk.Entry(left_inside_frame,width=22,textvariable=self.var_date,font=("times new roman",11,"bold"))
        atten_date.grid(row=2,column=3,pady=8,sticky=W)

         #AttendenceId
        attendencelabel=Label(left_inside_frame,text='AttendenceID:',font=("times new roman",11,"bold"),bg="white")
        attendencelabel.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font="comicsansns 11 bold",state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        # button frame

        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=260,width=630,height=25)

        import_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        import_btn.grid(row=0,column=0)

        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        export_btn.grid(row=0,column=1)

        update_btn=Button(btn_frame,text="Update",width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=21,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
       

         # right label frame

        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendence Details",font=("times new roman",11,"bold"))
        Right_frame.place(x=670,y=10,width=650,height=535)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=630,height=445)

        # ===========scroll bar table=
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendence ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    
    #=============fetch data=============

    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

    # +========= import csv==============
    
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*csv"),("ALl file","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ==========export csv=========
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data","No Data found to export",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv",filetypes=(("CSV File","*csv"),("ALl file","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to "+os.path.basename(fln)+" successfully.")
        except Exception as es:
            messagebox.showerror("ERROR",f"Due to: {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_dep.set(rows[3])
        self.var_time.set(rows[4])
        self.var_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])


    def reset_data(self):

        
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_atten_attendance.set("")








if __name__=="__main__":
    root=Tk()
    obj=attendence(root)
    root.mainloop()