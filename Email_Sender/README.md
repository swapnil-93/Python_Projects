# Sending EMail USing Python Script

**To send the email using python we have to use `smtplib` that uses SMTP(Simple Mail Transfer Protocol)**

_To use smtp service you have to make changes to your gmail account_
1. While logged into your gmail at gmail.com, go to https://myaccount.google.com/security 
2. Scroll down to the part that says "Allow less secure apps"
3. Turn ON "allow less secure apps".

_If you don't want to make your main gmail less secure, or if you don't already have gmail, then sign up for a new gmail solely for this purpose._
### Email_Sender 

* In this project we have created a simple program to send email
* We have used smtp protocol and module to send email.
* For more detail about smtp library use can go to [docs](https://docs.python.org/3/library/smtplib.html)
* You have to run the python file 
* Enter your email id and password
* Enter email id of the receiver
* Enter message you want to send

### Multipart_email
* To add the small details for email such as `From`, `To`, `Subject` we have to include a new package i.e. `MIMEMultipart` and `MIMEText`
* For more detail about `MSMEMultipart` and `MIMEText` go to [docs](https://docs.python.org/3.8/library/email.mime.html)

### Email_Attachment
_To add attachment we have to use libraries as shown in program._

**Steps to Send Mail with attachments using SMTP (smtplib)**

    1. Add sender, receiver address into the MIME
    2. Create MIME
    3. Add the mail title into the MIME
    4. Attach the body into the MIME
    5 Open the file as binary mode, which is going to be attached with the mail
    6. Read the byte stream and encode the attachment using base64 encoding scheme.
    7. Add header for the attachments
    8. Start the SMTP session with valid port number with proper security features.
    9. Login to the system.
    10. Send mail and exit