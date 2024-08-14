#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #1
Example solution to the homework assignment, It could use some cleanup of the
values and the functions

@author: danielbiediger
"""

import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def Draw(vertices, edges):
    glColor(1,1,1) # Draw the cube in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Tetrahedron():
    d = math.sqrt(3)/3
    vertices = (
        (d, d, -d), (-d, -d, -d), (d, -d, d), (-d, d, d)
        )

    edges = (
        (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
        )
    Draw(vertices, edges)
    

def Cube():
    d = math.sqrt(3)/3
    vertices = (
        (d, -d, -d), (d, d, -d), (-d, d, -d), (-d, -d, -d),
        (d, -d, d), (d, d, d), (-d, -d, d), (-d, d, d)
        )

    edges = (
        (0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4),
        (6,7), (5,1), (5,4), (5,7)
        )
    Draw(vertices, edges)


def Octohedron():
    vertices = (
        (1, 0, 0), (0, -1, 0), (-1, 0, 0), (0, 1, 0),
        (0, 0, 1), (0, 0, -1)
        )

    edges = (
        (0,1), (0,3), (0,4), (0,5), (1,2), (1,4), (1,5), (2,3),
        (2,4), (2,5), (3,4), (3,5)
        )
    Draw(vertices, edges)


def Dodecahedron():
    phi = (1 + math.sqrt(5))/2
    k = 1/math.sqrt(3)
    vertices = (
        (k, k, k), (-k, k, k),
        (k, -k, k), (-k, -k, k),
        (k, k, -k), (-k, k, -k),
        (k, -k, -k), (-k,-k,-k),
        (0, k/phi, k*phi), (0, k/phi, -k*phi),
        (0, -k/phi, k*phi), (0, -k/phi, -k*phi),
        (k/phi, k*phi, 0), (k/phi, -k*phi, 0),
        (-k/phi, k*phi, 0), (-k/phi, -k*phi, 0),
        (k*phi, 0, k/phi), (k*phi, 0, -k/phi),
        (-k*phi, 0, k/phi), (-k*phi, 0, -k/phi)
        )

    edges = (
       (0, 8), (0, 12), (0, 16), (1, 8), (1, 14), (1, 18), 
       (2, 10), (2, 13), (2, 16), (3, 10), (3, 15), (3, 18), 
       (4, 9), (4, 12), (4, 17), (5, 9), (5, 14), (5, 19), 
       (6, 11), (6, 13), (6, 17), (7, 11), (7, 15), (7, 19), 
       (8, 10), (9, 11), (12, 14), (13, 15), (16, 17), (18, 19)
        )

    Draw(vertices, edges)


def Icosahedron():
   
    phi = (1 + math.sqrt(5))/2
    k = 1/math.sqrt(1+phi**2)
    vertices = (
        (k, 0, phi*k), (-k, 0, phi*k),
        (phi*k, k, 0), (phi*k, -k, 0),
        (0, -phi*k, k), (0, -phi*k, -k), 
        (-phi*k, k, 0), (-phi*k, -k, 0),
        (0, phi*k, k), (0, phi*k, -k),
        (k, 0, -phi*k), (-k, 0, -phi*k)
        )

    edges = (
        (0,1), (0,2), (0,3), (0,4), (0,8), (1,4), (1,6), (1,7),
        (1,8), (2,3), (2,8), (2,9), (2,10), (3,4), (3,5), (3,10),
        (4,5), (4,7), (5,7), (5,10), (5,11), (6,7), (6,8), (6,9),
        (6,11), (7,11), (8,9), (9,10), (9,11), (10,11)
        )

    Draw(vertices, edges)


def Axes():
    glBegin(GL_LINES)
    glColor(1,0,0) # Red for the x-axis
    glVertex3fv((0,0,0))
    glVertex3fv((1.5,0,0))
    glColor(0,1,0) # Green for the y-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,1.5,0))
    glColor(0,0,1) # Blue for the z-axis
    glVertex3fv((0,0,0))
    glVertex3fv((0,0,1.5))
    glEnd()


def main():
    pygame.init()
    display = (800,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #1')
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    shape = Cube
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
                #quit()
        
        keys = pygame.key.get_pressed() # Get pressed keys
    
        # pick shape based on keys pressed
        options = {pygame.K_1:Tetrahedron, pygame.K_2:Cube, pygame.K_3:Octohedron,
                   pygame.K_4:Dodecahedron, pygame.K_5:Icosahedron}
        for key,value in options.items():
            if keys[key]:
                shape = value

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Axes()
        shape()
        
        # Draw the circle on the screen
        glPushMatrix()
        glLoadIdentity()
        glOrtho(-2, 2, -2, 2, -2, 2)
        glColor(1,0,1) # Purple for the limits
        glBegin(GL_LINE_LOOP)
        for i in range(36):
            angle = 2.0 * math.pi * i / 36
            x = math.cos(angle)
            y = math.sin(angle)
            glVertex3fv((x, y, 0))
        glEnd()
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()