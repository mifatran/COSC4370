#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSC 4370 Sample solution to the programming problem on the midterm exam.
"""
import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


def Circle(radius = 1.0):
    glPushMatrix()
    #glColor(0.5,0.5,0.5) # Purple for the limits
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
    pygame.display.set_caption('Exam #1')
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_CULL_FACE)
    glOrtho(-5, 5, -5, 5, -5, 5)
    glMatrixMode(GL_MODELVIEW)
    orbits = [0, 120, 240]
    y_angle = 0
    x_angle = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        keys = pygame.key.get_pressed() # Get pressed keys
        glPushMatrix()
        
        if keys[pygame.K_LEFT]:
            if(y_angle < 45):
                y_angle +=1
        if keys[pygame.K_RIGHT]:
            if(y_angle > -45):
                y_angle -=1
        if keys[pygame.K_UP]:
            if(x_angle < 45):
                x_angle += 1
        if keys[pygame.K_DOWN]:
            if(x_angle > -45):
                x_angle -= 1
        if keys[pygame.K_r]:
            x_angle = 0
            y_angle = 0
                
                
        glRotate(y_angle, 0, 1, 0)
        glRotate(x_angle, 1, 0, 0)        
        
        glColor(1.0, 1.0, 0)
        draw_sphere(2.0,50,50)
        
        glPushMatrix()
        glRotate(-90, 1, 0, 0)
        glColor(1.0,0.4,0.4)
        Circle(4)
        glRotate(orbits[0], 0, 0, 1)
        glTranslatef(4, 0, 0)
        draw_sphere(0.5,50,50)
        glPopMatrix()
        
        glPushMatrix()
        glRotate(-90, 1, 0, 0)
        glRotate(60, 0, 1, 0)
        glColor(0.4,1.0,0.4)
        Circle(4)
        glRotate(orbits[1], 0, 0, 1)
        glTranslatef(4, 0, 0)
        draw_sphere(0.5,50,50)
        glPopMatrix()
        
        glPushMatrix()
        glRotate(-90, 1, 0, 0)
        glRotate(-60, 0, 1, 0)
        glColor(0.4,0.4,1.0)
        Circle(4)
        glRotate(orbits[2], 0, 0, 1)
        glTranslatef(4, 0, 0)
        draw_sphere(0.5,50,50)
        glPopMatrix()
        
        glPopMatrix()
        
        for i in range(3):
            orbits[i] = (orbits[i] + 2) % 360
        
        pygame.display.flip()
        pygame.time.wait(5)


main()