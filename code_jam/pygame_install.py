# Raymond Nault
# Basketball
# Putting Basketball on screen

import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
my_image = pygame.image.load('assignments/code_jam/images/basketball_small.png')
image_rect = my_image.get_rect(center=(320, 240))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))

    image_rect.x += 1

    if image_rect.x > screen.get_width():
        image_rect.x = -image_rect.width
    screen.blit(my_image, image_rect)
    pygame.display.flip()
    clock.tick(60)