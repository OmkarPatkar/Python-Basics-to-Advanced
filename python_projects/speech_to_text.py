# import libraries
import pyttsx3
import speech_recognition as sr

def get():
    # define recognizer function
    r = sr.Recognizer()
    # define microphone function
    with sr.Microphone() as source:
        print('Say Something...')
        # collect data from microphone
        audio = r.listen(source)
        print('Done Listening!')

    try:
        # recognize the speech and convert
        text = r.recognize_google(audio)
        print('You said ' + text)
    except Exception as e:
        print(e)

get()