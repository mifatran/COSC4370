import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GL.shaders import compileProgram, compileShader
from OpenGL.GLU import *
import numpy as np
import pywavefront

scene = pywavefront.Wavefront('teapot.obj', collect_faces=True)



def cal_normal(v0, v1, v2):
    normal = np.cross(v1 - v0, v2 - v0)
    norm = np.linalg.norm(normal)
    normal = normal / norm
        
    return normal

def draw_obj(verts, faces, NORMALS):
    glColor3fv((0,1,0))
    glBegin(GL_TRIANGLES)
    for i_face, face in enumerate(faces):
        glNormal3fv(NORMALS[i_face])
        for i_vertex, vertex in enumerate(face):
            index = (i_face + i_vertex) % 2
            glVertex3fv(verts[vertex])
    glEnd()

# Main loop

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()
    
    scene = pywavefront.Wavefront('teapot.obj', collect_faces=True)

    verts = []
    faces = []

    # Extract vertices and faces
    vertex_map = {}
    for mesh in scene.mesh_list:
        for face in mesh.faces:
            face_indices = []
            for vertex_i in face:
                vertex = scene.vertices[vertex_i]
                if vertex not in vertex_map:
                    vertex_map[vertex] = len(verts)
                    verts.append(vertex)
                face_indices.append(vertex_map[vertex])
            faces.append(tuple(face_indices))

    # Calculate normals for each face
    NORMALS = []
    for face in faces:
        v0 = np.array(verts[face[0]])
        v1 = np.array(verts[face[1]])
        v2 = np.array(verts[face[2]])
        NORMALS.append(cal_normal(v0, v1, v2))

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    glLight(GL_LIGHT0, GL_POSITION,  (10, -20, 0, 1)) # point light from the below
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    
    glEnable(GL_DEPTH_TEST)
    
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE ) 
    
    glShadeModel(GL_SMOOTH)
        
    glOrtho(-15,15,-15,15,-15,15)
    glTranslate(0,-5, 0)
    glRotatef(-100, 1, 0, 0)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  
                
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        
        glRotate(2,0,0,1)
        draw_obj(verts, faces, NORMALS)
        
        
        pygame.display.flip()
        clock.tick(50)
        pygame.time.wait(1)

main()
