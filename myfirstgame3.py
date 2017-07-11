import pygame

pygame.init()


gameWidth = 800
gameHeight = 600

gamecolor1= (0,0,0)
gamecolor2= (255, 255, 204)
gamecolor3= (153, 0, 0)

gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption("Race")
clock = pygame.time.Clock()

mycar = pygame.image.load("ball3.png")

def car(x,y):
    gameDisplay.blit(mycar,(x,y))

def game_looping():
    
    x = gameWidth * 0.5 #Initial loation
    y = gameHeight * 0.8 #Initial loation

    car_width = 59 

    x_movement= 0 #Movement variable

    collision = False

    while not collision:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                collision = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_movement = x_movement - 5
                elif event.key == pygame.K_RIGHT:
                    x_movement = x_movement + 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_movement = 0

        x = x+x_movement
        
        gameDisplay.fill(gamecolor2)
        car(x,y)
        if x > gameWidth - car_width or x<0:
            collision = True
            
        pygame.display.update()
        clock.tick(30)

game_looping()
pygame.quit()
quit()
