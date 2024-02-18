import pygame
from Map_Loader import MapLoader

pygame.init()

width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Boum Game :)")

game_map = MapLoader.loader('data/laby-03.dat')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.QUIT()