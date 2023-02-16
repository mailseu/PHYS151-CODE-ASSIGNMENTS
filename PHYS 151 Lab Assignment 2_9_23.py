Web VPython 3.2

#Henry Samala
#PHYS 151 Lab 2.9.23

floor=box(pos=vector(0,0,0),
        size=vector(300,2,5),
        color=color.red,
        opacity = 0.4)
        
#Yellow = Ball with Momentum principle
#Red = Ball with Kinematic equation x and y
#Blue = Ball without Gravity

particleGravity=sphere(pos=vector(-150,1,0), 
        radius = 0.5, 
        color = color.yellow,
        make_trail = True) 

particleGravityKinematic=sphere(pos=vector(-150,1,0), 
        radius = 0.5, 
        color = color.red,
        make_trail = True) 

particleNoGravity=sphere(pos=vector(-150,1,0), 
        radius = 0.5, 
        color = color.blue,
        make_trail = True) 
        
KinematicV = vector(5,5,0)
v = vector(7,7,0)
g = vector(0,-9.8,0)

particleMass = 10 
particleMomentum = particleMass*v

delta_t = 0.05
t = 0

#graphing function
velocityXGraph = graph(title = "Velcoity in X", xtitle = "t (s)", ytitle = "vel (m/s)")
gravXCruve = gcurve(graph = velocityXGraph, color = color.yellow)
nogravXCurve = gcurve(graph = velocityXGraph, color = color.blue)

velocityYGraph = graph(title = "Velcoity in Y", xtitle = "t (s)", ytitle = "vel (m/s)")
gravYCruve = gcurve(graph = velocityYGraph, color = color.yellow)
nogravYCurve = gcurve(graph = velocityYGraph, color = color.blue)

while t < 40:
    rate(100)
    t = t + delta_t
    
    gravV = (particleMomentum/particleMass) * delta_t
    nogravV = v * delta_t
    
    #ball movement
    if particleNoGravity.pos.y < 100:
        particleNoGravity.pos = particleNoGravity.pos + nogravV

    if particleGravity.pos.y >= 0:
        particleMomentum = particleMomentum + g * delta_t
        particleGravity.pos = particleGravity.pos + gravV 
    
    if particleGravityKinematic.pos.y >= 0:
        particleGravityKinematic.pos = particleGravityKinematic.pos + KinematicV * t + ((g/2)*(t**2))
    else:
        print("Final Displacement of Kinematic Equation = ", particleGravityKinematic.pos.x + 150)
    
    #graphing values
    nogravXCurve.plot(t,nogravV.x)
    nogravYCurve.plot(t,nogravV.y)
    
    gravXCruve.plot(t,gravV.x)
    gravYCruve.plot(t,gravV.y)
    
