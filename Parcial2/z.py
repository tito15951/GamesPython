import pygame
import random
import configparser
from ClasePersonaje import *
from ClaseEnemigo import *
from ClaseDisparos import *
from ClaseBonus import *
from ClaseBloque import *
from ClaseGenerador import *
from ClaseJefe import *
from Constantes import *
from librerias import * # --------------------------------------------------

VELOCIDADDISPAROS=10
DISPARORAPIDO=True
PROBABILIDADBONUS=0
#Voltear imagenes: imagen=pygame.transform.flip(imagen,True,False)

def RecortarSprite(nombre,can_an,can_al):
    imagen=pygame.image.load(nombre)
    info=imagen.get_rect()
    an_im=info[2]
    al_im=info[3]
    #print('Ancho:',an_im,'\nAlto',al_im)
    sp_an=int(an_im/can_an)
    sp_al=int(al_im/can_al)
    imagenes_fondo=[]
    for i in range(can_al):
        fila=[]
        imagenes_fondo.append(fila)
        for e in range(can_an):
            cuadro=imagen.subsurface(e*sp_an,i*sp_al,sp_an,sp_al)
            imagenes_fondo[i].append(cuadro)
    return imagenes_fondo

if __name__=='__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    Pantalla=pygame.display.set_mode([ANCHO,ALTO])

    recortar_imagen() # -----------------------------------------------------

    mapa_actual=1
    nombre_mapa='fondo'

    #--------------------------------------------------------

    fin=False

    izq=False

    #Recorte se todos los sprites
    Sprites_Enemigos=RecortarSprite('naveizq.png',7,4)
    Sprites_Jefe1=RecortarSprite('jefe1.png',4,1)
    Sprites_Jefe2=RecortarSprite('jefe2.png',4,1)
    Sprites_Jefe3=RecortarSprite('jefe3.png',4,1)
    Sprites_Personaje=RecortarSprite('Personaje.png',3,3)
    Sprites_Meteoritos=RecortarSprite('Meteoritoseditado.png',8,2)
    Sprites_Disparo1=RecortarSprite('Disparo1.png',4,1)
    Sprites_Disparo2=RecortarSprite('Disparo2.png',3,1)
    Sprites_Disparo3=RecortarSprite('Disparo3.png',4,1)
    Sprites_DisparosEnemigos=RecortarSprite('DisparosEnemigos.png',7,1)
    Sprites_Bonus=RecortarSprite('Bonus.png',3,1)
    Sprites_mapa=RecortarSprite('tileset1.png', 8, 6)
    Sprites_MuertePJ=RecortarSprite('ExplosionPErsonaje.png',7,1)    
    Sprites_Generadores=RecortarSprite('GeneradoresEditado.png',10,1)
#Fin recortes de sprites
#Grupos
    Personajes=pygame.sprite.Group()
    DisparosPersonajes=pygame.sprite.Group()
    Enemigos=pygame.sprite.Group()
    DisparosEnemigos=pygame.sprite.Group()
    Bonus=pygame.sprite.Group()
    Bloques=pygame.sprite.Group()
    Generadores=pygame.sprite.Group()
    Jefes=pygame.sprite.Group()

    G=ClaseGenerador([ANCHO-100,200],Sprites_Generadores)
    Generadores.add(G)
    G=ClaseGenerador([ANCHO,400],Sprites_Generadores)
    Generadores.add(G)

    '''
    G=ClaseGenerador([ANCHO,200])
    Generadores.add(G)
    G=ClaseGenerador([ANCHO,400])
    Generadores.add(G)
    '''
    
    grupo_bloques = obtener_bloques('mapa1')
    texturas_bloques=Retornovector()
    print("puto",len(texturas_bloques))
    for n in range(len(grupo_bloques)):   #Se crean los bloques arror 4745
        b = ClaseBloque(grupo_bloques[n],texturas_bloques[n])
        Bloques.add(b)

    J=ClasePersonaje([200,300],Sprites_Personaje,Bloques,Sprites_MuertePJ)
    Personajes.add(J)
    Je=ClaseJefe([ANCHO+30,200],Sprites_Jefe1,Bloques,Sprites_MuertePJ)
    Jefes.add(Je)

#ciclo juego
    while not fin:

        Pantalla.fill(NEGRO)
        
        leer_mapa(Pantalla,nombre_mapa)

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if J.estado!=3:
                    if event.key==pygame.K_UP:
                        J.vely=-5
                        J.estado=0
                    if event.key==pygame.K_DOWN:
                        J.vely=5
                        J.estado=2
                    if event.key==pygame.K_a:
                        if J.tipoDisparo==0:
                            if DISPARORAPIDO:
                                D=ClaseDisparos(J.rect,Sprites_Disparo1,0,3,VELOCIDADDISPAROS,5)
                                DisparosPersonajes.add(D)
                            if J.contadordisparo>20:
                                D=ClaseDisparos(J.rect,Sprites_Disparo1,0,3,VELOCIDADDISPAROS,5)
                                DisparosPersonajes.add(D)
                                J.contadordisparo=0
                        if J.tipoDisparo==1:
                            if DISPARORAPIDO:
                                D=ClaseDisparos(J.rect,Sprites_Disparo2,0,2,VELOCIDADDISPAROS,10)
                                DisparosPersonajes.add(D)
                            if J.contadordisparo>20:
                                D=ClaseDisparos(J.rect,Sprites_Disparo2,0,2,VELOCIDADDISPAROS,10)
                                DisparosPersonajes.add(D)
                                J.contadordisparo=0
                        if J.tipoDisparo==2:
                            pos=[J.rect.x,J.rect.y-5]
                            if DISPARORAPIDO:
                                D1=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20,-1)
                                D2=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20)
                                D3=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20,1)
                                DisparosPersonajes.add(D1)
                                DisparosPersonajes.add(D2)
                                DisparosPersonajes.add(D3)
                            if J.contadordisparo>20:
                                D=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20)
                                DisparosPersonajes.add(D)
                                J.contadordisparo=0
            if event.type==pygame.KEYUP:
                if J.estado!=3:
                    if event.key==pygame.K_UP:
                        J.vely=0
                        J.estado=1
                    if event.key==pygame.K_DOWN:
                        J.vely=0
                        J.estado=1




#Control de generadores:
        for g in Generadores:
            if g.con<0:
                g.con=random.randrange(100,200)
                E=ClaseEnemigo(g.rect,Sprites_Enemigos,Bloques)
                Enemigos.add(E)



#Revision de los enemigos
        for e in Enemigos:
#Control de disparo enemigos:
            if e.contadordisparo<0:
                D=ClaseDisparos(e.rect,Sprites_DisparosEnemigos,3,4,-1*VELOCIDADDISPAROS)
                DisparosEnemigos.add(D)
                e.contadordisparo=random.randrange(200)



#Control de impactos con los enemigos
            ls_col=pygame.sprite.spritecollide(e,DisparosPersonajes,True)
            if len(ls_col)>0:#Una bala del personaje impactó a un enemigos
                e.salud-=ls_col[0].dano

#Control de vida de enemigos:
            if e.salud<=0:
                e.estado=3
                e.contadordisparo=1000
                e.vely=0
                if e.con>35:
                    r=random.randrange(100)
                    if r>PROBABILIDADBONUS:
                        B=ClaseBonus(e.rect,Sprites_Bonus)
                        Bonus.add(B)
                    Enemigos.remove(e)


#Revvision de personaje:
        ls_col=pygame.sprite.spritecollide(J,DisparosEnemigos,True)
        if len(ls_col)>0:
            J.salud-=ls_col[0].dano
            print(J.salud)
            if J.salud<=0:
                J.estado=3
#Colision con bonus
        ls_col=pygame.sprite.spritecollide(J,Bonus,True)
        for b in ls_col:
            if b.tipo==0:
                if J.salud<50:
                    print('Mas salud')
                    J.salud+=5
            if b.tipo==1:
                print('Arma mejorada')
                if J.tipoDisparo<2:
                    J.tipoDisparo+=1
            if b.tipo==2:
                print('mas Puntuacion')


#Verifica que sigan en la pantalla:
        for b in DisparosEnemigos:
            if b.rect.left<0:
                DisparosEnemigos.remove(b)
        for b in DisparosPersonajes:
            if b.rect.left>ANCHO:
                DisparosPersonajes.remove(b)

        for j in Jefes:
            if j.salud<=0:
                j.estado=3
            if j.conmorir>40:
                r=random.randrange(100)
                if r>PROBABILIDADBONUS:
                    B=ClaseBonus(e.rect,Sprites_Bonus)
                    Bonus.add(B)
                Jefes.remove(j)

            if j.contadordisparo<=0:
                j.contadordisparo=random.randrange(200)
                D=ClaseDisparos(j.rect,Sprites_DisparosEnemigos,0,2,-1*VELOCIDADDISPAROS,20)
                DisparosEnemigos.add(D)

            ls_col=pygame.sprite.spritecollide(j,DisparosPersonajes,True)
            if len(ls_col)>0:
                j.salud-=ls_col[0].dano
                print(j.salud)

            for b in Bloques:
                b.velx=-5



        #Pantalla.blit(fondo,[FondoX,FondoY]) #Muestra la imagen del fondo del juego
        DisparosPersonajes.update(Pantalla,izq)
        DisparosEnemigos.update(Pantalla,izq)
        Personajes.update(Pantalla,izq)
        Enemigos.update(Pantalla,izq)
        Bonus.update(Pantalla,izq)
        Jefes.update(Pantalla,izq)
        Bloques.update(Pantalla)
        Generadores.update()


        Bloques.draw(Pantalla)
        pygame.display.flip()
        reloj.tick(20)

    pygame.quit()
