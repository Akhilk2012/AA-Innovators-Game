import pygame

pygame.init()

clock = pygame.time.Clock()
FPS = 60

# Making our game window

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600
LOWER_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + LOWER_MARGIN))
pygame.display.set_caption('Level Editor for our Game')

# Game Variables

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1

# Images

BG_1 = pygame.image.load('AA-Innovators-Game/Game Assets/Background/BackGround.png').convert_alpha()

# Define colors 
GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,25,25)
# Function for drawing BG
def draw_bg():
    screen.fill(GREEN)
    width = BG_1.get_width()
    for x in range(1):
        screen.blit(BG_1, ((x * width) - scroll * 0.5, 0))


run = True
while run:
    
    clock.tick(FPS)
    
    draw_bg()


    # Scrolling of Map
    if scroll_left == True and scroll > 0:
        scroll -= 5
    if scroll_right == True:
        scroll += 5


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keyboard Controls
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            scroll_left = True
        if event.key == pygame.K_RIGHT:
            scroll_right = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            scroll_left = False
        if event.key == pygame.K_RIGHT:
            scroll_right = False  


    pygame.display.update()

pygame.quit()