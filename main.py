import pygame

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
pygame.display.set_caption("TEST")


x = 200
y = 200
scale = 3
# img = pygame.image.load(PATH TO IMG)
# img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
# rect = img.get_rect()
# rect.center = (x,y)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()