import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui

def draw_roi(img, vertices):
	mask = np.zeros_like(img)
	mask = cv2.fillPoly(mask, vertices, 255)

	masked = cv2.bitwise_and(img, mask)
	return masked