import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
moving_left = False
moving_right = False 
# Game Variables

 
icon = pygame.image.load('AA-Innovators-Game/Game Assets/Germs/icon.png')

run = True 

# Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Germ Invaders')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load('AA-Innovators-Game/Game Assets/Player/4.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def motion(self,moving_left,moving_right):
        dx = 0
        dy = 0
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx 
        self.rect.y += dy 
               
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


player = Player(200, 200, 1, 5)
 


# Colors

BG = (69, 42, 29)

def draw_bg():
    screen.fill(BG)
     

# Game Loop
     

while run:
    
    draw_bg()
    clock.tick(FPS)
    player.draw()
    player.motion(moving_left,moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False


        # Key Controls


    pygame.display.update()
pygame.quit()