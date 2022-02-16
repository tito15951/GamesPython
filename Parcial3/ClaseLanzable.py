import pygame
from Constantes import *
class ClaseLanzable(pygame.sprite.Sprite):
    def __init__(self, pos ,m,velx,dir,tip):
        pygame.sprite.Sprite.__init__(self)
        self.image=m
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=velx
        self.orientacion=dir
        self.tipo=tip
        self.activo=True
        self.esquivado=False

    def Dibujar(self,p):
        if self.orientacion=='izq':
            imagen=pygame.transform.flip(self.image,True,False)
            p.blit(imagen,self.rect)
        else:
            p.blit(self.image,self.rect)

    def update(self,p,velfondo):
        self.rect.x+=self.velx+velfondo
        self.Dibujar(p)
