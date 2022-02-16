import pygame
from Constantes import *
class ClaseGolpe(pygame.sprite.Sprite):
    def __init__(self, pos ,m,t,puntuacion=100):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.image=m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.con=10
        self.tipo=t
        self.pun=puntuacion
        self.Fuente1=pygame.font.SysFont('cooperblack',15)
        self.elev=0

    def Dibujar(self,p):
        Texto=str(self.pun)
        dib=self.Fuente1.render(Texto,True,ROJO)
        p.blit(dib,[self.rect.x,self.rect.y+self.elev])
        if self.tipo==0:
            p.blit(self.m[0][0],self.rect)
        else:
            p.blit(self.m[1][0],self.rect)

    def update(self,p):
        self.con-=1
        self.elev-=3
        self.Dibujar(p)
