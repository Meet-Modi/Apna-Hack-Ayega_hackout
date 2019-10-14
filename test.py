import numpy as np
import cv2

cap = cv2.VideoCapture("/home/jinesh/HACKATHON/input_videos/1.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

frame_number = -1

while(True):
    frame_number += 1
    ret, frame = cap.read()
    if frame_number == 3:  # if frame is the third frame than replace it with blank drame
        frame = np.zeros_like(frame)
        #change_frame_with = np.zeros_like(frame)
        #frame = change_frame_with
    out.write(frame)

    
cap.release()
out.release()
exit()