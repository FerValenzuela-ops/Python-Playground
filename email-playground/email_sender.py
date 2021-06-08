import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # os.path

html = Template(Path('index.html').read_text())

### https://support.google.com/mail/?p=BadCredentials

email = EmailMessage()

email['from'] = 'Fernando'
email['to'] = 'games@startgaming.net'
email['subject'] = '[AGAIN] Netflix problems'


email.set_content(html.substitute({'name':'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # smtp.login('pyferdevs@gmail.com' , 'justforfun69420')
    smtp.login('fernandox240997@gmail.com' , 'Superclave2mil.')
    smtp.send_message(email)
    print('All good boss')