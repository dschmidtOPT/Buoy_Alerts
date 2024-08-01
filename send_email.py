import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


subject = "Event Based SMTP Notification Testing"
body = "This is the SWPB-01 MIO sending a SMTP Python test alert with attachment (from Doug :-)" 

sender_email = "oceanpowertechbuoyalerts@gmail.com"
sender_password = "aeos jlsh kllt nksd"
## Add email to recipient list if desired
recipient_emails = ["aremo@oceanpowertech.com",
                  "dgoldstein@oceanpowertech.com",
                  "dschmidt@oceanpowertech.com"]



with open("attachment.txt", "rb") as attachment:
    # Add the attachment to the message
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename= attachment.txt")



for recipient in recipient_emails:
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient
    html_part = MIMEText(body)
    message.attach(html_part)
    message.attach(part)
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient, message.as_string())
    server.quit()
