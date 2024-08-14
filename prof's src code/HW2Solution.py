#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Homework #1
This is the starter code for the first homework assignment.
It should run as is and will serve as the starting point for development.
"""
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


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


def Circle(radius = 1.0):
    glPushMatrix()
    glColor(0.5,0.5,0.5) # Purple for the limits
    glBegin(GL_LINE_LOOP)
    STEPS = 72
    for i in range(STEPS):
        angle = 2.0 * math.pi * i / STEPS
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3fv((x, y, 0))
    glEnd()
    glPopMatrix()


def draw_sphere(radius, lats = 32, longs = 16):
    quadric = gluNewQuadric()
    gluSphere(quadric, radius, lats, longs)  # Draw sphere


def main():
    pygame.init()
    display = (1000,1000)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    pygame.display.set_caption('Homework #2')
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glOrtho(-20, 20, -20, 20, -20, 20)
    glMatrixMode(GL_MODELVIEW)
    mercury_orbit = 0
    venus_orbit = 0
    earth_orbit = 0
    moon_orbit = 0
    mars_orbit = 0
    angle = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        keys = pygame.key.get_pressed() # Get pressed keys
        if keys[pygame.K_UP]:
            if(angle < 0):
                angle += 1
                glRotate(1, 1, 0, 0)
        if keys[pygame.K_DOWN]:
            if(angle > -90):
                angle -= 1
                glRotate(-1, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #Axes() # Draw the axes
        #Cube() # Draw the cube
        #Circle() # Draw the limit circle
        glColor(1.0, 1.0,0)
        draw_sphere(2.0,50,50)
        glPushMatrix()
        Circle(3.9)
        glRotate(mercury_orbit, 0, 0, 1)
        glTranslated(3.9, 0, 0)
        glColor(1.0,0,0)
        draw_sphere(0.38,50,50)
        glPopMatrix()
        glPushMatrix()
        Circle(7.2)
        glRotate(venus_orbit, 0, 0, 1)
        glTranslated(7.2, 0, 0)
        glColor(0,1.0,0)
        draw_sphere(0.95,50,50)
        glPopMatrix()
        glPushMatrix()
        Circle(10)
        glRotate(earth_orbit, 0, 0, 1)
        glTranslated(10, 0, 0)
        Circle(1.5)
        glColor(0,0,1.0)
        draw_sphere(1,50,50)
        glColor(0.8, 0.8, 0.8)
        glRotate(moon_orbit, 0, 0, 1)
        glTranslated(1.5, 0, 0)
        draw_sphere(0.27,50,50)
        glPopMatrix()
        glPushMatrix()
        Circle(15)
        glRotate(mars_orbit, 0, 0, 1)
        glTranslated(15, 0, 0)
        glColor(1.0,0,0)
        draw_sphere(0.5,50,50)
        glPopMatrix()
        
        mercury_orbit += 365.26 / 87.97
        venus_orbit += 365.26 / 224.70
        earth_orbit += 1
        moon_orbit += 365.26 / 27.3
        mars_orbit += 365.26 / 686.98
        pygame.display.flip()
        pygame.time.wait(20)


main()