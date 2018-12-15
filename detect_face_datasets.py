
import cv2

from os import listdir
import time

def cropImage(img, box):
	[p, q, r, s]= box

	write_img_color= img[q:q+ s, p:p+ r]
	saveCropped(write_img_color, name)


def saveCropped(img, name):
	cv2.imwrite(output_path+ name+ ".jpg", img)

if __name__== "__main__":

	input_path= "./input_images/"
	output_path= "./output_images/"


	frontal_face= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
	input_names= listdir("./input_images")

	print("Starting to detect faces and save the cropped images to output file...")
	sttime= time.clock()
	i= 1
	for name in input_names:
		print(input_path+name)
		color_img= cv2.imread(input_path+ name)

		gray_img= cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)


		bBoxes= frontal_face.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
		#print(bBoxes)

		for box in bBoxes:

			cropImage(color_img, box)
			i+= 1

	print("Completed the task in %.2f Secs." % (time.clock()- sttime))
