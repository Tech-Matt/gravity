#MAIN --> simulation of a particles system influenced by gravity and temperatures
from particle import Particle
from particle_system import Particle_System

num_particles = 20
system = Particle_System(num_particles)

show = False #To show the distance with particles that are interacting (LATER)

def setup():
    size(1000, 600)
    
def draw():
    background(255)
    system.display()
    #system.interactions()
    system.update_system()
    # for i in range(len(particle_array)):
    #     particle_array[i].display()
    #     #I'm creating another array without the particle considered in the loop. So i can confront the first one with
    #     #every other particle except itself.
    #     part_array = [elem for elem in particle_array if elem != particle_array[i]]
    #     #check interaction with every particles
    #     for k in range(len(part_array)):
    #         particle_array[i].check_interaction(part_array[k], show)
    
    # #different loops to first determine the acceleration without changing positions
    # #and later on updating the positions
    # for elem in particle_array: 
    #     elem.update()
        
    # #fill(173, 164, 164)
    # #rect(10, 10, 20, 20) #Show Interactions box
    
