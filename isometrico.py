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
            v.Draw(color)

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

    def Rote(self, angle):#rotar sobre un angulo
        p = self.getVectors()
        for v in p:#por cada vector que hay en p
            v.Rote(angle)

    def scale(self, s): #escalar todos los puntos del cuadrado. Puede reducirlos como agrandarlos
        p = self.getVectors()

        for i in p:
            print i.getPoints()

        pivote = p[0].getPoints()[1]#Debe ser el mismo punto
        #pivote = [86, 49]
        print "pivote: " , pivote

        for v in p:#por cada vector que hay en p
            #Primero se pasa al origen
            v.returnTo(pivote)
            #Despues se escala
            v.scale(s)
            #Despues se devuelve al punto inicial
            v.moveTo(pivote)

        print "-----------------------------------"


class Cube:
    #Un cubo es un conjunto de cuadrados
    def __init__(self,s1,s2,s3,s4,s5,s6):#un cubo tiene 6 lados
        self.arrPoints = [s1,s2,s3,s4,s5,s6]

    def getSquares(self):
        return self.arrPoints

    def setSquares(self,s1,s2,s3,s4,s5,s6):
        self.arrPoints = [p1,p2,p3,p4]

    def Draw(self, color):
        p = self.getSquares() #sacamos todos los cuadrados del cubo
        for s in p : #para cada uno de ellos
            s.Draw(color)

    def moveTo(self, pivote):#mueve cada uno de los cuadrados del cubo a un punto
        p = self.getSquares()
        for s in p : #para cada cuadrado en p
            s.moveTo(pivote)

    def returnTo(self, pivote):#retorna cada uno de los cuadrados del cubo al origen
        p = self.getSquares()
        for s in p : #para cada cuadrado en p
            s.returnTo(pivote)

    def Rote(self, angle):
        p = self.getSquares()
        for s in p : #para cada cuadrado en p
            s.Rote(angle)

    def scale(self, s):#escala cada uno de los cuadrados
        p = self.getSquares()
        for i in range (0,6):
            #p[i].Draw(BLANCO)
            p[i].scale(0.8)
            if i == 5:
                p[i].Draw(VERDE)
            else :
                print i



libreria1.makePlane()

#---------------------------------------------------------------
#ISOMETRICO1
A = libreria1.Polar(100,libreria1.DegToRad(30))
B = libreria1.Polar(80,libreria1.DegToRad(135))

VA = libreria1.V([0,0],A)
#VA.Draw(AZUL)
VB = libreria1.V([0,0],B)
#VB.Draw(AZUL)

V_SUMA = libreria1.VectorAdd(VA,VB)
#V_SUMA.Draw(BLANCO)
V_ = libreria1.parallelogramMethod(VA,VB,V_SUMA)

base = Square(VA,VB,V_[0],V_[1])
#base.Draw(VERDE)

base_copy = copy.deepcopy(base) #El cuadrado de arriba es exactamente el mismo, pero trasladado
base_copy.moveTo([0,20]) #sube traslada a un punto
#base_copy.Draw(AZUL)
base_copy_vectors = base_copy.getVectors()#vectores de base_copy
A_copy = base_copy_vectors[0].getPoints()#el primer vector es la copia de A
B_copy = base_copy_vectors[1].getPoints()#el segundo vector es la copia de B

#LADO1
V1 = libreria1.V(VA.getPoints()[0], A_copy[0])
V2 = libreria1.V(VA.getPoints()[1], A_copy[1])
side1 = Square(VA,base_copy_vectors[0],V1,V2)
#side1.Draw(AZUL)

#LADO2
V2 = libreria1.V(VB.getPoints()[1], B_copy[1])
side2 = Square(VB,base_copy_vectors[1],V1,V2)
#side2.Draw(AZUL)

#LADO3
V3 = libreria1.V(V_SUMA.getPoints()[1], libreria1.moveToPoint(V_SUMA.getPoints()[1],[0,20]))
V4 = libreria1.V(A,A_copy[1])
side3 = Square(V_[0],base_copy_vectors[2],V3,V4)
#side3.Draw(AZUL)

#LADO4
side4 = Square(V2,V3,V_[1], base_copy_vectors[3])
#side4.Draw(AZUL)

iso1 = Cube(base,base_copy,side1,side2,side3,side4)
iso1.Draw(AZUL)

p = iso1.getSquares()

'''for s in p: #vamos a escalar cada cuadrado
    s.Draw(BLANCO)
    s.scale(0.8)
    s.Draw(VERDE)

p[3].Draw(BLANCO)
p[3].scale(0.8)
p[3].Draw(VERDE)'''

#iso1.scale(0.8)
#iso1.Draw(ROJO)

#---------------------------------------------------------------
#ISOMETRICO2
A = libreria1.Polar(60,libreria1.DegToRad(30))
B = libreria1.Polar(40,libreria1.DegToRad(135))

VA = libreria1.V([0,0],A)
VA.Draw(AZUL)
VB = libreria1.V([0,0],B)
VB.Draw(AZUL)

V_SUMA = libreria1.VectorAdd(VA,VB)
#V_SUMA.Draw(BLANCO)
especial = V_SUMA.getPoints()#para mover el segundo isometrico a ese punto
V_ = libreria1.parallelogramMethod(VA,VB,V_SUMA)

base = Square(VA,VB,V_[0],V_[1])
#base.Draw(VERDE)

base_copy = copy.deepcopy(base) #El cuadrado de arriba es exactamente el mismo, pero trasladado
base_copy.moveTo([0,30]) #sube traslada a un punto
#base_copy.Draw(AZUL)
base_copy_vectors = base_copy.getVectors()#vectores de base_copy
A_copy = base_copy_vectors[0].getPoints()#el primer vector es la copia de A
B_copy = base_copy_vectors[1].getPoints()#el segundo vector es la copia de B

#LADO1
V1 = libreria1.V(VA.getPoints()[0], A_copy[0])
V2 = libreria1.V(VA.getPoints()[1], A_copy[1])
side1 = Square(VA,base_copy_vectors[0],V1,V2)
#side1.Draw(AZUL)

#LADO2
V2 = libreria1.V(VB.getPoints()[1], B_copy[1])
side2 = Square(VB,base_copy_vectors[1],V1,V2)
#side2.Draw(AZUL)

#LADO3
V3 = libreria1.V(V_SUMA.getPoints()[1], libreria1.moveToPoint(V_SUMA.getPoints()[1],[0,30]))
V4 = libreria1.V(A,A_copy[1])
side3 = Square(V_[0],base_copy_vectors[2],V3,V4)
#side3.Draw(AZUL)

#LADO4
side4 = Square(V2,V3,V_[1], base_copy_vectors[3])
#side4.Draw(AZUL)

iso2 = Cube(base,base_copy,side1,side2,side3,side4)
#iso2.Draw(AZUL)

#Hasta aca esta construido todo pero en el origen, ahora hay que trasladarlo
iso2.moveTo(especial[1])
iso2.Draw(BLANCO)

iso2.Rote(pi/2)
iso2.Draw(VERDE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
