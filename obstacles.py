import random
import pygame
from globals import *

class Pipe():
    x: int
    y1: int
    y2: int
    width: int
    height: int
    velocity: float
    
    def __init__(self, velocity):
        self.width = 100
        self.height = 800
        self.velocity = velocity
        
    def move_pipe(self):
        self.x -= self.velocity
        

class Pipes():
    pipes: 'list[Pipe]'
    pipe_collisions: 'list[Pipe]'
    max_pipes: int
    
    def __init__(self):
        self.pipes = []
        self.pipe_collisions = []
        self.max_pipes = 2
    
    def spawn_pipe(self, y):
        velocity = 2 + (score/10)
        pipe = Pipe(velocity)
        pipe.x = SCREEN_WIDTH + pipe.width
        pipe.y = y
        
        self.pipes.append(pipe)
        
    def spawn_pipe_pair(self):
        self.pipe_collisions.clear()
        if len(self.pipes) < self.max_pipes:
            y1 = random.randint(-700, -200)
            # Gap of 200
            y2 = y1 + 1000
            self.spawn_pipe(y1)
            self.spawn_pipe(y2)
    
    def draw_pipes(self, screen=screen):
        self.spawn_pipe_pair()
        for pipe in self.pipes:
            pipe.move_pipe()
            new_pipe = pygame.draw.rect(screen, WHITE, (pipe.x, pipe.y, pipe.width, pipe.height))
            self.pipe_collisions.append(new_pipe)
            if pipe.x < -pipe.width:
                self.pipes.remove(pipe)
                
    def check_collisions(self, player):
        for pipe in self.pipe_collisions:
            if pipe.colliderect(player.rect):
                return True
        return False        
            
    
    