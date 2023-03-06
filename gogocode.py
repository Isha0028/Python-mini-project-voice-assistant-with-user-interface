import sys
import time
import webbrowser
import pyjokes
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import pyaudio
import cv2
import random
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import pyautogui
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import PyPDF2
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import instaloader #pip install instaloader
import operator #for calculation using voice
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from IVA import Ui_MainWindow
from bs4 import BeautifulSoup


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[1].id)


#TEXT TO SPEECH
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
    


def wish():
    hour = int(datetime.datetime.now().hour)
    tt=time.strftime("%I:%M:%p")
    if hour>=0 and hour<=12:
        speak(f"Good morning, its {tt}")
    elif hour>12 and hour <18:
        speak(f"Good afternoon, its {tt}")
    else:
        speak(f"Good evening, its {tt}")
    speak("Hello! I am your  Assistant IVA")
    speak("How may I help you.")
    # i





def news():
    # for news updates
        main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8103079ca5d742e49c850d93d7661505'

        main_page = requests.get(main_url).json()
        # print(main_page)
        articles = main_page["articles"]
        # print(articles)
        head = []
        day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
        for ar in articles:
            head.append(ar["title"])
        for i in range(len(day)):
            # print(f"today's {day[i]} news is: ", head[i])
            speak(f"today's {day[i]} news is: {head[i]}")


def pdf_reader():
    book = open('literatura-matlab.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)



class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
        
   
    
    def run(self):
        
        speak("please say wakeup to continue")
        while True:
            self.query = self.takecommand()
            if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
                self.TaskExecution()
                
                
                
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            # audio = r.listen(source, timeout=100, phrase_time_limit=10)
            # r.pause_threshold = 0.5
            r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            audio = r.listen(source,timeout=10,phrase_time_limit=50)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        query = query.lower()
        return query



                        

    def TaskExecution(self):
        wish()
     
        while True:
            self.query = self.takecommand()

            #logic building for tasks

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

          

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                # cv2.destroyAllWindows()


            elif "play music" in self.query:
                music_dir ="C:\\Users\\ISHA\\Music"
                songs = os.listdir(music_dir)
                print(songs)   
                random = os.startfile(os.path.join(music_dir, songs[1]))
            
            elif 'exit' in self.query:
                 speak("Thanks for giving me your time")
                 exit()  
                 
            elif "who made you" in self.query or "who created you" in self.query:
                 speak("I have been created by Isha and Prachi.")       

            elif "who i am" in self.query:
                 speak("If you talk then definitely your human.")
 
            elif "why you came to world" in self.query:
                speak("Thanks to ISHA and PRACHI. further It's a secret")
 
            elif 'open powerpoint presentation' in self.query:
                speak("opening Power Point presentation")
                power = r"C:\Users\ISHA\OneDrive\Desktop\gogo\IVA-INTELLIGENT VOICE ASSISTANT.pptx"
                os.startfile(power)
                
            elif "who are you" in self.query:
                speak("I am your intelligent virtual assistant : IVA")
 
            elif 'reason for you' in self.query:
                speak("I was created as a Minor project by PRACHI AND ISHA")
     

            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            elif "wikipedia" in self.query:
                speak("searching wikipedia....")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query, sentences=2)
                speak("according to wikipedia")
                speak(results)
                # print(results)

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open google" in self.query:
                speak("sir, what should i search on google")
                cm = takecommand()
                webbrowser.open(f"{cm}")
            
           

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay , i am going to sleep you can call me anytime.")
                sys.exit()
                gifThread.exit()
                break
                


            #to close any application
            elif "close notepad" in self.query:
                speak("okay, closing notepad")
                os.system("taskkill /f /im notepad.exe")

           
                    
            #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif "shut down the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "sleep the system" in self.query:
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            elif "hello" in self.query or "hey" in self.query:
                speak("hello , may i help you with something.")
            
            elif "how are you" in self.query:
                speak("i am fine , what about you.")

            elif "thank you" in self.query or "thanks" in self.query:
                speak("it's my pleasure .")


            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(5)
                pyautogui.keyUp("alt")
                    

            elif "tell me news" in self.query:
                speak("please wait , feteching the latest news")
                news()


           


            ##########################################################################################################################################
            ###########################################################################################################################################

            elif "do some calculations" in self.query or "can you calculate" in self.query:            
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("Say what you want to calculate, example: 3 plus 3")
                    print("listening.....")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' :operator.__truediv__,
                        'Mod' : operator.mod,
                        'mod' : operator.mod,
                        '^' : operator.xor,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                print(eval_binary_expr(*(my_string.split())))


            #-----------------To find my location using IP Address

            elif "where i am" in self.query or "where we are" in self.query:
                speak("wait, let me check")
                try:
                    ipAdd = requests.get('https://api.ipify.org').text
                    print(ipAdd)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    # print(geo_data)
                    city = geo_data['city']
                    state = geo_data['state']
                    country = geo_data['country']
                    speak(f"i am not sure, but i think we are in {city} city of {country} country")
                except Exception as e:
                    speak("sorry , Due to network issue i am not able to find where we are.")
                    pass


            

            #-------------------To check a instagram profile----
            elif "show me a instagram profile" in  self.query or "profile on instagram" in self.query:
                speak(" please enter the user name correctly.")
                name = input("Enter username here:")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"here is the profile of the user {name}")
                time.sleep(5)
                speak("sir would you like to download profile picture of this account.")
                condition = self.takecommand()
                if "yes" in condition:
                    mod = instaloader.Instaloader() #pip install instadownloader
                    mod.download_profile(name, profile_pic_only=True)
                    speak("i am done , profile picture is saved in our main folder. now i am ready for next command")
                else:
                    pass

            #-------------------  To take screenshot -------------
            elif "take screenshot" in self.query or "take a screenshot" in self.query:
                speak(" please tell me the name for this screenshot file")
                name = self.takecommand()
                speak("please hold the screen for few seconds, i am taking sreenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done , the screenshot is saved in our main folder. now i am ready for next command")


            # speak("sir, do you have any other work")

            #-------------------  To Read PDF file -------------
            elif "read pdf" in self.query:
                pdf_reader()

            #--------------------- To Hide files and folder ---------------
            elif "hide all files" in self.query or "hide this folder" in self.query or "visible for everyone" in self.query:
                speak(" please tell me you want to hide this folder or make it visible for everyone")
                condition = self.takecommand()
                if "hide" in condition:
                    os.system("attrib +h /s /d") #os module
                    speak(", all the files in this folder are now hidden.")                

                elif "visible" in condition:
                    os.system("attrib -h /s /d")
                    speak(" all the files in this folder are now visible to everyone. i wish you are taking this decision in your own peace.")
                    
                elif "leave it" in condition or "leave for now" in condition:
                    speak("Ok")

            elif "give me the weather updates" in self.query:
                search = "weather in Himachal Pradesh"
                url = f"https://www.google.com/search?q={search}"
                req = requests.get(url)
                save = BeautifulSoup(req.text,"html.parser")
                tempp = save.find("div",class_= "BNeawe").text
                speak(f"current {search} is {tempp}")
            
startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:\python project\gif3.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        # self.ui.movie = QtGui.QMovie("E:/wallpaper/jar/intial.gif")
        # self.ui.label_2.setMovie(self.ui.movie)
        # self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(500)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
IVA= Main()
IVA.show()
sys.exit(app.exec_())        