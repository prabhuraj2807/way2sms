import urllib2
import sys
import os
import cookielib
from stat import *

message=raw_input('Enter Message :')
sender = raw_input('Enter Receiver Mob Number : ');
if __name__ == "__main__":
    print("\t\t\t\t***** m.way2sms.com ******")
    user = '9698079048'
    password='MOUNaguru24'
 
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
