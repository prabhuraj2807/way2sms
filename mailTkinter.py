import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import encoders
import Tkinter
import tkMessageBox
from Tkinter import *
import getpass

root = Tk(className='Gmail')
root.resizable(width=False,height=False)
def sendmail():
    sender = frommail.get()
    message= msgmail.get()
    getter = tomail.get()
    password = pasword.get()
    sub=subject.get()
    msg = MIMEMultipart()
    msg['From']=sender
    msg['To']=getter
    msg['Subject']=sub
    msg.attach(MIMEText(message,'plain'))
    filenames = filename.get()
    attachfile = attach.get()
    attachment = open(attachfile,"rb")

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filenames)
    msg.attach(part)
    

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,password)
    txt = msg.as_string()
    server.sendmail(sender,getter,txt)
    server.quit()
    tkMessageBox.showinfo('Mail Sended','Mail sended for '+getter+ ' Successfully')
root.configure(background='')
frommail = StringVar()
tomail=StringVar()
msgmail= StringVar()
pasword = StringVar()
subject=StringVar()
attach=StringVar()
filename=StringVar()
L1 =Label(root,text='From :')
L1.pack(side = TOP)
E1 = Entry(root,textvariable=frommail)
E1.pack(side = TOP)

L11 =Label(root,text='Password :')
L11.pack(side = TOP)
E11 = Entry(root,show="*",textvariable=pasword)
E11.pack(side = TOP)

L2 =Label(root,text='To :')
L2.pack(side = TOP)
E2 = Entry(root,textvariable=tomail)
E2.pack(side = TOP)

L4 =Label(root,text='Subject :')
L4.pack(side = TOP)
E4 = Entry(root,textvariable=subject)
E4.pack(side = TOP)

L3 =Label(root,text='Message :')
L3.pack(side = TOP)
E3 = Entry(root,textvariable=msgmail)
E3.pack(side = TOP)

L6 =Label(root,text='FileName :')
L6.pack(side = TOP)
E6 = Entry(root,textvariable=filename)
E6.pack(side = TOP)

L6 =Label(root,text='Attachement :')
L6.pack(side = TOP)
E6 = Entry(root,textvariable=attach)
E6.pack(side = TOP)

B= Tkinter.Button(root,text='Send Mail',command=sendmail)
B.pack(side=TOP)
root.mainloop()
