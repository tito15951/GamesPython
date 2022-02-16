import pygame
from Constantes import *
class ClasePersonaje(pygame.sprite.Sprite):
    def __init__(self,pos,m,bloques,sp_m):#Constructor
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.estado=1
        self.salud=100
        self.tipoDisparo=0
        self.bloques=bloques
        self.spritesmuerte=sp_m
        self.seccion=0
        self.conmorir=0
        self.tipoMapa=1 #especifica el fondo que tendra en cada mapa
        self.disparo=pygame.mixer.Sound('DisparoJugador.wav') #sonido de disparo 1
        self.disparo.set_volume(0.1)
        
    def ReiniciarPosicion(self,y):
        self.rect.x=200
        self.rect.y=y
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
            elif self.conmorir<35:
                imagen=self.spritesmuerte[0][0]
            self.Dibujar(p,imagen,izq)
            self.conmorir+=1

    def update(self,p,izq):
        if self.con<2:
            self.con+=1
        else:
            self.con=0
        if self.rect.top<0:
            self.vely=0
            self.rect.top=0
        if self.rect.bottom>ALTO:
            self.vely=0
            self.rect.bottom=ALTO
        self.rect.x+=self.velx
        self.rect.y+=self.vely

        ls_obj = pygame.sprite.spritecollide(self, self.bloques, False) #Colision con los Bloques
        for b in ls_obj:
            if self.rect.top <= b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom+5
                self.estado=1
            elif self.rect.bottom >= b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top-5
                self.estado=1
            elif (self.rect.right >= b.rect.left) and self.vely==0:
                self.estado=3

        colisionPj=pygame.mixer.Sound('MuerteJugador.wav')
        colisionPj.set_volume(0.1)

        if self.estado!=3:
            imagen=self.m[self.estado][self.con]
            self.Dibujar(p,imagen,izq)
        else:
            self.Muriendo(p,izq)
            colisionPj.play()


