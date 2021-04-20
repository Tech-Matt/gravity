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
        for i in range(len(self.particle_array)):
            part_array = [elem for elem in self.particle_array if elem != self.particle_array[i]]
            for j in range(len(part_array)):
                self.particle_array[i].check_interaction(part_array[j], show)
        
    
    def update_system(self):
        for part in self.particle_array:
            part.update()
