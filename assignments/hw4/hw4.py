import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import pywavefront

def cal_normal(v0, v1, v2):
    normal = np.cross(v1 - v0, v2 - v0)
    norm = np.linalg.norm(normal)
    return normal / norm if norm != 0 else np.array([0.0, 0.0, 0.0])

def compute_vertex_normals(verts, faces):
    vertex_normals = np.zeros_like(verts)
    face_normals = []
    
    for face in faces:
        v0, v1, v2 = [verts[vertex] for vertex in face]
        normal = cal_normal(v0, v1, v2)
        face_normals.append(normal)
        for vertex in face:
            vertex_normals[vertex] += normal
    
    # Normalize the vertex normals
    vertex_normals = np.array([n / np.linalg.norm(n) if np.linalg.norm(n) != 0 else n for n in vertex_normals])
    return vertex_normals

def draw_obj(verts, faces, vertex_normals):
    glColor3f(0, 0.5, 1.0)
    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glNormal3fv(vertex_normals[vertex])
            glVertex3fv(verts[vertex])
    glEnd()

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
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
                vertex = np.array(scene.vertices[vertex_i])
                if tuple(vertex) not in vertex_map:
                    vertex_map[tuple(vertex)] = len(verts)
                    verts.append(vertex)
                face_indices.append(vertex_map[tuple(vertex)])
            faces.append(tuple(face_indices))

    # Calculate vertex normals
    vertex_normals = compute_vertex_normals(np.array(verts), faces)

    # OpenGL setup
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)  # Move the camera back

    # Lighting setup
    glLightfv(GL_LIGHT0, GL_POSITION, (10, -20, 0, 1))  # Light position moved lower and right
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.1, 0.1, 0.1, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1))

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    glShadeModel(GL_SMOOTH)  # Enable smooth shading
    
    glOrtho(-15,15,-15,15,-15,15)
    glTranslate(0,-5, 0)
    glRotatef(-100, 1, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glRotatef(2, 0, 0, 1)  # Rotate the object for dynamic view
        draw_obj(verts, faces, vertex_normals)
        
        pygame.display.flip()
        clock.tick(50)
        pygame.time.wait(1)

main()
