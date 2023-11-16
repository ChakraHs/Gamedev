import pygame
import sys
import math 

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My First Pygame Program")


Running = True
angle = 2

R = 200

# Main game loop
while Running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                R -= 10
            
            if event.key == pygame.K_UP:
                R += 10
            
            if event.key == pygame.K_RIGHT:
                angle += 4

            if event.key == pygame.K_LEFT:
                angle -= 4

    screen.fill((0,0,0))

    #for i in range(0,width + 1, 20):
    #    pygame.draw.line(screen, (255, 255, 255), (0,i), (i, height), width=1)

    #for i in range(0,height, 20):
    #    pygame.draw.line(screen, (255, 255, 255), (i,0), (width, i), width=1)

    for i in range(0, 360, angle):
        pygame.draw.circle(screen, (255, 255, 255), (width//2 + R*math.cos((i/360)* 2*math.pi), height//2 + R*math.sin((i/360)* 2 *math.pi)), R//2, width=1)
    

    pygame.display.update()
