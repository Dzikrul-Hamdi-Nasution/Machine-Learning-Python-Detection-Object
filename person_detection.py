import numpy as np 
import cv2 
import time 

# Load the cascade
face_cascade = cv2.CascadeClassifier("fullbody.xml")
# To capture video from webcam.
cap = cv2.VideoCapture(0)
cv2.resolution = (640, 480)
cv2.framerate = 32
prev_frame_time = 0
new_frame_time = 0
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

out = cv2.VideoWriter(
    'output.avi',
    cv2.VideoWriter_fourcc(*'MJPG'),
    15.,
    (640,480))

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX 
	# time when we finish processing for this frame 

	 

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
       
        
    # Display
    new_frame_time = time.time() 
    fps = 1/(new_frame_time-prev_frame_time) 
    prev_frame_time = new_frame_time 
    fps = int(fps) 
    fps = str(fps)
    cv2.putText(img, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA) 
    out.write(img.astype('uint8'))
    cv2.imshow("img", img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break
# Release the VideoCapture object

cap.release()
out.release()