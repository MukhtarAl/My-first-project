import pygame

WIN = pygame.display.set_mode((1100,650))
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0, 173, 239)
WIN.fill(BLUE)

#pygame.set_caption("Colors")

pygame.display.update()

def UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition):
    WIN.fill(BLUE)
    WIN.blit(Paddle,PaddlePosition)



def KEYCHECK(KEYS):
    if KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT]:
        return(0.2,0)#right working

    elif KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT] or (KEYS[pygame.K_w] or KEYS[pygame.K_UP]):
       return(0.2,-0.2)


    #elif KEYS[pygame.K_d] or KEYS[pygame.K_RIGHT] + (KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]):
        #return(0.2,0.2)

    elif KEYS[pygame.K_a] or KEYS[pygame.K_LEFT]:
        return(-0.2,0)

    #elif KEYS[pygame.K_a] or KEYS[pygame.K_LEFT] + (KEYS[pygame.K_w] or KEYS[pygame.K_UP]):
        #return(0.2,-0.2)


    #elif KEYS[pygame.K_a] or KEYS[pygame.K_LEFT] + (KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]):
        #return(-0.2,0.2)

    elif KEYS[pygamwwe.K_w] or KEYS[pygame.K_UP]:#up working
       return(0,-0.2)

    elif KEYS[pygame.K_s] or KEYS[pygame.K_DOWN]:#down working
        return(0,0.2)

    else:
        return(0,0)


def main():
    PingPongTable = pygame.image.load("PingPongTable.jpg")
    PingPongTable = pygame.transform.scale(PingPongTable, (500,250))
    WIN.blit(PingPongTable,(325,200))
    frames  = pygame.time.Clock()

    PingPongBall = pygame.image.load("PingPongBall.png")
    PingPongBall = pygame.transform.scale(PingPongBall, (30,30))
    WIN.blit(PingPongBall, (560,310))

    PaddlePosition = (300,310)
    Paddle = pygame.image.load("Paddle.png")
    Paddle = pygame.transform.scale(Paddle, (50,50))
    WIN.blit(Paddle, PaddlePosition)
    running = True
    while running:
        KEYS = pygame.key.get_pressed()
        XCHANGE = 0
        YCHANGE = 0
        XCHANGE,YCHANGE = KEYCHECK(KEYS)
        PaddlePosition = (PaddlePosition[0]+ XCHANGE,PaddlePosition[1]+ YCHANGE )
        UPDATE(PingPongTable, PingPongBall, Paddle, PaddlePosition)
        print(KEYCHECK(KEYS))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()



    pygame.quit()

if __name__ == "__main__":
    main()