# Personal Assistant

_In this project we have created a personal assistant which will respond you based on your request_

** I have created two program for personal assistance one will take text as an Input and another will take speech as an input**

## personal_assistant:
* I have created a simple assistant system in which we provide text as an input to the progarm.
* We imported following packages for our program to execute properly
    * `pyttsx3` This package is used for converting text to speech
    * `datetime` This package is used to get the current time
    * `wikipedia` this package is used to get the information from wikipedia
* We have crated a variable to initiate the text to speech process
* We created a function to read the input
* We created a time function to get current time
* Finally we created a function which will read the input that will be search in wikipedia and we will get the results in form of speech.

## pa_with_voice_command:
* This is a next step for our personal assistant which will take the input in speech convert it to text process it and again convert the output into speech
* for this we have imported all packages from our previous program and added one more package to it
    * `speech_recognition` for reading the speech input and process it.
* Initial steps are same for both program i.e initialisation and time function.
* Then we have created a `takeCommand()` function which will process our speech input and give us result in speech as well

**Detail about packages used.**
1. [pyttsx3](https://pypi.org/project/pyttsx3/)
2. [speech_recognition](https://pypi.org/project/SpeechRecognition/1.2.3/)
3. [wikipedia](https://pypi.org/project/wikipedia/)
4. [datetime](https://docs.python.org/3/library/datetime.html)

_To run speech recognition package we need to install pyaudio to use inbuilt audio_
_But the python version after 3.5 does not support the pyaudio for that we have to perform one of the following action_
    1. Try to downgrade your python version to 3.5 or less
    2. Install visual studio with Microsoft Visual C++ 14.0 
    3. Download and install `Unofficial Windows Binaries for Python Extension Packages` from `https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio` and follow the steps
        1. Find your Python version by python --version mine is 3.7.6 for example.
        2. Find the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio), for example mine is PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl, and download it.
        3. Save the downloaded file into python package path.
        4. Install the `.whl` file with pip for example in my case:
            `pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl`
        5. Install `pipwin` : `pip install pipwin` then install pyaudio using pipwin i.e. `pipwin install pyaudio`

**Credits for pyaudio Solutions - [Stackoverflow](https://stackoverflow.com/)**