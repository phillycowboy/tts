import pyttsx3 

engine = pyttsx3.init()
name = input("What is your name? ")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[7].id)
engine.setProperty("rate", 178)
engine.say(f"Hello, {name}, I'm so sorry that you had a rough day, fuck them shitty parents!")
engine.runAndWait()
engine.stop()

# run python3 first-tts.py
# then type in name 