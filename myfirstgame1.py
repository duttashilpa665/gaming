import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Race")
clock = pygame.time.Clock()



collision = False

while not collision:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            collision = True

        print(event)

    pygame.display.update()
    clock.tick(30)

pygame.quit()
