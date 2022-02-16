import pygame
import random

class ClaseBonus(pygame.sprite.Sprite):
    def __init__(self,pos,m):#Constructor
        pygame.sprite.Sprite.__init__(self)
        self.tipo=random.randrange(2)
        #self.tipo=1
        self.m=m
        self.image=m[0][self.tipo]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.vely=0

    def update(self,p,velfondo):
        self.rect.x+=velfondo
        p.blit(self.image,self.rect)
