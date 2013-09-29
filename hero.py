from person import *

class Hero(Person):

    keys = pygame.key.get_pressed()

    def __init__(self):
        Person.__init__(self)
        self.shirt_count = 0:
        self.resume_count = 15;

    def give_shirt(self, x):
        Person.give_shirt(x)
        self.shirt_count += x
        self.resume_count -= 1
        self.waiting = False
    
    def update(self, actors, key_pressed):
        if not key_pressed and self.waiting:
            self.velocity = self.wait_AI()
        elif keys[K_w]:
            go_up()
        elif keys[K_s]
            go_down()
        elif keys[K_a]
            go_left()
        elif keys [K_d]
            go right()
        else:
            self.velocity = adjust_for_collision()


    def go_up():
        self.velocity = (0,1)

    def go_down():
        self.velocity = (-1,0)

    def go_left():
        self.velocity = (-1,0)

    def go_right():
        self.velocity = (1,0)