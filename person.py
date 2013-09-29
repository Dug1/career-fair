class Person:
    import pygame
    import random
    def __init__(self, actor, rect, sprite, waiting, velocity = [0, 0]):
        self.rect = rect
        self.sprite = sprite
        self.velocity = x, y = velocity												#Right and Up are positive; Left/down negative
        self.waiting = False														#Speed is in pixels per tick
        self.unit = 16
        self.speed = 0
        new_stand(actor)


    def update(self, time, actors):
        if is_waiting():
            self.velocity = wait_AI()
        else:
            self.velocity = destination_AI(actors)
        testrect = Rect((0, 0), (3, 3))
        testrect = self.rect.copy()
        testrect.move(velocity[0] * time, velocity[1] * time)
        if collide(testrect, actors):
            self.changespeed()
        self.rectmove(velocity[0] * time, velocity[1] * time)
        
        
    def get_shirt(self, num_shirts):
        change_waiting(False)
        new_stand(actors)
    
    
    def put_in_line(self, endpoint):
        self.waiting = True
        self.endpoint = endpoint
    
    def get_center(self):
        center = x, y = self.rect.centerx, self.rect.centery
        return center
			
    def is_waiting(self):
        return self.waiting
		
    def change_Waiting(x):
        self.waiting = x
		
    def change_speed(self, xcomp = 0, ycomp = 0):
        self.speed = x, y = xcomp, ycomp
	
    def new_stand(self, x):															#x is an array of stands
        if self.is_waiting():
            return x[random.randrange(0, len(x))]
        else:
            while True:
                i = x[random.randrange(0, len(x))]									#get random stand
                if i.rect.centerx == self.endpoint[0] and i.rect.centery == self.endpoint[1]:
                    pass															
                else:
                    return i														
                    
    def collide(self, testrect, x):											    #x is an array of actors 
        for i in x:																#Tests for collision of current position with all actors
            if i.rect.colliderect(testrect):
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
        dest = find_route(available_adjacent(actors))
        velocity
        pos = []
        pos = self.getcenter()
        if dest.centerx > pos[0]:
            velocity = x, y = .5, 0
        if dest.centerx < pos[0]:
            velocity = x, y = -.5, 0
        if dest.centery > pos[1]:
            velocity = x, y = 0, .5
        if dest.centery < pos[1]:
            velocity = x, y = 0, -.5
        return velocity
        def available_adjacent(actors):
            a=[]
            for i in range (0, 3):
                a.append = self.rect.copy()
            a[0].move(0, self.unit)						#Adjacent rectangles
            a[1].move(0, -1 * self.unit)
            a[2].move(unit, 0)
            a[3].move(-1 * unit, 0)
            for i in range(0, 3):						#Get rid of collisions
                for x in actors:
                    if i.colliderect(x):
                        a[i] = 0
            a.remove(0)									#Delete unnecessary items
            return a
		#Begin processing minimal distance
        def find_route(a):
            dist = []
            for i in a:
                x = (endpoint.centerx - i.centerx) + (endpoint.centery - i.centery)
                dist.append(x)
            least = a[0]
            for i in a:
                if i < least:
                    least = i
            return a[a.index(least)]
				