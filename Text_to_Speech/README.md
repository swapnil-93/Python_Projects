# Text to Speech

_In this project we are converting the text to speech using different libraries_

1. tts_using_pyttsx :
    * This project uses `pyttsx3` library for running the Text-to-Speech.
    * We have to install the library using `pip install pyttsx3`
    * After that we have to install the support package for that library `pip install pywin32`
    * If you face issue in running the file then try to downgrade the version of the `pyttsx3` library to `verison 2.71` using `pip install pyttsx3==2.71`
    * For more detail about `pyttsx3` library do visit:  [Docs](https://pypi.org/project/pyttsx3/)
   
2. tts_using_gtts :
    * This is another project which converts text to speech.
    * For this we have to install `gTTS` library using `pip install gTTS`.
    * This module read the text and save it to an audible format.
    * To run the audio we imported os module.
    * For more detail on `gTTS` library do visit : [Docs](https://pypi.org/project/gTTS/)
 
3. tts_using_mse:
    * This project is created using Microsoft Speech Engine
    * We have to import `win32com.clinet` to automate the windows tasks.
    * provide the text to be converted