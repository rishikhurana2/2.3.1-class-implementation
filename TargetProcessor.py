import cv2
import numpy as np
from TargetMaker import TargetMaker

class TargetProcessor:
	def imageProcess(self, width, height, xOffset, yOffset):
		rectHeight = 10
		rectWidth = 20
		focalLength = 720
		dist = (focalLength * rectWidth)/width
		azi = np.arctan(xOffset/focalLength)*180/np.pi
		alt = np.arctan(yOffset/focalLength)*180/np.pi
		return dist,azi,alt
