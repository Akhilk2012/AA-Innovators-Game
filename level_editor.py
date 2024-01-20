import pygame
import button
import pickle
import csv

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
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 14
current_tile = 0

# Images

BG_1 = pygame.image.load('AA-Innovators-Game/Game Assets/Background/image.png').convert_alpha()
# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"AA-Innovators-Game/Game Assets/Tiles/{x}.png").convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE,TILE_SIZE))
    img_list.append(img)


# Define colors 
GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,25,25)


# Function for drawing BG
def draw_bg():
    screen.fill(GREEN)
    width = BG_1.get_width()
    for x in range(4):
        screen.blit(BG_1, ((x * width) - scroll * 0.5, 0))


# Grid 
        
def draw_grid():
    # Vertical lines
    for c in range(MAX_COLS + 1):
        pygame.draw.line(screen, WHITE, (c * TILE_SIZE - scroll, 0), (c * TILE_SIZE - scroll,SCREEN_HEIGHT))
    for c in range(ROWS + 1): 
        pygame.draw.line(screen, WHITE, (0,c * TILE_SIZE), (SCREEN_WIDTH,c * TILE_SIZE))


# Creating buttons and list for storing buttons
button_list = []
button_col = 0
button_row = 0
for i in range(len(img_list)):
    tile_button = button.Button(SCREEN_WIDTH + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
    button_list.append(tile_button)
    button_col += 1
    if button_col == 3:
        button_row += 1
        button_col = 0



run = True
while run:
    
    clock.tick(FPS)
    
    draw_bg()
    draw_grid()


    # Drawing panel for buttons
    pygame.draw.rect(screen, GREEN, (SCREEN_WIDTH, 0, SIDE_MARGIN, SCREEN_HEIGHT))


    # Choosing a tile
    button_count = 0
    for button_count, i in enumerate(button_list):
        if i.draw(screen):
            current_tile = button_count

    # Highlight the selected tile
    pygame.draw.rect(screen, RED, button_list[current_tile].rect, 3)

    # Scrolling of Map
    if scroll_left == True and scroll > 0:
        scroll -= 5 * scroll_speed
    if scroll_right == True:
        scroll += 5 * scroll_speed


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keyboard Controls
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            scroll_left = True
        if event.key == pygame.K_RIGHT:
            scroll_right = True
        if event.key == pygame.K_RSHIFT:
            scroll_speed = 5

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            scroll_left = False
        if event.key == pygame.K_RIGHT:
            scroll_right = False
        if event.key == pygame.K_RSHIFT:
            scroll_speed = 1  


    pygame.display.update()

pygame.quit()
