import pygame
import random
from Constantes import *

class ClaseJefe(pygame.sprite.Sprite):
    def __init__(self,pos,m,bloques,sp_m,salud=100):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.estado=0
        self.contadordisparo=random.randrange(50)
        self.salud=salud
        self.velx=0
        self.vely=0
        self.bloques=bloques
        self.spritesmuerte=sp_m
        self.conmorir=0
        self.connuevoestado=random.randrange(25,50)
        self.contadorGenerar=0
        self.colisionatras=False
        self.MuerteJefe=pygame.mixer.Sound('MuerteJefe.wav')
        self.MuerteJefe.set_volume(0.1)

    def Dibujar(self,p,imagen,izq):
        if izq:
            posefectivax=ANCHO-self.rect.x
            imagen=pygame.transform.flip(imagen,izq,False)
        else:
            posefectivax=self.rect.x
        p.blit(imagen,[posefectivax,self.rect.y])

    def Muriendo(self,p,izq):
            if self.conmorir<5:
                imagen=self.spritesmuerte[0][6]
            elif self.conmorir<10:
                imagen=self.spritesmuerte[0][5]
            elif self.conmorir<15:
                imagen=self.spritesmuerte[0][4]
            elif self.conmorir<20:
                imagen=self.spritesmuerte[0][3]
            elif self.conmorir<25:
                imagen=self.spritesmuerte[0][2]
            elif self.conmorir<30:
                imagen=self.spritesmuerte[0][1]
            else:
                imagen=self.spritesmuerte[0][0]
            self.Dibujar(p,imagen,izq)
            self.conmorir+=1

    def update(self,Pantalla,izq):
        self.contadordisparo-=1
        self.contadorGenerar+=1
        if self.rect.x>ANCHO-210:
            self.velx=-2
        else:
            self.velx=0
        ls_obj = pygame.sprite.spritecollide(self, self.bloques, False) #Colision con los Bloques
        colisionarriba=False
        colisionabajo=False
        for b in ls_obj:
            if self.rect.top <= b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                self.estado=2
                colisionarriba=True
            elif self.rect.bottom >= b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                self.estado=1
                colisionabajo=True
            if self.rect.right > b.rect.left:
                if colisionabajo:
                    self.estado=2
                elif colisionarriba:
                    self.estado=1

        #Controla los movimientos y el sprite que debe de mostrar
        if self.connuevoestado<=0 and self.estado!=3:
            self.estado=AutomataProbabilistico(self.estado,10)
            self.connuevoestado=random.randrange(25,50)
        self.connuevoestado-=1
        imagen=self.m[0][0]
        if self.estado==0:
            self.vely=0
        if self.estado==1:
            self.vely=-3
        if self.estado==2:
            self.vely=3
        if self.salud>=75:
            imagen=self.m[0][0]
        elif self.salud>=50:
            imagen=self.m[0][1]
        elif self.salud>=25:
            imagen=self.m[0][2]
        elif self.salud>=0:
            imagen=self.m[0][3]

        
        #Verifica que este en los limites:
        if self.rect.top<0:
            self.rect.top=0
            self.estado=0
        if self.rect.bottom>ALTO:
            self.rect.bottom=ALTO
            self.estado=0
        if self.estado!=3:
            self.Dibujar(Pantalla,imagen,izq)
        else:
            self.Muriendo(Pantalla,izq)
            self.MuerteJefe.play()
        self.rect.y+=self.vely
        self.rect.x+=self.velx
