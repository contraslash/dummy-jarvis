import speech_recognition
import pyespeak


speech_engine = pyespeak.ESpeak()


def speak(text):
    speech_engine.say(text)


print("starting recognizer")
recognizer = speech_recognition.Recognizer()
print("recognizer started")


def listen():
    with speech_recognition.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_sphinx(audio)
    except speech_recognition.UnknownValueError:
        print("Could not understand audio")
    except speech_recognition.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

speak("Say something!")
speak("I heard you say " + listen())
