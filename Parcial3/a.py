import pygame
import random
from ClaseBloque import *
from ClasePersonaje import *
from Constantes import *
from ClaseEnemigoNormal import *
from ClaseGenerador import *
from ClaseGolpe import *
from ClaseMago import *
from ClaseLanzable import *
from ClaseBonus import *
from ClaseEnemigoLanza import *
from ClaseJefe import *
INICIO=-2095 #lo normal es -2095

def HistoriaMitad(pantalla,reloj):
    contador=0
    finIntro=False
    while not finIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finIntro=True
        contador+=1
        if contador<80:
            CancionHistoria.play()
            Pantalla.blit(Hist4,[0,0])
        elif contador<160:
            Pantalla.blit(Hist5,[0,0])
        else:
            CancionHistoria.stop()
            finIntro=True
        contador+=1
        pygame.display.flip()
        reloj.tick(10)

def HistoriaFinal(pantalla,reloj):
    contador=0
    finIntro=False
    while not finIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finIntro=True
        contador+=1
        if contador<80:
            CancionFondo.stop()
            Win.play()
            Pantalla.blit(Hist6,[0,0])
            Personaje.empty()
            Bloques.empty()
            EnemigosNormales.empty()
            EnemigosLanza.empty()
            Jefes.empty()
            Lanzables.empty()
            LanzablesPj.empty()

        else:
            finIntro=True
        contador+=1
        pygame.display.flip()
        reloj.tick(10)

if __name__ == '__main__':
    pygame.init()
    Pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Sprites_Personaje=RecortarSprite('Personaje.png',15,1)
    Sprites_EnemigoCuchillo=RecortarSprite('EnemigoLanzaCuchillo.png',9,1)
    Sprites_EnemigoNormal=RecortarSprite('EnemigoNormal.png',6,1)
    Sprites_Golpes=RecortarSprite('Golpes.png',1,2)
    Sprites_Jefe1=RecortarSprite('Mago.png',10,1)
    Sprites_Bonus=RecortarSprite('Bonus.png',2,1)
    Sprites_Jefe2=RecortarSprite('Jefe2.png', 17, 1)
    Fondo1=pygame.image.load('KungFu1Floor.png')
    Fondo2=pygame.image.load('KungFu2Floor.png')
    Im_Vidas=pygame.image.load('Vidas.png')
    Hist1=pygame.image.load('Historia1.png')
    Hist2=pygame.image.load('Historia2.png')
    Hist3=pygame.image.load('Historia3.png')
    Hist4=pygame.image.load('Historia4.png')
    Hist5=pygame.image.load('Historia5.png')
    Hist6=pygame.image.load('Historia6.png')
    Hist7=pygame.image.load("FinTiempo.png")
    Menu=pygame.image.load('Inicio.png')
    Creditos=pygame.image.load('Creditos.png')

    Fuente1=pygame.font.SysFont('cooperblack',24)
    Fuente2=pygame.font.SysFont('cooperblack',30)
    Bloques=pygame.sprite.Group()
    Personaje=pygame.sprite.Group()
    EnemigosNormales=pygame.sprite.Group()
    EnemigosLanza=pygame.sprite.Group()
    Generadores=pygame.sprite.Group()
    Golpes=pygame.sprite.Group()
    Jefes=pygame.sprite.Group()
    Lanzables=pygame.sprite.Group()
    Bonus=pygame.sprite.Group()
    LanzablesPj=pygame.sprite.Group()

    #Efectos de Sonido ----------------------------------------------------------------------------
    EPuño=pygame.mixer.Sound('Puño.wav')
    EPatadaBaja=pygame.mixer.Sound('patadaBaja.wav')
    EPatadaVoladora=pygame.mixer.Sound('PatadaVoladora.wav')
    EMuerteJefe=pygame.mixer.Sound('MuerteJefes.wav')
    ERisaJefe=pygame.mixer.Sound('RisaJefe.wav')
    EBolaFuego=pygame.mixer.Sound('BolaFuego.wav')
    EVidaExtra=pygame.mixer.Sound('VidaExtra.wav')
    ELanzaCuchillo=pygame.mixer.Sound('LanzaCuchillo.wav')
    #Canciones ----------------------------------------------------------------------------
    CancionFondo= pygame.mixer.Sound('main.wav')
    CancionTutorial = pygame.mixer.Sound('Shinrin-Yoku.ogg')
    CancionTutorial.set_volume(0.1)
    CancionHistoria= pygame.mixer.Sound('Battleship.ogg')
    CancionHistoria.set_volume(0.1)
    CancionPerdida= pygame.mixer.Sound('Perdida.ogg')
    CancionPerdida.set_volume(0.1)
    Win=pygame.mixer.Sound('win.wav')
    Win.set_volume(0.1)
    MenuPrincipal=pygame.mixer.Sound('MenuPrincipal.wav')
    MenuPrincipal.set_volume(0.1)


    reloj=pygame.time.Clock()
    counter=0
    finMenu=False
    finJuego=False
    finTuturial=False
    finIntro=False
    OpcionMenu=1
    Alternacion=False
    Jefefinal=False


#Control del menú
    MenuPrincipal.play()
    while not finMenu:
        Pantalla.fill(NEGRO)
        #MenuPrincipal.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finMenu=True
                finJuego=True
                finIntro=True
                finTuturial=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    OpcionMenu=1
                if event.key==pygame.K_DOWN:
                    OpcionMenu=2
                if event.key==pygame.K_a:
                    if OpcionMenu==1:
                        finMenu=True
                        MenuPrincipal.stop()
                    else:
                        OpcionMenu=3
        Pantalla.blit(Menu,[0,0])
        if OpcionMenu==1:
            if Alternacion:
                imagen=pygame.transform.flip(Sprites_Personaje[0][0],True,False)
                Pantalla.blit(imagen,[350,300])
            else:
                imagen=pygame.transform.flip(Sprites_Personaje[0][1],True,False)
                Pantalla.blit(imagen,[350,300])
        if OpcionMenu==2:
            if Alternacion:
                imagen=pygame.transform.flip(Sprites_Personaje[0][0],True,False)
                Pantalla.blit(imagen,[350,380])
            else:
                imagen=pygame.transform.flip(Sprites_Personaje[0][1],True,False)
                Pantalla.blit(imagen,[350,380])
        if OpcionMenu==3:
            Pantalla.blit(Creditos,[0,0])


        Alternacion=not(Alternacion)
        pygame.display.flip()
        reloj.tick(10)
    contador=0
#Control historia inicial:
    while not finIntro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finMenu=True
                finJuego=True
                finIntro=True
                finTuturial=True
        contador+=1
        if contador<80:
            CancionHistoria.play()
            Pantalla.blit(Hist1,[0,0])#Dibuja el fondo
        elif contador<160:
            Pantalla.blit(Hist2,[0,0])#Dibuja el fondo
        elif contador<240:
            Pantalla.blit(Hist3,[0,0])#Dibuja el fondo
        else:
            CancionHistoria.stop()
            finIntro=True
        contador+=1
        pygame.display.flip()
        reloj.tick(10)

#Control del tuturial:
    B=ClaseBloque([0,260],[1000,50])#Piso
    Bloques.add(B)
    Pj=ClasePersonaje([490,150],Sprites_Personaje,Bloques)
    Personaje.add(Pj)
    contador=0
    Texto=''
    pos=[140,100]
    CancionTutorial.play()
    while not finTuturial:

        Pantalla.fill(NEGRO)
        Pantalla.blit(Fondo1,[0,0])#Dibuja el fondo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finMenu=True
                finJuego=True
                finTuturial=True
                Personaje.empty()
                Bloques.empty()
        contador+=1
        if contador<30:
            Pj.estado=1
            Texto=str('A continuación, veremos los movimientos basicos')
        elif contador<60:
            Pj.estado=2
            Texto=str('Presione la flecha izquierda para moverse hacia ese lado')
        elif contador<90:
            Pj.estado=3
            Texto=str('Presione la flecha derecha para moverse hacia ese lado')
        elif contador<120:
            Pj.estado=6
            Pj.velx=0
            if contador==90:
                Pj.Saltar()
            Texto=str('Presione la flecha arriba para saltar')
        elif contador<150:
            Pj.estado=8
            Texto=str('Presione la flecha abajo para agacharse')
        elif contador<180:
            Pj.estado=4
            Texto=str('Presione la tecla A para pegar una patada')
            if contador==179:
                Pj.con=0
        elif contador<210:
            Pj.estado=5
            Texto=str('Presione la tecla S para pegar un puño')
        elif contador<230:
            Pj.estado=5
            Texto=str('Pueden realizarce combinaciones para combos')
        elif contador<260:
            Pj.estado=1
            Texto=str('A lo largo del mapa se encuentran bonus')
        elif contador<290:
            Pj.estado=1
            Pantalla.blit(Sprites_Bonus[0][1],[750,140])
            Texto=str('Uno de ellos otorga salud')
        elif contador<320:
            Pj.estado=1
            Pantalla.blit(Sprites_Bonus[0][0],[350,140])
            Texto=str('El otro da un disparo especial')
        elif contador<350:
            Pj.estado=1
            Texto=str('El objetivo es salvar a la novia de Thomas, Suerte')
        else:
            CancionTutorial.stop()
            finTuturial=True
            Personaje.empty()
            Bloques.empty()
        Dib=Fuente2.render(Texto,True,NEGRO)
        Pantalla.blit(Dib,pos)
        Bloques.update(Pantalla)
        Personaje.update(Pantalla,0)
        pygame.display.flip()
        reloj.tick(10)
    Personaje.empty()
#Cintrol Ciclo Juego
    CancionFondo.play()
    posxfondo=INICIO#Lo normal es -2095
    velxfondo=0
    nivel=1
    Puntuacion=0
    tiempo=2000
    Jefe1Derrotado=False
    Jefe2Derrotado=False
    animacionGolpe=False
    HistoriaHecha=False
    vidas=3

    B=ClaseBloque([0,260],[1000,50])#Piso
    Bloques.add(B)
    Pj=ClasePersonaje([490,150],Sprites_Personaje,Bloques)
    Personaje.add(Pj)
    G1=ClaseGenerador([-10,180],'der',True)
    Generadores.add(G1)
    G1=ClaseGenerador([ANCHO+10,180],'izq',True)
    Generadores.add(G1)
    x=17
    y=104
    for i in range(8):
        w=ClaseBloque([x+INICIO,y],[60,5])#Escalas
        Bloques.add(w)
        x+=19
        y+=19.5
    while not finJuego:
        Pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finJuego=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    posxfondo=0
                    for b in Bloques:
                        b.rect.x-=INICIO
                if event.key==pygame.K_a:#Volear pata
                    if Pj.estado==6:#Que este en el aire y volie pata
                        EPatadaVoladora.play()
                        Pj.estado=7
                        Pj.con=0
                        velxfondo=0
                    elif Pj.estado==8:#Que este agachado y volie pata
                        EPatadaBaja.play()
                        Pj.estado=10
                        Pj.con=0
                        velxfondo=0
                    elif Pj.estado!=4 and Pj.estado!=5:#Que no este pegando puños ni patadas normales
                        EPatadaVoladora.play()
                        Pj.RecordarEstado()
                        Pj.estado=4
                        Pj.con=0
                        velxfondo=0
                if event.key==pygame.K_s:#Volear puño
                    if (Pj.estado!=4 and Pj.estado!=5) and Pj.estado!=6:#Que no este pegando puños ni patadas normales ni saltando
                        EPuño.play()
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
#Control de los golpes:
        for g in Golpes:
            if g.con<0:
                Golpes.remove(g)
#Control de lanzamientos de jefes:
        if Jefefinal != True:
            for J in Jefes:
                if J.estado==3 and J.disparar:
                    J.disparar=False
                    r=random.randrange(2)
                    if r==0:
                        posefectiva=[J.rect.x,J.rect.y+20]
                        tipo='bajo'
                    else:
                        posefectiva=[J.rect.x,J.rect.y-20]
                        tipo='alto'
                    if J.orientacion=='der':
                        vel=VELOCIDADMOVIMIENTO+5
                    else:
                        vel=-1*VELOCIDADMOVIMIENTO-5
                    L=ClaseLanzable(posefectiva,Sprites_Jefe1[0][5],vel,J.orientacion,tipo)
                    Lanzables.add(L)
                    EBolaFuego.play()#-------------------------------------------
                if J.salud<=0 and J.estado!=5:
                    J.estado=5
                    J.ReiniciarContador()
                    J.velx=0
                    if nivel==1:
                        EMuerteJefe.play()
                        Jefe1Derrotado=True
                if J.con>=5 and J.estado==5:
                    Jefes.remove(J)
#Control de lanzables para optimizar memoria:
        for L in Lanzables:
            if L.rect.x>ANCHO+100 or L.rect.x<-20:
                Lanzables.remove(L)
#Control de vidas y muerte
        if Pj.salud<=0:
            vidas-=1
            Pj.salud=100
            Puntuacion=0
            tiempo=2000
            EnemigosNormales.empty()
            EnemigosLanza.empty()
            Jefes.empty()
            Lanzables.empty()
            LanzablesPj.empty()

            posxfondo=INICIO

        #Colisiones de lanzables con PJ
        ls_col=pygame.sprite.spritecollide(Pj,Lanzables,False)#modificacion------------------
        for i in ls_col:
            if Pj.estado==6 and i.tipo=='bajo' and i.esquivado==False:#Esquivado
                i.esquivado=True
                i.activo=False
            elif Pj.estado==8 and i.tipo=='alto' and i.esquivado==False:#Esquivado
                i.esquivado=True
                i.activo=False
            else:
                if i.activo:
                    Pj.salud-=3
                    i.activo=False
                    Lanzables.remove(i)#posible fallo
#Colision de Pj con jefes:
        if Jefefinal != True:
            ls_col=pygame.sprite.spritecollide(Pj,Jefes,False)
            for i in ls_col:
                if ((Pj.estado==4 or Pj.estado==5) or (Pj.estado==7 or Pj.estado==9 or Pj.estado==10)):#Esta pegando de alguna forma
                    M.salud-=1
        else:
            ls_col=pygame.sprite.spritecollide(Pj,Jefes,False)
            for i in ls_col:
                if ((Pj.estado==4 or Pj.estado==5) or (Pj.estado==7 or Pj.estado==9 or Pj.estado==10)):#Esta pegando de alguna forma
                    MrX.salud-=1
#Colisiones de Pj con conBonus
        ls_col=pygame.sprite.spritecollide(Pj,Bonus,False)
        for B in ls_col:
            Bonus.remove(B)
            if B.tipo==1:#El tipo 1 da mas vida
                if Pj.salud<=120:
                    Pj.salud+=10
                    EVidaExtra.play()
            else:#Hacer un disparo
                vel=0
                if Pj.orientacion=='der':
                    vel=VELOCIDADMOVIMIENTO+5
                else:
                    vel=-1*VELOCIDADMOVIMIENTO-5
                posefectiva=[Pj.rect.x,Pj.rect.y]
                D=ClaseLanzable(posefectiva,Sprites_Jefe1[0][5],vel,Pj.orientacion,'bajo')
                LanzablesPj.add(D)
                EBolaFuego.play()
#Colisiones de enemigos normales con Pj:
        ls_col=pygame.sprite.spritecollide(Pj,EnemigosNormales,False)
        if len(ls_col)>0:
            for l in ls_col:
                #Pj.velx=0
                if (((Pj.estado==1 or Pj.estado==2) or Pj.estado==3) or Pj.estado==11) and l.estado!=4:#Si no esta pegando
                    if l.contadorgolpe<=0:
                        l.ReiniciarContadorGolpe()
                        Pj.salud-=2
                    Pj.estado=11
                    Pj.velx=0
                else:
                    if (l.estado!=4) and (((((Pj.estado!=1 and Pj.estado!=2) and Pj.estado!=3) and Pj.estado!=8) and Pj.estado!=11) and Pj.estado!=6):
                        if l.orientacion!=Pj.orientacion:
                            l.estado=4
                            Posefectiva=0
                            tipoGolpe=0
                            if Pj.estado==5:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+20]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+20]
                                tipoGolpe=0
                            if Pj.estado==4:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+20]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+20]
                                tipoGolpe=1
                            if Pj.estado==9:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+50]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+50]
                                tipoGolpe=1
                            if Pj.estado==7:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[l.rect.left,l.rect.top+20]
                                else:
                                    Posefectiva=[l.rect.right,l.rect.top+20]
                                tipoGolpe=1
                            try:
                                g=ClaseGolpe(Posefectiva,Sprites_Golpes,tipoGolpe)
                                Golpes.add(g)
                                Puntuacion+=100
                            except:
                                pass
#Control de colisiones con emeigos Lanzables
        ls_col=pygame.sprite.spritecollide(Pj,EnemigosLanza,False)
        if len(ls_col)>0:
            for l in ls_col:
                #Pj.velx=0
                if (((Pj.estado==1 or Pj.estado==2) or Pj.estado==3) or Pj.estado==11) and l.estado!=4:#Si no esta pegando
                    if l.contadorgolpe<=0:
                        l.ReiniciarContadorGolpe()
                        Pj.salud-=2
                    Pj.estado=11
                    Pj.velx=0
                else:
                    if (l.estado!=4) and (((((Pj.estado!=1 and Pj.estado!=2) and Pj.estado!=3) and Pj.estado!=8) and Pj.estado!=11) and Pj.estado!=6):
                        if l.orientacion!=Pj.orientacion:
                            l.estado=4
                            Posefectiva=0
                            tipoGolpe=0
                            if Pj.estado==5:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+20]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+20]
                                tipoGolpe=0
                            if Pj.estado==4:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+20]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+20]
                                tipoGolpe=1
                            if Pj.estado==9:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[Pj.rect.x,Pj.rect.y+50]
                                else:
                                    Posefectiva=[Pj.rect.x+40,Pj.rect.y+50]
                                tipoGolpe=1
                            if Pj.estado==7:
                                if Pj.orientacion=="izq":
                                    Posefectiva=[l.rect.left,l.rect.top+20]
                                else:
                                    Posefectiva=[l.rect.right,l.rect.top+20]
                                tipoGolpe=1
                            try:
                                g=ClaseGolpe(Posefectiva,Sprites_Golpes,tipoGolpe)
                                Golpes.add(g)
                                Puntuacion+=100
                            except:
                                pass
#Eliminacion de enemigos que no esten en la Pantalla
        for E in EnemigosNormales:
            if E.rect.top>=ALTO-200:
                EnemigosNormales.remove(E)
        for E in EnemigosLanza:
            if E.rect.top>=ALTO-200:
                EnemigosLanza.remove(E)
        for E in EnemigosLanza:
            if E.disparar:
                E.disparar=False
                vel=0
                if E.orientacion=='der':
                    vel=VELOCIDADMOVIMIENTO+5
                else:
                    vel=-1*VELOCIDADMOVIMIENTO-5

                if E.ultimoestado==2:
                    posefectiva=[E.rect.x,E.rect.y-20]
                    D=ClaseLanzable(posefectiva,Sprites_EnemigoCuchillo[0][7],vel,E.orientacion,'alto')
                else:
                    posefectiva=[E.rect.x,E.rect.y+20]
                    D=ClaseLanzable(posefectiva,Sprites_EnemigoCuchillo[0][7],vel,E.orientacion,'bajo')
                Lanzables.add(D)#posible cagada
                ELanzaCuchillo.play()#--------------------------

        for g in Generadores:
            if g.con<=0:
                g.NuevoCon()
                r=random.randrange(2)
                #r=2
                if r==1:
                    F=ClaseEnemigoNormal(g.rect,Sprites_EnemigoNormal,g.orientacion)
                    EnemigosNormales.add(F)
                else:
                    F=ClaseEnemigoLanza(g.rect,Sprites_EnemigoCuchillo,g.orientacion)
                    EnemigosLanza.add(F)
            if g.conBonus<=0:
                g.NuevoConBonus()
                posefectiva=[g.rect.x,g.rect.y+30]
                B=ClaseBonus(posefectiva,Sprites_Bonus)
                Bonus.add(B)

#Colision de los lanzables con EnemigosLanza
        for L in LanzablesPj:
            ls_col=pygame.sprite.spritecollide(L,EnemigosNormales,False)
            for E in ls_col:
                E.estado=4
                LanzablesPj.remove(L)
            ls_col=pygame.sprite.spritecollide(L,EnemigosLanza,False)
            for E in ls_col:
                E.estado=4
                LanzablesPj.remove(L)

#Control del fondo
        if nivel==1:
            if posxfondo<=-2100:
                velxfondo=0
            if posxfondo==0 and len(Jefes)==0 and Jefe1Derrotado==False:
                M=ClaseMago([-20,180],Sprites_Jefe1)
                Jefes.add(M)
            if posxfondo==0 and Pj.estado==3 and Pj.rect.right==560:
                posxfondo=0
                Pj.velx=VELOCIDADMOVIMIENTO
            if posxfondo==-2100 and Pj.estado==2 and Pj.rect.left==440:
                posxfondo=-2095
                Pj.velx=-1*VELOCIDADMOVIMIENTO
            if posxfondo==0:
                posxfondo=0
                velxfondo=0
            else:
                posxfondo+=velxfondo
            if nivel==1 and Pj.rect.top<=50 and len(Jefes)==0:
                CancionFondo.stop()
                nivel=2
                Pj.salud=100
                tiempo=2000
                EnemigosLanza.empty()
                EnemigosNormales.empty()
                Bloques.empty()
                Lanzables.empty()
                LanzablesPj.empty()
                Bonus.empty()
                B=ClaseBloque([0,260],[1000,50])#Piso
                Bloques.add(B)
                posxfondo=INICIO
                velxfondo=0
                Pj.estado=1
                Pj.ReiniciarPosicion()
                HistoriaMitad(Pantalla,reloj)
                CancionFondo.play()
            Pantalla.blit(Fondo1,[posxfondo,0])
        if nivel==2:

            if posxfondo<=-2100:
                velxfondo=0
            if posxfondo==0 and len(Jefes)==0 and Jefe2Derrotado==False:
                MrX=ClaseJefe([300,180], Sprites_Jefe2, 'der')
                Jefes.add(MrX)
                ERisaJefe.play()
                Jefefinal=True
            if posxfondo==0 and Pj.estado==3 and Pj.rect.right==560:
                posxfondo=0
                Pj.velx=VELOCIDADMOVIMIENTO
            if posxfondo==-2100 and Pj.estado==2 and Pj.rect.left==440:
                posxfondo=-2095
                Pj.velx=-1*VELOCIDADMOVIMIENTO
            if posxfondo==0:
                posxfondo=0
                velxfondo=0
            else:
                posxfondo+=velxfondo
            Pantalla.blit(Fondo2,[posxfondo,0])
            #Cambiar orientacion del Jefe si sobrepasa el PJ
            for n in Jefes:
                if MrX.rect.left >= Pj.rect.right:
                    MrX.orientacion='izq'
                else:
                    MrX.orientacion='der'

            #Colision del Pj con Enemigo Principal
            if Jefefinal==True:
                ls_col=pygame.sprite.spritecollide(MrX,Personaje,False)
                for i in ls_col:#3, 4, 5, 7 y 8
                    if ((MrX.estado==3 or MrX.estado==4) or (MrX.estado==5 or MrX.estado==7 or MrX.estado==8)):
                        Pj.salud-=1
            #Muerte enemigo principala
            for E in Jefes:
                if MrX.salud <= 0:
                    MrX.estado=9
                    Jefe2Derrotado=True
                    EMuerteJefe.play()
                    HistoriaFinal(Pantalla,reloj)
                    finJuego=True
                    CancionFondo.stop()


        Texto='Puntuacion del jugador: '+str(Puntuacion)
        Dib=Fuente1.render(Texto,True,BLANCO)
        Pantalla.blit(Dib,[50,450])

        Texto='Tiempo: '+str(tiempo)
        Dib=Fuente1.render(Texto,True,BLANCO)
        Pantalla.blit(Dib,[800,450])

        Texto='Vidas: '
        Dib=Fuente1.render(Texto,True,BLANCO)
        Pantalla.blit(Dib,[620,450])
        pygame.draw.polygon(Pantalla,ROJO,[[50,420],[50+3*Pj.salud,420],[50+3*Pj.salud,440],[50,440]])
        x=700
        for i in range(vidas):
            Pantalla.blit(Im_Vidas,[x+i*25,450])
        if Jefe1Derrotado==False and len(Jefes)==1 and nivel==1:
            pygame.draw.polygon(Pantalla,VERDE,[[500,420],[500+3*M.salud,420],[500+3*M.salud,440],[500,440]])
        if Jefe2Derrotado==False and len(Jefes)==1 and nivel==2:
            pygame.draw.polygon(Pantalla,AMARILLO,[[500,420],[500+5*MrX.salud,420],[500+5*MrX.salud,440],[500,440]])
        Bloques.update(Pantalla,velxfondo)


        if tiempo <= 0 or vidas<=0:
            CancionFondo.stop()
            CancionPerdida.play()
            if counter<50:
                Pantalla.blit(Hist7,[0,0])
                counter+=1
                Personaje.empty()
                Bloques.empty()
                EnemigosNormales.empty()
                EnemigosLanza.empty()
                Jefes.empty()
                Lanzables.empty()
                LanzablesPj.empty()

            else:
                finJuego=True

        #print('Velocidad:', velxfondo, ' Posicion: ',posxfondo)
        EnemigosNormales.update(Pantalla,velxfondo,Personaje)
        EnemigosLanza.update(Pantalla,velxfondo,Personaje)
        Personaje.update(Pantalla,posxfondo)
        Generadores.update()
        Golpes.update(Pantalla)
        Jefes.update(Pantalla)
        Lanzables.update(Pantalla,velxfondo)
        LanzablesPj.update(Pantalla,velxfondo)
        Bonus.update(Pantalla,velxfondo)
        tiempo-=1
        pygame.display.flip()
        reloj.tick(15)#15 ticks es lo mejor
