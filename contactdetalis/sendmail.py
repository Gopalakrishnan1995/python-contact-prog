from tkinter import *
from tkinter import messagebox
import sqlite3
import smtplib
class mailclass():
   def display(self):
      self.mail=Tk()
      self.mail.title("ADDING CONTACT DETAILS")
      self.mail.geometry("300x300+500+100")
      self.sublabel=Label(self.mail,text="Subject:").grid(row=1)
      self.msglabel=Label(self.mail,text="Message:").grid(row=2)
      self.subbox=Entry(self.mail,bd=5)
      self.msgbox=Entry(self.mail,bd=5)
      self.subbox.grid(row=1,column=1)
      self.msgbox.grid(row=2,column=1)
      self.mailsubmit=Button(self.mail,text="Sent",command=self.sendmail_fun).grid(row=4)
      self.mailcancel=Button(self.mail,text="Cancel",command=self.mail.destroy)
      self.mailcancel.grid(row=4,column=1)
   def sendmail_fun(self):
      conn=sqlite3.connect("database1.db")
      sender='krishnagopalan95@gmail.com'
      receivers=[]
      cur=conn.cursor()
      data=cur.execute("SELECT Email from ContactDetails")
      s = smtplib.SMTP('smtp.gmail.com', 587)
      s.starttls()
      s.login("krishnagopalan95@gmail.com", "password")     
      for row in data:
         receivers.append(row[0])
      for i in receivers:
         message = "Subject: {} \n\n {}".format(self.subbox.get(),self.msgbox.get())
         try:
            s.sendmail(sender,i, message)
         except Exception as e:
            messagebox.showinfo("Error",e)
      else:
         res=messagebox.showinfo("Confirm","Successfully sent email")
         if res=="ok":
            self.mail.destroy()
      s.quit()
      conn.close()
