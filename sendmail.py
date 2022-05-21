import smtplib
import sys
from email.message import EmailMessage
import json
from decouple import config



def get_info():
    for line in sys.stdin:
        data = json.loads(line)
        
    return data

def send_mail():
    data_info = get_info()
    emails , msg_content , subject = data_info.values()
    for person in emails :
        try : 
            msg = EmailMessage()
            msg.set_content(msg_content)
            msg['Subject'] = subject
            msg['From'] = config('EMAIL_ACCOUNT')
            msg['To'] = person
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login(msg['From'],config('EMAIL_PASSWORD'))
            server.send_message(msg)
            server.quit()
            print('email sent to' + " " +  person)
        except :
            print('Unable to send the Email')

send_mail()


