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
        for part in self.particle_array:
            part.check_interactions()
    
    def update_system(self):
        for part in self.particle_array:
            part.update()
