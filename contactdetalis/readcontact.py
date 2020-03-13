from tkinter import *
from tkinter import messagebox
import sqlite3

class ReadContactDetails:    
    def display(self):
        self.read=Tk()
        self.read.title("READING CONTACT DETAILS")
        self.read.geometry("300x300+500+100")
        self.namelabel=Label(self.read,text="Name:").grid(row=1)
        self.namebox=Entry(self.read,bd=5) 
        self.namebox.grid(row=1,column=1)
        self.addsubmit=Button(self.read,text="Submit",command=self.readtodb).grid(row=4)
        self.addcancel=Button(self.read,text="Cancel",command=self.read.destroy)
        self.addcancel.grid(row=4,column=1)
    def readtodb(self):
        conn=sqlite3.connect("database1.db")
        try:
            cur=conn.cursor()
            row=cur.execute("SELECT * FROM ContactDetails WHERE Name=?",(self.namebox.get(),))
            for i in row:
                phno,email=i[1],i[2]
            self.mobilebox=Label(self.read,bd=5,text=phno)
            self.mailbox=Label(self.read,bd=5,text=email)
            self.mobilebox.grid(row=2,column=1)
            self.mailbox.grid(row=3,column=1)
        except Exception as e:
            messagebox.showinfo("Error","Name Dosen't Exists")
            self.namebox.delete(0,END)
        else:
            self.mobilelabel=Label(self.read,text="MobileNo:").grid(row=2)
            self.maillabel=Label(self.read,text="E-Mail").grid(row=3)
           
        finally:
            conn.close()
