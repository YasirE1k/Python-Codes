#This isn't happening in gmail anymore probably. 
#I will try with outlook this, instead of gmail.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText    
import sys

message=MIMEMultipart()

message["From"]="yelktms612@outlook.com"
message["To"]="yelktms613@outlook.com"
message["Subject"]="Smtp Mail Sending"

write="""
I'm sending the mail with smtp
Yasir
"""

message_body= MIMEText(write,"plain")

message.attach(message_body)

try:
    mail=smtplib.SMTP("smtp.outlook.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("yelktms612@outlook.com","")

    mail.sendmail(message["From"],message["To"],message.as_string())

    print("Mail was send")

    mail.close()

except:
    sys.stderr.write("It happened a problem")
    sys.stderr.flush()
