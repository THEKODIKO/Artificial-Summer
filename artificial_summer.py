from speak import speak
from ai import ai_respond
import speech_recognition as sr

# Create a Recognizer instance
recognizer = sr.Recognizer()

def recognize_speech():

    text= None

    # Capture audio input from the microphone
    with sr.Microphone() as source:
        print("Speak something...")
        audio_data = recognizer.listen(source)

    # Perform speech recognition using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand audio.")
    except sr.RequestError as e:
        print("Error: Could not request results from Google Speech Recognition service;")
    
    return "Could not hear what the user said" if not text else text
