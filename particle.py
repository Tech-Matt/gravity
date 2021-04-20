screen_width = 1000
screen_height = 600

mass_min = 10 #minimum mass
mass_max = 50 #maximum mass
thickness_min = 2
thickness_max = 15

G = 1  #Gravitational constant (I will tweak the original value to suit my needs)

class Particle():
    def __init__(self):
        self.pos = PVector(random(screen_width),random(screen_height), 0)
        self.temp = 0 #Temperature of the particle, temperature will also influence the color of the particle
        self.mass = int(random(mass_min, mass_max)) 
        self.v = PVector(0, 0, 0) #The particle will have a random velocity
        self.a = PVector(0, 0, 0) #Resulting acceleration due to gravity interactions
        
    def display(self):
        self.thickness = map(self.mass, mass_min, mass_max, thickness_min, thickness_max)#Mapping size based on mass
        fill(30, 209, 48)
        circle(self.pos.x, self.pos.y, self.thickness)
    
    def check_interaction(self, p2, show_interactions): #Determine the force and verse of the force of gravity between 2 particles
        """ p2: instance of another particle
            show_interactions: True to show, False to not show """
        
        direction = PVector.sub(p2.pos, self.pos)#Calculate the direction
        r = direction.mag() #Distance between particles
        
        #OPTIONAL --> SHOW THE INTERACTIONS 
        if r < 200 and show_interactions: #If distance is low show the distance
            stroke(110);
            line(self.pos.x, self.pos.y, p2.pos.x, p2.pos.y) #Line to visualize the distance of the interactions
            
        #I now cut out all the interactions with r < 1 or r > 200 because they are not relevant
        #or cause problems
        if r < 200 and r > 1:
            strength = (G * self.mass * p2.mass) / (r * r)
            direction.setMag(strength)
            acc = PVector.div(direction, self.mass) #Acceleration
            self.a.add(acc)#Updating acceleration
        
    def update(self):#Update the particle movement
        self.v.add(self.a) #Updating velocity
        self.pos.add(self.v) #Updating position
        self.a.set(0, 0, 0)#reset acceleration
        
    
        
        
