screen_width = 1000
screen_height = 600

mass_min = 100 #minimum mass
mass_max = 500 #maximum mass
thickness_min = 1 
thickness_max = 10 

G = (6.67)  #Gravitational constant (I will tweak the original value to suit my needs)

class Particle():
    def __init__(self):
        self.x = random(screen_width)
        self.y = random(screen_height)
        self.temp = 0 #Temperature of the particle, temperature will also influence the color of the particle
        self.mass = int(random(mass_min, mass_max)) 
        self.v = PVector.random2D() #The particle will have a random velocity
        self.a = PVector(0, 0, 0) #Resulting acceleration due to gravity interactions
        
    def display(self):
        self.thickness = map(self.mass, mass_min, mass_max, thickness_min, thickness_max)#Mapping size based on mass
        fill(30, 209, 48)
        circle(self.x, self.y, self.thickness)
    
    def check_interaction(self, p2, show_interactions): #Determine the force and verse of the force of gravity between 2 particles
        """ p2: instance of another particle
            show_interactions: True to show, False to not show """
        m1 = self.mass
        m2 = p2.mass
        x1 = self.x
        y1 = self.y
        x2 = p2.x
        y2 = p2.y
        r = sqrt(((x2 - x1)**2) + ((y2 - y1)**2)) #Distance between the particles
        
        #OPTIONAL --> SHOW THE INTERACTIONS 
        if r < 200 and show_interactions: #If distance is low show the distance
            stroke(110);
            line(x1, y1, x2, y2) #Line to visualize the distance of the interactions
            
        #I now cut out all the interactions with r < 1 or r > 200 because they are not relevant
        #or cause problems
        if r < 200 and r > 1:
            f = G * (m1 * m2)/ (r ** 2) #Particle is subjected to this force of gravity
            a = f / m1 #Acceleration due to force of gravity
            #print("F: " + str(f), "A: " + str(a))
            
            angle = acos((x2 - x1) / r) #Orientation of the acceleration vector
            print("Angle: " + str(angle) + "x1, y1, x2, y2: " + str(x1) +" "+ str(y1) +" "+ str(x2) +" "+ str(y2), "R: " + str(r))
            #print("New Angle: " + str(angle), "X1; Y1, X2, Y2: " + str(x1) +str(y1) + str(x2) + str(y2))
            ax = a * cos(angle)
            ay = a * sin(angle)
            self.a.add(ax, ay, 0) #update Acceleration vector
        
        
    def update(self):#Update the particle movement
        Vx = self.v.x + self.a.x#I add the acceleration to to speed
        Vy = self.v.y + self.a.y
        
        self.x += Vx #Update the motion
        self.y += Vy 
        self.a.set(0, 0, 0)#reset acceleration
        
    
        
        
