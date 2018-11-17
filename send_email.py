# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *


def send_email(email, message):
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("heart_sentinel_server@example.com")
    to_email = Email(email)
    subject = "Warning: Tachycardic Patient Alert"
    content = Content("text/plain", message)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


if __name__ == "__main__":
    message = "Patient is tachycardic"
    email = "haerynk@gmail.com"
    send_email(email, message)