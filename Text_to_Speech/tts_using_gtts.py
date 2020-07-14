from gtts import gTTS   # import gTTS library
import os       # import os Module

# give input
text = input("Enter text: ")
tts = gTTS(text= text, lang='en')   # Create a variable which takes text and language as parameter
tts.save("good.mp3")    # Save the text into a mp3 format
os.system("good.mp3")   # run the file using OS module