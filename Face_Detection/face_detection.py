import cv2      # import OpenCV Library

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")         # Pass the haar cascade classifier feature for detection

# Create a function for Face detection
def detect():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)        # Create a camera variable

    while True:
        _,img = cap.read()          # Read each frame from camera
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)        # convert the frame from BGR(Blue, Green, Red to Greyscale)
        face = face_cascade.detectMultiScale(grey, 1.1, 4)  # Create a multiple face detection variable (image, scalefactor, minimum neighbors )

        # Draw a rectangle around the faces
        for (x, y, w, h) in face:
            cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)     # green rectangle

        # Display the resulting frame
        cv2.imshow("Face Detection", img)

        # Exit by pressing q
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()

detect()