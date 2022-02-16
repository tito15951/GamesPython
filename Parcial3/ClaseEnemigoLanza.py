import pygame
from Constantes import *
from ClaseBloque import *
class ClaseEnemigoLanza(pygame.sprite.Sprite):
    #Estado 1:Moviendose
    #Estado 3:Atacando
    #Estado 4:Muriendo

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
        self.con=0
        self.salud=1
        self.contadorgolpe=30
        self.disparar=False
        self.ultimoestado=0
        if self.orientacion=='der':
            posdetector1=[self.rect.x+150,self.rect.y+40]
            self.detector1=ClaseBloque(posdetector1,[200,10])#Detector de colision cercana para el primer estado
        else:
            posdetector1=[self.rect.x-150,self.rect.y+40]
            self.detector1=ClaseBloque(posdetector1,[200,10])#Detector de colision cercana para el primer estado
    def ReiniciarContadorGolpe(self):
        self.contadorgolpe=5
    def Dibujar(self,p):
        if self.orientacion=='izq':
            imagen=pygame.transform.flip(self.image,True,False)
            p.blit(imagen,self.rect)
        else:
            p.blit(self.image,self.rect)

    def update(self,p,velfondo,Pj):
        velenemigo=0
        if self.orientacion=='izq':
            velenemigo=-1*VELOCIDADMOVIMIENTO
        else:
            velenemigo=VELOCIDADMOVIMIENTO
        if self.estado==1:#Se esta moviendo
            self.velx=velenemigo
            if self.alternacion:
                self.image=self.m[0][0]
            else:
                self.image=self.m[0][1]
            self.alternacion=not(self.alternacion)
        elif self.estado==2:#Se esta acercando al pj y va a disparar por arriba
            self.velx=0
            if self.con<=2:
                self.image=self.m[0][2]
            elif self.con<=4:
                self.image=self.m[0][3]
            else:
                self.disparar=True
                self.estado=1
                self.ultimoestado=2
            self.con+=1
        elif self.estado==3:#Se esta acercando al pj y va a disparar por abajo
            self.velx=0
            if self.con<=2:
                self.image=self.m[0][4]
            elif self.con<=4:
                self.image=self.m[0][5]
            else:
                self.disparar=True
                self.ultimoestado=3
                self.estado=1
            self.con+=1
        else:#Muriendo
            self.image=self.m[0][8]
            self.vely+=1
            if self.con<=2:
                self.velx=-1*velenemigo
            elif self.con<=6:
                self.velx=(-1*velenemigo)/2
            self.con+=1
            try:
                self.detector1.remove()
            except:
                pass
        self.detector1.update(p,self.velx+velfondo)#Actualiza el detector

        ls_col=pygame.sprite.spritecollide(self.detector1,Pj,False)#Revisa si el detector colisiona con el personaje para pasar al estado 2
        if len(ls_col)>0 and self.estado==1 and self.contadorgolpe>=50:
            r=random.randrange(2)
            if r==1:
                self.estado=2
            else:
                self.estado=3
            self.contadorgolpe=0
        if len(ls_col)>0:
            self.contadorgolpe+=1

        self.rect.x+=self.velx+velfondo
        self.rect.y+=self.vely
        self.Dibujar(p)
