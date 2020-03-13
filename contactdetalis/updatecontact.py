from tkinter import *
from tkinter import messagebox
import sqlite3
class UpdateContactDetails:    
    def display(self):
        self.update=Tk()
        self.update.title("UDATE CONTACT DETAILS")
        self.update.geometry("300x300+500+100")
        self.namelabel=Label(self.update,text="Name:").grid(row=1)        
        self.namebox=Entry(self.update,bd=5)        
        self.namebox.grid(row=1,column=1)
        self.addsubmit=Button(self.update,text="Submit",command=self.viewdb).grid(row=4)
        self.addcancel=Button(self.update,text="Cancel",command=self.update.destroy)
        self.addcancel.grid(row=4,column=1)
    def viewdb(self):
        self.namebox.config(state=DISABLED)
        conn=sqlite3.connect("database1.db")
        try:
            cur=conn.cursor()
            row=cur.execute("SELECT * FROM ContactDetails WHERE Name=?",(self.namebox.get(),))
            for i in row:
                phno,email=i[1],i[2]
            self.mobilebox=Entry(self.update,bd=5,textvariable=phno)
            self.mailbox=Entry(self.update,bd=5,textvariable=email)
            self.mobilebox.grid(row=2,column=1)
            self.mailbox.grid(row=3,column=1)
        except Exception as e:
            messagebox.showinfo("Error","Name Dosen't Exists")
            self.namebox.delete(0,END)
        else:
            self.mobilelabel=Label(self.update,text="MobileNo:").grid(row=2)
            self.maillabel=Label(self.update,text="E-Mail").grid(row=3)
            self.addupdate=Button(self.update,text="Update",command=self.updatetodb).grid(row=4)
            self.addcancel=Button(self.update,text="Cancel",command=self.update.destroy)
            self.addcancel.grid(row=4,column=1)
        finally:
            conn.close()
        
    def updatetodb(self):
        conn=sqlite3.connect("database1.db")
        try:
            cur=conn.cursor()            
            if len(self.namebox.get())>=1 and self.namebox.get().isalpha() and len(self.mobilebox.get())==10 and self.mobilebox.get().isdigit() and len(self.mailbox.get())!=0 and  '@' in self.mailbox.get():
                cur.execute("UPDATE ContactDetails SET MobileNo=?,Email=? WHERE Name=?",(self.mobilebox.get(),self.mailbox.get(),self.namebox.get()))
                conn.commit()
                mes=messagebox.showinfo("Update", "Updated Successfully")
                if mes=="ok":
                    self.update.destroy()                
            else:
                raise Exception
        except:
            if not(len(self.namebox.get())>=1 and self.namebox.get().isalpha()):
                messagebox.showinfo("Error", " name should not be empty or name must contains alpha")
            elif not(len(self.mobilebox.get())==10 and self.mobilebox.get().isdigit()):
                messagebox.showinfo("Error", "Mobile no must contain 10 digits or only contain numbers")
            elif not(len(self.mailbox.get())!=0 and  '@' in self.mailbox.get()):
                messagebox.showinfo("Error", "Invalid MailID")
            else:
                messagebox.showinfo("Error", "Name,Mobile No,Maild ID must be unique")
        finally:
            conn.close()


