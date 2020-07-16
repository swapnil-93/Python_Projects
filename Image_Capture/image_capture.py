import cv2
import time
img = cv2.VideoCapture(0, cv2.CAP_DSHOW)

img_name = time.strftime("%Y%m%d-%H%M%S")   # create a variable to generate a timestamp
img_name = "/Capture/IMG_"+img_name+'.png'       # Create a path where we want to save the the image

ret, frame = img.read()             # ret takes the value of image capture and frame store the image
cv2.imwrite(img_name, frame)        # Write name to the captured frame
print("Image Captured....")

img.release()           # release the capture window
cv2.destroyAllWindows()     # close the camera and close all open window