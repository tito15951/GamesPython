import pygame
import configparser
from Constantes import *

lista_terreno = []
texturas_mapa = []
tipo_bloque=[]


def recortar_imagen():

    archivo = configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    nombre_imagen = archivo.get('info', 'imagen')
    ancho_imagen = int(archivo.get('info', 'cantidad_ancho'))
    alto_imagen = int(archivo.get('info', 'cantidad_alto'))

    terreno = pygame.image.load(nombre_imagen)
    info = terreno.get_rect()
    ancho_pixeles = info[2]
    alto_pixeles = info[3]

    ancho_patron = ancho_pixeles/ancho_imagen
    alto_patron = alto_pixeles/alto_imagen

    #parametros  subsurface: posicion x, posicion y, ancho corte (ancho patron), alto corte(alto patron)

    for fila in range(alto_imagen):
        lista_terreno.append([])
        for col in range(ancho_imagen):
           cuadro = terreno.subsurface(ancho_patron*col, alto_patron*fila, ancho_patron, alto_patron)
           lista_terreno[fila].append(cuadro)


def leer_mapa(pantalla,nombre_mapa):
    archivo = configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    #se carga informacion del archivo info_mapa
    mapa = archivo.get('info', nombre_mapa)
    ls_filas = mapa.split('\n')  # divide el mapa por filas
    x = 0
    y = 0
    i = 0
    for j in range(len(ls_filas)):
        i = 0
        for e in ls_filas[j]:
            columna = int(archivo.get(e, 'col'))
            fila = int(archivo.get(e, 'fila'))
            x = i*32
            y = j*32
            pantalla.blit(lista_terreno[fila][columna],[x, y])
            i += 1


def obtener_bloques(nombre_mapa):
    archivo = configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    coordenadas_bloques = []
    bloques_fondo = []
    #se carga informacion del archivo info_mapa
    mapa = archivo.get('info', nombre_mapa)
    ls_filas = mapa.split('\n')  # divide el mapa por filas
    x = 0
    y = 0
    i = 0
    for j in range(len(ls_filas)):
        i = 0
        for e in ls_filas[j]:
            if e!= '.' and e!='*' and e!=';': #cambio
                columna = int(archivo.get(e, 'col'))
                fila = int(archivo.get(e, 'fila'))
                x = i*32
                y = j*32
                coordenadas_bloques.append([x,y])
                texturas_mapa.append(lista_terreno[fila][columna])
            i += 1
    return coordenadas_bloques


def obtener_bloquesalterno(nombre_mapa,recortes):
    archivo = configparser.ConfigParser()
    archivo.read('info_mapa.txt')
    coordenadas_bloques=[]
    texturas_mapa=[]
    #se carga informacion del archivo info_mapa
    mapa = archivo.get('info', nombre_mapa)
    ls_filas = mapa.split('\n')  # divide el mapa por filas
    x = 0
    y = 0
    i = 0
    for j in range(len(ls_filas)):
        i = 0
        for e in ls_filas[j]:
            if e!= '.' and e!='*' and e!=';': #cambio
                columna = int(archivo.get(e, 'col'))
                fila = int(archivo.get(e, 'fila'))
                x = i*32
                y = j*32
                coordenadas_bloques.append([x,y])
                texturas_mapa.append(recortes[fila][columna])
            i += 1
    return coordenadas_bloques,texturas_mapa
def Retornovector():
    return texturas_mapa
