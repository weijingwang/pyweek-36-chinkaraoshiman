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

    def update(self, surface, pos):
        surface.blit(self.image, self.rect)
        if self.rect.collidepoint(pos):
            return True
        return False
        #     return False
        # return False
    
    def render(self, surface):
        surface.blit(self.image, self.rect)


class itemButton:
    def __init__(self, x, y, content, repurchasable, width=260, height=50):
        """self, x, y, content, repurchase)"""
        self.font = pygame.font.SysFont(None, 40)
        self.content = content

        self.repurchasable = repurchasable
        self.x = x
        self.y = y
        self.width = width
        self.height = height

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

    def update(self, pos):
        if self.rect.collidepoint(pos):
            self.activated = True
        elif self.repurchasable:
            self.activated = False

        if self.activated:
            self.fg = "black"
            self.bg = "green"
        else:
            self.fg = "white"
            self.bg = "black"


    def render(self, surface):
        self.image.fill(self.bg)
        self.text = self.font.render(self.content, False, self.fg) #false antialiasing
        self.image.blit(self.text, self.text_rect)
        surface.blit(self.image, self.rect)




class textInput:
    def __init__(self, x, y, name):
        self.name = name
        # basic font for user typed
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''
        # create rectangle
        self.input_rect = pygame.Rect(x, y, 140, 32)
        
        # color_active stores color(lightskyblue3) which
        # gets active when input box is clicked by user
        self.color_active = pygame.Color('lightskyblue3')
        
        # color_passive store color(chartreuse4) which is
        # color of input box.
        self.color_passive = pygame.Color('chartreuse4')
        self.color = self.color_passive
  
        self.active = False

    def input_control(self, event):
        if self.active:
            if event.type == pygame.KEYDOWN:
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
                    # get text input from 0 to -1 i.e. end.
                    self.user_text = self.user_text[:-1]
                # Unicode standard is used for string
                # formation
                elif event.key == pygame.K_RETURN and self.user_text != "":
                    print(self.name,self.user_text,"rats")
                    self.user_text = ""
                elif event.key == pygame.K_0 or event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:
                    self.user_text += event.unicode
      

    def update(self, pos):
        if self.input_rect.collidepoint(pos):
            self.active = True
        else:
            self.active = False
            # else:
            #     self.active = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if input_rect.collidepoint(event.pos):
        #         active = True
        #     else:
        #         active = False
  
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
            
        # draw rectangle and argument passed which should
        # be on screen

    def render(self, surface):
        pygame.draw.rect(surface, self.color, self.input_rect)
    
        self.text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        
        # render at position stated in arguments
        surface.blit(self.text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        
        # set width of textfield so that text cannot get
        # outside of user's text input
        self.input_rect.w = max(100, self.text_surface.get_width()+10)

