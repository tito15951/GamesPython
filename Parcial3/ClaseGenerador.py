import pygame
import random
from Constantes import *
class ClaseGenerador(pygame.sprite.Sprite):
    def __init__(self, pos,orientacion,activo):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([10,10])
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.orientacion=orientacion
        self.con=random.randrange(50,100)
        self.conBonus=random.randrange(50,200)
        self.activo=activo
    def NuevoCon(self):
        self.con=random.randrange(50,100)
    def NuevoConBonus(self):
        self.conBonus=random.randrange(50,200)

    def update(self):
        if self.activo:
            self.con-=1
            self.conBonus-=1
