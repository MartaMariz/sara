import pygame

from support import import_folder

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character()
        self.frame_index = 0
        self.animation_speed = 0.05
        self.status = 'idle'
        print(self.animations)
        self.image = self.animations['idle'][0]
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0.1
        self.gravity = 0.4
        self.jump_force = -5
    
    def import_character(self):
        character_path = './images'
        self.animations = {'idle':[], 'run':[]}
        for animation in self.animations.keys():
            full_path = character_path + '/' + animation
            print(full_path)
            self.animations[animation] = import_folder(full_path)
            print(self.animations[animation])
    
    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        self.image = animation[int(self.frame_index)]
        
            
    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x += 1
        elif keys[pygame.K_LEFT]:
            self.direction.x -= 1
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.jump()

    def get_status(self):

       # if self.direction.y > 1:
       #     self.status = 'fall'
       # elif self.direction.y < 0:
    #    self.status = 'jump'
        
        if self.direction.x != 0:
            self.status = 'run'

        else:
            self.status = 'idle'
    
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_force

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        
