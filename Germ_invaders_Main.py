import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

# Game Variables

icon = pygame.image.load('AA-Innovators-Game/Game Assets/Germs/icon.png')
x = 200
y = 200
scale = 1
img = pygame.image.load('AA-Innovators-Game/Game Assets/Player/4.png')
img = pygame.transform.scale(img,(int(img.get_width() * scale)),(int(img.get_height() * scale)))
rect = img.get_rect()
rect.center = (x, y)
run = True 

# Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Germ Invaders')
pygame.display.set_icon(icon)




# Colors

BG = (69, 42, 29)

def draw_bg():
    screen.fill(BG)
     

# Game Loop
     

while run:
    
    draw_bg()
    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()
pygame.quit()