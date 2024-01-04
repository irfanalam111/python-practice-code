import pyttsx3
name=input("enter your name")
engine=pyttsx3.init()
engine.say(f"hello {name}")
engine.runAndWait()