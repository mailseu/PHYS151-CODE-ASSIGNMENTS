Web VPython 3.2
from visual import *

box(pos=vector(0,0,-1),
    size=vector(5,5,0.5),
    color=color.red,
    opacity = 0.4)
particle = sphere(pos=vector(-5,0,-5),
                    radius=0.3,
                    color=color.cyan,
                    make_trail = True)
v = vector(0.5,0,0.5)
delta_t = 0.05
t = 0
while t < 20:
    rate(100)
    particle.pos = particle.pos + v * delta_t
    t = t + delta_t
    if particle.pos.z > -1 - particle.radius:
        v.z = -0.5 
        
    

#floor = box (pos=vec(0,0,0), length=4, height=0.5, width=4, color=color.blue)
#ball = sphere (pos=vec(0,4,0), radius=1, color=color.red)
#ball.velocity = vector(0,-1,0)
#dt = 0.01
#
#while 1:
#    rate (100)
#    ball.pos = ball.pos + ball.velocity*dt
#    if ball.pos.y < ball.radius:
#        ball.velocity.y = abs(ball.velocity.y)
#    else:
#        ball.velocity.y = ball.velocity.y - 9.8*dt
                
