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

class TT:
    def __init__(self, lista):
        self.lista = lista

    def copyT(self):
        T_copy = copy.deepcopy(self)
        return T_copy

    def Draw(self, color):
        for e in self.lista:
            e.Draw(color)

    def Rotar(self, a):
        for e in self.lista:
            e.Rote(a)

def imprimeLista(l,color):
    for e in l:
        e.Draw(color)

def rotarFigura(l, a):
    for e in l:
        e.Rote(a)

libreria1.makePlane()

#-----------------1------------------------


v_l = [] #aqui van a quedar todos los vectores de la figura

#v0
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(30)))
v_l.append(v)
#v1
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(180-30)))
v_l.append(v)
#v2
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(90)))
v.moveTo(v_l[1].getPoints()[1])
v_l.append(v)
#v3
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(90)))
v_l.append(v)
#v4
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180-30)))
v.moveTo(v_l[3].getPoints()[1])
v_l.append(v)
#v5
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(30)))
v.moveTo(v_l[3].getPoints()[1])
v_l.append(v)
#v6
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180-30)))
v.moveTo(v_l[5].getPoints()[1])
v_l.append(v)
#v7
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180+30)))
v.moveTo(v_l[6].getPoints()[1])
v_l.append(v)
#v8
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(90)))
v.moveTo(v_l[6].getPoints()[1])
v_l.append(v)
#v9
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(90)))
v.moveTo(v_l[4].getPoints()[1])
v_l.append(v)
#v10
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180+30)))
v.moveTo(v_l[8].getPoints()[1])
v_l.append(v)
#v11
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180-30)))
v.moveTo(v_l[10].getPoints()[1])
v_l.append(v)
#v12
v = libreria1.V([0,0],libreria1.Polar(100,libreria1.DegToRad(30)))
v.moveTo(v_l[11].getPoints()[1])
v_l.append(v)
#v13
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(-30)))
v.moveTo(v_l[12].getPoints()[1])
v_l.append(v)
#v14
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180+30)))
v.moveTo(v_l[13].getPoints()[1])
v_l.append(v)
#v15
v = libreria1.V([0,0],libreria1.Polar(90,libreria1.DegToRad(-60)))
v.moveTo(v_l[14].getPoints()[1])
v_l.append(v)
#v16
v = libreria1.V([0,0],libreria1.Polar(88,libreria1.DegToRad(-60)))
v.moveTo(v_l[14].getPoints()[0])
v_l.append(v)
#v17
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180+30)))
v.moveTo(v_l[16].getPoints()[1])
v_l.append(v)
#v18
v = libreria1.V([0,0],libreria1.Polar(50,libreria1.DegToRad(180+90)))
v.moveTo(v_l[17].getPoints()[0])
v_l.append(v)

#imprimeLista(v_l, AZUL) #imprime lista de vectores

#------------------2--------------------------

T = []

v = libreria1.V([0,0],[0,50])
T.append(v)

v = libreria1.V([0,0],[-50,0])
v.moveTo(T[0].getPoints()[1])
T.append(v)

v = libreria1.V([0,0],[50,0])
v.moveTo(T[0].getPoints()[1])
T.append(v)

t = TT(T)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        else :
            imprimeLista(T, NEGRO) #imprime lista de vectores
            rotarFigura(T,libreria1.DegToRad(30))
            imprimeLista(T, VERDE) #imprime lista de vectores
