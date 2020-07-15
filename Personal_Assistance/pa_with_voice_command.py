# For More information read the README.md file

import datetime     # to get current time
import speech_recognition       # for speech recognition
import pyttsx3          # to convert text into speech
import wikipedia        # to access wikipedia


engine = pyttsx3.init()     # initialize the text to speech

# Create a function to convert text to speech
def speak(audio):
    engine.say(audio)       # pass the parameter for converting text to speech
    engine.runAndWait()     # run and wait for response

print ("#### Welcome to Our Personal Assistance Service #####\n")
speak("Welcome to Our Personal Assistance Service")

# Create a function for getting current time
def Time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")         # Create a variable which will store current time  "%H:%M:%S" - 24hr format "%I:%M:%S" - 12 hr format
    print(Time)
    speak(f"The current time is {Time}")

# Create a function to get the input through speech
def takeCommand():
    try:
        r = speech_recognition.Recognizer()     # to recognize speech
        with speech_recognition.Microphone() as source:     # use default microphone as the audio source
            print("I'm Listening to You, Please Speak...")
            speak("I'm Listening to You, Please Speak...")

            r.pause_threshold = 1       # take a pause for 1 sec.
            audio = r.listen(source)            # listen for the first phrase and extract it into audio data

            print("Recognising what you have said...")
            speak("Recognising what you have said...")

            query = r.recognize_google(audio, language="en-In")  # using Google speech recognition system
            print(f"You said :{query}")
            speak(f"You said :{query}")
            print(f'Searching for {query} in Wikipedia')
            speak(f'Searching for {query} in Wikipedia')

            results = wikipedia.summary(query,sentences=2)  # using wikipedia to get the information upto 2 sentences

            print(f"According to Wikipedia\n {results}")
            speak(f"According to Wikipedia{results}")

            print("Do you want to try again ? y/n")
            speak("Do you want to try again ?")
            speak(" Say yes to continue or No to Stop")

            print("Listening")
            speak("Listening")
            r.pause_threshold = 1
            audio = r.listen(source)        # To try again
            query = r.recognize_google(audio, language="en-In")

            print(f"You said :{query}")
            speak(f"You said :{query}")

            if query == "yes" or query == "Yes" or query == "YES":      # if you said yes then program will repeat
                takeCommand()
            elif query == "No" or query == "no" or query == "NO":          # if you said no program will exit
                print("Thank You for using Our Personal Assistant")
                speak("Thank You for using Our Personal Assistant")
                exit()

    # if you got an error while running the program
    except Exception as e:
        print(e)
        print ("Please Speak again....")
        speak("Please Speak again....")
        takeCommand()
        return "None"
    return query

# Main Program:

if __name__ == '__main__':
    Time()
    takeCommand()
