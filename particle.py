screen_width = 1000
screen_height = 600

mass_min = 10 #minimum mass
mass_max = 500 #maximum mass

thickness_min = 2
thickness_max = 15

G = 0.2  #Gravitational constant (I will tweak the original value to suit my needs)

class Particle():
    def __init__(self, mass=0, x=0, y=0):
        self.mass = int(random(mass_min, mass_max))
        #Random coordinates
        self.x = random(0, screen_width)
        self.y = random(0, screen_height)
        
        #Fixed coordinates given by the parameter
        if (x != 0 or y != 0):
            self.x = x
            self.y = y
        
        #Fixed mass given by the parameter    
        if mass != 0:
            self.mass = mass    
        
            
        self.pos = PVector(self.x,self.y, 0)
        self.temp = 0 #Temperature of the particle, temperature will also influence the color of the particle
        self.v = PVector.random2D() #The particle will have a random velocity
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
            
        #I now cut out all the interactions with r < 3 or r > 200 because they are not relevant
        #or cause problems
        if r < 200 and r > 3:
            strength = (G * self.mass * p2.mass) / (r * r)
            direction.setMag(strength)
            acc = PVector.div(direction, self.mass) #Acceleration
            self.a.add(acc)#Updating acceleration
            
        elif r < 5: #Collision
            return p2 #Notify particle system to delete this two particles and add another one
            
        
    def update(self):#Update the particle movement
        self.v.add(self.a) #Updating velocity
        self.pos.add(self.v) #Updating position
        self.a.set(0, 0, 0)#reset acceleration
        
    
        
        
