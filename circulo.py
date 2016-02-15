import pygame
import sys
import math

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0) #rgb
VERDE = (0,255,0)
AZUL = (0,0,255)
X_MIN = ANCHO/2 - ANCHO
X_MAX = ANCHO/2 + ANCHO

class L: #linea(para el plano cartesiano)
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

def imprime(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makePlane(): #construye el plano cartesiano
    pfin = [ANCHO,ALTO/2] #ancho, alto
    pini = [0,ALTO/2]

    pi = [ANCHO/2, 0]
    pf = [ANCHO/2, ALTO]

    r1 = L(pini, pfin)
    r2 = L(pi, pf)

    #dibujamos el plano cartesiano
    imprime(r1, ROJO, 3)
    imprime(r2, ROJO, 3)


def makeCircle(p, r): #recibe un punto de la pantalla, no hay que trasladarlo
    pygame.draw.circle(pantalla, VERDE, p, r, 2)
    pygame.display.flip()

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

#dibuja el plano cartesiano
makePlane()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            r = int(input("radio: "))
            makeCircle([x,y], r)
