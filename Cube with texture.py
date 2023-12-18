import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import * 

def add_texture():
    image = pygame.image.load('texture.jpg')
    data = pygame.image.tostring(image, 'RGBA')
    texID = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texID)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glEnable(GL_TEXTURE_2D)


def draw_square():
    
    glBegin(GL_TRIANGLES)
    glTexCoord2f(0, 0)
    glVertex3f(-1, -1, 0)
    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 0)

    glTexCoord2f(1, 0)
    glVertex3f(1, -1, 0)
    glTexCoord2f(1, 1)
    glVertex3f(1, 1, 0)
    glTexCoord2f(0, 1)
    glVertex3f(-1, 1, 0)
    glEnd()

def draw_cube():

    glPushMatrix()
    glTranslatef(0,0,1)
    draw_square()
    glPopMatrix()
    
    glPushMatrix()
    glTranslatef(1,0,0)
    glRotatef(90,0,1,0)
    draw_square()
    glPopMatrix()

    
    glPushMatrix()
    glTranslatef(0,1,0)
    glRotatef(-90,1,0,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,0,-1)
    glRotatef(180,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(-1,0,0)
    glRotatef(-90,0,1,0)
    draw_square()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(0,-1,0)
    glRotatef(90,1,0,0)
    draw_square()
    glPopMatrix()
    

def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    pygame.display.set_caption("06 Lab Emnacin Jovel Kenth")
    glEnable(GL_DEPTH_TEST)
    add_texture()
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0, 0, -5)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        glRotatef(1,1,1,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    main()