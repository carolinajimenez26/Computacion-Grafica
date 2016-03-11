import libreria1
import pygame
import sys
import copy
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)


def imprimeLista(l,color):
    for e in l:
        e.Draw(color)

def rotarFigura(l, a):
    for e in l:
        e.Rote(a)

libreria1.makePlane()

v_l = [] #aqui van a quedar todos los vectores de la figura

#v1
v = libreria1.V([0,0],[-100,0])
v_l.append(v)
#v2
v = libreria1.V([0,0],[0,40])
v.moveTo([-100,0])
v_l.append(v)
#v3
v = libreria1.V([0,0],libreria1.Polar(120,libreria1.DegToRad(30)))
v_l.append(v)
#v4
v = libreria1.V([0,0],[0,20])
v_l.append(v)
#v5
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180-30)))
v.moveTo([0,20])
v_l.append(v)
#v6
v = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(30)))
v.moveTo([0,20])
v_l.append(v)
#v7
v = libreria1.V([0,0],[-60,0])
v.moveTo([-40,40])
v_l.append(v)
#v8
v2 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(30)))
v2.moveTo(v.getPoints()[1])
v_l.append(v2)
#v9
v2 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(30)))
v2.moveTo(v.getPoints()[0])
v_l.append(v2)
#v10
v3 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(360-30)))
v3.moveTo(v2.getPoints()[1])
v_l.append(v3)
#v11
v4 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(180)))
v4.moveTo(v2.getPoints()[1])
v_l.append(v4)
#v12
v = libreria1.V([0,0],[0,40])
v.moveTo(v3.getPoints()[1])
v_l.append(v)
#v13
v2 = libreria1.V([0,0],[0,20])
v2.moveTo(v4.getPoints()[1])
v_l.append(v2)
#v14
v3 = libreria1.V(v2.getPoints()[1],v.getPoints()[1])
v_l.append(v3)
#v15
v4 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(30)))
v4.moveTo(v.getPoints()[1])
v_l.append(v4)
#v18
v = libreria1.V([0,0],[0,60])
v.Rote(libreria1.DegToRad(180))
v.moveTo(v4.getPoints()[1])
v_l.append(v)

#v16
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(180)))
v.moveTo(v4.getPoints()[1])
v_l.append(v)

#v17
v = libreria1.V(v3.getPoints()[0],v.getPoints()[1])
v_l.append(v)
reloj = pygame.time.Clock()

i = 0
while(i < 360):
    rotarFigura(v_l, libreria1.DegToRad(30))
    imprimeLista(v_l, VERDE) #imprime lista de vectores
    reloj.tick(1)
    if i != 360-30:
        imprimeLista(v_l, NEGRO) #imprime lista de vectores
    i += 30
    print i

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
