01 April 2021

I've just started this project.
IDEAS --> I could use a particle class to store the information of every particle. I want the particles to have an xPos, yPOS, a temperature and a mass. It will
          also have a radius that will depend upon its mass. I will also want to consider entropy.
          
14 April 2021
I've uploaded a new version of the sketch. I've added the main functionalities of the particles. Now they can spawn randomly on the screen with a velocity vector, and they can also interact with themselves (Though I think there is some problems with the motion influenced by gravity). I cutted out the interactions over long distances or short distances because they are either too low or cause strange behaviours (For short distances i want to add a function that unify 2 particles making one bigger). I've also added an optional visual line that show the interaction that one particle is having with another one.

ISSUES: Something is not working with the coordinates. From time to time one pair (usually x2, y2) become NaN, crashing the code. I've forced them to be 0 if that happens but id didn't work out.
