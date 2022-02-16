import pygame
from Constantes import *
import random

def AutomataJefe(estado):
    r=random.randrange(100)
    if estado==1:
        if r<=40:
            return 2
        elif r<=70:
            return 4
        else:
            return 3
    elif estado==2:
        if r<=20:
            return 1
        else:
            return 3
    elif estado==3:
        return 1
    else:
        return 1


class ClaseMago(pygame.sprite.Sprite):
    #Estado 1=Quieto
    #Estado 2=Moviendose
    #Estado 3=Disparando
    #Estado 4=Teletransportand
    #Estado 5=Muriendo

    def __init__(self, pos,imagenes):
        pygame.sprite.Sprite.__init__(self)
        self.m=imagenes
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.orientacion='der'
        self.estado=2
        self.alternacion=False
        self.con=0
        self.estadoanterior=1#Sirve para recordar en que estado estaba antes de golpear
        self.salud=10
        self.disparar=False
        self.conestado=self.Aleatorio()
        self.cambioListo=True
    def Aleatorio(self):
        return random.randrange(30,50)

    def CambiarOrientacion(self):
        if self.orientacion=='izq':
            self.orientacion='der'
        else:
            self.orientacion='izq'
    def ReiniciarContador(self):
        self.con=0

    def Dibujar(self,p):
        if self.orientacion=='izq':
            imagen=pygame.transform.flip(self.image,True,False)
            p.blit(imagen,self.rect)
        else:
            p.blit(self.image,self.rect)

    def update(self,p):
        #print(self.estado)
        #print(self.conestado)
        self.conestado-=1
        if self.conestado<=0 and self.cambioListo and self.estado!=5:
            self.estado=AutomataJefe(self.estado)
            self.conestado=self.Aleatorio()
        if self.estado==1:#Quieto
            self.image=self.m[0][0]
            self.velx=0
        if self.estado==2:#Moviendose
            if self.alternacion:
                self.image=self.m[0][0]
            else:
                self.image=self.m[0][1]
            self.alternacion=not(self.alternacion)
            if self.orientacion=='izq':
                self.velx=-1*VELOCIDADMOVIMIENTO
            else:
                self.velx=VELOCIDADMOVIMIENTO
        if self.estado==3:#Disparando
            self.cambioListo=False
            self.con+=1
            self.velx=0
            if self.con<=2:
                self.image=self.m[0][2]
            elif self.con<=4:
                self.image=self.m[0][3]
            elif self.con<=5:
                self.image=self.m[0][4]
            elif self.con<=6:
                self.image=self.m[0][4]
                self.disparar=True
            else:
                self.ReiniciarContador()
                self.estado=1
                self.cambioListo=True
        if self.estado==4:#teletransportando
            self.con+=1
            self.cambioListo=False
            self.velx=0
            if self.con<=2:
                self.image=self.m[0][6]
            elif self.con<=4:
                self.image=self.m[0][7]
            elif self.con<=6:
                self.image=self.m[0][8]
            elif self.con==7:
                if self.orientacion=='der':
                    self.rect.x=800
                else:
                    self.rect.x=200
                self.CambiarOrientacion()
            elif self.con<=10:
                self.image=self.m[0][8]
            elif self.con<=12:
                self.image=self.m[0][7]
            elif self.con<=14:
                self.image=self.m[0][6]
            else:
                self.ReiniciarContador()
                self.estado=1
                self.cambioListo=True
        if self.estado==5:
            self.image=self.m[0][9]
            self.con+=1


        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.Dibujar(p)
