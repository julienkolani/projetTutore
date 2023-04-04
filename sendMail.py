#Envoie de mail : 

import smtplib, ssl

# Specify the Gmail SMTP server and port
smtp_server = "smtp.gmail.com"
smtp_port = 465
API_KEY = "your_password_or_API_key_here"

# Specify the sender and recipient email addresses
sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@example.com"

def sendMail(currentIp):

    message = f"""\
Subject: Adresse Ip actuelle de l'user 

Cher utilisateur votre ip actuelle est {currentIp} veuillez le modifier auprès de votre explorateur de fichier."""

    # Create a secure SSL connection to the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
        # Login to the sender's Gmail account
        server.login(sender_email, API_KEY)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, message)
