# Speech To Text

_We have created two program one for printing audio into text and another to save that text into a file._

* To do conversion of speech to text we have used `speech_recognition packge`.
* This package will listen the audio and convert it to text.

**Detail about package**
[speech_recognition](https://pypi.org/project/SpeechRecognition/1.2.3/)

To run speech recognition package we need to install pyaudio to use inbuilt audio_
_But the python version after 3.5 does not support the pyaudio for that we have to perform one of the following action_
    1. Try to downgrade your python version to 3.5 or less
    2. Install visual studio with Microsoft Visual C++ 14.0 
    3. Download and install `Unofficial Windows Binaries for Python Extension Packages` from `https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio` and follow the steps
        1. Find your Python version by python --version mine is 3.7.6 for example.
        2. Find the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio), for example mine is PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl, and download it.
        3. Save the downloaded file into python package path.
        4. Install the `.whl` file with pip for example in my case:
            `pip install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl`
    4. Install `pipwin` : `pip install pipwin` then install pyaudio using pipwin i.e. `pipwin install pyaudio`
    5. pip3 install pyaudio
    
**Credits for pyaudio Solutions - [Stackoverflow](https://stackoverflow.com/)**


