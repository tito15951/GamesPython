import random
import pygame
ANCHO=1000
ALTO=500
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
AMARILLO=[200,200,0]
VELOCIDADMOVIMIENTO=5

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
