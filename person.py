import pygame
from pygame import Rect
import random
from random import choice

class Person:
    def __init__(self, rect, sprite, stands, velocity = (0,0)):
        self.rect = rect
        self.sprite = sprite
        self.velocity = velocity	
        self.unit = 16
        self.ai = self.search_AI
        self.stands = stands
        self.waiting = False
        self.find_new_stand()
    
    def update(self, time_passed, actors):
        if self.is_at_goal_stand(): 
            self.ai = self.wait_AI
            self.stand.add_person(self)
        if collides_with(*actors)
            self.velocity = (0, 0)
        else:
            self.velocity = self.ai(*actors)

      
    def collides_with(self, *actors):
        for actor in actors:
            if actor.rect.colliderect(self.rect)
                return True
        return False

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

    def search_AI(self, time_passed, actors):
        velocity_constant, vlimit, hlimit = 400, 832, 0.5
        rect, endpoint = self.rect, self.stand.get_end_of_line()
        direction =(cmp(endpoint[0], self.rect.centerx), cmp(endpoint[1], self.rect.centery)) 
       
        #variables are declared for readability
        move_towards_x = direction[0] * time_passed * velocity_constant
        if direction[0] != 0 or rect.move(move_towards_x, 0).collidelist(actor.rect for actor in actors) != -1:
            return (move_towards_x, 0)

        move_towards_y = direction[1] * time_passed * velocity_constant
        if direction[1] != 0 or rect.move(0, move_towards_y).collidelist(actor.rect for actor in actors) == -1:
            return (0, move_towards_y)

        if rect.move(-move_towards_x, 0).collidelist(actor.rect for actor in actors) == -1:
            return (-move_towards_x, 0)

        return (0, -move_towards_y)
            
    def wait_AI(self, rectangle, end_point, actors):
        velocity_constant = .5
        if end_point[0] < rectangle.centerx:
            return (-1 * velocity_constant, 0)
        if end_point[0] > rectangle.centerx:
            return (velocity_constant, 0)
        if end_point[1] < rectangle.centery:
            return (0, -1 * velocity_constant)
        if end_point[1] > rectangle.centery:
            return (0, velocity_constant)

>>>>>>> e187a20194695ddee253f630796673551e5c808c
