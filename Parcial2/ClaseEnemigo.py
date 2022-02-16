import pygame
import random
from Constantes import *
class ClaseEnemigo(pygame.sprite.Sprite):
    def __init__(self,pos,m,bloques):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.estado=2
        self.tiempo=0
        self.Sprite0=False
        self.contadordisparo=random.randrange(50)
        self.salud=10
        self.velx=-1
        self.vely=0
        self.bloques=bloques
        self.SoundDisparo=pygame.mixer.Sound('disparoEnemigo.wav')
        self.SoundDisparo.set_volume(0.1)

    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,izq,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def update(self,Pantalla,izq):
        self.tiempo-=1
        self.contadordisparo-=1
        ls_obj = pygame.sprite.spritecollide(self, self.bloques, False) #Colision con los Bloques
        for b in ls_obj:
            if self.rect.top <= b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                self.estado=2
            elif self.rect.bottom >= b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                self.estado=1
            elif self.rect.right > b.rect.left and self.velx<0:
                self.salud=-1
        imagen=self.m[0][6]
        #Controla los movimientos y el sprite que debe de mostrar
        if self.tiempo<0 and self.estado!=3:#El estado 3 es que va a morir
            self.tiempo=random.randrange(50)
            antiguo=self.estado
            self.estado=AutomataProbabilistico(self.estado)
            if self.estado==0:
                self.vely=0
            if self.estado==1:
                self.vely=-3
            if self.estado==2:
                self.vely=3
            if antiguo != self.estado:
                self.con=0
        if self.estado==0:
            if self.Sprite0==False:
                imagen=self.m[0][6]
            else:
                imagen=self.m[1][3]
            self.Sprite0=not(self.Sprite0)
        if self.estado==1:
            if self.con<5:
                imagen=self.m[0][2]
                self.vely=-1
            elif self.con<10:
                imagen=self.m[0][1]
                self.vely=-3
            else:
                imagen=self.m[0][0]
                self.vely=-5
            self.con+=1
        if self.estado==2:
            if self.con<5:
                imagen=self.m[0][5]
                self.vely=1
            elif self.con<10:
                imagen=self.m[0][4]
                self.vely=3
            else:
                imagen=self.m[0][3]
                self.vely=5
            self.con+=1
        if self.estado==3:
            if self.con<5:
                imagen=self.m[3][6]
            elif self.con<10:
                imagen=self.m[3][5]
            elif self.con<15:
                imagen=self.m[3][4]
            elif self.con<20:
                imagen=self.m[3][3]
            elif self.con<25:
                imagen=self.m[3][2]
            elif self.con<30:
                imagen=self.m[3][1]
            elif self.con<35:
                imagen=self.m[3][0]
            self.con+=1
        #Verifica que este en los limites:
        if self.rect.top<0:
            self.rect.top=0
            self.estado=0
        if self.rect.bottom>ALTO:
            self.rect.bottom=ALTO
            self.estado=0
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.Dibujar(Pantalla,imagen,izq)
