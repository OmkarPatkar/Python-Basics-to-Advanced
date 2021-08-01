import pyttsx3

data = input("Enter something you want to convert to speech: ")
engine = pyttsx3.init()
engine.say(data)
engine.runAndWait()