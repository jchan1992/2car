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

class car1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.pos = LEFT
                self.x = 20
                self.y = displayh - 100
                self.loc = (self.x,self.y)
                self.image = pygame.image.load('car1.jpg')
                self.rect = self.image.get_rect()
                print(self.x,'\t',self.y,'\t',self.rect)

        def update(self):
                self.pos = self.pos^1
                if self.pos == LEFT:
                        self.x = 20
                        self.y = displayh - 100
                        self.loc = (self.x,self.y)
                else:
                        self.x = displayw/4+20
                        self.y = displayh - 100
                        self.loc = (self.x,self.y)
                print(self.x,'\t',self.y,'\t',self.rect)

class car2(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.pos = RIGHT
                self.x = displayw*3/4+20
                self.y = displayh - 100
                self.loc = (self.x,self.y)
                self.image = pygame.image.load('car2.jpg')
                self.rect = self.image.get_rect()
                print(self.x,'\t',self.y,'\t',self.rect)

        def update(self):
                self.pos = self.pos^1
                if self.pos == RIGHT:
                        self.x = displayw*3/4+20
                        self.y = displayh - 100
                        self.loc = (self.x,self.y)
                else:
                        self.x = displayw/2+20
                        self.y = displayh - 100
                        self.loc = (self.x,self.y)
                print(self.x,'\t',self.y,'\t',self.rect)

class coin1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.x = 0
                self.y = 0
                self.loc = (self.x,self.y)
                self.image = pygame.image.load('coin1.jpg')
                self.rect = self.image.get_rect()
                # print(self.x,'\t',self.y,'\t',self.rect)

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

def displaycrash(display):
        (tsurf,trect) = message_display('crashed!',white)
        trect.center = ((displayw/2),(displayh/2))
        display.blit(tsurf,trect)
        pygame.display.update()

def displayfps(display,clock):
        font = pygame.font.SysFont(None, 25)
        text = font.render("fps: "+str(clock.get_fps()), True, white)
        display.blit(text,(400,1))      
        
def displaydodged(display,count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, white)
    display.blit(text,(1,1))

def randomcoin(display,rand):
        coin11 = coin1()
        
