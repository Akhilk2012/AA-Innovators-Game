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
BELOW_MARGIN = 100
SIDE_MARGIN = 300

screen = pygame.display.set_mode((SCREEN_WIDTH + SIDE_MARGIN, SCREEN_HEIGHT + BELOW_MARGIN))
pygame.display.set_caption('Level Editor for our Game')

# Game Variables

scroll_left = False
scroll_right = False
scroll = 0
scroll_speed = 1
ROWS = 16
MAX_COLS = 150
TILE_SIZE = SCREEN_HEIGHT // ROWS
TILE_TYPES = 16
current_tile = 0
level = 0

# Images

BG_1 = pygame.image.load('AA-Innovators-Game/Game Assets/Background/image.png').convert_alpha()
# store tiles in a list
img_list = []
for x in range(TILE_TYPES):
    img = pygame.image.load(f"AA-Innovators-Game/Game Assets/Tiles/{x}.png").convert_alpha()
    img = pygame.transform.scale(img, (TILE_SIZE,TILE_SIZE))
    img_list.append(img)
save_img = pygame.image.load('AA-Innovators-Game/Game Assets/Menu/Buttons/save_btn.png').convert_alpha()

# Define colors 
GREEN = (144,201,120)
WHITE = (255,255,255)
RED = (200,25,25)


# Created empty tile list
world_data = []
for row in range(ROWS):
    r = [-1] * MAX_COLS
    world_data.append(r)

# Creating Ground
for tile in range(0, MAX_COLS):
    world_data[ROWS -1][tile] = 0


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


# Functions for drawing tiles
def draw_world():
    for y, row in enumerate(world_data):
        for x, tile in enumerate(row):
            if tile >= 0:
                screen.blit(img_list[tile], (x * TILE_SIZE - scroll, y * TILE_SIZE))


# Creating buttons and list for storing buttons
save_button = button.Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT + BELOW_MARGIN - 50, save_img, 1)

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
    draw_world()

    if save_button.draw(screen):
        with open(f'level{level}_data.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for row in world_data:
                writer.writerow(row)

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
    if scroll_right == True and scroll < (MAX_COLS * TILE_SIZE):
        scroll += 5 * scroll_speed

    # Adding new tiles and getting the mouse position
    pos = pygame.mouse.get_pos()
    x = (pos[0] + scroll) // TILE_SIZE
    y = pos[1] // TILE_SIZE

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Check if the audit are within the tile area.
    if pos[0] < SCREEN_WIDTH and pos[1] < SCREEN_HEIGHT:
        # Updating the tile value
        if pygame.mouse.get_pressed()[0] == 1:
            if world_data[y][x] != current_tile:
                world_data[y][x] = current_tile
        if pygame.mouse.get_pressed()[2] == 1:
            world_data[y][x] = -1

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