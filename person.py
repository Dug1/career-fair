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

    def search_AI(self, rectangle, end_point, actors):
        velocity_constant = .5
        def find_adjacent(actors):
            unit = 16
            vlimit = 400
            hlimit = 832
            available_moves = []
            available_moves.append(rectangle.move(unit, 0))
            available_moves.append(rectangle.move(- 1 * unit, 0))
            available_moves.append(rectangle.move(0, unit))
            available_moves.append(rectangle.move(0, -1 * unit))
            for move in available_moves: 
                if move.centerx > hlimit:             #If outside horizontal border
                    available_moves.pop(i)
                elif move.centery < vlimit:           #If outside vertical border
                    move.pop(i)
                else:
                    for actor in actors:
                        if move.colliderect(actor):   #If collides with another actor
                            move.pop()
                for i in range(0, numbad):
                    available_moves.remove(0)
            return available_moves
        def find_route(available_moves, end_point):
            distances = []
            for i in available_moves:
                distances.append(math.fabs(end_point[0] - i.centerx) + math.fabs(end_point[1] - i.centery))
            return available_moves[available_moves.index(available_moves.min())]
            
        available_moves = find_adjacent(actors)
        target_position = find_route(available_moves)
        
        if target_position.centerx < rectangle.centerx:
            return (-1 * velocity_constant, 0)
        if target_position.centerx > rectangle.centerx:
            return (velocity_constant, 0)
        if target_position.centery < rectangle.centery:
            return (0, -1 * velocity_constant)
        if target_position.centery > rectangle.centery:
            return (0, velocity_constant)
            
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
