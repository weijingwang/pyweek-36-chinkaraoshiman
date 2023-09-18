import pygame

#diologe box near bottom of screen like visual novel
#show next text after press space
#despawn when diologue is finished
# https://www.youtube.com/watch?v=ZP4VOoDNuZA (tutorial source)
# font ideas: free royalty free open source victiorian British font (on weijing's behalf LOL)

pygame.font.init() # imports all the libraries from pygame derived from text 
grab_all = pygame.font.get_fonts() # to get all text fonts available on the machine, just to see what desirable font complements our game the most

width = 800
height = 800
screen = pygame.display.set_mode((width, height))
text_font = pygame.font.SysFont("Comic Sans", 35) # font is default for now but might change the font later, just testing it to see how it looks

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  textTBD = text_font.render("hello world", 1, (244,244,244)) # (text, alias/anti-aliasing, text color in RGB) // testing color for now, currently set to white
  screen.blit(textTBD, (0, 650)) # parameters:(text, width/height of text) || screen.blit() writes text onto a screen

  pygame.display.update()

## what to do left:
## showing the next text when space is pressed

pygame.quit()

# exit = pygame.font.quit()
