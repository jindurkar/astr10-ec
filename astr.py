import smtplib
import os
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_image_email(url, sender_email, sender_password, recipient_email):
    # Download the image
    response = requests.get(url)
    image_name = 'image.png'
    with open(image_name, 'wb') as image_file:
        image_file.write(response.content)

    # Create the email message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Today's Photo of the Day"

    # Attach the image to the email
    with open(image_name, 'rb') as image_file:
        image = MIMEImage(image_file.read())
    message.attach(image)

    # Send the email
    with smtplib.SMTP('smtp.office365.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())

    # Delete the local image file
    os.remove(image_name)

# Set the URL and email credentials
url = 'https://apod.nasa.gov/apod/image/2306/abell2744_jwst1024.png'
sender_email = 'joelastr10@outlook.com'
sender_password = '123gmail'
# recipient_email = 'joelindurkar.astr.10@gmail.com'
recipient_email = str(input("enter email: "))

# Send the email with the image
print("processing (~40 seconds)")
send_image_email(url, sender_email, sender_password, recipient_email)

