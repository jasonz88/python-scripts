#!/usr/bin/python

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

def login(user, pwd):
    mail_server = smtplib.SMTP("wmail.austin.utexas.edu", 587)
    mail_server.ehlo()
    mail_server.starttls()
    mail_server.ehlo()
    mail_server.login(user, pwd)
    return mail_server

def send_mail(mail_server, from_id, to_id, subject, text = None, attach = None):
    msg = MIMEMultipart()

    msg['From'] = from_id
    msg['To'] = to_id
    msg['Subject'] = subject

    if text:
        msg.attach(MIMEText(text))

    if attach:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attach, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
        msg.attach(part)

    mail_server.sendmail(from_id, to_id, msg.as_string())
    
def logout(mail_server):
    mail_server.close()
