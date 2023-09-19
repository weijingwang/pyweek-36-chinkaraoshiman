import pygame

class Button:
    def __init__(self, x, y, width, height, fg, bg, content):
        """self, x, y, width, height, fg, bg, content)"""
        self.font = pygame.font.SysFont(None, 40)
        self.content = content

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.fg =fg
        self.bg = bg

        self.image = pygame.Surface((self.width, self.height)) 
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def update(self, surface, pos, pressed):
        surface.blit(self.image, self.rect)
        if self.rect.collidepoint(pos):
            if pressed:
                return True
        return False
        #     return False
        # return False

class itemButton:
    def __init__(self, x, y, content):
        """self, x, y, content)"""
        self.font = pygame.font.SysFont(None, 40)
        self.content = content

        self.x = x
        self.y = y
        self.width = 260
        self.height = 50

        self.activated = False
        if self.activated:
            self.fg = "black"
            self.bg = "green"
        else:
            self.fg = "white"
            self.bg = "black"

        self.image = pygame.Surface((self.width, self.height)) 
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.center = (self.x, self.y)

        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.text, self.text_rect)

    def update(self, surface, pos, pressed, owned):
        if owned:
            self.fg = "black"
            self.bg = "green"
        else:
            self.fg = "white"
            self.bg = "black"
        self.image.fill(self.bg)
        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.image.blit(self.text, self.text_rect)
        surface.blit(self.image, self.rect)
        if self.rect.collidepoint(pos):
            if pressed:
                return True
        return False
        #     return False
        # return False

# class itemButtonGrid():
#     def __init__(self, dict_data):
#         self.dict_data = dict_data
#     def update(self, surface, pos, pressed):
#         surface.blit(self.image, self.rect)
#         if self.rect.collidepoint(pos):
#             if pressed:
#                 return True
#         return False