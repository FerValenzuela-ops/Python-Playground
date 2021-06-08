import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

html = Template(Path('index.html').read_text())

### https://support.google.com/mail/?p=BadCredentials

email = EmailMessage()

email['from'] = 'Your name'
email['to'] = 'Email of that person/entity'
email['subject'] = 'The subject '


email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login('email@gmail.com' , 'password')
    smtp.login('email@gmail.com' , 'password')
    smtp.send_message(email)
    print('All good boss')
