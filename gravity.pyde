#MAIN --> simulation of a particles system influenced by gravity and temperatures
from particle import Particle

num_particles = 100
particle_array = []

def setup():
    size(1000, 600)
    
    for i in range(num_particles):
        p = Particle()
        p.display()
        
    
    
def draw():
    pass
    
