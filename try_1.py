import cv2 

path = '/home/jinesh/HACKATHON/output_frames/13.jpg'
vidObj = cv2.VideoCapture("/home/jinesh/HACKATHON/input_videos/1.mp4")
image = cv2.imread(path) 

font = cv2.FONT_HERSHEY_SIMPLEX 
org = (1200, 2200) 
fontScale = 10
color = (0, 0, 255) 
thickness = 20

image = cv2.putText(image, 'Detected!!', org, font, 
				fontScale, color, thickness, cv2.LINE_AA) 

image = cv2.resize(image,(848,480))		
cv2.imwrite("/home/jinesh/HACKATHON/try.jpg", image) 


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (848,480))

success, vid_image = vidObj.read()    
frame_number = 0

while success :
    frame_number += 1
    success, vid_image = vidObj.read()
    if frame_number == 3:  # if frame is the third frame than replace it with blank drame
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
      vid_image = image
      out.write(vid_image)

      success, vid_image = vidObj.read()
    
    out.write(vid_image)


out.write(vid_image)
vidObj.release()
out.release()