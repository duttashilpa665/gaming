import pygame
import time
import random

pygame.init()


gameWidth = 800
gameHeight = 600

gamecolor1= (0,0,0)#Black
gamecolor2= (255, 255, 204)
gamecolor3= (153, 0, 0)

gameDisplay = pygame.display.set_mode((gameWidth,gameHeight))
pygame.display.set_caption("Race")
clock = pygame.time.Clock()

mycar = pygame.image.load("ball3.png")

#creation of obstacle
def obstacle(obstacleX, obstacleY, obstacleH, obstacleW,color):
    pygame.draw.rect(gameDisplay,color, [obstacleX,obstacleY,obstacleH,obstacleW])
    
#draw the car in display  
def car(x,y):
    gameDisplay.blit(mycar,(x,y))

def text_object(text,font):
    textSurface = font.render(text, True, gamecolor3)
    return textSurface, textSurface.get_rect()
    
def message_display(text): #Message section
    message = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_object(text,message)
    TextRect.center = ((gameWidth/2.0),(gameHeight/2))
    gameDisplay.blit(TextSurf,TextRect)

    pygame.display.update()

    time.sleep(2)
    game_looping()

    
def gamecrash(): #Crash function
    message_display("You've crashed buddy")
    
def game_looping():
    
    x = gameWidth * 0.5 #Initial loation
    y = gameHeight * 0.8 #Initial loation

    car_width = 59 

    x_movement= 0 #Movement variable
    obstacle_startX = random.randrange(0, gameWidth)
    obstacle_startY = -500
    obstacle_height = 100
    obstacle_width = 100
    obstacle_speed = 15
    

    collision = False

    while not collision:
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            #event handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_movement = x_movement - 5
                elif event.key == pygame.K_RIGHT:
                    x_movement = x_movement + 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_movement = 0

        x = x+x_movement #updated location
        
        gameDisplay.fill(gamecolor2)#fill the window with color

         
        obstacle(obstacle_startX, obstacle_startY, obstacle_height, obstacle_width,gamecolor1)#call the obstacle
        obstacle_startY = obstacle_startY+obstacle_speed
        car(x,y)#calling the car function

        if x > gameWidth - car_width or x < 0:
            gamecrash()

        if obstacle_startY > gameWidth:
            obstacle_startY = 0 - obstacle_height
            obstacle_startX = random.randrange(0, gameWidth)

        if y < obstacle_startY+obstacle_height:
            if x > obstacle_startX and x < obstacle_startX + obstacle_width or x + car_width > obstacle_startX and x+car_width<obstacle_startX+obstacle_width:
                gamecrash()
            
        pygame.display.update()
        clock.tick(50)#speed of the animation

game_looping()
pygame.quit()
quit()
