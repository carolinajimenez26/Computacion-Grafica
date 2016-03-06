import libreria1
import pygame
import sys
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)

class Square:#cuadrado
    #un cuadrado es un conjunto de vectores
    def __init__(self,v1,v2,v3,v4):
        self.arrPoints = [v1,v2,v3,v4]

    def getPoints(self):
        return self.arrPoints

    def setPoints(self, p1,p2,p3,p4):
        self.arrPoints = [v1,v2,v3,v4] #se reemplazan

    def Draw(self, color):
        p = self.getPoints()
        for v in p: #dibujamos cada vector
            v.Draw(AZUL)


class Cube:
    #Un cubo es un conjunto de cuadrados
    def __init__(self,s1,s2,s3,s4):
        self.arrPoints = [s1,s2,s3,s4]

    def getPoints(self):
        return self.arrPoints

    def setPoints(self, p1,p2,p3,p4):
        self.arrPoints = [p1,p2,p3,p4]



libreria1.makePlane()

#ISOMETRICO1
A = libreria1.Polar(100,libreria1.DegToRad(30))
B = libreria1.Polar(80,libreria1.DegToRad(135))

VA = libreria1.V([0,0],A)
VA.Draw(AZUL)
VB = libreria1.V([0,0],B)
VB.Draw(AZUL)

V_SUMA = libreria1.VectorAdd(VA,VB)
#V_SUMA.Draw(BLANCO)
V_ =libreria1.parallelogramMethod(VA,VB,V_SUMA)

base = Square(VA,VB,V_[0],V_[1])
base.Draw(VERDE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
