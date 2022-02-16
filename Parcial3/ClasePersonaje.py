import pygame
from Constantes import *
class ClasePersonaje(pygame.sprite.Sprite):
    #Estado 1:Quieto
    #Estado 2:Izq
    #Estado 3:Der
    #Estado 4:Patada
    #Estado 5:Puño
    #Estado 6:Saltando
    #Estado 7:Patada voladora
    #Estado 8:Agachado
    #Estado 9:Puño bajo
    #Estado 10:Patada baja
    #Estado 11:Bajo ataque

    def __init__(self, pos,imagenes,bloques):
        pygame.sprite.Sprite.__init__(self)
        self.m=imagenes
        self.image=self.m[0][0]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.bloques=bloques
        self.orientacion='izq'
        self.estado=1
        self.alternacion=False
        self.saltodisponible=False
        self.con=0
        self.estadoanterior=1#Sirve para recordar en que estado estaba antes de golpear
        self.debemoverfondo=False
        self.salud=100
    def ReiniciarPosicion(self):
        self.rect.x=490
        self.rect.y=150

    def RecordarEstado(self):
        self.estadoanterior=self.estado

    def Dibujar(self,p):
        if self.orientacion=='der':
            imagen=pygame.transform.flip(self.image,True,False)
            p.blit(imagen,self.rect)
        else:
            p.blit(self.image,self.rect)


    def Saltar(self,vely=-14):
        self.vely=vely
        self.rect.y-=1

    def Gravedad(self,cte):
        if self.rect.bottom<260:
            self.vely+=cte
            self.saltodisponible=False
        else:
            self.rect.bottom=260
            self.vely=0
            self.saltodisponible=True

    def update(self,p,posfondo):
        if self.estado==1:
            self.velx=0
            self.image=self.m[0][0]
        elif self.estado==2:
            self.orientacion='izq'
            if self.rect.left<=440:
                self.velx=0
                self.debemoverfondo=True
                if posfondo>=0:
                    self.velx=-1*VELOCIDADMOVIMIENTO
            else:
                self.velx=-1*VELOCIDADMOVIMIENTO
                self.debemoverfondo=False
        elif self.estado==3:
            self.orientacion='der'
            if posfondo==0:
                self.velx=VELOCIDADMOVIMIENTO
            elif self.rect.right>=560:#Para que este en los limites, siempre debe de estar por la mitad
                self.velx=0
                self.debemoverfondo=True
                if posfondo<=-2100:#Para cuando llegue a los limites, se mueve el pj y no el fondo
                    self.velx=VELOCIDADMOVIMIENTO
            else:
                self.velx=VELOCIDADMOVIMIENTO
                self.debemoverfondo=False


        if self.estado==3 or self.estado==2:
            if self.alternacion:
                self.image=self.m[0][0]
                self.alternacion=not(self.alternacion)
            else:
                self.image=self.m[0][1]
                self.alternacion=not(self.alternacion)
        elif self.estado==4:#Pegando patada
            self.velx=0
            if self.con==0:
                self.image=self.m[0][2]
            elif self.con==1:
                self.image=self.m[0][3]
            elif self.con<=3:
                self.image=self.m[0][4]
            else:
                self.image=self.m[0][0]
                self.estado=self.estadoanterior
            self.con+=1
        elif self.estado==5:#Pegando puño
            self.velx=0
            if self.con==0:
                self.image=self.m[0][2]
            elif self.con==1:
                self.image=self.m[0][5]
            elif self.con<=3:
                self.image=self.m[0][2]
            else:
                self.image=self.m[0][0]
                self.estado=self.estadoanterior
            self.con+=1
        elif self.estado==6:#Saltando
            if self.rect.bottom==260:
                self.estado=self.estadoanterior
                self.image=self.m[0][0]
            else:
                self.image=self.m[0][10]
        elif self.estado==7:#Patada voladora
            if self.rect.bottom==260:
                self.estado=self.estadoanterior
                self.image=self.m[0][0]
            else:
                self.image=self.m[0][11]
        elif self.estado==8:#Agachado
            self.image=self.m[0][6]
            self.velx=0
        elif self.estado==9:
            if self.con==0:
                self.image=self.m[0][6]
            elif self.con==1:
                self.image=self.m[0][7]
            elif self.con==2:
                self.image=self.m[0][6]
            else:
                self.estado=8
            self.con+=1
        elif self.estado==10:
            if self.con==0:
                self.image=self.m[0][8]
            elif self.con==1:
                self.image=self.m[0][9]
            elif self.con==2:
                self.image=self.m[0][8]
            else:
                self.estado=8
            self.con+=1

        if self.rect.left<=0:
            self.rect.left=0
            self.estado=1
        if self.rect.right>=ANCHO:
            self.rect.right=ANCHO
            self.estado=1

        ls_col=pygame.sprite.spritecollide(self,self.bloques,False)
        for l in ls_col:
            if self.rect.bottom>l.rect.top:
                self.vely=0
                self.rect.bottom=l.rect.top
        self.Gravedad(2)
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        self.Dibujar(p)
