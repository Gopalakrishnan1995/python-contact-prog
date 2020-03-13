from tkinter import *
from tkinter import messagebox
import sqlite3

class AddContactDetails:
    
    def display(self):
        self.add=Tk()
        self.add.title("ADDING CONTACT DETAILS")
        self.add.geometry("300x300+500+100")
        self.namelabel=Label(self.add,text="Name:").grid(row=1)
        self.mobilelabel=Label(self.add,text="MobileNo:").grid(row=2)
        self.maillabel=Label(self.add,text="E-Mail").grid(row=3)
        self.namebox=Entry(self.add,bd=5)
        self.mobilebox=Entry(self.add,bd=5)
        self.mailbox=Entry(self.add,bd=5)
        self.namebox.grid(row=1,column=1)
        self.mobilebox.grid(row=2,column=1)
        self.mailbox.grid(row=3,column=1)
        self.addsubmit=Button(self.add,text="Submit",command=self.addtodb).grid(row=4)
        self.addcancel=Button(self.add,text="Cancel",command=self.add.destroy)
        self.addcancel.grid(row=4,column=1)
    def addtodb(self):
        conn=sqlite3.connect("database1.db")
        try:
            conn.execute("create table ContactDetails (Name VARCHAR(30) NOT NULL UNIQUE, MobileNo VARCHAR(10) NOT NULL UNIQUE,Email text NOT NULL UNIQUE)")
        except:
            pass
        try:
            if len(self.namebox.get())>=1 and self.namebox.get().isalpha() and len(self.mobilebox.get())==10 and self.mobilebox.get().isdigit() and len(self.mailbox.get())!=0 and  '@' in self.mailbox.get():
                conn.execute("Insert into ContactDetails(Name,MobileNo,Email) values(?,?,?)",(self.namebox.get(),self.mobilebox.get(),self.mailbox.get()))
                conn.commit()
                messagebox.showinfo("Register", "Thanks for register")
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
        else:
            self.namebox.delete(0,END)
            self.mobilebox.delete(0,END)
            self.mailbox.delete(0,END)
            #messagebox.showinfo("Register", "Thanks for register")
        finally:
            conn.close()
        
