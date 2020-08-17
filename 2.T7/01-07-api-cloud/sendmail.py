import smtplib, ssl
from email.mime.text import MIMEText
from getpass import getpass
from datetime import datetime
import time

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "quang.cvtot@gmail.com"
receiver_email = "congnghe.lmdt@gmail.com"

#password = getpass('Enter your password: ')
#print(password)

message = """
       Sample Email sent by Python.
       """

msg = MIMEText(message)
msg['to'] = receiver_email
msg['Subject'] = 'Python send mail test program'

context = ssl.create_default_context()

#Tạo vòng lặp true để lấy dữ liệu và lưu trữ về database
# while True:
#        print(datetime.now())
#        time.sleep(1)

while True:
       if datetime.today().time == "19:06:50":
              print(datetime.now())
              time.sleep(1)
              break
              

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
   server.login(sender_email, password)
   server.sendmail(sender_email, receiver_email, msg.as_string())