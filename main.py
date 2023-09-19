import pygame
from player import Player


#main game is platformer
#player jumps and stands on walls
#player can shoot gun really fast
#enemies will attack player when in range, otherwise, walk around
#bullets
#player can talk to npcs
#player moves to room/change level by going though a door

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("platformer")

clock = pygame.time.Clock()
FPS = 60


RED = (255, 0, 0)

def draw_bg():
	screen.fill((0,66,66))
	#pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

player = Player(200, 200, 1)

def player_updates():
    screen.blit(player.image, player.rect)
    player.movement()


run = True
while run:

    clock.tick(FPS)

    draw_bg()
    
    player_updates()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False

        #if event.type == pygame.KEYDOWN:
        #    if event.key == pygame.K_a:

    

    pygame.display.update()

pygame.quit()