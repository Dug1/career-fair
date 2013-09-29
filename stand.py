import pygame

class Stand:

    def __init__(self, rect, image, facing_left, shirt_number = 10):
        self.clock = pygame.time.Clock()
        self.cooldown = 0
        self.image = image
        self.shirt_number = shirt_number
        self.line = []
        self.rect = rect
        pos_multiple = 5/6
        if not facing_left:
            pos_multiple = 1/6
        self.line_endpoint = (16 + rect.top + pos_multiple * rect.height, 16 + rect.left + pos_multiple * rect.width)
        self.not_waiting = True
        self.end_of_line = self.line_endpoint
        self.facing_left = facing_left
        

    def give_shirt(self, person):
        if self.shirt_number == 0:
            person.give_shirt(0)
        else:
            person.give_shirt(1)

    def add_person(self, person):
        if len(self.line) < 8:
            self.line.append(person)
            person.put_in_line(self.line_endpoint)
            return True
        else:
            return False

    def update(self):
        # delay for giving out shirts
        if self.cooldown == 0 and first.get_center() == self.line_endpoint:
            self.give_shirt(self,self.line[0])
            self.cooldown = 5000
        else:
            self.cooldown = max(self.cooldown - self.clock.tick(), 0) 

    def get_end_of_line(self):
        if facing_left:
            return (self.line_endpoint[0] - len(self.line) * 16, self.line_endpoint[1])
        return (self.line_endpoint[0] - len(self.line) * 16, self.line_endpoint[1])

