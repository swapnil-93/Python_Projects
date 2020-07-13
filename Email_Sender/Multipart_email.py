import smtplib      # import the library for sending email
from email.mime.multipart import MIMEMultipart      # This is used to combine parts of message
from email.mime.text import MIMEText        # this is used to send text through email


sender = input("Enter your Email Id.: ")    # Enter your email id
pas = input("Enter your password: ")        # Enter Your Password
receiver = input("Enter Recipient Email id: ")  # Enter Recipient's Email id
body = input("Enter your Message Body: ")   # Enter the body part
subject = input("Enter your email subject: ")   # Enter the subject of mail

message = MIMEMultipart()   # Create a variable for MIMEMultipart to create message parts
message["From"] = sender     # This will create From part
message["To"] = receiver     # This will create To part
message["Subject"] = subject    # This will create subject part

message.attach(MIMEText(body, "plain")) # attach the body of message to main message part

def sendEmail(receiver, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)        # creating a server to connect with gmail.
    server.ehlo()       # connect to server and client
    server.starttls()   # To add the security into the mail
    server.login(sender, pas) # login to the smtp server with your email and password
    server.sendmail(sender, receiver, message.as_string()) # send email to the given address with given message
    server.close()         # close the connection after sending mail

try:
    sendEmail(receiver, message)

except Exception:
    print("Error in sending mail")
else:
    print("Email Sent\n")
finally:
    print("Thank You!!")