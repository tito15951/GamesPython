import pygame
from Constantes import *
class ClaseDisparos(pygame.sprite.Sprite):
    def __init__(self,pos,m,iniciosprite,finsprite,velx,dano=5,vely=0):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]+20
        self.rect.y=pos[1]+15
        self.velx=velx
        self.vely=vely
        self.iniciosprite=iniciosprite
        self.finsprite=finsprite
        self.dano=dano

    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,izq,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def update(self,Pantalla,izq):
        if self.con<self.finsprite:
            self.con+=1
        else:
            self.con=self.iniciosprite

        self.rect.y+=self.vely
        self.rect.x+=self.velx
        imagen=self.m[0][self.con]
        self.Dibujar(Pantalla,imagen,izq)
