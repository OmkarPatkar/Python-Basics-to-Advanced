import cv2 as cv

img = cv.VideoCapture(0)
result = True

while(result):
    _, frame = img.read()
    cv.imwrite("test.jpg", frame)
    result = False
    print("Image Captured")

img.release()

