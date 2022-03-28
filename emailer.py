import smtplib, ssl
import admincreds

dictionary = dict(admincreds.credentials)

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "nkrei.me@gmail.com"
# receiver_email = "nkento2007@gmail.com"
# print(dictionary)
password = dictionary["nkrei.me@gmail.com"]
message = """\
Subject: Welcome to Nkrei!

Thanks for siging up. You don't get any benefits or anything by the way. It's just that you can now log in to our website."""

def email(receiver_email):
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# email("nkento2007@gmail.com")