import cv2

class cam:
	def declareCam(self, cameraID):
		c = cv2.VideoCapture(cameraID)
		return c
	def getFrame(self, c):
		ret, frame = c.read()
		return frame