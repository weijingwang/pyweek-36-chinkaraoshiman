import pygame

class counterText:
    def __init__(self, size=80):
        self.font = pygame.font.SysFont(None, size)

    def render(self,text,surface, x, y):
        image = self.font.render(str(text), True, (255, 0, 0))#.convert_alpha()
        image_rect = image.get_rect(bottomright = (x,y))#center = surface.get_rect().center)
        
        temp_surface = pygame.Surface(image.get_size())
        temp_surface.fill('black')
        temp_surface.blit(image, image_rect)
        surface.blit(temp_surface, image_rect)
        surface.blit(image, image_rect)