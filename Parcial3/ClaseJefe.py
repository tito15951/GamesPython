import pygame
import random
from Constantes import *

class ClaseJefe(pygame.sprite.Sprite):

    '''
    Estados:

    1---> 0 y 1 Caminando
    2---> 2 y 3 en guardia
    3---> 4 y 5 patada baja
    4---> 6 y 7 puño bajo
    5---> 8 y 9 patada alta
    6---> 10 y 11 en guardia 2    (el sprite 11 puede ser el inicial)
    7---> 12 puño normal
    8---> 15 y 16 patada voladora
    9 --> 14 muriendo
    
    '''
    def __init__(self, pos,imagenes,orientacion):
        pygame.sprite.Sprite.__init__(self)
        self.m=imagenes
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.orientacion=orientacion
        self.estado=1
        self.alternacion=False
        self.salud=20
        self.cont=0
        self.con=5
        self.disparar=False
        #self.bloques=bloques
    
    def Dibujar(self,p):
        if self.orientacion=='izq':
            imagen=pygame.transform.flip(self.image,True,False)
            p.blit(imagen,self.rect)
        else:
            p.blit(self.image,self.rect)
    
    def update (self, p):
        velenemigo=0
        if self.orientacion=='izq':
            velenemigo=-1*VELOCIDADMOVIMIENTO
        else:
            velenemigo=VELOCIDADMOVIMIENTO
        self.velx=0
        if self.estado != 9:
            if self.cont==8:
                accion= random.randrange(9)
                self.estado=accion
                self.cont=0
                print(accion)
        
        if self.estado == 1:

            if self.orientacion=='izq':
                self.velx=-2
            else:
                self.velx=2
            if self.alternacion:
                self.image=self.m[0][0]
            else:
                self.image=self.m[0][1]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==2:
            if self.alternacion:
                self.image=self.m[0][2]
            else:
                self.image=self.m[0][3]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==3:
            if self.alternacion:
                self.image=self.m[0][4]
            else:
                self.image=self.m[0][5]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
            if self.orientacion=='izq':
                self.velx=-1
            else:
                self.velx=1
        elif self.estado ==4:
            if self.alternacion:
                self.image=self.m[0][6]
            else:
                self.image=self.m[0][7]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado == 5:
            if self.alternacion:
                self.image=self.m[0][8]
            else:
                self.image=self.m[0][9]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==6:
            if self.alternacion:
                self.image=self.m[0][10]
            else:
                self.image=self.m[0][11]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==7:
            if self.alternacion:
                self.image=self.m[0][11]
            else:
                self.image=self.m[0][12]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==8:
            if self.alternacion:
                self.image=self.m[0][15]
            else:
                self.image=self.m[0][16]
            if self.cont==5:
                self.alternacion=not(self.alternacion)
        elif self.estado ==9:
            self.image=self.m[0][14]
            self.vely+=1
            if self.con<=2:
                self.velx=-1*velenemigo
            elif self.con<=6:
                self.velx=(-1*velenemigo)/2
            self.con+=1
            
        '''
        ls_col=pygame.sprite.spritecollide(self,self.bloques,False)
        for l in ls_col:
            if self.rect.bottom>l.rect.top:
                self.vely=0
                self.rect.bottom=l.rect.top
        '''
        self.cont+=1
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.Dibujar(p)
