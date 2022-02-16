import pygame
import random
from Constantes import *
class ClaseGenerador(pygame.sprite.Sprite):
    def __init__(self, pos,m,velx=-1):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,10])
        self.rect=self.image.get_rect()
        self.m=m
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.con=self.Aleatorio()
        self.activo=True
        self.velx=velx
    def Aleatorio(self):
        #return random.randrange(5)
        return random.randrange(100,130)
    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,izq,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def update(self,p,izq):
        if self.activo:
            self.con-=1
        if self.con<50 and self.con>=45:
            imagen=self.m[0][0]
        elif self.con<45 and self.con>=40:
            imagen=self.m[0][1]
        elif self.con<40 and self.con>=35:
            imagen=self.m[0][2]
        elif self.con<35 and self.con>=30:
            imagen=self.m[0][3]
        elif self.con<30 and self.con>=25:
            imagen=self.m[0][4]
        elif self.con<25 and self.con>=20:
            imagen=self.m[0][5]
        elif self.con<20 and self.con>=15:
            imagen=self.m[0][6]
        elif self.con<15 and self.con>=10:
            imagen=self.m[0][7]
        elif self.con<10 and self.con>=5:
            imagen=self.m[0][8]
        elif self.con<5:
            imagen=self.m[0][9]
        else:
            imagen=self.m[0][0]
        self.rect.x+=self.velx
        self.Dibujar(p,imagen,izq)
