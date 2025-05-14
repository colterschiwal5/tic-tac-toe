import pygame
import button

#create display window
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


#load button images
start_img = pygame.image.load('button .png').convert_alpha()
settings_img = pygame.image.load('settings.png').convert_alpha()
background_img = pygame.image.load('cover_without_button .png').convert_alpha()
#create button instances
start_button = button.Button(220, 365, start_img, 0.8)
settings_button = button.Button(500, 50, settings_img, 0.8)
#game loop

bg_image = pygame.image.load('cover_without_button .png')
run = True
while run:
	
	screen.blit(bg_image, (0,0))

	if start_button.draw(screen):
		print('START')
	elif settings_button.draw(screen):
		bg_image = pygame.image.load('secret.png')
		print(pygame.image.load('back.png'))
	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()