import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 640
moving_left = False
moving_right = False
idle = True 
spc = 0
# Game Variables

icon = pygame.image.load('AA-Innovators-Game/Game Assets/Germs/icon.png')

run = True 

# Screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Germ Invaders')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60
#
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 
        self.update_time = pygame.time.get_ticks()
        for i in range(8):
            img = pygame.image.load(f'AA-Innovators-Game/Game Assets/Player/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
            self.animation_list.append(img)

        self.image = self.animation_list[self.frame_index]
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

    def update_animation(self):
        # Keep updating animation
        ANIMATION_COOLDOWN = 100
        # Update image depending on current frame
        self.image = self.animation_list[self.frame_index]
        # Check if time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN :
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If the animation is done repeat
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0 

    def update_action(self, new_action):
        # Confirming if the updated action is different from the previous one.
        if new_action != self.action:
            self.action = new_action
            # Updating animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
               
    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)



player = Player(200, 200, 0.2, 5)
    


# Colors

BG = (69, 42, 29)

def draw_bg():
    screen.fill(BG)
     

# Game Loop
     

while run:
    
    draw_bg()
    draw_floor(spc)
    clock.tick(FPS)
    player.update_animation()
    player.draw()


    # Player Actions
    if moving_left or moving_right:
        player.update_action(1)
    else:
        player.update_action(0)
    player.motion(moving_left, moving_right)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                idle == False 
                moving_left = True
            if event.key == pygame.K_d:
                idle == False 
                moving_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                idle = False
                moving_left = False
            if event.key == pygame.K_d:
                idle = False
                moving_right = False


        # Key Controls


    pygame.display.update()
pygame.quit()
