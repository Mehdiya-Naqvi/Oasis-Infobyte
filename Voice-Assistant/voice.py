import speech_recognition as sr
import pyttsx3
import datetime
# import distutils

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            print("Sorry, there was an issue with the request.")
            return ""

def process_command(command):
    if 'hello' in command:
        speak("Hello! How can I help you today?")
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    elif 'stop' in command:
        speak("Goodbye!")
        return False
    elif 'say my name' in command:
        speak("Mehdiya Naqvi")
    
    else:
        speak("Sorry, I didn't catch that.")
    return True

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        command = listen()
        if not process_command(command):
            break

if __name__ == "__main__":
    main()
