import pygame, sys
from globals import * 
from player import Player
from obstacles import Pipes


pygame.init()
 
def death_screen():
    dead = True
    while dead:
        clock.tick(144)
        screen.fill(GRAY)
        font = pygame.font.SysFont('Calibri', 40, True) 
        
        troll = pygame.image.load("assets/sprites/player.jpg")
        troll = pygame.transform.scale(troll, (300, 300))
        
        screen.blit(troll, ((SCREEN_WIDTH / 2) - (troll.get_width() / 2), (SCREEN_HEIGHT / 2) - (troll.get_height() / 2) - 200))
        
        text = font.render("You died! Press SPACE to restart", True, WHITE)
        screen.blit(text, ((SCREEN_WIDTH / 2) - (text.get_width() / 2), (SCREEN_HEIGHT / 2) - (text.get_height() / 2)))
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            dead = False
            game_loop()
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
            
        pygame.display.flip()
 
def game_loop():
    player = Player()
    pipes = Pipes()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        clock.tick(144)
        screen.fill(GRAY)
        
        pipes.draw_pipes()
        pipes.check_collisions(player)
        if pipes.check_collisions(player):
            running= False
            death_screen()
        
        player.update()
        if player.y > SCREEN_HEIGHT - player.rect.height:
            running = False
            death_screen()

        pygame.display.flip()


if __name__ == "__main__":
    game_loop()