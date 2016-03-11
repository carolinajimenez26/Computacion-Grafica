import libreria1
import pygame
import sys
import copy
pi = 3.1415

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

def mueveLista(l):
    for e in l:
        e.moveTo([0,-100])

libreria1.makePlane()

v_l = [] #aqui van a quedar todos los vectores de la figura

#v1
v1 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(30)))
v_l.append(v1)
#v2
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(180-30)))
v_l.append(v)
#v3
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(90)))
v_l.append(v)
#v4
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(90)))
v.moveTo(v1.getPoints()[1])
v_l.append(v)
#v5
v1 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+30)))
v1.moveTo(v.getPoints()[1])
v_l.append(v1)
#v6
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(180-30)))
v.moveTo(v1.getPoints()[1])
v_l.append(v)
#v7
v1 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+90)))
v1.moveTo(v.getPoints()[1])
v_l.append(v1)
#v8
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(30)))
v.moveTo(v1.getPoints()[0])
v_l.append(v)
#v9 PIVOTE
v1 = libreria1.V([0,0],libreria1.Polar(80,libreria1.DegToRad(-30)))
v1.moveTo(v.getPoints()[1])
v_l.append(v1)
#v10
v = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(90)))
v.moveTo(v1.getPoints()[1])
v_l.append(v)
#v11
v4 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(30)))
v4.moveTo(v1.getPoints()[1])
v_l.append(v4)
#v12
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(90)))
v.moveTo(v1.getPoints()[0])
v_l.append(v)
#v13  PIVOTE
v2 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(-30)))
v2.moveTo(v.getPoints()[1])
v_l.append(v2)
#v14
v5 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(90)))
v5.moveTo(v4.getPoints()[1])
v_l.append(v5)
#v19
v3 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(30)))
v3.moveTo(v.getPoints()[1])
v_l.append(v3)
#v15
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)
#v16
v3 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180-30)))
v3.moveTo(v.getPoints()[1])
v_l.append(v3)
#v17 YA NO SE NECESITA EL PIVOTE DEL V13, ESTE ES EL NUEVO PIVOTE
v3 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+90)))
v3.moveTo(v2.getPoints()[1])
v_l.append(v3)
#v18
v2 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(-30)))
v2.moveTo(v3.getPoints()[1])
v_l.append(v2)
#v20
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)
#v21
v2 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180-30)))
v2.moveTo(v.getPoints()[1])
v_l.append(v2)
#v22
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)
#v23
v2 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(90)))
v2.moveTo(v.getPoints()[0])
v_l.append(v2)
#v24
v2 = libreria1.V([0,0],libreria1.Polar(60,libreria1.DegToRad(-30)))
v2.moveTo(v4.getPoints()[1])
v_l.append(v2)
#v25
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(180+30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)
#v27
v1 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+90)))
v1.moveTo(v2.getPoints()[1])
v_l.append(v1)
#v26
v2 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180+90)))
v2.moveTo(v.getPoints()[1])
v_l.append(v2)
#v28
v3 = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180-30)))
v3.moveTo(v.getPoints()[1])
v_l.append(v3)
#v29
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)
#v30
v = libreria1.V([0,0],libreria1.Polar(40,libreria1.DegToRad(180-30)))
v.moveTo(v2.getPoints()[1])
v_l.append(v)

mueveLista(v_l)#porque la pantalla no me alcanza
imprimeLista(v_l, AZUL) #imprime lista de vectores

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
