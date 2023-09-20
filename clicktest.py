import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640, 480),0,32)
clock = pygame.time.Clock()

def makeButton(cur, rect):
    if rect.collidepoint(cur):
        print ("button pressed")

square = pygame.Rect((0,0), (32,32))

while True:
    screen.fill((255,255,255))
    screen.fill((55,155,0), square)
    pygame.display.update()
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # left mouse button?
                makeButton(event.pos, square)