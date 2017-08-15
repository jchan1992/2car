#!/usr/bin/python

# load functions and classes from test2
import test2
from test2 import *   

#main game loop
def gameloop():
        #set score counter
        score = 0

        #instantiate car objects
        car11 = test2.car1()
        car22 = test2.car2()

        #instantiate surface
        pygame.init()
        #instantiate clock
        clock = pygame.time.Clock()
        #set screen size
        screen = pygame.display.set_mode((displayw,displayh))
        pygame.display.set_caption("My first game")
        pygame.mixer.music.load('initiald.mid')
        pygame.mixer.music.play(-1)
        end_game = False
        

        #loop
        while not end_game:

                #draw background
                screen.fill(black)
                pygame.draw.lines(screen,yellow,False,[(displayw/4-2,0),(displayw/4-2,displayh)],4)
                pygame.draw.lines(screen,yellow,False,[(displayw/2-2,0),(displayw/2-2,displayh)],4)
                pygame.draw.lines(screen,yellow,False,[(3*displayw/4-2,0),(3*displayw/4-2,displayh)],4)
                #draw car
                screen.blit(car11.image,car11.loc)
                screen.blit(car22.image,car22.loc)
                #keyboard inputs
                for event in pygame.event.get():
                        print(event)
                        if event.type == pygame.QUIT:
                                end_game = True
                        if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_q:
                                        end_game = True
                                if event.key == pygame.K_LEFT:
                                        car11.update()
                                        screen.blit(car11.image,car11.loc)
                                if event.key == pygame.K_RIGHT:
                                        car22.update()
                                        screen.blit(car22.image,car22.loc)
                                if event.key == pygame.K_UP:
                                        displaycrash(screen)

                displaydodged(screen,score)
                clock.tick(60)
                # print(clock.get_fps())
                displayfps(screen,clock)
                pygame.display.update()
                

        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
        quit()

gameloop()
