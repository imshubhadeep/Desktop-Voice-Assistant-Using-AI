import pyttsx3 #pip install pyttsx3 (text to speech convertion)
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
#import requests
import random
# import wolframalpha

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17: # here 17 means 5PM
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I'm your voice assistant How may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please tell me I'm Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Please wait I'm Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email@gmail.com', 'your-password')
    server.sendmail('email@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            exit()

        elif 'youtube' in query:
            speak('searching youtube.....')
            webbrowser.open('https://www.youtube.com/results?search_query=' + query)
            exit()

        elif 'google' in query:
            speak('searching google.....')
            webbrowser.open('https://www.google.com/search?q=' + query)
            exit()

        elif 'open spotify' in query:
            speak('searching spotify.....')
            webbrowser.open('https://www.spotify.com/in/' + query)
            exit()

        elif 'facebook' in query:
            speak('searching facebook.....')
            webbrowser.open('https://www.facebook.com/' + query)
            exit()
        
        elif 'open gaana' in query:
            speak('searching gaana.....')
            webbrowser.open('https://gaana.com/' + query)
            exit()

        elif 'open code' in query:
            codePath = "C:\\Users\\joydi\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
            exit()


        # elif "calculate" or "what is" in text: 
        #     question=takeCommand()
        #     app_id="Mention your API Key"
        #     client = wolframalpha.Client(app_id)
        #     res = client.query(question)
        #     answer = next(res.results).text
        #     speak("The answer is " + answer)
        #     exit()

        elif 'open media' in query:
            music_dir = 'F:\song'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
            exit()

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            exit()
        
        elif 'location' in query:
            speak('searching location.....')
            query = query.replace("location", "")
            webbrowser.open('https://www.google.com/maps/search/'+query)
            exit()

        elif 'my location' in query:
            speak('searching location.....')
            url = "https://www.google.com/maps/search/Where+am+I+?/"
            webbrowser.get().open(url)
            exit()
        
        elif 'toss a coin' in query:
            moves = ["head","tails"]
            move = random.choice(moves)
            query = query.replace("toss a coin", move)
            speak(query)
            exit()

        elif "what's the weather" in query:
            speak('searching weather.....')
            url = "https://www.google.com/search?q=weather"
            url1 = webbrowser.get().open(url)
            # speak(url1)
            exit()

        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shubhadeep.sc@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'stop' in query:
            speak("Ok See You soon.")
            exit()

