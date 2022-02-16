import random
ANCHO=800
ALTO=600
VERDE=[0,255,0]
AZUL=[0,0,255]
ROJO=[255,0,0]
NEGRO=[0,0,0]
BLANCO=[255,255,255]
AMARILLO=[200,200,0]
VELOCIDADFONDO=-2





def AutomataProbabilistico(estado,prob=50):
    Probabilidad=prob
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
    elif estado==3:
        nuevoestado=3
    return nuevoestado
