import pygame
from Constantes import *
class ClaseBloque(pygame.sprite.Sprite):
    def __init__(self, pos , imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen #---> pasar por parametro

        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=VELOCIDADFONDO

    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,False,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def update(self,p,izq):
        self.rect.x+=self.velx
        self.Dibujar(p,self.image,izq)
