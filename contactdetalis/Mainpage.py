from tkinter import *
from tkinter import messagebox
import sqlite3
from addcontact import AddContactDetails
from readcontact import ReadContactDetails
from updatecontact import UpdateContactDetails
from deletecontact import DeleteContactDetails
from readallcontact import readcon
addobj=AddContactDetails()
readobj=ReadContactDetails()
updateobj=UpdateContactDetails()
deleteobj=DeleteContactDetails()
r=Tk()
var=IntVar()
r.title("CONTACT DETAILS")
r.geometry("250x100")
addcontact=Button(r,text="ADD",command=addobj.display).grid(row=0)
readcontact=Button(r,text="READ",command=readobj.display)
upadatecontact=Button(r,text="UPDATE",command=updateobj.display)
deletecontact=Button(r,text="DELETE",command=deleteobj.display)
readall=Button(r,text="READALL",command=readcon)
readcontact.grid(row=0,column=1)
upadatecontact.grid(row=0,column=2)
deletecontact.grid(row=0,column=3)
readall.grid(row=0,column=4)
r.mainloop()
