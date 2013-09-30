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
        if self.collides_with(*actors):
            self.velocity = (0, 0)
        else:
            self.velocity = self.ai(time_passed, *actors)
        self.rect.move_ip(self.velocity[0]*time_passed, self.velocity[1]*time_passed)

      
    def collides_with(self, *actors):
        for actor in actors:
            if actor.rect.colliderect(self.rect):
                return True
        return False

    def give_shirt(self, num_shirt):
        self.find_new_stand
        self.ai = self.search_AI()

    def put_in_line(self):
        self.ai = waitAI()
        self.waiting = True
            
    def is_at_goal_stand(self):
        return self.rect.center == self.current_stand.end_of_line

    def find_new_stand(self):
        self.current_stand = choice(self.stands)

    @staticmethod
    def distance(point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def search_AI(self, time_passed, *actors):
        speed, vlimit, hlimit = 400, 832, 0.5
        rect, endpoint = self.rect, self.current_stand.get_end_of_line()
        direction =(cmp(endpoint[0], self.rect.centerx), cmp(endpoint[1], self.rect.centery)) 
       
        #variables are declared for readability
        moves = [(direction[0] * speed , 0), (0, direction[1] * speed), (-direction[0] * speed, 0), (0, -direction[1])]
        valid_distances_and_moves = {}
        for move in moves:
            rect = self.rect.move(move[0] * time_passed, move[1] * time_passed)
            #check for bounds first, then collisions
            if rect.top > 0 and rect.left > 0 and rect.right < hlimit and rect.bottom < vlimit and rect.collidelist([actor.rect for actor in actors]) != -1:
                valid_moves[Person.distance(rect.center, endpoint)] = move
        self.velocity = valid_moves[min(valid_moves.keys())]


            
    def wait_AI(self, rectangle, end_point, *actors):
        velocity_constant = .5
        if end_point[0] < rectangle.centerx:
            return (-1 * velocity_constant, 0)
        if end_point[0] > rectangle.centerx:
            return (velocity_constant, 0)
        if end_point[1] < rectangle.centery:
            return (0, -1 * velocity_constant)
        if end_point[1] > rectangle.centery:
            return (0, velocity_constant)

