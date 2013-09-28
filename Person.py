#Person class

class Person:
	import pygame
	import random
	def __init__(self, rect, stand, sprite, speed = [0, 0]):
		self.position = rect
		self.stand = stand
		self.sprite = sprite
		self.speed = x, y = speed												#Right and Up are positive; Left/down negative
		self.waiting = False													#Speed is in pixels per tick
	
	def update(x):																#x is an array of stands
		if waiting == True:
			pass
		else:
			self.stand = newstand(x)
	
	def changespeed(self, xcomp, ycomp):
		self.speed = x, y = xcomp, ycomp
	
	def newstand(self, x):															#x is an array of stands
		while True:
			i = x[random.randrange(0, len(x))]									#get random stand
			if i.rect.colliderect(self.stand.rect) == True:						#test stand position to current stand position
				pass															
			else:
				return i														
				
	def collide(self, x): 															#x is an array of actors 
		for i in x:																#Tests for collision of current position with all actors
			if i.rect.colliderect(self.rect) == True:
				return True
		return False