import pygame
from Map_Loader import MapLoader
from Player_Loader import Player

pygame.init()

width, height, game_map = MapLoader.loader('data/laby-03.dat')

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_width))
pygame.display.set_caption("Boum Game :)")

tile_width = screen_width // width
tile_height = screen_height // height

screen = pygame.display.set_mode((tile_width * width, tile_height * height))

player = Player("NomDuJoueur", 1, 1, 5)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for y in range(height):
        for x in range(width):
            if game_map[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x * tile_width, y * tile_height, tile_width, tile_height))

    pygame.display.flip()

pygame.quit()