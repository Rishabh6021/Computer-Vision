import cv2              #import computer vision library cv2 

img=cv2.imread('parrot.jpg',0) #Reads/Loads the image in grayscale mode and stores in img
print(img)

if img is None :                # If image isn't found ,it prints following msg
	print("Object not found")

else:
	cv2.imshow('Image',img)       #Displays image in a window
	cv2.imwrite('bananasGray.jpg',img) # Saves the grayscale image in current directory
	cv2.waitKey()                # Holds on the image window
	cv2.destroyAllWindows()       #Destroys all the windows we created