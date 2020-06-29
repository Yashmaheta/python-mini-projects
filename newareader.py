import requests
import json
import os
import datetime
import webbrowser
import wikipedia
import speech_recognition as sr
from win32com.client import Dispatch
def speak(str):

    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
def wishme():
    #the function for greetings
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Tech . Tell me how may i help U. ")

def takecommand():
    # the main function and it wiil recigize all the words one says actually we can set all the command that we want to get result of.
    r = sr.Recognizer() # it will recognize the words..
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
        # print(audio)  #uncooment to see the words u say


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print("Say that again please....")
        return "None"
    return query


if __name__ == '__main__':
    print("say hello.")
    wishme()
    print("start")
    query = takecommand().lower()
    if 'read news' in query:
        speak("news for today")
        url="https://newsapi.org/v2/top-headlines?country=in&apiKey=c32abd35466f409c859b365d44ff5fa0"
        burl="https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c32abd35466f409c859b365d44ff5fa0"
        enterurl="https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c32abd35466f409c859b365d44ff5fa0"
        healthurl="https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c32abd35466f409c859b365d44ff5fa0"
        scienceurl="https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c32abd35466f409c859b365d44ff5fa0"
        sporturl="https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c32abd35466f409c859b365d44ff5fa0"
        techurl="https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c32abd35466f409c859b365d44ff5fa0"
        print("news catagory:\n 1.BUSSINESS\n 2.ENTERTAINMENT\n 3.HEALTH\n 4.SCIENCE\n 5.SPORTS\n 6.TECHNOLOGY"  )
        speak("Well hello there hope you having a good day if you are not affected to corona ..just kiding")
        speak("I am here to read a news for you")
        speak("say which kind of news you want to hear  BUSSINESS  \n  ENTERTAINMENT\n   HEALTH\n  SCIENCE\n  SPORTS\n  TECHNOLOGY"  )
        a = takecommand().lower()
        if a=="BUSSINESS":
            Bnews=requests.get(burl).text
            Bnews_dict=json.loads(Bnews)
            print(Bnews_dict["articles"])
            arts=Bnews_dict['articles']
            speak("bussiness news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        elif a=="ENTERTAINMENT":
            enews=requests.get(enterurl).text
            enews_dict=json.loads(enews)
            print(enews_dict["articles"])
            arts=enews_dict['articles']
            speak("entertainment news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        elif a=="HEALTH":
            hnews=requests.get(healthurl).text
            hnews_dict=json.loads(hnews)
            print(hnews_dict["articles"])
            arts=hnews_dict['articles']
            speak("health news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        elif a=="SCIENCE":
            Snews=requests.get(scienceurl).text
            Snews_dict=json.loads(Snews)
            print(Snews_dict["articles"])
            arts=Snews_dict['articles']
            speak("science news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        elif a=="SPORTS":

            snews=requests.get(sporturl).text
            snews_dict=json.loads(snews)
            print(snews_dict["articles"])
            arts=snews_dict['articles']
            speak("sport news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        elif a=="TECHNOLOGY":

            tnews=requests.get(techurl).text
            tnews_dict=json.loads(tnews)
            print(tnews_dict["articles"])
            arts=tnews_dict['articles']
            speak("tech news")
            for article in arts:
                speak(article['title'])
                speak("Moving on the next news.. listen carefully")
        
        
    #logic for executing tasks based on query
    elif 'wikipedia' in query:
        speak('Searching Wikipedia.....')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        speak("According to Wikipedia")
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'E:\\MUSIC'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[0]))

    elif 'the time' in query:
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir the time is {strtime}")

    elif 'open code' in query:
        #here when ever u print any path make sure that u put extra'\' in it..it will help in accurance or something like that ...it is important but i forgot why it is important..
        code_path = "C:\\Users\\YASH MAHETA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
        os.startfile(code_path)

    else:
        exit()
        