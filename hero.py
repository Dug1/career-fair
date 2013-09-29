from person import *

class Hero(Person):
    def __init__(self):
        Person.__init__(self)
        self.shirt_count = 0:
        self.resume_count = 15;

    def give_shirt(self, x):
        self.shirt_count += x
        self.resume_count -= 1
        self.waiting = False
    
    def update(self, actors, key_pressed):
        if not key_pressed and self.waiting:
            self.velocity = self.wait_AI()
        Person.update(self, actors)

        
    
