import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640

# Game Variables

icon = pygame.image.load('AA-Innovators-Game/Game Assets/Germs/icon.png')

run = True 

# Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Germ Invaders')
pygame.display.set_icon(icon)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('AA-Innovators-Game/Game Assets/Player/4.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self):
        screen.blit(self.image, self.rect)


player = Player(200, 200, 1)        


# Colors

BG = (69, 42, 29)

def draw_bg():
    screen.fill(BG)
     

# Game Loop
     

while run:
    
    draw_bg()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Key Controls


    pygame.display.update()
pygame.quit()