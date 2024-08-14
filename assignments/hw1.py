import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def Cube():
    d = (3**0.5) / 3
    vertices = (
        (d, -d, -d), (d, d, -d), (-d, d, -d), (-d, -d, -d),
        (d, -d, d), (d, d, d), (-d, -d, d), (-d, d, d)
    )
    edges = (
        (0, 1), (0, 3), (0, 4), (2, 1), (2, 3), (2, 7),
        (6, 3), (6, 4), (6, 7), (5, 1), (5, 4), (5, 7)
    )
    glColor(1, 1, 1)  # Draw the cube in white
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Tetrahedron():
    vertices = (
        (0, 1, 0), (3/4, -0.5, -(3**0.5)/4), 
        (-3/4, -0.5, -(3**0.5)/4), (0, -0.5, (3**0.5)/2)
    )
    edges = (
        (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)
    )
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Octahedron():
    d = 1
    vertices = (
        (0, d, 0), (0, -d, 0), (d, 0, 0), 
        (-d, 0, 0), (0, 0, d), (0, 0, -d)
    )
    edges = (
        (0, 2), (0, 3), (0, 4), (0, 5), 
        (1, 2), (1, 3), (1, 4), (1, 5),
        (2, 4), (2, 5), (3, 4), (3, 5)
    )
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Dodecahedron():
    d = (3**0.5) / 3
    vertices = (
        (d, -d, -d), (d, d, -d), (-d, d, -d), (-d, -d, -d),
        (d, -d, d), (d, d, d), (-d, d, d), (-d, -d, d),
        ((3**0.5) / (6 * math.sin(math.radians(54))), math.sin(math.radians(69.1)), 0),
        (-(3**0.5) / (6 * math.sin(math.radians(54))), math.sin(math.radians(69.1)), 0),
        ((3**0.5) / (6 * math.sin(math.radians(54))), -(math.sin(math.radians(69.1))), 0),
        (-(3**0.5) / (6 * math.sin(math.radians(54))), -(math.sin(math.radians(69.1))), 0),
        (0, (3**0.5) / (6 * math.sin(math.radians(54))), math.sin(math.radians(69.1))),
        (0, -(3**0.5) / (6 * math.sin(math.radians(54))), math.sin(math.radians(69.1))),
        (0, (3**0.5) / (6 * math.sin(math.radians(54))), -math.sin(math.radians(69.1))),
        (0, -(3**0.5) / (6 * math.sin(math.radians(54))), -math.sin(math.radians(69.1))),
        (math.sin(math.radians(69.1)), 0, (3**0.5) / (6 * math.sin(math.radians(54)))),
        (math.sin(math.radians(69.1)), 0, -(3**0.5) / (6 * math.sin(math.radians(54)))),
        (-(math.sin(math.radians(69.1))), 0, (3**0.5) / (6 * math.sin(math.radians(54)))),
        (-(math.sin(math.radians(69.1))), 0, -(3**0.5) / (6 * math.sin(math.radians(54))))
    )
    edges = (
        (0, 17), (0, 10), (0, 15), (1, 17), (1, 14), (1, 8), 
        (2, 9), (2, 14), (2, 19), (3, 11), (3, 15), (3, 19), 
        (4, 10), (4, 13), (4, 16), (5, 8), (5, 12), (5, 16), 
        (6, 9), (6, 12), (6, 18), (7, 11), (7, 13), (7, 18), 
        (8, 9), (10, 11), (12, 13), (14, 15), (16, 17), (18, 19)
    )
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Icosahedron():
    phi = (1 + math.sqrt(5)) / 2
    scale = 1 / math.sqrt(phi ** 2 + 1)
    vertices = (
        (-scale, phi * scale, 0), (scale, phi * scale, 0),
        (-scale, -phi * scale, 0), (scale, -phi * scale, 0),
        (0, -scale, phi * scale), (0, scale, phi * scale),
        (0, -scale, -phi * scale), (0, scale, -phi * scale),
        (phi * scale, 0, -scale), (phi * scale, 0, scale),
        (-phi * scale, 0, -scale), (-phi * scale, 0, scale)
    )
    edges = (
        (0, 1), (0, 10), (0, 11), (0, 7), (0, 5), 
        (1, 5), (1, 7), (1, 8), (1, 9), (2, 10), 
        (2, 11), (2, 3), (2, 4), (2, 6), (3, 6), 
        (3, 4), (3, 8), (3, 9), (4, 5), (4, 11), 
        (4, 9), (5, 11), (5, 9), (6, 7), (6, 8), 
        (8, 10), (7, 8), (7, 10), (8, 9), (10, 11)
    )
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def Axes():
    glBegin(GL_LINES)
    glColor(1, 0, 0)  # Red for the x-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((1.5, 0, 0))
    glColor(0, 1, 0)  # Green for the y-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 1.5, 0))
    glColor(0, 0, 1)  # Blue for the z-axis
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 1.5))
    glEnd()

def Circle():
    glPushMatrix()
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -2, 2)
    glColor(1, 0, 1)  # Purple for the limits
    glBegin(GL_LINE_LOOP)
    for i in range(36):
        angle = 2.0 * math.pi * i / 36
        x = math.cos(angle)
        y = math.sin(angle)
        glVertex3fv((x, y, 0))
    glEnd()
    glPopMatrix()

def draw_shape(shape):
    if shape == 1:
        Tetrahedron()
    elif shape == 2:
        Cube()
    elif shape == 3:
        Octahedron()
    elif shape == 4:
        Dodecahedron()
    elif shape == 5:
        Icosahedron()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Homework #1')
    glOrtho(-2, 2, -2, 2, -2, 2)
    glMatrixMode(GL_MODELVIEW)
    current_shape = 2

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            current_shape = 1
        elif keys[pygame.K_2]:
            current_shape = 2
        elif keys[pygame.K_3]:
            current_shape = 3
        elif keys[pygame.K_4]:
            current_shape = 4
        elif keys[pygame.K_5]:
            current_shape = 5

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        Axes()
        draw_shape(current_shape)
        Circle()
        pygame.display.flip()
        pygame.time.wait(10)

main()
