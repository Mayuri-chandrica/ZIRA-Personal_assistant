import subprocess
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import time
import wolframalpha

print("Loading your AI personal assistance - ZIRA :")

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')  # getting details of current voice

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        print("Good morning")
        speak("good morning")

    elif 12 <= hour < 18:
        print("Good afternoon")
        speak("good afternoon")

    else:
        print("Good evening")
        speak("good evening")




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)
        print("Say that again please...")  
        return "None"  
    return query


if __name__ == "__main__":
    wishme()
    while True:
        print("please tell me , how may i help you ")
        speak("please tell me , how may i help you ")

        query = takeCommand().lower()
        if query==0:
            continue

        if "good bye" in query or "ok bye" in query or "stop" in query:
            print('your personal assistant zira is shutting down,Good bye')
            speak('your personal assistant zira is shutting down,Good bye')
            break  

        if 'who are you' in query or 'what can you do' in query:
            print('I am zira, your persoanl assistant. I am programmed to do minor tasks like opening youtube,google,chrome,gmail and stackoverflow,visual studio code,predict time,take a photo,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
            speak('I am zira , your persoanl assistant. I am programmed to do minor tasks like opening youtube,google,chrome,gmail and stackoverflow,visual studio code,predict time,search wikipedia,predict weather in different cities , get top headline news from times of india and you can ask me computational or geographical questions too!')
        
        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            print("I was built by Mayuri chandrika")
            speak("I was built by Mayuri chandrika")
            
            
        elif "wikipedia" in query:  
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            print(query)
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            time.sleep(5)

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India,Happy reading')
            time.sleep(5)


        elif "open google" in query:
            webbrowser.open("google.com")
            time.sleep(5)

        elif 'search'  in query:
            query = query.replace("search", "")
            webbrowser.open_new_tab(query)
            time.sleep(5)


        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            time.sleep(5)


        elif "play music" in query:
            music_dic="D:\\music\\my fav song"
            songs = os.listdir(music_dic)
            print(songs)
            os.startfile(os.path.join(music_dic,songs[0]))

        
        elif "the time" in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"mam the time is {strtime}")

        elif "open chrome" in query:
            chromepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromepath)

        
        elif 'open code' in query:
            codepath = "C:\\Users\\sagar\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
            os.startfile(codepath)
        

        elif "email" in query:
            try:
                speak("what should i say ?")
                content = takeCommand()
                to = "chandrikamayuri@gmail.com"
                sendEmail(to,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry mam , i am not able to send email right now ")

        elif 'ask' in query:
            speak('I can answer to computational and geographical questions and what question do you want to ask now')
            question=takeCommand()
            app_id="7K9LTX-YP5VU5G5KL"
            client = wolframalpha.Client('7K9LTX-YP5VU5G5KL')
            res = client.query(question)
            answer = next(res.results).text
            print(question)
            print(answer)
            speak(answer)
            
        

        
        elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])



