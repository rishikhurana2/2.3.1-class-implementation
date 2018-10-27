import cv2
import numpy as np

class TargetMaker:
	def thresher(self, image): 
		img = image
		image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		THRESHOLD_MIN = np.array([0,0,0], np.uint8)
		THRESHOLD_MAX = np.array([250,0,250], np.uint8)
		img = cv2.inRange(image, THRESHOLD_MIN, THRESHOLD_MAX)
		cv2.imshow("Thresholded Image", img)
		hsv = image
		return img, hsv
	def contour(self, threshedImage, originalImg, hsvImg):
		minX = 10000
		minY = 10000
		maxX = 0
		maxY = 0
		count = -1
		image, contours, hierarchy = cv2.findContours(threshedImage, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		for cont in contours:
			count = count + 1
			approx = cv2.approxPolyDP(cont, 0.1*cv2.arcLength(cont, True), True)
			area = cv2.contourArea(approx)
			if (area > 300):
				cv2.drawContours(originalImg, contours, count, (255,10,255), 5)
				for i in approx:
					if i[0][0] < minX:
						minX = i[0][0]
					if i[0][0] > maxX:
						maxX = i[0][0]
					if i[0][1] < minY:
						minY = i[0][1]
					if i[0][1] > maxY:
						maxY = i[0][1]
		width = maxX - minX
		height = maxY - minY
		imgCenterX = (maxX + minX)/2
		imgCenterY = (maxY + minY)/2
		xOffset = hsvImg.shape[0]-imgCenterX
		yOffset = hsvImg.shape[1]-imgCenterY
		cv2.imshow("contour", originalImg)
		return width, height, xOffset, yOffset