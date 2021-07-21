# Important imports
import speech_recognition as speech
import pyttsx3
import threading
import time


class Eis():

    def __init__(self):
        self.word = ''
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)
        self.Dict = {'Greetings': ['hello', 'hi']}

    def listen(self):
        while self.word != 'exit':
            sound = speech.Recognizer()
            with speech.Microphone() as audio:
                said = sound.listen(audio)
            try:
                self.word = sound.recognize_google(said, language='en-IN')
                self.respond()
            except LookupError:
                print("Could not understand. Please repeat.")

    def respond(self):
        if(self.word == 'hello'):
            self.speak('Hello Endri')
        elif(self.word == 'exit'):
            self.speak('Goodbye Endri')

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()


app = Eis()
app.listen()
