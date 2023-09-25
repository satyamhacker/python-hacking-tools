import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui
import time
import psutil
import webbrowser


''' all variables are defined here''';

turn_on_bulb='ok sir turning on the bulb';
turn_off_bulb='ok sir turning off the bulb';
sorry_word= "sorry sir i didn't understand what you said";
start_number=1;

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Say something:")

        text_to_speech(' sir Any help you need ')

        # Listen for audio
        audio = recognizer.listen(source)

        try:
            # Recognize the speech using Google's service
            text = recognizer.recognize_google(audio);
            print(text);

            #text_to_speech(text);


            words = text.split(' ');

            '''from here if else condition will be met'''
        
            if 'on' in words and 'bulb' in words:
                print('found words');
                text_to_speech(turn_on_bulb);
        
            elif 'time' in words and 'now' in words:
                text_to_speech(time_now());

            elif 'off' in words and 'bulb' in words:
                text_to_speech(turn_off_bulb);

            elif 'move' in words and 'down' in words:
                 press_down_arrowkey();

            elif 'maximise' in words and 'window' in words:
                 maximize_window();

            elif 'minimise' in words and 'window' in words:
                 minimize_window();
            elif 'minimise' in words and 'everytheing' in words:
                 minimize_everything();
            
            elif 'anything' in words and 'Remember' in words:
                 remember_readFile()
                
            elif 'remember' in words:
                 remember_writeFile(text)

            elif 'battery' in words and 'status' in words:
                    battery_status();

            elif 'screenshot' in words:
                    take_screenshot();
        
            elif 'search' in words or 'google' in words or  'Google' in words:
                    chrome_search('google.com')

            elif 'nothing' in words or 'else' in words or 'no more help jarvis' in words:
                    jarvis_sleep()
            
            

          
        
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            text_to_speech(sorry_word);
            return None
        except sr.RequestError as e:
            print("Sorry, I encountered an error while making a request to Google Speech Recognition:")
            print(e)
            return None



def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # engine.setProperty('rate', 150)  # Speed of speech
    # engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


def time_now():

    current_time = datetime.datetime.now()

    return current_time.strftime("%H:%M:%S")

def press_down_arrowkey():
    # Delay to give you time to switch to the desired window
    time.sleep(1)
    # Simulate pressing the down arrow key ten times
    for i in range(10):
        pyautogui.press('down')
        time.sleep(0.5)  # Optional delay between key presses

def maximize_window():
    # Delay to give you time to switch to the desired window
    time.sleep(1)

    # Simulate pressing the Windows key and the Up arrow key (to maximize the window)
    pyautogui.hotkey('win', 'up')


def minimize_window():

    # Delay to give you time to switch to the desired window
    time.sleep(1)

    # Simulate pressing the Windows key and the Up arrow key (to maximize the window)
    pyautogui.hotkey('win', 'down')

def minimize_everything():

    # Delay to give you time to switch to the desired window
    time.sleep(2)

    # Simulate pressing the Windows key and the Up arrow key (to maximize the window)
    pyautogui.hotkey('win', 'd')

def remember_writeFile(text):

    # Open a file in write mode ('w')
    file_path = 'remember_note.txt'
    content = text;

    with open(file_path, 'w') as file:
        file.write(content)

def remember_readFile():
        # Open a file in read mode ('r')
        file_path = 'remember_note.txt'

        with open(file_path, 'r') as file:
            content = file.read()

        text_to_speech(content);

def battery_status():
    battery = psutil.sensors_battery()

    if battery is not None:
        plugged = battery.power_plugged
        percent = battery.percent

        if plugged:
            status = "charging";
        else:
            status = "discharging";

        text_to_speech(f"Battery status: {status}")
        text_to_speech(f"Battery percentage: {percent}%")        

def take_screenshot():

    global start_number;
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot to a file
    screenshot.save("screenshot"+str(start_number)+".png");

    print("Screenshot saved as screenshot"+str(start_number)+".png")

    text_to_speech("sir screenshot saved as screenshot"+str(start_number)+".png");

    start_number=start_number+1;

def chrome_search(url_without_http):

    url = "https://"+url_without_http;
    browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # Example path, replace with actual path
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(browser_path))
    webbrowser.get('chrome').open(url)

def jarvis_sleep():
    text='ok then sir going in sleep mode for one minute'
    text_to_speech(text);
    time.sleep(60);


while True:
    speech_to_text()
    time.sleep(2);

# speech_to_text()










