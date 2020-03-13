from tkinter import *
from tkinter import messagebox
import sqlite3
from sendmail import mailclass
mailobj=mailclass()
def readcon():
    conn=sqlite3.connect("database1.db")
    readallcon=Tk()
    readallcon.title("SHOWING ALL CONTACT DETAILS")
    readallcon.geometry("300x300+500+100")
    cur=conn.cursor()
    data=cur.execute("SELECT * from ContactDetails")
    namelabel=Label(readallcon,text="Name:").grid(row=1)
    mobilelabel=Label(readallcon,text="MobileNo:",width=20)
    maillabel=Label(readallcon,text="E-Mail")
    mobilelabel.grid(row=1,column=2)
    maillabel.grid(row=1,column=3)
    count=2
    for row in data:
        entrylabel=Label(readallcon,text=row[0]).grid(row=count)
        phnolabel=Label(readallcon,text=row[1])
        emaillabel=Label(readallcon,text=row[2])
        phnolabel.grid(row=count,column=2)
        emaillabel.grid(row=count,column=3)
        count+=1
    sendmailbutton=Button(readallcon,text="Send mail",command=mailobj.display).grid(row=count)
    cancelbutton=Button(readallcon,text="Cancel",command=readallcon.destroy)
    cancelbutton.grid(row=count,column=2)
    conn.close()

