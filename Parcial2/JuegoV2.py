import pygame
import random
ANCHO=1200
ALTO=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
AMARILLO=[200,200,0]

def AutomataProbabilistico(estado):
    Probabilidad=50
    nuevoestado=0
    r=random.randrange(100)
    if estado==0:
        if r>Probabilidad:
            r=random.randrange(100)
            if r>50:
                nuevoestado=1
            else:
                nuevoestado=2
        else:
            nuevoestado=0
    elif estado==1:
        if r>Probabilidad:
            r=random.randrange(100)
            if r>50:
                nuevoestado=0
            else:
                nuevoestado=2
        else:
            nuevoestado=0
    elif estado==2:
        if r>Probabilidad:
            r=random.randrange(100)
            if r>50:
                nuevoestado=1
            else:
                nuevoestado=0
        else:
            nuevoestado=0
    return nuevoestado
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
class Personaje(pygame.sprite.Sprite):
    def __init__(self,pos,m):#Constructor
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
        self.bloques=[]

    def update(self):
        if self.con<2:
            self.con+=1
        else:
            self.con=0
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        Pantalla.blit(self.m[self.estado][self.con],[self.rect.x,self.rect.y])

        ls_obj = pygame.sprite.spritecollide(self, self.bloques, False)
        for b in ls_obj:

            if self.rect.right > b.rect.left and self.velx>0:
                self.rect.right = b.rect.left
                self.velx = 0

            if self.rect.left < b.rect.right and self.velx<0:
                self.rect.left = b.rect.right
                self.velx = 0

            if self.rect.top < b.rect.bottom and self.vely<0:
                self.rect.top = b.rect.bottom
                self.vely = 0

            if self.rect.bottom > b.rect.top and self.vely>0:
                self.rect.bottom = b.rect.top
                self.vely = 0
class Disparos(pygame.sprite.Sprite):
    def __init__(self,pos,m,velx,cant_sprites):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=velx+5
        self.limites=cant_sprites-1

    def update(self):
        if self.con<self.limites:
            self.con+=1
        else:
            self.con=0
        self.rect.x+=self.velx
        Pantalla.blit(self.m[0][self.con],[self.rect.x,self.rect.y])
class Enemigo(pygame.sprite.Sprite):
    def __init__(self,pos,m,velx):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.con=0
        self.image=m[0][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=velx-5
        self.estado=0
        self.iniciosprite=0
        self.finsprite=0
        self.finaccion=0
        self.tiempo=0

    def update(self):
        self.tiempo-=1
        if self.tiempo<0:
            print('Cambio estado')
            self.tiempo=random.randrange(50)
            self.estado=AutomataProbabilistico(self.estado)
            if self.estado==0:
                self.vely=0
            if self.estado==1:
                self.vely=-3
            if self.estado==2:
                self.vely=3

        Pantalla.blit(self.m[0][6],[self.rect.x,self.rect.y])
        self.rect.x+=self.velx
        self.rect.y+=self.vely
class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, matriz):
        pygame.sprite.Sprite.__init__(self)
        self.m=matriz
        self.con=2
        self.dir=2
        self.image=self.m[self.dir][self.con]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0

    def update(self):
        self.rect.x+=self.velx

if __name__=='__main__':
    pygame.init()
    reloj=pygame.time.Clock()
    Pantalla=pygame.display.set_mode([ANCHO,ALTO])
    fin=False

    #Recorte se todos los sprites
    Sprites_Enemigos=RecortarSprite('naveizq.png',7,4)
    Sprites_Jefe1=RecortarSprite('jefe1.png',4,1)
    Sprites_Jefe2=RecortarSprite('jefe2.png',4,1)
    Sprites_Jefe3=RecortarSprite('jefe3.png',2,2)
    Sprites_Personaje=RecortarSprite('Personaje.png',3,3)
    Sprites_Meteoritos=RecortarSprite('Meteoritoseditado.png',8,2)
    Sprites_Disparo1=RecortarSprite('Disparo1.png',4,1)
    Sprites_Disparo2=RecortarSprite('Disparo2.png',3,1)
    Sprites_Disparo3=RecortarSprite('Disparo3.png',4,1)
    Sprites_DisparosEnemigos=RecortarSprite('DisparosEnemigos.png',7,1)
    Sprites_Bonus=RecortarSprite('Bonus.png',2,3)
    Sprites_mapa=RecortarSprite('tileset1.png', 8, 6)

    #Para el fondo
    fondo = pygame.image.load('prueba.jpg')#-----> cambiar imagen (esta en el drive) por fondo de morado

    info= fondo.get_rect()
    fondo_ancho = info[2]
    fondo_alto = info[3]
    FondoX = 0
    FondoVelX = 0
    FondoY = 0
    lim_derecho = 650
    lim_izquierdo = 550

    #Grupos
    Personajes=pygame.sprite.Group()
    DisparosPersonajes=pygame.sprite.Group()
    Enemigos=pygame.sprite.Group()
    bloques=pygame.sprite.Group()

    #creacion de bloques morados
    ls_bloques=[]
    cont=0
    for i in range(100):
        B=Bloque([cont,568], Sprites_mapa)
        bloques.add(B)
        cont+=32


    bloque1=Bloque([1100,300], Sprites_mapa)   #Bloque de prueba colisiones
    bloques.add(bloque1)

    E=Enemigo([900,400],Sprites_Enemigos,0)
    Enemigos.add(E)
    J=Personaje([600,300],Sprites_Personaje)
    Personajes.add(J)
    J.bloques=bloques #para que reconozca los bloques al colisionar


    #ciclo juego
    while not fin:
        Pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    J.vely=-5
                    J.velx=0
                    J.estado=0
                if event.key==pygame.K_DOWN:
                    J.vely=5
                    J.velx=0
                    J.estado=2
                if event.key==pygame.K_RIGHT:
                    J.velx=5
                    J.vely=0
                    J.estado=1
                if event.key==pygame.K_LEFT:
                    J.velx=-5
                    J.vely=0
                    J.estado=1
                if event.key==pygame.K_a:
                    D=Disparos(J.rect,Sprites_Disparo1,J.velx,4)
                    DisparosPersonajes.add(D)
            if event.type==pygame.KEYUP:
                J.vely=0
                J.velx=0
                J.estado=1
                FondoVelX = 0  #---->revisar: puede solucionar el bug de mapa (teclas abajo)
                for b in bloques:
                    b.velx=0

        #Verifica que sigan en la pantalla:
        for b in DisparosPersonajes:
            if b.rect.left>ANCHO:
                DisparosPersonajes.remove(b)
        for n in Enemigos:
            if n.rect.right<0:
                Enemigos.remove(n)
                print ('Eliminado')

        #Haciendo que el fondo se mueva con el objeto jugador
        if J.rect.right > lim_derecho:
            J.rect.right = lim_derecho
            J.velx = 0
            FondoVelX = -5
            if FondoX < fondo_ancho :
                for b in bloques:
                    b.velx=-5


        if J.rect.left < lim_izquierdo:
            J.rect.left = lim_izquierdo
            J.velx = 0
            FondoVelX = 5
            if FondoX < 0:
                for b in bloques:
                    b.velx=5
        #print(FondoX)

        #Haciendo el recorrido del fondo no pase de su limite
        if FondoX < (ANCHO - fondo_ancho):
            FondoX+=5
            FondoVelX = 0
        elif FondoX > 0:
            FondoVelX = 0
            FondoX-=5

        Pantalla.blit(fondo,[FondoX,FondoY]) #Muestra la imagen del fondo del juego

        Personajes.update()
        DisparosPersonajes.update()
        Enemigos.update()
        bloques.update()

        bloques.draw(Pantalla)
        #Personajes.draw(Pantalla)
        #Enemigos.draw(Pantalla)
        DisparosPersonajes.draw(Pantalla)


        pygame.display.flip()
        reloj.tick(30)
        FondoX+=FondoVelX #Hace que el fondo avance
    pygame.quit()
