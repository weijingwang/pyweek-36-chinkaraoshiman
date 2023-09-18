import pygame

class counterText:
    def __init__(self, ):
        self.font = pygame.font.SysFont(None, 100)
    def render(self,text,surface):
        image = self.font.render(str(text), True, (255, 0, 0)).convert_alpha()
        image_rect = image.get_rect(center = surface.get_rect().center)
        surface.blit(image, image_rect)



