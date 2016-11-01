import urllib2
import sys
import os
import cookielib
import tkMessageBox
import Tkinter
from stat import *
from Tkinter import *

root = Tk(className='way2sms')
root.configure(background='BROWN')
message1 = StringVar()
sender1 = StringVar()

def sendsms():
    if __name__ == "__main__":
        user = '9698079048'
        password='change accordingly'
        sender = sender1.get()
        message=message1.get()
        message = "+".join(message.split(' '))
        url= 'http://site24.way2sms.com/Login1.action?'
        urldata = 'username='+user+'&password='+password+'&&Submit=Sign+in'

        #Cookies to be saved
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        #Adding header details
        opener.addheader=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]

        try:
            url1=opener.open(url,urldata)
        except IOError:
            print('Error Occured')

        jession_id = str(cj).split('~')[1].split(' ')[0]
        sendurl = 'http://site24.way2sms.com/smstoss.action?'
        senddata = 'ssaction=ss&Token='+jession_id+'&mobile='+sender+'&message='+message+'&msglen=136'
        opener.addheaders = [('Referer','http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            url2=opener.open(sendurl,senddata)
        except IOError:
            print('Error Occured')
        print('Message Send Successfully for %s ' % sender)
        tkMessageBox.showinfo('Way2sms','Message sended for ' + sender + 'Succesfully')
        
L1 = Label(root,text='Enter Message')
L1.pack(side=TOP)
E1=Entry(root,textvariable = message1)
E1.pack(side=TOP)

lB = Label(root,text = '\n')
L1.pack()

L2 = Label(root,text='Enter Number:')
L2.pack(side=TOP)
E2=Entry(root,textvariable = sender1)
E2.pack(side=TOP)
B=Tkinter.Button(root,text='Send SMS',command =sendsms)
B.pack()
root.mainloop()
