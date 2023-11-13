import webbrowser
import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()

maquina = pyttsx3.init()

def hablar():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='ES')

    print(f'has dicho: {text}')
    return text.lower()

if 'amazon' in hablar():
    maquina.say('Que quieres comprar en amazon')
    maquina.runAndWait()
    text = hablar()
    webbrowser.open(f'https://www.amazon.es/{text}')