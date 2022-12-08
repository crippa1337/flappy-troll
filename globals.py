import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRAY = (30, 30, 30)
WHITE = (255, 255, 255)

pygame.display.set_caption("Flappy Trollface")
pygame.display.set_icon(pygame.image.load("assets/sprites/player.jpg"))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
score = 0