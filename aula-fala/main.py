import pyttsx3

#iniciativa motor de fala
engine=pyttsx3.init()

engine.setProperty("rate", 150)
engine.setProperty("volume", 10000000)

voices=engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def falar(texto):
    engine.say(texto)
    engine.runAndWait()

texto=input("digite alguma coisa: ")

falar(texto)