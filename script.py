Web VPython 3.2
#All radii of planets are scaled in their real value but in unit R🜨(Earth's radius).
#We converted Semimajor axis value of each planet from Astronomical Units to R🜨 usin AU = 23481R🜨 and then divided b 200 to be consistent with the planets' volume.
#We assumed here that all planets' paths and their shapes are prefect circles.

Kepler_62 = sphere(pos = vector(0, 0, 0), radius = 3.497, color = color.orange)
#The real radius of the star is 69.95 R🜨 but here we scaled it with factor 1/20 unlike the planets around it, just for the planets to be clear.

Kepler_62b = sphere(pos = vector(6.4925, 0, 0), radius = 1.31, color = color.red, make_trail=True, trail_color = color.white)
Kepler_62c = sphere(pos = vector(10.919, 0, 0), radius = 0.54, color = color.green, make_trail=True, trail_color = color.white)
Kepler_62d = sphere(pos = vector(14.089, 0, 0), radius = 1.95, color = color.yellow, make_trail=True, trail_color = color.white)
Kepler_62e = sphere(pos = vector(50.130, 0, 0), radius = 1.61, color = color.cyan, make_trail=True, trail_color = color.white)
Kepler_62f = sphere(pos = vector(84.295, 0, 0), radius = 1.41, color = color.blue, make_trail=True, trail_color = color.white)

t1 = 0
t2 = 0
t3 = 0
t4 = 0
t5 = 0
dt = 0.01
while True:
    rate(300)
    Kepler_62b.pos.x = 6.4925*cos(t1)
    Kepler_62b.pos.y = 6.4925*sin(t1)
    
    Kepler_62c.pos.x = 10.919*cos(t2)
    Kepler_62c.pos.y = 10.919*sin(t2)
    
    Kepler_62d.pos.x = 14.0885*cos(t3)
    Kepler_62d.pos.y = 14.0885*sin(t3)

    Kepler_62e.pos.x = 50.13*cos(t4)
    Kepler_62e.pos.y = 50.13*sin(t4)

    Kepler_62f.pos.x = 84.295*cos(t5)
    Kepler_62f.pos.y = 84.295*sin(t5)
    
    t1 = t1 + dt
    t2 = t2 + dt/2.177
    t3 = t3 + dt/3.17835
    t4 = t4 + dt/21.41538
    t5 = t5 + dt/46.77
   
#Created by "DetesTwox-Hazems": Youssef Mostafa (AKA Detestox), Hazem Hassan (me!), and Hazem Nasr.
