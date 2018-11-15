import aiml
import os
import time, sys
#from gtts import gTTS
#from pygame import mixer
import pyttsx
import warnings


engine = pyttsx.init()
engine.setProperty('rate', 150)

mode = "text"
if len(sys.argv) > 1:
    if sys.argv[1] == "--voice" or sys.argv[1] == "voice":
        try:
            import speech_recognition as sr
            mode = "voice"
        except ImportError:
            print("\nInstall SpeechRecognition to use this feature.\nStarting text mode\n")

terminate = ['bye','buy','shutdown','exit','quit','gotosleep','goodbye']
# def speak(eva_speech):
#   tts = gTTS(text=eva_speech, lang='en')
#   tts.save('eva_speech.mp3')
#   mixer.init()
#   mixer.music.load('eva_speech.mp3')
#   mixer.music.play()
#   while mixer.music.get_busy():
#       time.sleep(1)

def offline_speak(eva_speech):
    engine.say(eva_speech)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Talk to Eva: ")
        audio = r.listen(source)
    try:
        print r.recognize_google(audio)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        offline_speak("I couldn't understand what you said! Would you like to repeat?")
        return(listen())
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    #kernel.saveBrain("bot_brain.brn")

# kernel now ready for use
while True:
    if mode == "voice":
        response = listen()
    else:
        response = raw_input("Talk to Eva : ")
    if response.lower().replace(" ","") in terminate:
        break
    eva_speech = kernel.respond(response)
    print "Eva: " + eva_speech
    offline_speak(eva_speech)
    