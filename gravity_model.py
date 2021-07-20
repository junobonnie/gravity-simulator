# -*- coding: utf-8 -*-
"""
Created on Tue May 18 10:12:09 2021

@author: junob
"""
from vectortools import *
from atom import *
import sys

softening_length = 5.5

class Atom(Atom):
    def __init__(self, element, pos, vel = Vector(0, 0)):
        self.element = element
        self.pos = pos
        self.vel = vel
        
    def gravity_acc(self, other):
        r = self.pos - other.pos
        if not self == other:# and r.dot(r) > self.element.radius+other.element.radius:
            return -other.element.mass*r/((r.dot(r)+softening_length**2)**(3/2)) #-other.element.mass/r.dot(r)*(r/abs(r))
        else:
            return Vector(0, 0)
        
    def kinetic_energy(self):
        return (1/2)*self.element.mass*self.vel.dot(self.vel)
        
    def potential_energy(self, other):
        r = self.pos - other.pos
        if not self == other:# and r.dot(r) > self.element.radius+other.element.radius:
            return -self.element.mass*other.element.mass/m.sqrt(r.dot(r)+softening_length**2)
        else:
            return 0
        
class World(World):
    def __init__(self, t, atoms, walls, G, gravity = Vector(0, 0)):
        self.t = t
        self.atoms = atoms
        self.walls = walls
        self.G = G
        self.gravity = gravity
            
class Simulator(Simulator):
    def __init__(self, dt, world, render):
        self.dt = dt
        self.world = world
        self.render = render
        self.count = 0
        
    def main(self):
        x_ = []
        v_ = []
        for atom in self.world.atoms:
            atom_gravity = Vector(0, 0)
            for other_atom in self.world.atoms:
                atom_gravity += self.world.G*atom.gravity_acc(other_atom)
            new_v = atom.vel + atom_gravity*self.dt + self.world.gravity*self.dt
            v_.append(new_v)
            x_.append(atom.pos + new_v*self.dt)
        
        count = 0
        for atom in self.world.atoms:
            atom.pos = x_[count]
            atom.vel = v_[count]
            count = count + 1
            
if __name__ == '__main__':
    width = 1000
    height = 800

    screen = pg.display.set_mode((width, height))
    render = Render(screen, width, height)
    clock = pg.time.Clock()

    black = pg.Color('black')
    white = pg.Color('white')
    red = pg.Color('red')
    green = pg.Color('green')
    blue = pg.Color('blue')

    wall1 = Wall(1000, 50, 0, Vector(-500, -400), blue)
    wall2 = Wall(50, 800, 0, Vector(-500, -400), blue)
    wall3 = Wall(50, 800, 0, Vector(450,-400), blue)
    wall4 = Wall(1000, 50, 0, Vector(-500, 350), blue)
    wall5 = Wall(100, 50, m.pi/4, Vector(-300, 0), blue)

    e1 = Element(name = 'Helium', mass = 1, radius = 3, color = blue)
    e2 = Element(name = 'Uranium', mass = 100, radius = 5, color = red)
   
    # atom1 = Atom(e1, Vector(-200, 0), Vector(50, 0))
    # atom2 = Atom(e1, Vector(0, 0))
    # atom3 = Atom(e1, Vector(25, -10))
    # atom4 = Atom(e1, Vector(25, 10))
    # atom5 = Atom(e1, Vector(50, -20))
    # atom6 = Atom(e1, Vector(50, 0))
    # atom7 = Atom(e1, Vector(50, 20))

    walls = [] # [wall1, wall2, wall3, wall4, wall5]
    atoms = [] # [atom1, atom2, atom3, atom4, atom5, atom6, atom7]
    
    import random as r
    import math as m
    for i in range(50):
        rV = SO2(r.random()*2*m.pi).dot(Vector(r.randrange(-200, 200, 2*e1.radius) ,0))
        atoms.append(Atom(e1, rV))
    
    for i in range(50):
        rV = SO2(r.random()*2*m.pi).dot(Vector(r.randrange(-200, 200, 2*e1.radius) ,0))
        atoms.append(Atom(e2, rV))
        
    G = 1000
    gravity = Vector(0, 0)

    world = World(0, atoms, walls, G, gravity)

    simulator = Simulator(0.01, world, render)
    
    t_list = []
    K_list = []
    P_list = []
    TOT_E_list = []
    
    while True:
        t = simulator.clock()
        simulator.draw_background(white)
        simulator.draw_grid(100)
        simulator.draw_wall()
        simulator.main()
        simulator.atom_wall_collision()
        #simulator.atom_atom_collision()
        simulator.draw_atom()

        render.text('pos = (%.2f, %.2f)'%(atoms[0].pos.x, atoms[0].pos.y) , None, 30, Vector(atoms[0].pos.x -100, atoms[0].pos.y - 30), black)
        render.text('vel = (%.2f, %.2f)'%(atoms[0].vel.x, atoms[0].vel.y) , None, 30, Vector(atoms[0].pos.x -100, atoms[0].pos.y - 50), black)

        render.text('pos = (%.2f, %.2f)'%(atoms[50].pos.x, atoms[50].pos.y) , None, 30, Vector(atoms[50].pos.x -100, atoms[50].pos.y - 30), blue)
        render.text('vel = (%.2f, %.2f)'%(atoms[50].vel.x, atoms[50].vel.y) , None, 30, Vector(atoms[50].pos.x -100, atoms[50].pos.y - 50), blue)
        
        K = 0
        P = 0
        for atom in atoms:
            K = K + atom.kinetic_energy()
            for other_atom in atoms:
                P = P + world.G*atom.potential_energy(other_atom)
        P = P/2
            
        t_list.append(t)
        K_list.append(K)
        P_list.append(P)
        TOT_E_list.append(K+P)
        
        render.text('t = %.2f'%(t) , None, 30, Vector(-480, -270), red)
        render.text('K_E = %.2f'%(K) , None, 30, Vector(-480, -300), red)
        render.text('P_E = %.2f'%(P) , None, 30, Vector(-480, -330), red)
        render.text('TOT_E = %.2f'%(K+P) , None, 30, Vector(-480, -360), red)
        
    
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        clock.tick(100)
        pg.display.update()
        
        simulator.save_screen('images/gravity_model_demo')
        
        if t > 20:
            break
        
    import matplotlib.pyplot as plt
    
    plt.figure(figsize = (10,10))
    plt.plot(t_list, K_list, color='blue', label = 'Kinetic energy')
    plt.plot(t_list, P_list, color='orange', label = 'Potential energy')
    plt.plot(t_list, TOT_E_list, label = 'Total energy')
    plt.xlabel('time')
    plt.ylabel('energy')
    plt.axhline(sum(K_list)/len(t_list), 0, max(t_list), color='blue', linestyle='--', linewidth='1', label = 'Kinetic energy avg')
    plt.axhline(sum(P_list)/len(t_list), 0, max(t_list), color='orange', linestyle='--', linewidth='1', label = 'Potential energy avg')
    plt.legend(loc = 'best')
    plt.show()
    
    mass_list = []
    kinetic_energy_list = []
    speed_list = []
    e1_speed_list = []
    e2_speed_list = []
    r_list = []
    e1_r_list = []
    e2_r_list = []
    
    for atom in atoms:
        mass_list.append(atom.element.mass)
        kinetic_energy_list.append(atom.kinetic_energy())
        speed_list.append(abs(atom.vel))
        r_list.append(abs(atom.pos))
        
        if atom.element.name == e1.name:
            e1_speed_list.append(abs(atom.vel))
            e1_r_list.append(abs(atom.pos))
            
        elif atom.element.name == e2.name:
            e2_speed_list.append(abs(atom.vel))
            e2_r_list.append(abs(atom.pos))
        
    plt.hist(mass_list, bins = 50)
    plt.xlabel('mass')
    plt.show()
    
    plt.hist(kinetic_energy_list, bins = 50)
    plt.xlabel('kinetic energy')
    plt.show()
    
    plt.hist(speed_list, bins = 50, label = 'Total', alpha = 0.5)
    plt.hist(e1_speed_list, bins = 50, label = 'e1', alpha = 0.5)
    plt.hist(e2_speed_list, bins = 50, label = 'e2', alpha = 0.5)
    plt.xlabel('speed')
    plt.legend(loc = 'best')
    plt.show()
    
    plt.hist(r_list, bins = 50, label = 'Total', alpha = 0.5)
    plt.hist(e1_r_list, bins = 50, label = 'e1', alpha = 0.5)
    plt.hist(e2_r_list, bins = 50, label = 'e2', alpha = 0.5)
    plt.xlabel('distance')
    plt.legend(loc = 'best')
    plt.show()