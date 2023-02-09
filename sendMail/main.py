from pydoc import plain
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()


server.ehlo()

with open('password.txt','r') as f:
    password = f.read()
server.login('email',password)

msg = MIMEMultipart()

msg['From'] = 'Name'
msg['To'] = 'email'
msg['Subject'] = 'Just a Test'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'attachment.jpg'

attachment = open(filename,'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())


encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('toemailaddress','fromemailaddress',text)