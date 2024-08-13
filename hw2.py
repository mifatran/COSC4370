import math
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_orbit(radius, color, segments=100):
    glBegin(GL_LINE_LOOP)
    glColor3fv(color)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, 0)  # Draw in the XY plane
    glEnd()

def draw_sphere(radius, color, slices=30, stacks=30):
    glColor3fv(color)
    quadric = gluNewQuadric()
    gluQuadricNormals(quadric, GLU_SMOOTH)
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, radius, slices, stacks)
    gluDeleteQuadric(quadric)

def main():
    pygame.init()
    display = (800, 800)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption('Homework #2')
    glOrtho(-16, 16, -16, 16, -16, 16)
    glMatrixMode(GL_MODELVIEW)

    rot_x = 0  # Vertical rotation angle
    speed_factor = 0.5
    mecury_angle = 0
    venus_angle = 0
    earth_angle = 0
    moon_angle = 0
    mars_angle = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and rot_x < 90:
            rot_x += 10  # Increment rotation
        if pressed[pygame.K_DOWN] and rot_x > 0:
            rot_x -= 10  # Decrement rotation

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        glRotatef(rot_x, 1, 0, 0)  # Rotate around X-axis

        # Draw the Sun
        draw_sphere(2.0, (1, 1, 0))

        # Draw orbits
        draw_orbit(3.9, (0.1, 0.1, 0.1))  # Mercury orbit
        draw_orbit(7.2, (0.1, 0.1, 0.1))  # Venus orbit
        draw_orbit(10.0, (0.1, 0.1, 0.1)) # Earth orbit
        draw_orbit(15.0, (0.1, 0.1, 0.1)) # Mars orbit

        # Calculate and draw Mercury
        mecury_x = 3.9 * math.cos(math.radians(mecury_angle))
        mecury_y = 3.9 * math.sin(math.radians(mecury_angle))
        glPushMatrix()
        glTranslatef(mecury_x, mecury_y, 0)  # Move to Mercury's position
        draw_sphere(0.38, (1, 0, 0))  # Red sphere for Mercury
        glPopMatrix()

        # Calculate and draw Venus
        venus_x = 7.2 * math.cos(math.radians(venus_angle))
        venus_y = 7.2 * math.sin(math.radians(venus_angle))
        glPushMatrix()
        glTranslatef(venus_x, venus_y, 0)  # Move to Venus's position
        draw_sphere(0.95, (0, 1, 0))  # Green sphere for Venus
        glPopMatrix()

        # Calculate and draw Earth and Moon
        earth_x = 10 * math.cos(math.radians(earth_angle))
        earth_y = 10 * math.sin(math.radians(earth_angle))
        glPushMatrix()
        glTranslatef(earth_x, earth_y, 0)  # Move to Earth's position
        draw_sphere(1.0, (0, 0, 1))  # Blue sphere for Earth

        draw_orbit(1.5, (0.1, 0.1, 0.1))  # Moon's orbit
        moon_x = 1.5 * math.cos(math.radians(moon_angle))
        moon_y = 1.5 * math.sin(math.radians(moon_angle))
        glPushMatrix()
        glTranslatef(moon_x, moon_y, 0)  # Move to Moon's position
        draw_sphere(0.27, (1, 1, 1))  # White sphere for Moon
        glPopMatrix()  # Pop Moon's transformation

        glPopMatrix()  # Pop Earth's transformation

        # Calculate and draw Mars
        mars_x = 15 * math.cos(math.radians(mars_angle))
        mars_y = 15 * math.sin(math.radians(mars_angle))
        glPushMatrix()
        glTranslatef(mars_x, mars_y, 0)  # Move to Mars's position
        draw_sphere(0.53, (1, 0, 0))  # Red sphere for Mars
        glPopMatrix()

        glPopMatrix()

        # Update the angle for the next frame
        mecury_angle += (360 / 87.97) * speed_factor
        venus_angle += (360 / 224.7) * speed_factor
        earth_angle += (360 / 365.26) * speed_factor
        moon_angle += (360 / 27.3) * speed_factor
        mars_angle += (360 / 686.98) * speed_factor

        # Keep angles within 0-360 degrees
        if mecury_angle >= 360:
            mecury_angle -= 360
        if venus_angle >= 360:
            venus_angle -= 360
        if earth_angle >= 360:
            earth_angle -= 360
        if moon_angle >= 360:
            moon_angle -= 360
        if mars_angle >= 360:
            mars_angle -= 360

        pygame.display.flip()
        pygame.time.wait(10)

main()
