import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

#Game variables

icon = pygame.image.load('AA-Innovators-Game/Game Assets/Germs/icon.png')

run = True

# Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Germ Invaders')
pygame.display.set_icon(icon)

# Game Loop

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()