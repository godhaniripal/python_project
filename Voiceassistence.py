import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()  # Fix typo: it should be sr.Recognizer() instead of sr.recognizers
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening>>>>')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
            return command
    except sr.UnknownValueError:
        return ""  # Handle UnknownValueError by returning an empty string
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""  # Handle RequestError by returning an empty string


def run_voice_assistance():
    command = take_command()
    if 'hello' in command:
        speak("hello bro what's up")


speak("hello, I am your voice assistant")

while True:
    run_voice_assistance()
