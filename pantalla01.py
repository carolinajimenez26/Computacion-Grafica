import pygame
import sys
import math

ANCHO = 700
ALTO = 400
CENTRO = ANCHO/2, ALTO/2
ROJO = (255,0,0) #rgb
VERDE = (0,255,0)
AZUL = (0,0,255)

class V:#vector
    def __init__(self,pi,pf):#recibe los puntos como si el centro fuera 0,0
        self.pi = pi
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

class L: #linea
    def __init__(self,pi,pf):
        self.pi = pi
        self.pf = pf
        x1 = pi[0] + CENTRO[0]
        x2 = pi[1] + CENTRO[1]
        y1 = pf[0] - CENTRO[0]
        y2 = pf[1] - CENTRO[1]

def imprime(o, c, a): #objeto, color, ancho
    pygame.draw.line(pantalla, c, [o.x2,o.x1], [o.y2,o.y1], a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def sumaVec(v1, v2) :
    return V(v1.pi[0] + v2.pi[0], v1.pf[0] + v2.pf[0])

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
#v3 = sumaVec(v1, v2)

#imprime(v3, VERDE, 3)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        #else:
            #print event #muestra lo que esta pasando en la pantalla,
                        #como las posiciones donde se ubica el raton
