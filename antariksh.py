import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
from bs4 import BeautifulSoup


engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


# def sendEmail(do,content):




def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning ")

    elif hour>=12 and hour<18:
        speak("good afternoon")

    

    else:
        speak("good evening")

   




def takeCommand():
    # it takes microphone input from the user
    
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio= r.listen(source)
 


    try:
         print("recognizing....")
         query = r.recognize_google(audio, language='en-in')
         speak(f"user said: {query}\n")
         print(f"user said: {query}\n")



    except Exception as e:
        print("say that again please...")
        return "none"   

    return query






if __name__== "__main__":
    wishMe()
while True:   
    query=takeCommand().lower()

    #logic for task
    if 'wikipedia' in query:
        speak("searching wikipedia...")
        query= query.replace("wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak("Acording to wikipedia")
        print(results)
        speak(results)

    elif'name' in query:
        speak("as i am an generative bot i dont have name")
    
        
     
    
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    
    elif 'open google' in query:
        speak("just a second")
        webbrowser.open("google.com")
    
    elif 'open my webpage' in query:
        speak("just a seconds")
        webbrowser.open("https://jagtapom.netlify.app/")
        
    elif 'what can you do' in query:
        speak("i can do lots of things like opening app,browser,i can play music ,i can do temperature forcast etc")
     

    elif 'open instagram' in query:
        speak("just a seconds")
        webbrowser.open("instagram.com")
    
    elif 'open mail' in query:
        speak("just a second")
        webbrowser.open("mail.google.com")
        


    elif "the time" in query:
        strtime= datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir,the time is {strtime}")
        print(strtime)

    elif "open vs code" in query:
        speak("just a seconds")
        codePath= "parth"
        os.startfile(codePath)

 
   
   
    elif "open browser" in query:
        codepath= "path"
        os.startfile(codepath)

    elif "temperature" in query:
        
     search= "temperature in pune"
     url=f"https://www.google.com/search?q={search}"
     rk= requests.get(url)
     data= BeautifulSoup(rk.text,"html.parser")
     temp= data.find("div",class_="BNeawe").text
     speak(f"current {search} is {temp}")
     print("current temperature is",temp)
 

  
    




    

    
