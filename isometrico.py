import libreria1
import pygame
import sys

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)


class Square:#cuadrado
    #un cuadrado es un conjunto de puntos
    def __init__(self,p1,p2,p3,p4):
        self.arrPoints = [p1,p2,p3,p4]

    def getPoints(self):
        return self.arrPoints

    def setPoints(self, p1,p2,p3,p4):
        self.arrPoints = [p1,p2,p3,p4] #se reemplazan

'''class Cube:
    #Un cubo es un conjunto de cuadrados
    __init__(self,s1,s2,s3,s4):
        self.arrPoints = [s1,s2,s3,s4]'''


print "holaa"
cuadrado = Square([0,0],[0,10],[10,0],[10,10])
points = cuadrado.getPoints()
for p in points:
    print p
    print "hola"

pantalla = pygame.display.set_mode([ANCHO,ALTO])
libreria1.makePlane(pantalla)
#libreria1.main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
