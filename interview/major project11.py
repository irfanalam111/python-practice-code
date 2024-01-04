import os
import pyttsx3
import calendar
import speech_recognition as sr
import datetime
import wikipedia as wp
import webbrowser as wb
import pywhatkit as pw

engine = pyttsx3.init()

def speak(audio) : 
    voices = engine.getProperty('voices')       
    engine.setProperty('voice', voices[1].id)   
    rate = engine.getProperty('rate')                 
    engine.setProperty('rate', 160)
    volume = engine.getProperty('volume')   
    engine.setProperty('volume',1)
    engine.say(audio)
    engine.runAndWait()
def takeCommand() :
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print("You just said : ",query)
        
    except Exception as e:
        print(e)
        print("Please say that again!")
        return "None"
    
    return query
def _calender():
    try:
        speak("which years")
        cld=int(takeCommand())
        while True:
            if cld<=0:
                print("try again only int is vailid")
                speak("try again only int is vailid")
            ab=calendar.calendar(cld)
            print(f"calender is {ab}")
            break
    except ValueError:
        print("only inter is valid")
    except TypeError:
        print("please enter valid input")
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("goog morning sir!")
    elif hour >= 12 and hour < 18:
        speak("good afternoon sir!")
    else:
        speak("good evining sir!")
    speak("i am start for you . please tell me how may i help you")
def time() :
    Time = datetime.datetime.now().strftime("%I:%M")
    speak("The current time is")
    speak(Time)
def date() :
    Year = datetime.datetime.now().year
    Month = datetime.datetime.now().month
    Day = datetime.datetime.now().day
    speak("Today's date is")
    speak(Day)
    speak(Month)
    speak(Year)
def wikiSearch():
    try:
        speak("Please Enter the topic")
        topic = takeCommand()
        result = wp.summary(topic)
        print(result)
        speak("Your result is ready,displayed on your screen")
        speak("should i read it for you")
        speak("Say yes or no")
        inp = takeCommand()
        if "yes" in inp:
            speak(result)
        elif "no" in inp:
            speak("okey Sir")
        else:
            speak("Please Try Again !")
    except OSError:
        print("something is wrong")
        speak("something is wrong try again")
def googleSearch() :
    try:

        speak("What should i search for you?")
        inp = takeCommand()
        if inp == 'None':
            googleSearch()
        else:

            speak("Opening your browser")

            search = query.replace('search', ' ')

            pw.search(search)

    except OSError:
        print("something is wrong try again")
        speak("something is wrong try again")
    except ValueError:
        print("speak again i am not getting!")
        speak("speak again i am not getting!")
def playSong() :
    try:
        songs_dir = "C:\\Users\\\HP\\Desktop\\music"
        songs = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir, songs[1]))
    except Exception:
        song=query.replace('play......','')
        speak('play'+song)
        pw.playonyt(song)
def takeNote() :
    speak("I am taking note in a new file. please start speaking.")
    file = open("F:\BOOKS","w")
    test = True
    while test == True :
        inp = takeCommand()
        if "stop" in inp :
            speak("Stopping my note taking command")
            file.close()
            test = False
        else :
            file.write("{} \n".format(inp))
            test = True


if __name__ == "__main__":
    wishme()
    while True :
        query = takeCommand().lower()
    
        if "date" in query :
            date()
        elif "time" in query :
            time()
        elif "wikipedia" in query :
            wikiSearch()
        elif "search" or "open" in query :
            googleSearch()
        elif "song" or "music" in query :
            playSong()
        elif "notes" in query : 
            takeNote()
        elif "offline" in query :
            speak("Going Offline. Its my pleasure to work for you.")
            exit()