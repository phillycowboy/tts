import pyttsx3 

engine = pyttsx3.init()
name = input("What is your name? ")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[7].id)
engine.setProperty("rate", 178)
engine.say(f"Hello, {name}, I hope you feel better!")
engine.runAndWait()
engine.stop()