from tkinter import *
from tkinter import messagebox
import sqlite3

class DeleteContactDetails:    
    def display(self):
        self.delete=Tk()
        self.delete.title("DELETE CONTACT DETAILS")
        self.delete.geometry("300x300+500+100")
        self.namelabel=Label(self.delete,text="Name:").grid(row=1)        
        self.namebox=Entry(self.delete,bd=5)        
        self.namebox.grid(row=1,column=1)
        self.addsubmit=Button(self.delete,text="Submit",command=self.deletetodb).grid(row=4)
        self.addcancel=Button(self.delete,text="Cancel",command=self.delete.destroy)
        self.addcancel.grid(row=4,column=1)
        
    def deletetodb(self):        
        res=messagebox.askyesno("Confirmation","Do you want to delete?")
        if res:
            conn=sqlite3.connect("database1.db")
            try:
                cur=conn.cursor()
                vil=cur.execute("DELETE from ContactDetails WHERE Name=?",(self.namebox.get(),))
                print(vil)
                conn.commit()
            except Error as error:
                print(error)
                messagebox.showinfo("Error","Name Dosen't Exists")
            else:
                mes=messagebox.showinfo("Deleted", "Deleted Successfully")
                if mes=="ok":
                    self.delete.destroy()
            finally:
                conn.close()
