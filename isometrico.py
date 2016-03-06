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

class Square:#cuadrado
    #un cuadrado es un conjunto de vectores
    def __init__(self,v1,v2,v3,v4):
        self.arrPoints = [v1,v2,v3,v4]

    def getVectors(self):
        return self.arrPoints

    def setVectors(self,p1,p2,p3,p4):
        self.arrPoints = [v1,v2,v3,v4] #se reemplazan

    def Draw(self, color):
        p = self.getVectors()
        for v in p: #dibujamos cada vector
            v.Draw(AZUL)

    def moveTo(self, pivote):#se mueve a un punto
        p = self.getVectors()
        for v in p:#por cada vector que hay en p
            point = v.getPoints() #[(x1,y1),(x2,y2)]
            v.setPoints(libreria1.moveToPoint(point[0],pivote), libreria1.moveToPoint(point[1],pivote))

    def returnTo(self, pivote):#se devuelve a un punto
        p = self.getVectors()
        for v in p:#por cada vector que hay en p
            point = v.getPoints() #[(x1,y1),(x2,y2)]
            v.setPoints(libreria1.moveToCenter(point[0],pivote), libreria1.moveToCenter(point[1],pivote))

class Cube:
    #Un cubo es un conjunto de cuadrados
    def __init__(self,s1,s2,s3,s4,s5,s6):#un cubo tiene 6 lados
        self.arrPoints = [s1,s2,s3,s4,s5,s6]

    def getSquares(self):
        return self.arrPoints

    def setSquares(self,s1,s2,s3,s4,s5,s6):
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

base_copy = copy.deepcopy(base) #El cuadrado de arriba es exactamente el mismo, pero trasladado
base_copy.moveTo([0,20]) #sube traslada a un punto
base_copy.Draw(AZUL)
base_copy_vectors = base_copy.getVectors()#vectores de base_copy
A_copy = base_copy_vectors[0].getPoints()#el primer vector es la copia de A
B_copy = base_copy_vectors[1].getPoints()#el segundo vector es la copia de B

#LADO1
V1 = libreria1.V(VA.getPoints()[0], A_copy[0])
V2 = libreria1.V(VA.getPoints()[1], A_copy[1])
side1 = Square(VA,base_copy_vectors[0],V1,V2)
side1.Draw(AZUL)

#LADO2
V2 = libreria1.V(VB.getPoints()[1], B_copy[1])
side2 = Square(VB,base_copy_vectors[1],V1,V2)
side2.Draw(AZUL)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
