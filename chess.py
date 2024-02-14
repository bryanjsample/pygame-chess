import pygame

pygame.init()

# set up window
size = (800, 800)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit