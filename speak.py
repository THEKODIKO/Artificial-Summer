import pyttsx3


engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

if __name__=="__main__":
    speak("Hi I'm Connor, The android sent by Cyberlife.")