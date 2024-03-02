import pygame
import cpu


#TO-DO configure keyboard and sound
pygame.init()
screen = pygame.display.set_mode((64*10, 32*10))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
