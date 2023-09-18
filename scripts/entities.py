import pygame

WALKING_SPEED_CONSTANT = 7

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        self.image = pygame.Surface(size)
        self.image.fill('black')

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def update(self, tilemap, movement=(0, 0)):
        print(self.pos)
        print(self.velocity)

        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}
        
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        
        self.pos[0] += frame_movement[0] * WALKING_SPEED_CONSTANT 
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[0] > 0: #moving left
                    entity_rect.right = rect.left
                    self.collisions['right'] = True
                if frame_movement[0] < 0: #moving right
                    entity_rect.left = rect.right
                    self.collisions['left'] = True
                self.pos[0] = entity_rect.x
        
        self.pos[1] += frame_movement[1]
        entity_rect = self.rect()
        for rect in tilemap.physics_rects_around(self.pos):
            if entity_rect.colliderect(rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collisions['down'] = True
                if frame_movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collisions['up'] = True
                self.pos[1] = entity_rect.y
        
        self.velocity[1] = min(15, self.velocity[1] + 2)

        if self.collisions['down'] or self.collisions['up']:
            self.velocity[1] = 0
        
    def jump(self):
        self.velocity[1] = -25

    def render(self, surf, offset=(0, 0)):
        # surf.fill('white')
        surf.blit(self.image, (self.pos[0] - offset[0], self.pos[1] - offset[1]))
        