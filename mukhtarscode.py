import pygame
import random
WIN = pygame.display.set_mode((1100,650))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 173, 239)
WIN.fill(BLUE)

#pygame.set_caption("Ping Pong")

pygame.display.update()

def UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition, PingPongBallPosition, Wall, WallPosition):
    WIN.fill(BLUE)
    WIN.blit(PingPongTable, (325,200))
    WIN.blit(Paddle,PaddlePosition)
    WIN.blit(PingPongBall, PingPongBallPosition)
    WIN.blit(Wall, WallPosition)




def KEYCHECK(KEYS):
    #DONW
    if KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:
        if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
            return (0.2, 0.2)
        if KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
            return (-0.2, 0.2)
        else:
            return(0, 0.2)
    #UP
    if KEYS[pygame.K_w] or KEYS[pygame.K_UP]:
        if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
            return (0.2, -0.2)
        if KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
            return (-0.2, -0.2)
        else:
            return(0, -0.2)
    #RIGHT
    if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
        if KEYS[pygame.K_w] or KEYS[pygame.K_UP]:
            return (0.2, -0.2)
        if KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:
            return (0.2, 0.2)
        else:
            return(0.2,0)
    #LEFT
    if KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
        if KEYS[pygame.K_w] or KEYS[pygame.K_UP]:
            return (-0.2, -0.2)
        if KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:
            return (-0.2, 0.2)
        else:
            return (-0.2, 0)

    else:
        return(0,0)


def PingPongBallMovement(PingPongBallDirection):

    if PingPongBallDirection >= 90 and PingPongBallDirection <= 180:
        XCHANGE = (PingPongBallDirection- 90) /90
        YCHANGE = 1 - XCHANGE
    if PingPongBallDirection >= 180 and PingPongBallDirection <= 270:
        XCHANGE = (PingPongBallDirection - 180) / 180 * -1
        YCHANGE = (1 + XCHANGE) * -1
    if PingPongBallDirection >= 270 and PingPongBallDirection <= 360:
        XCHANGE = (PingPongBallDirection - 270) / 270 * -1
        YCHANGE = (1 + XCHANGE) * -1
    if PingPongBallDirection >= 0 and PingPongBallDirection <= 90:
        XCHANGE = PingPongBallDirection / 90
        YCHANGE = (1 - XCHANGE) * -1




    pygame.display.update()
def main():
    PingPongTable = pygame.image.load("PingPongTable.jpg")
    PingPongTable = pygame.transform.scale(PingPongTable, (500,250))
    WIN.blit(PingPongTable,(325,200))
    frames  = pygame.time.Clock()

    PingPongBall = pygame.image.load("PingPongBall.png")
    PingPongBall = pygame.transform.scale(PingPongBall, (30,30))
    WIN.blit(PingPongBall, (560,310))
    PingPongBallPosition = (767, 310)
    TempRandom = random.randint(1, 2)
    if TempRandom == 1:
        PingPongBallDirection = 90
    else:
        PingPongBallDirection = 270

    PaddlePosition = (150,310)
    Paddle = pygame.image.load("Paddle.png")
    Paddle = pygame.transform.scale(Paddle, (50,50))
    WIN.blit(Paddle, PaddlePosition)

    Wall = pygame.image.load("Wall.png")
    Wall = pygame.transform.scale(Wall, (50,250))
    WallPosition = (775, 200)
    WIN.blit(Wall, WallPosition)
    running = True
    while running:
        KEYS = pygame.key.get_pressed()
        XCHANGE = 0
        YCHANGE = 0
        XCHANGE,YCHANGE = KEYCHECK(KEYS)
        XCHANGE = XCHANGE * 15
        YCHANGE = YCHANGE * 15
        PaddlePosition = (PaddlePosition[0]+ XCHANGE,PaddlePosition[1]+ YCHANGE)

        #left barrier
        if PaddlePosition[0] < -3.5999999999999486:
            PaddlePosition = (-3.5999999999999486, PaddlePosition[1])
        #right barrier
        if PaddlePosition[0] > 303:
           PaddlePosition = (303, PaddlePosition[1])
        if PaddlePosition[1] < -1.0:
            PaddlePosition = (PaddlePosition[0], -1)
        #bottom barrier
        if PaddlePosition[1] > 600:
            PaddlePosition = (PaddlePosition[0], 600)
        UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition,PingPongBallPosition, Wall, WallPosition)
        print(PaddlePosition)
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False


        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()