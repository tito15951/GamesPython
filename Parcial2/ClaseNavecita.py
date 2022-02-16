import pygame
from Constantes import *
class ClaseNavecita(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('Navecita.png')
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=3
        self.con=0
        self.contadordisparo=1
        self.salud=1

    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,izq,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def update(self,p,izq):
        if self.con>15:
            self.vely=1
        elif self.con>30:
            self.vely=0
        else:
            self.velx=-6
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.con+=1
        self.Dibujar(p,self.image,izq)
