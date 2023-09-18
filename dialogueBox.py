import pygame

#diologe box near bottom of screen like visual novel
#show next text after press space
#despawn when diologue is finished

class dialoguePanel:
  def __init__(self):
    pygame.init()
    self.width = 250
    self.height = 215
    self.screen = pygame.display.set_mode((self.width, self.height))
