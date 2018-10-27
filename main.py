from cam import cam
from TargetMaker import TargetMaker
from TargetProcessor import TargetProcessor
import cv2

maker = TargetMaker()
processor = TargetProcessor()
cam = cam()
c = cam.declareCam(0)

while (cv2.waitKey(10) != 27):
	frame = cam.getFrame(c)	
	threshedImg, hsv = maker.thresher(frame)
	width, height, xOffset, yOffset = maker.contour(threshedImg, frame, hsv)
	distance, azimuth, altitude = processor.imageProcess(width, height, xOffset, yOffset)
	print(distance)
	print(azimuth)
	print(altitude)