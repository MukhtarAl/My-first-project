import fileinput

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
FONT = pygame.font.Font('ComicSansMS3.ttf', 25)
FONT1 = pygame.font.Font('ComicSansMS3.ttf', 25)
FONT2 = pygame.font.Font('slkscreb.ttf', 75)
#pygame.set_caption("Ping Pong")

pygame.display.update()

file = open('HighScore.txt', 'r')
Highscore = int(file.read())
file.close()


def start():

    WIN.fill(BLACK)
    WIN.blit(FONT2.render('PING PONG', True, (255,255,255)),(260,200))
    WIN.blit(FONT1.render('click anywhere to begin', True, (255, 255, 255)), (410, 400))

    #Paddle
    PaddlePosition = (875, 310)
    Paddle = pygame.image.load("Paddle.png")
    Paddle = pygame.transform.scale(Paddle, (150, 150))
    WIN.blit(Paddle, PaddlePosition)

    #Ping pong ball
    PingPongBall = pygame.image.load("PingPongBall.png")
    PingPongBall = pygame.transform.scale(PingPongBall, (120, 120))
    WIN.blit(PingPongBall, (100, 325))

    pygame.display.update()
    running = True
    while running == True:
        for events in pygame.event.get():
            if events.type == pygame.MOUSEBUTTONDOWN:
                running = False
                main()
            if events.type == pygame.QUIT:
                running = False

def UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition, PingPongBallPosition, Wall, WallPosition, SCORE, PermanentHighscore):
    SCORE = FONT.render('Score: ' + SCORE, True, (255,255,255))
    HIGHSCORE = FONT.render('HI: ' + str(PermanentHighscore), True, (255, 255, 255))
    WIN.fill(BLUE)

    WIN.blit(SCORE, (30, 10))
    WIN.blit(PingPongTable, (325,200))
    WIN.blit(HIGHSCORE, (200, 10))
    WIN.blit(PingPongBall, PingPongBallPosition)
    WIN.blit(Wall, WallPosition)
    WIN.blit(FONT1.render('press "R" to restart', True, (255, 255, 255)), (800, 10))
    WIN.blit(Paddle, PaddlePosition)





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
        YCHANGE = (PingPongBallDirection - 270) / 90 * -1
        XCHANGE = (1 + YCHANGE) * -1
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
    PingPongBallPosition = (700, 310)
    TempRandom = random.randint(1, 2)
    TempRandom = random.randint(1, 2)
    PingPongBallDirection = 270

    PaddlePosition = (150,310)
    Paddle = pygame.image.load("kungfupanda.png")
    Paddle = pygame.transform.scale(Paddle, (60,60))
    WIN.blit(Paddle, PaddlePosition)

    Wall = pygame.image.load("Wall.png")
    Wall = pygame.transform.scale(Wall, (50,250))
    WallPosition = (775, 200)
    WIN.blit(Wall, WallPosition)

    LOSS = pygame.image.load("kungfuloss.png")
    LOSS = pygame.transform.scale(LOSS, (1100, 650))

    running = True

    SCORE = 0

    PermanentHighscore = Highscore

    fps = pygame.time.Clock()
    time = 0

    while running:
        #time
        fps.tick(90)
        time = pygame.time.get_ticks() // 1000
        time = FONT.render('Seconds: ' + str(time), True, (255, 255, 255))
        WIN.blit(time, (500, 10))
        print (time)
        #print(PingPongBallDirection)
        KEYS = pygame.key.get_pressed()
        XCHANGE = 0
        YCHANGE = 0
        XCHANGE,YCHANGE = KEYCHECK(KEYS)

        if KEYS[pygame.K_LSHIFT]:
            XCHANGE = XCHANGE * 30
            YCHANGE = YCHANGE * 30
        else:
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


        #PaddlePosition = PaddlePosition[0], PingPongBallPosition[1] #AIMBOT


        #UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition,PingPongBallPosition, Wall, WallPosition, str(SCORE))
        #print(PaddlePosition)

        PaddleRectangle = Paddle.get_rect(topleft = PaddlePosition)
        BallRectamgle = PingPongBall.get_rect(topleft = PingPongBallPosition)
        WallRectangle = Wall.get_rect(topleft = WallPosition)

        if PaddleRectangle.colliderect(BallRectamgle) and PingPongBallDirection >= 180:
            #print(PingPongBallDirection)
            PingPongBallDirection = PingPongBallToWall(PingPongBallPosition, WallPosition, PingPongBallDirection)
            SCORE = SCORE + 1
            #print(PingPongBallDirection)
            if PingPongBallDirection > 360:
                PingPongBallDirection = PingPongBallDirection - 360
            elif PingPongBallDirection < 0:
                PingPongBallDirection = PingPongBallDirection + 360
        if BallRectamgle.colliderect(WallRectangle):
            PingPongBallDirection = random.randint(240,312)
        #PaddlePosition = (PaddlePosition[0], PingPongBallPosition[1])


        #BALL SPEED

        PingPongBallX, PingPongBallY = PingPongBallMovement(PingPongBallDirection)
        if SCORE >= 9:
            PingPongBallPosition = PingPongBallPosition[0] + (PingPongBallX * (9 + 0)), PingPongBallPosition[1] + (PingPongBallY * (9 + 0))
        else:
            PingPongBallPosition = PingPongBallPosition[0] + (PingPongBallX * (SCORE + 0.5)), PingPongBallPosition[1] + (PingPongBallY * (SCORE + 0))


        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()

        if KEYS[pygame.K_r]:
            WallPosition = (775, 200)
            PingPongBallPosition = (700, 310)
            PingPongBallDirection = 270
            PaddlePosition = (150, 310)
            if SCORE > PermanentHighscore:
                PermanentHighscore = SCORE
            SCORE = 0


        if PingPongBallPosition[1] < 0 or PingPongBallPosition[1] > 650 or PingPongBallPosition[0] < 0 or PingPongBallPosition[0] > 1100:
            WIN.blit(LOSS, (0, 0))
            pygame.display.update()
            PaddlePosition = (150, 310)

        else:
            UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition, PingPongBallPosition, Wall, WallPosition, str(SCORE), PermanentHighscore)

    if SCORE > PermanentHighscore:
        PermanentHighscore = SCORE
    file = open('Highscore.txt', 'w')
    file.write(str(PermanentHighscore))
    file.close()
    pygame.quit()

if __name__ == "__main__":
    start()