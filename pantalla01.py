import pygame
import sys
import math

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0) #rgb
VERDE = (0,255,0)
AZUL = (0,0,255)

class V:#vector
    def __init__(self,pf): #recibe los puntos como si el centro fuera 0,0
        pi = [0,0] #punto inicial de todo vector
        self.pf = pf
        x1 = pi[0] + CENTRO[0]
        x2 = pi[1] + CENTRO[1]
        y1 = pf[0] - CENTRO[0]
        y2 = pf[1] - CENTRO[1]
        x = self.pi[1] - self.pi[0]
        y = self.pf[1] - self.pf[0]
        mag = math.sqrt(x*x + y*y) #magnitud
        if x == 0 :
            dire = 0
        else:
            dire = math.tan(y/x) #direccion

    def setInitialPoint(self, pi):
        self.pi = pi

    def setFinalPoint(self, pf):
        self.pf = pf

    def getInitialPoint(self):
        return pi

    def getFinalPoint(self):
        return pf


class L: #linea
    def __init__(self,pi,pf):
        self.pi = pi
        self.pf = pf
        x1 = pi[0] + CENTRO[0]
        x2 = pi[1] + CENTRO[1]
        y1 = pf[0] - CENTRO[0]
        y2 = pf[1] - CENTRO[1]

    def setInitialPoint(self, pi):
        self.pi = pi

    def setFinalPoint(self, pf):
        self.pf = pf

    def getInitialPoint(self):
        return pi

    def getFinalPoint(self):
        return pf

def imprime(o, c, a): #objeto, color, ancho
    pygame.draw.line(pantalla, c, c.getInitialPoint(), c.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def sumaVec(v1, v2) :
    #para mostrar el metodo del paralelogramo
    v1_c = V(v1.getFinalPoint()) #copia del v1
    v2_c = V(v2.getFinalPoint())

    v1_c.setInitialPoint(v2.getFinalPoint()) #empieza donde termina el segundo vector
    v2_c.setInitialPoint(v1.getFinalPoint() + v2.getFinalPoint())

    imprime(v1_c, AZUL, 3)
    imprime(v2_c, AZUL, 3)

    return V(v1.getFinalPoint()) #retorna el vector de la suma

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

pini = [ANCHO,ALTO/2] #ancho, alto
pfin = [0,ALTO/2]

pi = [ANCHO/2, 0]
pf = [ANCHO/2, ALTO]

r1 = L(pini, pfin)
r2 = L(pi, pf)

#pygame.draw.line(pantalla, ROJO, pfin, pini, 3)
#pygame.draw.line(pantalla, AZUL, pi, pf, 3)

#dibujamos el plano cartesiano
imprime(r1, ROJO, 3)
imprime(r2, AZUL, 3)

p1 = [50, 50]
p2 = [-50, -50]

#construimos el vector
v1 = V([0,0], p1)
v2 = V([0,0], p2)

#imprimimos el vector
imprime(v1, VERDE, 3)

#suma de vectores
v3 = sumaVec(v1, v2)

imprime(v3, VERDE, 3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        #else:
            #print event #muestra lo que esta pasando en la pantalla,
                        #como las posiciones donde se ubica el raton
