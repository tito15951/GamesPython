import pygame
import random
from ClaseBloque import *
from ClasePersonaje import *
from Constantes import *
from ClaseEnemigoNormal import *
from ClaseGenerador import *

if __name__ == '__main__':
    pygame.init()
    Pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Sprites_Personaje=RecortarSprite('Personaje.png',15,1)
    Sprites_EnemigoCuchillo=RecortarSprite('EnemigoLanzaCuchillo.png',9,1)
    Sprites_EnemigoMachete=RecortarSprite('EnemigoLanzaMachete.png',7,1)
    Sprites_EnemigoNormal=RecortarSprite('EnemigoNormal.png',6,1)
    Fondo1=pygame.image.load('KungFu1Floor.png')
    Fondo2=pygame.image.load('KungFu2Floor.png')

    Bloques=pygame.sprite.Group()
    Personaje=pygame.sprite.Group()
    EnemigosNormales=pygame.sprite.Group()
    Generadores=pygame.sprite.Group()

    posxfondo=-2095
    velxfondo=0

    B=ClaseBloque([0,260],[1000,50])
    Bloques.add(B)


    Pj=ClasePersonaje([490,100],Sprites_Personaje,Bloques)
    Personaje.add(Pj)
    G1=ClaseGenerador([-10,180],'der')
    Generadores.add(G1)
    G1=ClaseGenerador([ANCHO+10,180],'izq')
    Generadores.add(G1)


    reloj=pygame.time.Clock()
    fin=False
    while not fin:
        Pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:#Volear pata
                    if Pj.estado==6:#Que este en el aire y volie pata
                        Pj.estado=7
                        Pj.con=0
                        velxfondo=0
                    elif Pj.estado==8:#Que este agachado y volie pata
                        Pj.estado=10
                        Pj.con=0
                        velxfondo=0
                    elif Pj.estado!=4 and Pj.estado!=5:#Que no este pegando puños ni patadas normales
                        Pj.RecordarEstado()
                        Pj.estado=4
                        Pj.con=0
                        velxfondo=0
                if event.key==pygame.K_s:#Volear puño
                    if Pj.estado!=4 and Pj.estado!=5:#Que no este pegando puños ni patadas normales
                        Pj.RecordarEstado()
                        if Pj.estado==8:#Si esta agachado, haga el puño bajo
                            Pj.estado=9
                            velxfondo=0
                        else:#Si no esta agachado, puño normal
                            Pj.estado=5
                            velxfondo=0
                        Pj.con=0

                if event.key==pygame.K_RIGHT:
                    if Pj.estado!=11:
                        Pj.estado=3
                        velxfondo=-5
                    else:
                        Pj.orientacion='der'
                if event.key==pygame.K_LEFT:
                    if Pj.estado!=11:
                        Pj.estado=2
                        velxfondo=5
                    else:
                        Pj.orientacion='izq'
                if event.key==pygame.K_DOWN:
                    Pj.estado=8
                if event.key==pygame.K_UP:
                    if Pj.saltodisponible:
                        Pj.RecordarEstado()
                        Pj.Saltar()
                        Pj.estado=6
            if event.type==pygame.KEYUP:
                if (event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT) or event.key==pygame.K_DOWN:
                    Pj.estado=1
                    velxfondo=0

#Colisiones de enemigos normales con Pj:
        ls_col=pygame.sprite.spritecollide(Pj,EnemigosNormales,False)
        if len(ls_col)>0:
            for l in ls_col:
                #Pj.velx=0
                l.contadorgolpe-=1
                if ((Pj.estado==1 or Pj.estado==2) or Pj.estado==3) and l.estado!=4:#Si no esta pegando
                    if l.contadorgolpe<=0:
                        l.ReiniciarContadorGolpe()
                        Pj.salud-=2
                        print('golpe')
                    Pj.estado=11
                    Pj.velx=0
                else:
                    if ((((Pj.estado!=1 and Pj.estado!=2) and Pj.estado!=3) and Pj.estado!=8) and Pj.estado!=11):
                        if l.orientacion!=Pj.orientacion:
                            l.estado=4



#Eliminacion de enemigos que no esten en la Pantalla
        for E in EnemigosNormales:
            if E.rect.top>=ALTO:
                EnemigosNormales.remove(E)

        for g in Generadores:
            if g.con<=0:
                g.NuevoCon()
                F=ClaseEnemigoNormal(g.rect,Sprites_EnemigoNormal,g.orientacion)
                EnemigosNormales.add(F)

#Control del fondo
        if posxfondo<=-2100 or posxfondo>=0:
            velxfondo=0
        if posxfondo==0 and Pj.estado==3 and Pj.rect.right==560:
            posxfondo=-5
            print('Arreglado')
        if posxfondo==-2100 and Pj.estado==2 and Pj.rect.left==440:
            posxfondo=-2095
            print('Arreglado')
        print(posxfondo)
        posxfondo+=velxfondo
        
        Pantalla.blit(Fondo1,[posxfondo,0])

        Bloques.update(Pantalla)
        EnemigosNormales.update(Pantalla,velxfondo,Personaje)
        Personaje.update(Pantalla,posxfondo)
        Generadores.update()


        pygame.display.flip()
        reloj.tick(15)#10 ticks es lo mejor
