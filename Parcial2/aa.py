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
from ClaseNavecita import *
from Constantes import *
from librerias import *
#Commit ultimo
VELOCIDADDISPAROS=10
PROBABILIDADBONUS=40

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
    Fuente=pygame.font.Font(None,34)
    Fuente1=pygame.font.Font(None,30)
    Fuente2=pygame.font.Font(None,50)
    #recortar_imagen() # cambio
    Puntuacion=0
    Vidas=3
    ContadorFin=0
    CambiarFondo=True
    CambiarVelocidad=False
    Detenido=False
    Jefe1Generado=False
    Jefe2Generado=False
    Jefe3Generado=False
    velxfondo=VELOCIDADFONDO
    posxFondo=0
    gano=False

    #print(pygame.font.get_fonts())
    fin=False
#Creacion del mapa
    izq=False
    contadorGeneradores=random.randrange(100,200)
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
    Sprites_Mapa=RecortarSprite('tileset1.png',8,6)
    Sprites_MuertePJ=RecortarSprite('ExplosionPErsonaje.png',7,1)
    Sprites_Generadores=RecortarSprite('GeneradoresEditado.png',10,1)
    Sprite_Vida=pygame.image.load('Vidas.png')
    Fondo1=pygame.image.load('fondo1.png')
    Fondo2=pygame.image.load('fondo2.png')
    Fondo3=pygame.image.load('fondo3.png')
    Bloques_Mapa1,Texturas_Mapa1=obtener_bloquesalterno('mapa1',Sprites_Mapa)
    Bloques_Mapa2,Texturas_Mapa2=obtener_bloquesalterno('mapa2',Sprites_Mapa)
    Bloques_Mapa3,Texturas_Mapa3=obtener_bloquesalterno('mapa3',Sprites_Mapa)

#Fin recortes de sprites
#Grupos
    Personajes=pygame.sprite.Group()
    DisparosPersonajes=pygame.sprite.Group()
    Enemigos=pygame.sprite.Group()
    DisparosEnemigos=pygame.sprite.Group()
    Bonus=pygame.sprite.Group()
    Bloques=pygame.sprite.Group()
    Generadores=pygame.sprite.Group()
    GeneradoresFijos=pygame.sprite.Group()
    Jefes=pygame.sprite.Group()

    G=ClaseGenerador([ANCHO-100,200],Sprites_Generadores)
    Generadores.add(G)
    G=ClaseGenerador([ANCHO,400],Sprites_Generadores)
    Generadores.add(G)
    GeneradorFijo=ClaseGenerador([ANCHO+50,ALTO/2],Sprites_Generadores,0)

    J=ClasePersonaje([200,300],Sprites_Personaje,Bloques,Sprites_MuertePJ)
    Personajes.add(J)

    #Efectos de Sonido
    musica=pygame.mixer.Sound('MainSound.ogg')
    musica.set_volume(0.05)
    musica.play()
    win=pygame.mixer.Sound('Victoria.ogg')
    win.set_volume(0.1)
    MuertePj=pygame.mixer.Sound('MuerteJugador.wav')
    MuertePj.set_volume(0.05)
    bonificacion=pygame.mixer.Sound('Modificadores.wav')
    bonificacion.set_volume(0.1)
    DisparoEne=pygame.mixer.Sound('disparoEnemigo.wav')
    DisparoEne.set_volume(0.05)
    DisparoJefe=pygame.mixer.Sound('disparoJefe.wav')
    DisparoJefe.set_volume(0.05)



#ciclo juego
    while not fin:
        Pantalla.fill(NEGRO)
        if J.tipoMapa == 1:
            if CambiarFondo:
                CambiarFondo=False
                Bloques.empty()
                for b in range(len(Bloques_Mapa1)):
                    B=ClaseBloque(Bloques_Mapa1[b],Texturas_Mapa1[b])
                    Bloques.add(B)
        if J.tipoMapa == 2:
            if CambiarFondo:
                CambiarFondo=False
                Bloques.empty()
                for b in range(len(Bloques_Mapa2)):
                    B=ClaseBloque(Bloques_Mapa2[b],Texturas_Mapa2[b])
                    Bloques.add(B)
        if J.tipoMapa == 3:
            if CambiarFondo:
                CambiarFondo=False
                Bloques.empty()
                for b in range(len(Bloques_Mapa3)):
                    B=ClaseBloque(Bloques_Mapa3[b],Texturas_Mapa3[b])
                    Bloques.add(B)


        #leer_mapa(Pantalla,nombre_mapa) #Cambio ------------------------
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
                    if event.key==pygame.K_RIGHT:
                        if Detenido:
                            if J.tipoMapa==2:
                                J.velx=-4
                            else:
                                J.velx=4
                    if event.key==pygame.K_LEFT:
                        if Detenido:
                            if J.tipoMapa==2:
                                J.velx=4
                            else:
                                J.velx=-4
                    if event.key==pygame.K_a:
                        J.disparo.play()#sonido de disparo-------
                        if J.tipoDisparo==0:
                            D=ClaseDisparos(J.rect,Sprites_Disparo1,0,3,VELOCIDADDISPAROS,5)
                            DisparosPersonajes.add(D)
                        if J.tipoDisparo==1:
                            D=ClaseDisparos(J.rect,Sprites_Disparo2,0,2,VELOCIDADDISPAROS,10)
                            DisparosPersonajes.add(D)
                        if J.tipoDisparo==2:
                            pos=[J.rect.x,J.rect.y-5]
                            D1=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20,-1)
                            D2=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20)
                            D3=ClaseDisparos(pos,Sprites_Disparo3,0,3,VELOCIDADDISPAROS,20,1)
                            DisparosPersonajes.add(D1)
                            DisparosPersonajes.add(D2)
                            DisparosPersonajes.add(D3)
            if event.type==pygame.KEYUP:
                if J.estado!=3:
                    if event.key==pygame.K_UP:
                        J.vely=0
                        J.estado=1
                    if event.key==pygame.K_DOWN:
                        J.vely=0
                        J.estado=1
                    if event.key==pygame.K_RIGHT:
                        if Detenido:
                            J.velx=0
                    if event.key==pygame.K_LEFT:
                        if Detenido:
                            J.velx=0

#Control de generadores moviles:
        for g in Generadores:
            if g.rect.x<ANCHO/2:
                g.activo=False
            if g.con<0:
                g.con=g.Aleatorio()
                E=ClaseEnemigo(g.rect,Sprites_Enemigos,Bloques)
                Enemigos.add(E)
            if g.rect.x==-40:
                Generadores.remove(g)
            ls_col=pygame.sprite.spritecollide(g,Bloques,False)
            if len(ls_col)>0:
                Generadores.remove(g)
        if GeneradorFijo.con<0:
            GeneradorFijo.con=GeneradorFijo.Aleatorio()
            E=ClaseEnemigo(GeneradorFijo.rect,Sprites_Enemigos,Bloques)
            Enemigos.add(E)

#Revision de los enemigos
        for e in Enemigos:
#Control de disparo enemigos:
            if e.contadordisparo<0:
                D=ClaseDisparos(e.rect,Sprites_DisparosEnemigos,3,4,-1*VELOCIDADDISPAROS)
                DisparosEnemigos.add(D)
                e.contadordisparo=random.randrange(200)
                DisparoEne.play() #------------

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
                    Puntuacion+=5
                    r=random.randrange(100)
                    if r>PROBABILIDADBONUS:
                        B=ClaseBonus(e.rect,Sprites_Bonus)
                        Bonus.add(B)
                    Enemigos.remove(e)

#Revvision de personaje:

        ls_col=pygame.sprite.spritecollide(J,DisparosEnemigos,True)
        if len(ls_col)>0:
            J.salud-=ls_col[0].dano

        ls_col=pygame.sprite.spritecollide(J,Enemigos,False)
        for e in ls_col:
            J.salud-=5
            Enemigos.remove(e)
#Colision con bonus
        ls_col=pygame.sprite.spritecollide(J,Bonus,True)
        for b in ls_col:
            bonificacion.play()
            if b.tipo==0:
                if J.salud<100:
                    J.salud+=10
            if b.tipo==1:
                if J.tipoDisparo<2:
                    J.tipoDisparo+=1
                else:
                    Puntuacion+=5
            if b.tipo==2:
                Puntuacion+=10
        if J.salud<=0:
            MuertePj.play()
            J.estado=3
        if J.conmorir>=35:
            Vidas-=1
            #Restaura a valores iniciales el personaje
            J.ReiniciarPosicion(300)
            J.salud=100
            J.conmorir=0
            J.estado=1
            J.con=0
#Verifica que sigan en la pantalla:
        for b in DisparosEnemigos:
            ls_col=pygame.sprite.spritecollide(b,Bloques,False)
            if len(ls_col)>0:
                DisparosEnemigos.remove(b)
            if b.rect.left<0:
                DisparosEnemigos.remove(b)
        for b in DisparosPersonajes:
            ls_col=pygame.sprite.spritecollide(b,Bloques,False)
            if len(ls_col)>0:
                DisparosPersonajes.remove(b)
            if b.rect.left>ANCHO:
                DisparosPersonajes.remove(b)
        for b in Bonus:
            if b.rect.right<0:
                Bonus.remove(b)
        for e in Enemigos:
            if e.rect.right<0:
                Enemigos.remove(e)
#Verifica los jefes
        for j in Jefes:
            if j.salud<=0:
                j.estado=3
                j.contadordisparo=10000
            if j.conmorir>35:
                B=ClaseBonus(j.rect,Sprites_Bonus)
                Bonus.add(B)
                Jefes.remove(j)
                Puntuacion+=20

            if j.contadordisparo<=0:
                j.contadordisparo=random.randrange(200)
                D=ClaseDisparos(j.rect,Sprites_DisparosEnemigos,0,2,-1*VELOCIDADDISPAROS,20)
                DisparoJefe.play() #------------------
                DisparosEnemigos.add(D)

            ls_col=pygame.sprite.spritecollide(j,DisparosPersonajes,True)
            if len(ls_col)>0:
                j.salud-=ls_col[0].dano
            if j.contadorGenerar>100:
                N=ClaseNavecita(j.rect)
                Enemigos.add(N)
                j.contadorGenerar=0

#Generador de generadores:
        if contadorGeneradores<=0:
            contadorGeneradores=random.randrange(100,200)
            r=random.randrange(50,ALTO-50)
            G=ClaseGenerador([ANCHO+40,r],Sprites_Generadores)
            Generadores.add(G)

#Control de los bloques
        for B in Bloques:
            if Detenido==False:
                J.velx=0
            if J.tipoMapa==1:
                if B.rect.x<-2360:#Cuando llegue al limite del mapa 1, se detiene
                    for b in Bloques:
                        b.velx=0
                    for g in Generadores:
                        g.velx=0
                    Detenido=True
                    velxfondo=0
                    contadorGeneradores=9999999999999
                    GeneradorFijo.activo=False
                    for g in Generadores:
                        if g.rect.left>=ANCHO-50:
                            g.activo=False
                if B.rect.x<-500 and Jefe1Generado==False:#Controlador de aparcicion del Jefe 1
                    Jefe1Generado=True
                    Je=ClaseJefe([ANCHO+30,200],Sprites_Jefe1,Bloques,Sprites_MuertePJ)
                    Jefes.add(Je)
                if (Detenido and len(Jefes)==0) and J.rect.bottom>=ALTO:#Se encuentra en el limite para cambiar de mapa
                    Detenido=False
                    J.ReiniciarPosicion(50)
                    izq=True
                    #CambiarVelocidadFondo=True
                    J.tipoMapa=2
                    CambiarFondo=True
                    CambiarVelocidad=True
                    velxfondo=-1*VELOCIDADFONDO
                    posxFondo=-2400
                    GeneradorFijo.activo=True
                    Generadores.empty()
                    Enemigos.empty()
                    Bonus.empty()
                    DisparosPersonajes.empty()
                    DisparosEnemigos.empty()
                    J.tipoDisparo=0
                    for b in Bloques:
                        b.velx=VELOCIDADFONDO
                    for g in Generadores:
                        g.velx=-1
                    contadorGeneradores=50
            elif J.tipoMapa==2:
                if B.rect.x<-2320: #Cuando llegue al limite del mapa 2, se detiene
                    for b in Bloques:
                        b.velx=0
                    for g in Generadores:
                        g.velx=0
                    Detenido=True
                    velxfondo=0
                    GeneradorFijo.activo=False
                    contadorGeneradores=9999999999999
                if B.rect.x<-700 and Jefe2Generado==False: #Control de aparicion del jefe 2
                    Jefe2Generado=True
                    Je=ClaseJefe([ANCHO+30,200],Sprites_Jefe2,Bloques,Sprites_MuertePJ,150)
                    Jefes.add(Je)
                if (Detenido and len(Jefes)==0) and J.rect.bottom>=ALTO:#Se encuentra en el limite para cambiar de mapa
                    Detenido=False
                    J.ReiniciarPosicion(100)
                    izq=False
                    J.tipoMapa=3
                    CambiarFondo=True
                    CambiarVelocidad=True
                    velxfondo=VELOCIDADFONDO
                    posxFondo=0
                    for b in Bloques:
                        b.velx=VELOCIDADFONDO
                    for g in Generadores:
                        g.velx=-1
                    Enemigos.empty()
                    velxfondo=VELOCIDADFONDO
                    posxFondo=0
                    contadorGeneradores=50
                    J.tipoDisparo=0
                    GeneradorFijo.activo=True
                    Generadores.empty()
                    Enemigos.empty()
                    Bonus.empty()
                    DisparosPersonajes.empty()
                    DisparosEnemigos.empty()
            elif J.tipoMapa==3:
                if B.rect.x<-2360:#control de velocidad del limite
                    for b in Bloques:
                        b.velx=0
                    for g in Generadores:
                        g.velx=0
                        contadorGeneradores=9999999999999
                    Detenido=True
                    velxfondo=0
                    GeneradorFijo.activo=False
                if B.rect.x<-2000 and Jefe3Generado==False:#Control de aparicion del jefe 3
                    Jefe3Generado=True
                    Je=ClaseJefe([ANCHO+30,200],Sprites_Jefe3,Bloques,Sprites_MuertePJ,200)
                    Jefes.add(Je)
                if (Detenido and len(Jefes)==0):#Acabó todo
                    gano=True
            break

        if Vidas!=0 and not(gano):
    #Controlador de velocidad de los disparos dependiendo de para que lado vaya todo
            if J.tipoMapa==1:
                Pantalla.blit(Fondo1,[posxFondo,0])
            if J.tipoMapa==2:
                Pantalla.blit(Fondo2,[posxFondo,0])
            if J.tipoMapa==3:
                Pantalla.blit(Fondo3,[posxFondo,0])
            Bloques.update(Pantalla,izq)
            Generadores.update(Pantalla,izq)
            GeneradorFijo.update(Pantalla,izq)
            DisparosPersonajes.update(Pantalla,izq)
            DisparosEnemigos.update(Pantalla,izq)
            Personajes.update(Pantalla,izq)
            Enemigos.update(Pantalla,izq)
            Jefes.update(Pantalla,izq)
            Bonus.update(Pantalla,izq)
            posxFondo+=velxfondo

    #Barra interfaz
            pygame.draw.polygon(Pantalla,NEGRO,[[0,0],[270,0],[270,50],[0,50]])
            salud='Salud: '+str(J.salud)
            Texto=Fuente.render(salud,True,BLANCO)
            Pantalla.blit(Texto,[0,0])

            pun='Puntuacion: '+str(Puntuacion)
            Texto=Fuente1.render(pun,True,BLANCO)
            Pantalla.blit(Texto,[0,25])
            x=165
            for i in range(Vidas):
                Pantalla.blit(Sprite_Vida,[x,10])
                x+=35
        else:
            ContadorFin+=1
            Mensaje='FIN DEL JUEGO'
            musica.stop()
            if gano:
                Mensaje=Mensaje+ ', GANASTE'
                win.play()
                Texto=Fuente2.render(Mensaje,True,BLANCO)
                Pantalla.blit(Texto,[(ANCHO/2)-220,ALTO/2])


            else:
                Texto=Fuente2.render(Mensaje,True,BLANCO)
                Pantalla.blit(Texto,[(ANCHO/2)-130,ALTO/2])
            Mensaje='LA PUNTUACION FUE: '+str(Puntuacion)
            Texto=Fuente2.render(Mensaje,True,BLANCO)
            Pantalla.blit(Texto,[(ANCHO/2)-220,(ALTO/2)+70])
            if ContadorFin>200:
                fin=True
        pygame.display.flip()
        reloj.tick(40)
        contadorGeneradores-=1
    pygame.quit()
