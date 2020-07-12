import time     # import time for delay and timestamp
import pyautogui    # import pyautogui for capturing screenshot
import tkinter as tk    # import tkinter for creating gui

# define a function to take a screenshot
def screen_shot():
    img_name = time.strftime("%Y%m%d-%H%M%S")   # create a variable to generate a timestamp
    img_name = "C:/Users/Tanu-PC/Python_Project/Screen_Shot_Application/screens/IMG_"+img_name+'.png'       # Create a path whare we want to save the screenshot
    #time.sleep(5)     # create a delay of 5 seconds for without button
    img = pyautogui.screenshot(img_name)        # use pyautogui module for taking screenshot
    img.show()      #to show the screenshot


root = tk.Tk()          # create a variable for tkinter gui
frame = tk.Frame(root)      # Create a frame
frame.pack()            # pack the frame around buttons

# Create a button to take a screenshot
button1 = tk.Button(frame, text = "Take Screenshot", command = screen_shot)
# pack the button to left
button1.pack(side = tk.LEFT)
# Create a exit button

button2 = tk.Button(frame, text = "Exit", command = quit)
# pack the button to right
button2.pack(side = tk.RIGHT)

root.mainloop()