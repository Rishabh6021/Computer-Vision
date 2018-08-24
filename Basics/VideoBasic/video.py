import cv2

cam = cv2.VideoCapture(1)  #Captures webcam for capturing video
cam.isOpened()             #Returns true if cap have initialized capture
print(cam.get(4))          #Returns frame height ,here 4 is propid which denotes property of video

while (True):
	tf,frame=cam.read()                           #Capture frame by frame. cam.read() returns a bool True ,if frame is read correctly
	print(tf)
	#frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #Converts each frame to RGB to grayscale
	cv2.imshow('SingleFrame',frame)
	key =cv2.waitKey(1)                           #Will display the window infinitely until any keypress (it is suitable for image display)
	if key == 27:                                 # If key =27 i.e ESC key then loop breaks
		break
	elif key == ord('x'):                         #if key pressed is 'X'
	    print("You have pressed the letter X")	

cam.release()                                    #Closes video file or capturing device,deallocates memory and clears *capture pointer.
cv2.destroyAllWindows()
