import pygame
import button
import AI

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
FPS = 60

# Setup Display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

# Load Images
try:
    start_img = pygame.image.load('button.png').convert_alpha()
    settings_img = pygame.image.load('settings.png').convert_alpha()
    back_img = pygame.image.load('back.png').convert_alpha()
    menu_bg = pygame.image.load('cover_without_button.png').convert()
    secret_bg = pygame.image.load('secret.png').convert()
    mode_bg = pygame.image.load('start.png').convert()

    aivai_img = pygame.image.load('aivai.png').convert_alpha()
    pvp_img = pygame.image.load('pvp.png').convert_alpha()
    pva_img = pygame.image.load('pvai.png').convert_alpha()
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    exit()

# Buttons
start_button = button.Button(220, 365, start_img, 0.8)
settings_button = button.Button(500, 50, settings_img, 0.8)
back_button = button.Button(20, 20, back_img, 0.6)

# Mode buttons
aivai_button = button.Button(100, 150, aivai_img, 0.8)
pvai_button = button.Button(100, 250, pva_img, 0.8)
pvp_button  = button.Button(100, 350, pvp_img, 0.8)

# State
in_settings = False
in_mode_select = False
clock = pygame.time.Clock()
run = True

# Main Loop
while run:
    clock.tick(FPS)

    # Determine background
    if in_mode_select:
        screen.blit(mode_bg, (0, 0))
    elif in_settings:
        screen.blit(secret_bg, (0, 0))
    else:
        screen.blit(menu_bg, (0, 0))

    # Draw Buttons
    if in_mode_select:
        if aivai_button.draw(screen):
            print("AI vs AI mode selected")  # Replace with function later
        elif pvp_button.draw(screen):
            print("Player vs Player mode selected")
        elif pva_button.draw(screen):
            print("Player vs AI mode selected")
        if back_button.draw(screen):
            in_mode_select = False
    elif in_settings:
        if back_button.draw(screen):
            in_settings = False
    else:
        if start_button.draw(screen):
            in_mode_select = True
        elif settings_button.draw(screen):
            in_settings = True

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

