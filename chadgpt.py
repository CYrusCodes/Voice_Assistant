# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
#import subprocess
import pyjokes
import os
import requests
#from ShazamAPI import Shazam
# speaker = win32com.client.Dispatch("SAPI.SpVoice")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():  #will take command from user recognizing what is being said
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1) 
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
       # r.adjust_for_ambient_noise(source, duration=5)
        print("working")
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

if __name__=="__main__":
    #clear = lambda: os.system('cls')
    speak("hi, how may I help you")
    query = takeCommand().lower()

    if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
    elif 'open google' in query:
            speak("Here you go to Google\n")
            first_url = 'https://www.google.com/'
            webbrowser.open_new_tab(first_url)
    elif "open youtube" in query:
            speak("Here you go to youtube\n")
            first_url = 'https://www.youtube.com/'
            webbrowser.open_new_tab(first_url)
    elif "in youtube" in query:
            speak("song name please")
            query1 = takeCommand().lower()
            name=query1.split()
            str=''
            for i in range(len(name)):
                    if(i==len(name)-1):
                        str=str+name[i]
                    else:
                        str=str+name[i]+'+'
            first_url = 'https://www.youtube.com/results?search_query='+str
            webbrowser.open_new_tab(first_url)        
    elif 'joke' in query:
            joke=pyjokes.get_joke()
            print(joke)
            speak(joke)
    elif 'fifa 18' in query:
         command = "D:\FIFA18\FIFA18.exe"
         os.system(command)  

                               
