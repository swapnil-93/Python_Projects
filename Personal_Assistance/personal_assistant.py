import pyttsx3      # for text to speech
import datetime    # to get current time
import wikipedia    # to access wikipedia

engine = pyttsx3.init()     # initialize the text to speech

# Create a function to convert text to speech
def speak(audio):
    engine.say(audio)   # pass the parameter for converting text to speech
    engine.runAndWait() # run and wait for response

#speak("Hello")

# Create a function for getting current time
def time():

    Time = datetime.datetime.now().strftime("%I:%M:%S")     # Create a variable which will store current time  "%H:%M:%S" - 24hr format "%I:%M:%S" - 12 hr format
    print(Time)
    speak(f'The current time is {Time}')

# Create a function for fetching information from wikipedia
def wiki():

    results = wikipedia.summary(query, sentences=2)
    #results = wikipedia.summary(query)
    speak("According to Wikipedia")
    print(results)
    speak(results)

# main progarm
if __name__ == '__main__':
    print("Welcome to Our Personal Assistant Service")
    speak("Welcome to Our Personal Assistant Service")
    time()      # call time function
    speak("Please Enter What do You want to Search for: ")
    query = input("Enter: ")        # enter the input
    speak("You have Search for")
    speak(query)
    wiki()      # call the wikipedia
    print("Thank you for using our personal assistant")
    speak("Thank you for using our personal assistant")
