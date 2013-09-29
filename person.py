import pygame
from pygame import Rect
import random

class Person:
    def __init__(self, actor, rect, sprite, velocity = [0, 0]):
        self.rect = rect
        self.sprite = sprite
        self.velocity = x, y = velocity	
        #Right and Up are positive; Left/down negative       
        self.waiting = False
        #Speed is in pixels per tick
        self.unit = 16
        self.endpoint = x, y = -1, -1
        self.new_stand(actor)

    def update(self, time, actors):
        if self.is_waiting():
            self.velocity = self.wait_AI()
        else:
            self.velocity = self.destination_AI(actors, self.endpoint)
        testrect = Rect((0, 0), (3, 3))
        testrect = self.rect.copy()
        testrect = testrect.move(self.velocity[0] * time, self.velocity[1] * time)
        if self.collide(testrect, actors):
            self.changespeed()
        self.rect = self.rect.move(self.velocity[0] * time, self.velocity[1] * time)
        
        
    def get_shirt(self, num_shirts):
        self.change_waiting(False)
        self.new_stand(actors)

    def put_in_line(self, endpoint):
        self.waiting = True
        self.endpoint = endpoint
    
    def get_center(self):
        center = x, y = self.rect.centerx, self.rect.centery
        return center
                    
    def is_waiting(self):
        return self.waiting
            
    def change_waiting(x):
        self.waiting = x
            
    def change_speed(self, xcomp = 0, ycomp = 0):
        self.speed = x, y = xcomp, ycomp
	
    def new_stand(self, x):
        #x is an array of stands
        if self.is_waiting():
            return x[random.randrange(0, len(x))]
        else:
            while True:
                i = x[random.randrange(0, len(x))]									#get random stand
                if i.rect.centerx == self.endpoint[0] and i.rect.centery == self.endpoint[1]:
                    pass															
                else:
                    self.endpoint = i.rect.centerx, i.rect.centery
                    return i														
                    
    def collide(self, testrect, x):											    #x is an array of actors 
        for i in x:																#Tests for collision of current position with all actors
            if i.rect.colliderect(testrect):
                return True
            if i.rect.centerx < 0 or i.rect.centery < 0:
                return True
            if i.rect.centerx > 832 or i.rect.centery > 400:
                return True
        return False
    def wait_AI(self):
        velocity
        if self.position[0] < self.endpoint[0]:
            velocity = .5
        else:
            velocity = -.5
        self.change_speed(velocity)
        return velocity
			
    def destination_AI(self, actors, endpoint):
        def available_adjacent(actors):
            a=[]
            for i in range (0, 4):
                a.append(self.rect.copy())
            a.append(self.rect.move(0, self.unit))                     #Adjacent rectangles
            a.append(self.rect.move(0, -1 * self.unit))
            a.append(self.rect.move(self.unit, 0))
            a.append(self.rect.move(-1 * self.unit, 0))
            print(a)
            for i in range(0, 3):                       #Get rid of collisions
                for x in actors:
                    if a[i].colliderect(x):
                        a[i] = 0
                    elif a[i].centerx < 0 or a[i].centery < 0:
                       a[i] = 0
                    elif a[i].centerx > 832 or a[i].centery > 400:
                       a[i] = 0
            if a.count(0) > 0:
                a.remove(0)                                 #Delete unnecessary items
            return a
        #Begin processing minimal distance
        def find_route(a):
            dist = []
            for i in a:
                x = (endpoint[0] - i.centerx) + (endpoint[1] - i.centery)
                dist.append(x)
            least = a[0]
            for i in a:
                if i < least:
                    least = i
            return a[a.index(least)]
        dest = find_route(available_adjacent(actors))
        velocity = (0,0)
        pos = []
        pos = self.rect.center
        if dest.centerx > pos[0]:
            velocity = x, y = -.5, 0
        if dest.centerx < pos[0]:
            velocity = x, y = .5, 0
        if dest.centery > pos[1]:
            velocity = x, y = 0, -.5
        if dest.centery < pos[1]:
            velocity = x, y = 0, .5
        self.change_speed(velocity[0], velocity[1])
        return velocity
        		
