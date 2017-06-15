import logging
import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
import time
import matplotlib.pyplot as plt

from grab_screen import grab_screen
from processing import process_image

for i in xrange(4,0,-1):
    time.sleep(1)
    print i

last_time = time.time()
while 1:
	screen = np.array(ImageGrab.grab(bbox=(320, 240, 940, 700)))

	cv2.imshow("Screen", screen)

	print ('frame took {} seconds'.format(time.time() - last_time))
	last_time = time.time()

	new_screen, original = process_image(screen)

	cv2.imshow("Canny Edges", new_screen)
	cv2.imshow("Original", original)
	cv2.imshow("Screen", screen)

	logging.basicConfig(filename='frame_info.log', level=logging.DEBUG)
	logging.info('Time {} seconds'.format(time.time() - last_time))

	log_file = open('log_file', 'ab+')
	log_file.write('Time {} seconds'.format(time.time() - last_time))


	if cv2.waitKey(25) & 0xFF == ord('q'):
		cv2.destroyAllWindows()
		break



