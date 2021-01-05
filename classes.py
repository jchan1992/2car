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

#cars
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
                #flip position
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
                #flip position
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

class car3(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.pos = RIGHT
                self.x = displayw*3/4+20
                self.y = displayh - 100
                self.loc = (self.x,self.y)
                self.image = pygame.image.load('car3.jpg')
                self.rect = self.image.get_rect()
                print(self.x,'\t',self.y,'\t',self.rect)

        def update(self):
                #flip position
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

#coins
class coin1(pygame.sprite.Sprite):
        def __init__(self):
                pygame.sprite.Sprite.__init__(self)
                self.rand = random.randint(0,1)
                print("coin1 rand = ",self.rand)
                self.x = displayw/4*self.rand+20
                self.y = 0
                self.loc = (self.x,self.y)
                self.image = pygame.image.load('coin1.jpg')
                self.rect = self.image.get_rect()
                # print(self.x,'\t',self.y,'\t',self.rect)
                
        def update(self,speed):
                self.y = self.y + speed
                self.loc = (self.x,self.y)
                #print(self.x,'\t',self.y,'\t',self.rect)
                
class coin2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.rand = random.randint(2,3)
            
            self.x = displayw/4*self.rand+20
            self.y = 0
            self.loc =(self.x,self.y)
            self.image = pygame.image.load('coin2.jpg')
            self.rect =self.image.get_rect()
            
        def update(self,speed):
                self.y = self.y + speed
                self.loc = (self.x,self.y)
                #print(self.x,'\t',self.y,'\t',self.rect)   

class coin3(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.rand = random.randint(2,3)
            
            self.x = displayw/4*self.rand+20
            self.y = 0
            self.loc =(self.x,self.y)
            self.image = pygame.image.load('coin3.jpg')
            self.rect =self.image.get_rect()
            
        def update(self,speed):
                self.y = self.y + speed
                self.loc = (self.x,self.y)
                #print(self.x,'\t',self.y,'\t',self.rect) 
