import pygame
import sys
import time
import random

#set pos
LEFT = 0
RIGHT = 1
NEITHER = 2

#set  display values
displayw = 600
displayh = 800

#set colours
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)


def text_objects(text,font,colour):
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text,colour):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText,colour)
    return TextSurf,TextRect

def displayintro(display):
        (tsurf,trect) = message_display("My First Game", black)
        trect.center = ((displayw/2),(displayh/2))
        display.blit(tsurf,trect)
        pygame.display.update()
        # clock.tick(1)

def displayrestartmenu(display,count):
        (tsurf,trect) = message_display("You have lost!"+"You scored:"+ str(count), black)
        trect.center = ((displayw/2),(displayh/2))
        display.blit(tsurf,trect)
        pygame.display.update()

def displaygameboard(display):
        display.fill(black)
        pygame.draw.lines(display,white,False,[(displayw/2-2,0),(displayw/2-2,displayh)],4)
    
        i = 0
        while i<=displayh:
            pygame.draw.lines(display,yellow,False,[(displayw/4-2,i),(displayw/4-2,i+20)],4)
            pygame.draw.lines(display,yellow,False,[(3*displayw/4-2,i),(3*displayw/4-2,i+20)],4)
            i = i + 30

def displaycrash(display):
        (tsurf,trect) = message_display('crashed!',white)
        trect.center = ((displayw/2),(displayh/2))
        display.blit(tsurf,trect)
        pygame.display.update()
        
def displaymissed(display):  
        (tsurf,trect) = message_display('you missed a coin!',white)
        trect.center = ((displayw/2),(displayh/2))
        display.blit(tsurf,trect)
        pygame.display.update()

def displayfps(display,clock):
        font = pygame.font.SysFont(None, 25)
        text = font.render("fps: "+str(clock.get_fps()), True, white)
        display.blit(text,(400,1))  

def displayscore (display,count):
        font = pygame.font.SysFont(None,25)
        text = font.render("Score: "+str(count),True, white)
        display.blit(text,(1,30))
        
def displaydodged(display,count):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Dodged: "+str(count), True, white)
        display.blit(text,(1,1))

def quitgame():
        pygame.mixer.music.stop()
        pygame.quit()
        sys.exit()
        quit()
        
