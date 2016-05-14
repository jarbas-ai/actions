import smtplib

#Funcion that sends the email to the user

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



# jb == Jarbas' default email
# user == user's email
jb = "jarbas.butler@gmail.com"
user = '@gmail.com'

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "O encaminhamento tá funcionando!"
msg['From'] = jb
msg['To'] = user

# Body of the message (a plain-text and an HTML version).
# The HTML version is in comment for the time being. Might come in handy for some future use.
#text = "Fala galera\n o Jarbas quer saber como vcs estão.\n Deem sinal de vida.\n Todos digam OLÁ JARBAS."
html = """\
<html>
  <head></head>
  <body>
    <p>Fala galera<br>
       o Jarbas quer saber como vcs estão.<br>
       Deem sinal de vida.
       Todos digam OLÁ JARBAS.
    </p>
  </body>
</html>
"""

# Record the MIME types of both parts - text/plain and text/html.
#part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
#msg.attach(part1)
msg.attach(part2)

# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

# This puts the connection to the SMTP server into TLS mode.
mail.starttls()

mail.login('jarbas.butler@gmail.com', '')
mail.sendmail(jb, user, msg.as_string())
mail.quit()
