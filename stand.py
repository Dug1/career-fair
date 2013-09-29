class Stand:
	import pygame
	from pygame import Rect
	def __init__(self, rect = Rect((3, 4), (5, 5)), direction = True):
		self.rect = rect
		self.direction = direction
	def str(self):
		return self.rect

def makeStands():
	import pygame
	from pygame import Rect
	tilesize = 16
	width = 2 * tilesize
	height = 3 * tilesize
	intermittentspace = 10 * tilesize
	vspace = 5 * tilesize
	a = []
	x = intermittentspace
	while x <= (width * 3 + intermittentspace * 3):																	#True is left, False is right
		for y in range(vspace + height, vspace + 5 * height + 1, height):
			a.append(Stand(Rect((x, y), (width, height)), True))
		x += width
		for y in range(vspace + height, vspace + 5 * height + 1, height):
			a.append(Stand(Rect((x, y), (width, height)), False))
		x += intermittentspace
	return a