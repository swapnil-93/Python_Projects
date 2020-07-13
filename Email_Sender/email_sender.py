import smtplib


sender = input("Enter your email id.: ")
sender_pass = input("Enter your password: ")
receiver = input("Enter email of sender")
message = input("Enter message to mail:\n")

def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)        # creating a server to connect with gmail.
    server.ehlo()       # connect to server and client
    server.starttls()   # To add the security into the mail
    server.login(sender, sender_pass) # login to the smtp server with your email and password
    server.sendmail(sender, receiver, message) # send email to the given address with given message
    server.close()         # close the connection after sending mail

try:
    sendEmail(receiver, message)

except Exception:
    print("Error in sending mail")
else:
    print("Email Sent\n")
finally:
    print("Thank You!!")