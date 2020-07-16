import speech_recognition        # for speech recognition

def get():
    r = speech_recognition.Recognizer()     # to recognize speech
    with speech_recognition.Microphone() as source:     # use default microphone as the audio source
        print("Say Something....")
        audio = r.listen(source)            # listen for the first phrase and extract it into audio data
        print("Done!!")

    try:
        text = r.recognize_google(audio)        # using Google speech recognition system
        print('You said ' + text)
    except Exception as e:
        print(e)

# Call our Function
get()