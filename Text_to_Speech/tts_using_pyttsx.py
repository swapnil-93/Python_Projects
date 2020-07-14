import pyttsx3      # import the text to speech library

# Simple Text to Speech
x = pyttsx3.init()     # Initialise the library
x.say("Read the text")     # provide the text to be read
x.runAndWait()             # run the text

# Taking Input from User
text = input(" Enter the text You want to listen: ")
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()


# Opening a text file and Reading
with open("text.txt", "r") as text:

    engine = pyttsx3.init()
    engine.say(text.read())
    engine.runAndWait()

