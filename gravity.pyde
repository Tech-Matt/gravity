#MAIN --> simulation of a particles system influenced by gravity and temperatures
from particle import Particle
from particle_system import Particle_System

num_particles = 10
system = Particle_System(num_particles)

show = False #To show the distance with particles that are interacting (LATER)

def setup():
    size(1000, 600)
    
def draw():
    background(255)
    system.display()
    system.interactions(show)
    system.update_system()
        
    # #fill(173, 164, 164)
    # #rect(10, 10, 20, 20) #Show Interactions box
    
