screen_width = 1000
screen_height = 600

class Particle():
    def __init__(self):
        self.x = int(random(screen_width))
        self.y = int(random(screen_height))
        self.thickness = 10 #it should be very small, a few pixels
        self.temp = 0 #Temperature of the particle, temperature will also influence the color of the particle
        self.mass = int(random(5)) #minimum mass, 1 kg, max 5kg
        self.v = PVector.random2D() #The particle will have a random velocity
        
    def display(self):
        fill(30, 209, 48)
        circle(self.x, self.y, self.thickness)
        
    def update(self):#Update the particle coordinates and interactions with other particles
        pass
        
        
