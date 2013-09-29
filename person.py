import pygame
import random
from random import choice

class Person:
    def __init__(self, rect, sprite, stands, velocity = (0,0))  
        self.rect = rect
        self.sprite = sprite
        self.velocity = velocity	
        self.unit = 16
        self.ai = self.search_AI
        self.stands = stands
        self.waiting = False
        self.find_new_stand()
    
    def update(self, actors):
        if self.is_at_goal_stand(): 
            self.ai = self.wait_AI
            self.stand.add_person(self)
        self.velocity = adjust_for_collision(self.ai(self.rect, self.stand.get_end_of_line, actors))    
      
    def adjust_for_collision(self, actors):
        for actor in actor:
            if actor.rect.colliderect(self.rect)
                return (0,0)
        return self.velocity

    def give_shirt(self, num_shirt):
        self.find_new_stand
        self.ai = self.search_AI()

    def put_in_line(self):
        self.ai = waitAI()
        self.waiting = True
            
    def is_at_goal_stand(self):
        return self.center == self.current_stand.end_of_line

    def find_new_stand(self):
        self.current_stand = choice(self.stands)
                    
