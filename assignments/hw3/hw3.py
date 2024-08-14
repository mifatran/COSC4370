import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

phi = (1 + math.sqrt(5)) / 2

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1),
    (1 / phi, phi, 0),
    (-1 / phi, phi, 0),
    (1 / phi, -phi, 0),
    (-1 / phi, -phi, 0),
    (0, 1 / phi, phi),
    (0, -1 / phi, phi),
    (0, 1 / phi, -phi),
    (0, -1 / phi, -phi),
    (phi, 0, 1 / phi),
    (phi, 0, -1 / phi),
    (-phi, 0, 1 / phi),
    (-phi, 0, -1 / phi)
)

edges = (
    (0, 17), (0, 10), (0, 15), (1, 17), (1, 14), (1, 8), (2, 9), (2, 14), (2, 19),
    (3, 11), (3, 15), (3, 19), (4, 10), (4, 13), (4, 16), (5, 8), (5, 12), (5, 16),
    (6, 9), (6, 12), (6, 18), (7, 11), (7, 13), (7, 18), (8, 9), (10, 11), (12,
    13),
    (14, 15), (16, 17), (18, 19)
)

texture_coords = [(((0.125 - (math.cos(math.radians(72))/4)), 205/300), ((0.125 +
(math.cos(math.radians(72))/4)), 205/300), (0.25, 264/300), (0.125, 1), (0,
264/300)),
                (((0.375 - (math.cos(math.radians(72))/4)), 205/300), ((0.375 +
(math.cos(math.radians(72))/4)), 205/300), (0.5, 264/300), (0.375, 1), (0.25,
264/300)),
                (((0.625 - (math.cos(math.radians(72))/4)), 205/300), ((0.625 +
(math.cos(math.radians(72))/4)), 205/300), (0.75, 264/300), (0.625, 1), (0.5,
264/300)),
                (((0.875 - (math.cos(math.radians(72))/4)), 205/300), ((0.875 +
(math.cos(math.radians(72))/4)), 205/300), (1, 264/300), (0.875, 1), (0.75,
264/300)),
                (((0.125 - (math.cos(math.radians(72))/4)), 105/300), ((0.125 +
(math.cos(math.radians(72))/4)), 105/300), (0.25, 164/300), (0.125, 2/3), (0,
164/300)),
                (((0.375 - (math.cos(math.radians(72))/4)), 105/300), ((0.375 +
(math.cos(math.radians(72))/4)), 105/300), (0.5, 164/300), (0.375, 2/3), (0.25,
164/300)),
                (((0.625 - (math.cos(math.radians(72))/4)), 105/300), ((0.625 +
(math.cos(math.radians(72))/4)), 105/300), (0.75, 164/300), (0.625, 2/3), (0.5,
164/300)),
                (((0.875 - (math.cos(math.radians(72))/4)), 105/300), ((0.875 +
(math.cos(math.radians(72))/4)), 105/300), (1, 164/300), (0.875, 2/3), (0.75,
164/300)),
                (((0.125 - (math.cos(math.radians(72))/4)), 5/300), ((0.125 +
(math.cos(math.radians(72))/4)), 5/300), (0.25, 64/300), (0.125, 1/3), (0,
64/300)),
                (((0.375 - (math.cos(math.radians(72))/4)), 5/300), ((0.375 +
(math.cos(math.radians(72))/4)), 5/300), (0.5, 64/300), (0.375, 1/3), (0.25,
64/300)),
                (((0.625 - (math.cos(math.radians(72))/4)), 5/300), ((0.625 +
(math.cos(math.radians(72))/4)), 5/300), (0.75, 64/300), (0.625, 1/3), (0.5,
64/300)),
                (((0.875 - (math.cos(math.radians(72))/4)), 5/300), ((0.875 +
(math.cos(math.radians(72))/4)), 5/300), (1, 64/300), (0.875, 1/3), (0.75,
64/300))]

surfaces = ((0, 17, 16, 4, 10),
            (15, 14, 1, 17, 0),
            (14, 15, 3, 19, 2),
            (19, 3, 11, 7, 18),
            (11, 10, 4, 13, 7),
            (4, 16, 5, 12, 13),
            (17, 1, 8, 5, 16),
            (14, 2, 9, 8, 1),
            (2, 19, 18, 6, 9),
            (18, 7, 13, 12, 6),
            (3, 15, 0, 10, 11),
            (8, 9, 6, 12, 5)
            )

forced = False
def Dice(vx,vy,vz,texture):
    for surface_index,surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        for vertex_index,vertex in enumerate(surface):
            glTexCoord2fv(texture[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()
        
    glBegin(GL_LINES)
    glColor(0,1,0,1)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()
    
def loadTexture():
    textureSurface = pygame.image.load('hw3.png')
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
glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()
loadTexture()
run = True
angle = 0 # Rotation angle about the vertical axis
glColor(1,1,1,1)
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
    glColor(1,1,1,1)
    tilt = 15 + 10 * math.cos(angle * math.pi/180) # Tilt as we rotate
    glRotate(tilt, 1, 0, 0) # Tilt a bit to be easier to see
    angle = (angle + 1) % 360
    glRotatef(angle, 0, 0, 1) # Rotate around the box's vertical axis
    Dice(0,0,0,texture_coords)
    
    # glColor4f(0.5, 0.5, 0.5, 1)
    # glBegin(GL_POLYGON)
    # glVertex3f(-10, -10, -2)
    # glVertex3f(10, -10, -2)
    # glVertex3f(10, 10, -2)
    # glVertex3f(-10, 10, -2)
    # glEnd()
    glPopMatrix()
    
    pygame.display.flip()
    pygame.time.wait(30)
    
pygame.quit()