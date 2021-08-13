# import libraries
import cv2 as cv

# load the face detection classifier
facecc = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# create a function to detect faces
def detect():
    # capture the video from the webcam
    cap = cv.VideoCapture(0)

    while True:
        # reading and storing the capture in img
        _, img = cap.read()

        # convert the img to grayscale
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # detecting the faces (grayimg, scalefactor, no. of faces to detect)
        face = facecc.detectMultiScale(gray, 1.1, 4)

        # get the coordinates of the faces and draw rectangle around the faces
        for (x, y, w, h) in face:
            cv.rectangle(img, (x, y), ((x+w), (y+h)), (0, 255, 0), 2)
            cv.imshow('Face detection', img)

        # close the window on press of esc key
        if cv.waitKey(1) == 27:
            break

    # release the camera resource
    cap.release()

# run the function
detect()