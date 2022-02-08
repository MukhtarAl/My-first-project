import pygame
import random
import math
pygame.font.init()
WIN = pygame.display.set_mode((1100,650))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 173, 239)
WIN.fill(BLUE)
FONT = pygame.font.Font('ComicSansMS3.ttf', 50)
#pygame.set_caption("Ping Pong")

pygame.display.update()

def UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition, PingPongBallPosition, Wall, WallPosition, SCORE):
    SCORE = FONT.render(SCORE, True, (255,255,255))
    WIN.fill(BLUE)
    WIN.blit(SCORE, (10, 10))
    WIN.blit(PingPongTable, (325,200))
    WIN.blit(Paddle,PaddlePosition)
    WIN.blit(PingPongBall, PingPongBallPosition)
    WIN.blit(Wall, WallPosition)




def KEYCHECK(KEYS):
    #DONW
    if KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:
        if KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
            return (-0.2, 0.2)
        if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
            return (0.2, 0.2)
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


def PingPongBallToWall(PingPongBallPosition, WallPosition, PingPongBallDirection):
    Direction = PingPongBallDirection + 180
    if Direction > 360:
        Direction = Direction - 360

    return Direction


def PingPongBallMovement(PingPongBallDirection):

    if PingPongBallDirection >= 90 and PingPongBallDirection <= 180:
        YCHANGE = (PingPongBallDirection- 90) /90
        XCHANGE = 1 - YCHANGE
    if PingPongBallDirection >= 180 and PingPongBallDirection <= 270:
        XCHANGE = (PingPongBallDirection - 180) / 90 * -1
        YCHANGE = 1 + XCHANGE
    if PingPongBallDirection >= 270 and PingPongBallDirection <= 360:
        YCHANGE = (PingPongBallDirection - 360) / 90
        XCHANGE = (1 + YCHANGE)
    if PingPongBallDirection >= 0 and PingPongBallDirection <= 90:
        XCHANGE = PingPongBallDirection / 90
        YCHANGE = (1 - XCHANGE) * -1


    return XCHANGE, YCHANGE



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

    SCORE = 0

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
        #top barrier
        if PaddlePosition[1] < -1.0:
            PaddlePosition = (PaddlePosition[0], -1)
        #bottom barrier
        if PaddlePosition[1] > 600:
            PaddlePosition = (PaddlePosition[0], 600)


        PaddlePosition = PaddlePosition[0], PingPongBallPosition[1] #AIMBOT


        UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition,PingPongBallPosition, Wall, WallPosition, str(SCORE))
        #print(PaddlePosition)

        PaddleRectangle = Paddle.get_rect(topleft = PaddlePosition)
        BallRectamgle = PingPongBall.get_rect(topleft = PingPongBallPosition)
        WallRectangle = Wall.get_rect(topleft = WallPosition)

        if PaddleRectangle.colliderect(BallRectamgle):
            print(PingPongBallDirection)
            PingPongBallDirection = PingPongBallToWall(PingPongBallPosition, WallPosition, PingPongBallDirection)
            SCORE = SCORE + 1
            print(PingPongBallDirection)
            if PingPongBallDirection > 360:
                PingPongBallDirection = PingPongBallDirection - 360
            elif PingPongBallDirection < 0:
                PingPongBallDirection = PingPongBallDirection + 360
        if BallRectamgle.colliderect(WallRectangle):
            PingPongBallDirection = random.randint(240,320)
        #PaddlePosition = (PaddlePosition[0], PingPongBallPosition[1])

        PingPongBallX, PingPongBallY = PingPongBallMovement(PingPongBallDirection)
        PingPongBallPosition = PingPongBallPosition[0] + (PingPongBallX * (SCORE + 5)), PingPongBallPosition[1] + (PingPongBallY * (SCORE + 0))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False

        pygame.display.update()

        if KEYS[pygame.K_r]:
            WallPosition = (775, 200)
            PingPongBallPosition = (767, 310)
            PingPongBallDirection = 270
            PaddlePosition = (150, 310)
            SCORE = 0


    pygame.quit()

if __name__ == "__main__":
    main()