import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


vertices = ((1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
            (1, -1, 1), (1, 1, 1), (-1, -1, 1), (-1, 1, 1))


edges = ((0,1), (0,3), (0,4), (2,1), (2,3), (2,7), (6,3), (6,4),
         (6,7), (5,1), (5,4), (5,7))

texture_coords = [((0, 0.5), (0.333, 0.5), (0.333, 1), (0, 1)),
                  ((0.333, 0.5), (0.666, 0.5), (0.666, 1), (0.333, 1)),
                  ((0.666, 0), (1, 0), (1, 0.5), (0.666, 0.5)),
                  ((0.333, 0), (0.666, 0), (0.666, 0.5), (0.333, 0.5)),
                  ((0, 0), (0.333, 0), (0.333, 0.5), (0, 0.5)),
                  ((0.666, 0.5), (1, 0.5), (1, 1), (0.666, 1))
                 ]
NORMALS = [
    ( 0,  0, -1),  # surface 0
    (-1,  0,  0),  # surface 1
    ( 0,  0,  1),  # surface 2
    ( 1,  0,  0),  # surface 3
    ( 0,  1,  0),  # surface 4
    ( 0, -1,  0)   # surface 5
]

surfaces = ((0,1,2,3), (3,2,7,6), (6,7,5,4), (4,5,1,0), (1,5,7,2), (4,0,3,6))

COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))

forced = False
def Cube(texture):
    glBegin(GL_QUADS)

    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def loadTexture():
    textureSurface = pygame.image.load('dice_faces.png')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid

pygame.init()
display = (800, 800)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
glTranslatef(0, 0, -8)


glLight(GL_LIGHT0, GL_POSITION,  (0, -10, 0, 1)) # point light from the below
glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 0.2))
glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

glEnable(GL_DEPTH_TEST)

glEnable(GL_LIGHTING)
glEnable(GL_LIGHT0)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )

viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

loadTexture()

run = True
angle = 1 # Rotation angle about the vertical axis


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # Capture an escape key press to exit
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False

    # init model view matrix
    glLoadIdentity()

    # apply view matrix
    glMultMatrixf(viewMatrix)

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glPushMatrix()
    angle = (angle + 1) % 360
    glRotatef(angle, 1, 1, 1)
    Cube(texture_coords)

    glPopMatrix()

    pygame.display.flip()
    pygame.time.wait(10)
    clock.tick(50)

pygame.quit()