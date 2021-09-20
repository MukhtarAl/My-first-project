import pygame


WIN = pygame.display.set_mode((500,500))


WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
WIN.fill(BLUE)
#fps =

#pygame.set_caption("Colors")


pygame.display.update()

def main():
    running = True
    frames  = pygame.time.Clock()
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                running = False
        pygame.display.update()



    pygame.quit()




if __name__ == "__main__":
    main()

