import pygame
from Constantes import *
class ClaseBloque(pygame.sprite.Sprite):
    def __init__(self, pos ,dim=[50,50]):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface(dim)
        #self.image.fill(BLANCO)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0

    def Dibujar(self,p):
        p.blit(self.image,self.rect)

    def update(self,p,velx=0):
        self.rect.x+=velx
        #self.Dibujar(p)
