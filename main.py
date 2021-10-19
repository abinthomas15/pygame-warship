import pygame
import os

WIDTH , HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("WarShip")

WHITE = (255,255,255)
FPS = 60

YELLOW_SPACSHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACSHIP_IMAGE,(50,30)),90)
RED_SPACSHIP_IMAGE = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
RED_SPACSHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACSHIP_IMAGE,(50,30)),270) 

def draw_window(red,yellow):

    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACSHIP,(red.x,red.y))

    pygame.display.update()

def yellow_handle_pressed(key_pressed,yellow):
    if key_pressed [pygame.K_a]:
        yellow.x -= 5

def main():
    red = pygame.Rect(700,200,50,30)
    yellow = pygame.Rect(100,200,50,30)

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_pressed(keys_pressed,yellow)

        draw_window(red,yellow)


    pygame.quit()


if __name__ == '__main__':
    main()
