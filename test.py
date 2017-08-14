# import pygame
import test2
from test2 import *   

def gameloop():

        score = 0

        car11 = test2.car1()
        car22 = test2.car2()

        pygame.init()

        clock = pygame.time.Clock()
        display = pygame.display.set_mode((displayw,displayh))
        pygame.display.set_caption("My first game")

        pygame.mixer.music.load('initiald.mid')
        pygame.mixer.music.play(-1)	

        end_game = False

        while not end_game:
                display.fill(black)
                pygame.draw.lines(display,yellow,False,[(displayw/4-2,0),(displayw/4-2,displayh)],4)
                pygame.draw.lines(display,yellow,False,[(displayw/2-2,0),(displayw/2-2,displayh)],4)
                pygame.draw.lines(display,yellow,False,[(3*displayw/4-2,0),(3*displayw/4-2,displayh)],4)

                display.blit(car11.image,car11.loc)
                display.blit(car22.image,car22.loc)
                for event in pygame.event.get():
                        print(event)
                        if event.type == pygame.QUIT:
                                end_game = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        end_game = True
                                if event.key == pygame.K_LEFT:
                                        car11.update()
                                        display.blit(car11.image,car11.loc)
                                if event.key == pygame.K_RIGHT:
                                        car22.update()
                                        display.blit(car22.image,car22.loc)
                                if event.key == pygame.K_UP:
                                        displaycrash(display)
                # displayfps(display,clock)
                        displaydodged(display,score)
                clock.tick(120)
                pygame.display.update()
                

        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
        quit()

gameloop()
