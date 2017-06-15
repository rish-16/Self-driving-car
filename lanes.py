import logging
from threading import Thread
import numpy as np
import cv2
import math

def draw_lanes(img, lines):
	Thread(target = draw_lanes_right(img,lines)).start()
	Thread(target = draw_lanes_left(img,lines)).start()

def draw_lanes_right(img, lines):
	try:
		for line in lines:
			coordsright = line[0]

			grad = find_grad(coordsright[0],coordsright[1],coordsright[2],coordsright[3])

			if grad<0:
				cv2.line(img, (coordsright[0],coordsright[1]), (coordsright[2],coordsright[3]), [211,211,0], 3)
				line_len = find_length(coordsright[0],coordsright[1],coordsright[2],coordsright[3])
				message = "Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad)
				print message
				cv2.putText(img, "c0:{},c1:{}".format(coordsright[0], coordsright[1]), (coordsright[0], coordsright[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255)
				cv2.putText(img, "c2:{},c3:{}".format(coordsright[2], coordsright[3]), (coordsright[2], coordsright[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255)

				logging.basicConfig(filename='drawing_info.log', level=logging.DEBUG)
				logging.info("Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad))

				log_file = open('log_file', 'ab+')
				log_file.write("Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad))

	except:
		pass

def draw_lanes_left(img, lines):
	try:
		for line in lines:
			coordsleft = line[0]

			grad = find_grad(coordsleft[0],coordsleft[1],coordsleft[2],coordsleft[3])

			if grad>0:
				cv2.line(img, (coordsleft[0],coordsleft[1]), (coordsleft[2],coordsleft[3]), [211,211,0], 3)
				line_len = find_length(coordsleft[0],coordsleft[1],coordsleft[2],coordsleft[3])
				message = "Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad)
				print message
				cv2.putText(img, "c4:{},c5:{}".format(coordsleft[0], coordsleft[1]), (coordsleft[0], coordsleft[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255)
				cv2.putText(img, "c6:{},c7:{}".format(coordsleft[2], coordsleft[3]), (coordsleft[2], coordsleft[3]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 255)

				logging.basicConfig(filename='log_file.log', level=logging.DEBUG)
				logging.info("Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad))

				log_file = open('log_file', 'ab+')
				log_file.write("Length {} | Coordinates c0{},c1{} and c2{},c3{} | Gradient {}".format(line_len, coordsright[0],coordsright[1],coordsright[2],coordsright[3], grad))
	except:
		pass


def find_length(x1,y1,x2,y2):
	xsum = (x1-x2)^2
	ysum = (y1-y2)^2

	line_len = math.sqrt(xsum + ysum)

	return line_len

def find_grad(x1,y1,x2,y2):
	return (y1 - y2)/(x1 - x2)



