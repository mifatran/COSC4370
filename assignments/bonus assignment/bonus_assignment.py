import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

def calculate_normal(v1, v2, v3):
    # Calculate vectors from the vertices
    vector1 = np.subtract(v2, v1)
    vector2 = np.subtract(v3, v1)
    
    # Compute the cross product
    normal = np.cross(vector1, vector2)
    
    # Normalize the normal vector
    norm = np.linalg.norm(normal)
    if norm == 0:
        return normal  # avoid division by zero
    return normal / norm


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
    
    texture_coords = [((0, 0.75), (0.2, 0.75), (0.2, 1), (0, 1)),
                      ((0.2, 0.75), (0.4, 0.75), (0.4, 1), (0.2, 1)),
                      ((0.4, 0.75), (0.6, 0.75), (0.6, 1), (0.4, 1)),
                      ((0.6, 0.75), (0.8, 0.75), (0.8, 1), (0.6, 1)),
                      ((0.8, 0.75), (1, 0.75), (1, 1), (0.8, 1)),
                      ((0, 0.5), (0.2, 0.5), (0.2, 0.75), (0, 0.75))
                     ]
    
    surfaces = ((3,2,1,0), (6,7,2,3), (4,5,7,6), (0,1,5,4), (2,7,5,1), (6,3,0,4))
    
    NORMALS = [
        ( 0,  0, -1),  # surface 0
        (-1,  0,  0),  # surface 1
        ( 0,  0,  1),  # surface 2
        ( 1,  0,  0),  # surface 3
        ( 0,  1,  0),  # surface 4
        ( 0, -1,  0)   # surface 5
    ]
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1))

    
    glBegin(GL_QUADS)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
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
    
    texture_coords = [((0, 0.7825), (0.2, 0.7825), (0.1, 1)),
                      ((0.2, 0.7825), (0.4, 0.7825), (0.3, 1)),
                      ((0.4, 0.7825), (0.6, 0.7825), (0.5, 1)),
                      ((0.6, 0.7825), (0.8, 0.7825), (0.7, 1))
                     ]
    
    surfaces = ((1,2,0), (2,3,0), (3,1,0), (3,2,1))
    
    NORMALS = []
    for surface_index,surface in enumerate(surfaces):
        normal = calculate_normal(vertices[surface[0]], vertices[surface[1]], vertices[surface[2]])
        NORMALS.append(normal)
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0))
    
    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
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
    
    texture_coords = [((0, 0.7825), (0.2, 0.7825), (0.1, 1)),
                      ((0.2, 0.7825), (0.4, 0.7825), (0.3, 1)),
                      ((0.4, 0.7825), (0.6, 0.7825), (0.5, 1)),
                      ((0.6, 0.7825), (0.8, 0.7825), (0.7, 1)),
                      ((0.8, 0.9675), (1, 0.9675), (0.9, 0.75)),
                      ((0, 0.7175), (0.2, 0.7175), (0.1, 0.5)),
                      ((0.2, 0.7175), (0.4, 0.7175), (0.3, 0.5)),
                      ((0.4, 0.7175), (0.6, 0.7175), (0.5, 0.5))
                     ]
    
    surfaces = ((4,2,0), (2,5,0), (5,3,0), (3,4,0), (1,2,4), (1,5,2), (1,3,5), (1,4,3))
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0))
    
    NORMALS = []
    for surface_index,surface in enumerate(surfaces):
        normal = calculate_normal(vertices[surface[0]], vertices[surface[1]], vertices[surface[2]])
        NORMALS.append(normal)
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0))
    
    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
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
    
    texture_coords = [((0.0382, 305/400), ((0.1618), 305/400), (0.2, 364/400), (0.1, 1), (0, 364/400)),
                      ((0.2382, 305/400), ((0.3618), 305/400), (0.4, 364/400), (0.3, 1), (0.2, 364/400)),
                      ((0.4382, 305/400), ((0.5618), 305/400), (0.6, 364/400), (0.5, 1), (0.4, 364/400)),                      
                      ((0.6382, 305/400), ((0.7618), 305/400), (0.8, 364/400), (0.7, 1), (0.6, 364/400)),
                      ((0.8382, 305/400), ((0.9618), 305/400), (1, 364/400), (0.9, 1), (0.8, 364/400)),
                      ((0.0382, 205/400), ((0.1618), 205/400), (0.2, 264/400), (0.1, 0.75), (0, 264/400)),
                      ((0.2382, 205/400), ((0.3618), 205/400), (0.4, 264/400), (0.3, 0.75), (0.2, 264/400)),
                      ((0.4382, 205/400), ((0.5618), 205/400), (0.6, 264/400), (0.5, 0.75), (0.4, 264/400)),
                      ((0.6382, 205/400), ((0.7618), 205/400), (0.8, 264/400), (0.7, 0.75), (0.6, 264/400)),
                      ((0.8382, 205/400), ((0.9618), 205/400), (1, 264/400), (0.9, 0.75), (0.8, 264/400)),
                      ((0.0382, 105/400), ((0.1618), 105/400), (0.2, 164/400), (0.1, 0.5), (0, 164/400)),
                      ((0.2382, 105/400), ((0.3618), 105/400), (0.4, 164/400), (0.3, 0.5), (0.2, 164/400))
                     ]
    
    
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
    
    NORMALS = []
    for surface_index,surface in enumerate(surfaces):
        normal = calculate_normal(vertices[surface[0]], vertices[surface[1]], vertices[surface[2]])
        NORMALS.append(normal)
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0), (0,0,1), (1,0,0))
    
    for surface_index,surface in enumerate(surfaces):
        glBegin(GL_POLYGON)
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
        glEnd()
    
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
        (6, 10), (7, 8), (7, 10), (8, 9), (10, 11)
    )
    
    texture_coords = [((0, 0.7825), (0.2, 0.7825), (0.1, 1)),
                      ((0.2, 0.7825), (0.4, 0.7825), (0.3, 1)),
                      ((0.4, 0.7825), (0.6, 0.7825), (0.5, 1)),
                      ((0.6, 0.7825), (0.8, 0.7825), (0.7, 1)),
                      ((0.8, 0.7825), (1, 0.7825), (0.9, 1)),
                      
                      ((0, 0.5325), (0.2, 0.5325), (0.1, 0.75)),
                      ((0.2, 0.5325), (0.4, 0.5325), (0.3, 0.75)),
                      ((0.4, 0.5325), (0.6, 0.5325), (0.5, 0.75)),
                      ((0.6, 0.5325), (0.8, 0.5325), (0.7, 0.75)),
                      ((0.8, 0.5325), (1, 0.5325), (0.9, 0.75)),
                      
                      ((0, 0.4675), (0.2, 0.4675), (0.1, 0.25)),
                      ((0.2, 0.4675), (0.4, 0.4675), (0.3, 0.25)),
                      ((0.4, 0.4675), (0.6, 0.4675), (0.5, 0.25)),
                      ((0.6, 0.4675), (0.8, 0.4675), (0.7, 0.25)),
                      ((0.8, 0.4675), (1, 0.4675), (0.9, 0.25)),
                      
                      ((0, 0.2175), (0.2, 0.2175), (0.1, 0.0)),
                      ((0.2, 0.2175), (0.4, 0.2175), (0.3, 0.0)),
                      ((0.4, 0.2175), (0.6, 0.2175), (0.5, 0.0)),
                      ((0.6, 0.2175), (0.8, 0.2175), (0.7, 0.0)),
                      ((0.8, 0.2175), (1, 0.2175), (0.9, 0.0)),
                     ]
    surfaces = ((0,1,7), (1,8,7), (8,6,7), (6,10,7), (10,0,7),
                (11,5,0), (5,9,1), (9,3,8), (3,2,6), (2,11,10),
                
                (5,1,0), (9,8,1), (3,6,8), (2,10,6), (11,0,10),
                (4,5,11), (4,9,5), (4,3,9), (4,2,3), (4,11,2))
    
    COLORS = ((1,0,0), (0,0,1), (1,0,0))
    
    NORMALS = []
    for surface_index,surface in enumerate(surfaces):
        normal = calculate_normal(vertices[surface[0]], vertices[surface[1]], vertices[surface[2]])
        NORMALS.append(normal)
    
    glBegin(GL_TRIANGLES)
    for surface_index,surface in enumerate(surfaces):
        glNormal3fv(NORMALS[surface_index])
        for vertex_index,vertex in enumerate(surface):
            glColor3fv(COLORS[vertex_index])
            glTexCoord2fv(texture_coords[surface_index][vertex_index])
            glVertex3fv(vertices[vertex])
    glEnd()
    
    glColor(1, 1, 1)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

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
        
def loadTexture():
    textureSurface = pygame.image.load('bonus_assignment.png')
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

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glOrtho(-2, 2, -2, 2, -2, 2)
    current_shape = 2
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    
    glMatrixMode(GL_MODELVIEW)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()
    
    glLight(GL_LIGHT0, GL_POSITION,  (0, -10, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    glEnable(GL_DEPTH_TEST)
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    loadTexture()
    
    angle = 0 
    gluLookAt(0, -7, 2, 0, 0, 0, 0, 0, 1)

    
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
            
         
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glColor(1,1,1,1)
        tilt = 15 + 10 * math.cos(angle * math.pi/180) # Tilt as we rotate
        glRotate(tilt, 1, 0, 0) # Tilt a bit to be easier to see
        angle = (angle + 1) % 360
        glRotatef(angle, 1, 0, 1) # Rotate around the box's vertical axis
        draw_shape(current_shape)
        glPopMatrix()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
