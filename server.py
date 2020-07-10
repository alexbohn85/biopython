#!/usr/bin/env python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# Create a text/plain message
msg = MIMEText("Teste Teste Teste!!")


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "teste@teste.com"
msg['To'] = "teste@teste.com"

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail("teste@teste.com", "teste@teste.com", msg.as_string())
s.quit()