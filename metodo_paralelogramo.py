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

        #puntos iniciales trasladados
        x1 = CENTRO[0] - pi[0]
        y1 = CENTRO[1] - pi[1]
        self.pi_ = [x1,y1]

        #puntos finales trasladados
        x2 = CENTRO[0] + pf[0]
        y2 = CENTRO[1] - pf[1]
        self.pf_ = [x2,y2]

    def setInitialPoint(self, pi):
        self.pi = pi
        #puntos iniciales trasladados
        x1 = CENTRO[0] - pi[0]
        y1 = CENTRO[1] - pi[1]
        self.pi_ = [x1,y1]

    def setFinalPoint(self, pf):
        self.pf = pf
        #puntos finales trasladados
        x2 = CENTRO[0] + pf[0]
        y2 = CENTRO[1] - pf[1]
        self.pf_ = [x2,y2]

    def setInitialPointTranslate(self, pi):
        self.pi_ = pi

    def setFinalPointTranslate(self, pf):
        self.pf_ = pf

    def getInitialPoint(self):
        return self.pi_

    def getFinalPoint(self):
        return self.pf_

    def getPi(self):
        return self.pi

    def getPf(self):
        return self.pf

class L: #linea
    def __init__(self,pi,pf):
        self.pi = pi
        self.pf = pf
        x1 = CENTRO[0] + pi[0]
        x2 = CENTRO[1] + pi[1]
        y1 = CENTRO[0] - pf[0]
        y2 = CENTRO[1] - pf[1]

    def setInitialPoint(self, pi):
        self.pi = pi

    def setFinalPoint(self, pf):
        self.pf = pf

    def getInitialPoint(self): #retorna el punto inicial trasladado
        return self.pi

    def getFinalPoint(self):
        return self.pf


def imprime(o, c, a): #objeto, color, ancho
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def sumaVec(v1, v2) :
    #Para el vector resultante suma
    p1 = v1.getPf()
    p2 = v2.getPf()
    x = p1[0] + p2[0]
    y = p1[1] + p2[1]

    #Para mostrar el metodo del paralelogramo
    v1_c = V([x,y])
    v2_c = V([x,y])

    v1_c.setInitialPointTranslate(v2.getFinalPoint()) #empieza donde termina el segundo vector
    v2_c.setInitialPointTranslate(v1.getFinalPoint())

    imprime(v1_c, AZUL, 3)
    imprime(v2_c, AZUL, 3)

    return V([x,y]) #retorna el vector de la suma

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

pfin = [ANCHO,ALTO/2] #ancho, alto
pini = [0,ALTO/2]

pi = [ANCHO/2, 0]
pf = [ANCHO/2, ALTO]

r1 = L(pini, pfin)
r2 = L(pi, pf)

#dibujamos el plano cartesiano
imprime(r1, ROJO, 3)
imprime(r2, AZUL, 3)

p1 = [50, 50]
p2 = [30, 70]

#construimos el vector
v1 = V(p1)
v2 = V(p2)

#imprimimos el vector
imprime(v1, VERDE, 3)
imprime(v2, VERDE, 3)

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
