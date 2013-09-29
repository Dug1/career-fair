class Person:
	import pygame
	import random
	def __init__(self, rect, sprite, waiting = [0, 0]):
		self.rect = rect
		self.sprite = sprite
		self.velocity = x, y = velocity												#Right and Up are positive; Left/down negative
		self.waiting = False														#Speed is in pixels per tick
		self.unit = 16
		
	
	def update(x):																#x is an array of stands
		if waiting == True:
			pass
		else:
			self.stand = newstand(x)
	
	def putinline(self, endpoint):
		self.waiting = True
		self.destination = endpoint
		waitAI()
	
	def getcenter(self):
		center = x, y = self.rect.centerx, self.rect.centery
		return center
			
	def iswaiting(self):
		return self.waiting
		
	def changeWaiting(x):
		self.waiting = x
		
	def changespeed(self, xcomp = 0, ycomp = 0):
		self.speed = x, y = xcomp, ycomp
	
	def newstand(self, x):															#x is an array of stands
		if self.stand == None:
			return x[random.randrange(0, len(x))]
		else:
			while True:
				i = x[random.randrange(0, len(x))]									#get random stand
				if i.rect.center == self.stand.rect.center:							#test stand position to current stand position
					pass															
				else:
					return i														
				
	def collide(self, x): 														#x is an array of actors 
		for i in x:																#Tests for collision of current position with all actors
			if i.rect.colliderect(self.rect) == True:
				return True
		return False
	def waitAI(self, position):
		if self.position[0] < position[0]:
			self.changespeed(.5)
		else:
			self.changespeed(-.5)
			
	def destinationAI(self, actors, endpoint, nomanland = self.position):
		def availableadjacent(actors):
			a=[]
			for i in range (0, 3):
					a.append = self.rect.copy()
			a[0].move(0, self.unit)						#Adjacent rectangles
			a[1].move(0, -1 * self.unit)
			a[2].move(unit, 0)
			a[3].move(-1 * unit, 0)
			for i in range (0, 3):						#get rid of previous position
				if a[i].center == nomanland
					a[i] = 0
			for i in range(0, 3):						#Get rid of collisions
				for x in actors:
					if i.colliderect(x):
						a[i] = 0
			a.remove(0)									#Delete unnecessary items
			dist=[]
			#Begin processing minimal distance
			for i in a:
				dist.append(i.centerx
				
			
			
			return a
		def
				