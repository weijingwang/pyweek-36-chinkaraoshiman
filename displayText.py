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

class shopText:
    def __init__(self, pos, text='eretyh',size=80):
        self.font = pygame.font.SysFont(None, size)
        self.text = text
        self.pos = pos

        self.image = self.font.render(str(text), True, (255, 0, 0))#.convert_alpha()
        self.image_rect = self.image.get_rect(bottomright = pos)#center = surface.get_rect().center)
        
        self.temp_surface = pygame.Surface(self.image.get_size())
        self.temp_surface.fill('black')
        self.temp_surface.blit(self.image, self.image_rect)

    def update(self, new_text):
        self.text = new_text
        # if self.text != new_text:
        self.image = self.font.render(str(self.text), True, (255, 0, 0))#.convert_alpha()
        self.image_rect = self.image.get_rect(bottomright = self.pos)#center = surface.get_rect().center)
        self.temp_surface = pygame.Surface(self.image.get_size())
        self.temp_surface.fill('black')
        self.temp_surface.blit(self.image, self.image_rect)


    def render(self,surface):
        # image = self.font.render(str(text), True, (255, 0, 0))#.convert_alpha()
        # image_rect = image.get_rect(bottomright = (x,y))#center = surface.get_rect().center)
        
        # temp_surface = pygame.Surface(image.get_size())
        # temp_surface.fill('black')
        # temp_surface.blit(image, image_rect)
        surface.blit(self.temp_surface, self.image_rect)
        surface.blit(self.image, self.image_rect)