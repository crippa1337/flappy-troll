import pygame
from globals import *

class Player(pygame.sprite.Sprite):
    x: int
    y: int
    gravity = 0.1
    speed: int
    max_speed = 10
    jump_force = -5
    
    def __init__(self):
        self.image = pygame.image.load("assets/sprites/player.jpg")
        self.rect = self.image.get_rect()
        self.x = (SCREEN_WIDTH / 2) - (self.rect.width / 2)
        self.y = (SCREEN_HEIGHT / 2) - (self.rect.height / 2)
        self.rect.center = (self.x, self.y)
        self.speed = 0
        screen.blit(self.image, self.rect)
        
    def is_jumping(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.speed = self.jump_force
            
    def rotate(self):
        rotated_image = pygame.transform.rotate(self.image, -self.speed * 5)
        new_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=(self.x, self.y)).center)
        return screen.blit(rotated_image, new_rect.topleft)
    
    def update(self):
        self.is_jumping()
        self.rotate()
        
        if self.speed < self.max_speed:
            self.speed += self.gravity
        
        self.y += self.speed