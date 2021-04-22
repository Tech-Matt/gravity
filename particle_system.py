from particle import Particle

class Particle_System():
    
    def __init__(self, num):
        """
        num: Number of particles in the system
        """
        self.num = num
        self.particle_array = []
        
        for i in range(num):
            p = Particle()
            self.particle_array.append(p)
    
    def display(self):
        for part in self.particle_array:
            part.display()
            
    def interactions(self, show):
        collision = [] #its purpose is to store which pair of particles have collided ([[p1, p2], [p3, p4]])
        num = 0 #Counter to see if there are collisions
        
        for i in range(len(self.particle_array)):
            part_array = [elem for elem in self.particle_array if elem != self.particle_array[i]]
            for j in range(len(part_array)):
                if (self.particle_array[i].check_interaction(part_array[j], show) != None):#case of collision
                    p2 = self.particle_array[i].check_interaction(part_array[j], show)#Instance of p2
                    collision.append([self.particle_array[i], p2])#Add to an array to control it later
                    num += 1
                else:
                    self.particle_array[i].check_interaction(part_array[j], show) #Simply calculate interactions
                    
            
        #DELETE PARTICLES THAT HAVE COLLIDED AND ADD ANOTHER ONE WHICH MASS IT'S THE SUM OF THE ORIGINAL
        #PARTICLES MASS
        if num > 0:
            for p1, p2 in collision:
                m1 = p1.mass
                m2 = p2.mass
                
                x1 = p1.x
                y1 = p1.y
            
                self.particle_array.remove(p1)
                self.particle_array.remove(p2)
                
                fill(60, 34, 211) #new particles will be blue
                
                new_p = Particle(mass=m1+m2,x=x1, y=y1)
                self.particle_array.append(new_p)
                
                num = 0 #reset counter
                
    
    def update_system(self):
        for part in self.particle_array:
            part.update()
