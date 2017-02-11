import smtplib
from_addr = 'example@gmail.com'
to_addr = 'example@gmail.com'
to_name='superwoman'
from_name='keez'
subject='unicorns'
msg='Hi, how are you today?'
message= """From: {} <{}>
To: {} <{}> 
Subject: {}
{}
"""
message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
# Credentials (if needed)
username = 'example@gmail.com'
password = 'mypassword'
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)
server.sendmail(from_addr, to_addr, message_to_send)
server.quit() 