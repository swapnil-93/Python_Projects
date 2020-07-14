import win32com.client as wincl     # import to automate the windows task

text = input("Enter your text: ")

speak = wincl.Dispatch("SAPI.SpVoice")      # Created a variable for voice

speak.Speak(text)      # enter the text to be converted