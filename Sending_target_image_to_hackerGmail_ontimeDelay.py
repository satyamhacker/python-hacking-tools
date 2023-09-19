import cv2
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os

def send_mail(app_password,file_name_to_send):
    sender_email = 'satyamgrandmaster@gmail.com'  # storing the sender's mail id
    receiver_email = 'satyamgrandmaster@gmail.com'  # storing the receiver's mail id
    
    message = MIMEMultipart()
    
      # storing the password to log in
    # creating the SMTP server object by giving SMPT server address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_email, app_password)  # logging into out email id

   # Attach the image
    with open(file_name_to_send, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_name_to_send)}')
        message.attach(part)
        
    text = 'This is the message body.'
    message.attach(MIMEText(text, 'plain'))
    # Connect to the SMTP server and send the email
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, app_password)
        smtp_server.sendmail(sender_email, receiver_email,message.as_string())
        smtp_server.quit()
        print('Email sent successfully')
    except Exception as e:
        print('Error sending email:', str(e))



def capture_image_from_camera():
    # Initialize the camera (0 is usually the default camera, but you can change it)
    camera = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not camera.isOpened():
        print("Error: Camera not found or cannot be opened.")
        exit()

    # Capture a single frame
    ret, frame = camera.read()

    if not ret:
        print("Error: Could not capture an image.")
        camera.release()
        exit()

    # Save the captured image
    image_filename = "captured_image.jpg"
    cv2.imwrite(image_filename, frame)

    # Release the camera
    camera.release()

    print(f"Image saved as {image_filename}")
    
    send_mail('', 'captured_image.jpg')



while True:
    capture_image_from_camera();
    time.sleep(5)