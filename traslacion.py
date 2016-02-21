import pygame
import sys
import math
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

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


def Transform(p): #transforma un punto de la pantalla al plano cartesiano
    return [(CENTRO[0] + p[0]), (CENTRO[1] - p[1])]

def AntiTransform(p): #transforma un punto del plano cartesiano a la pantalla
    return [(CENTRO[0] - p[0]),(CENTRO[1] + p[1])]

def Rote(p,a): #puntos, angulo. Retorna un punto
    return [int(p[0]*math.cos(a) - p[1]*math.sin(a)), int(p[0]*math.sin(a) + p[1]*math.cos(a))]

def imprime(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def imprimeTriangulo(o, c, a): #objeto, color, ancho
    pygame.draw.line(pantalla, c, [TransformX(0),TransformY(0)] , [TransformX(0), TransformY(o.getSide())], a)
    makeCircle([AntiTransformX(0),AntiTransformY(0)], 1) #Dibuja el punto del vertice
    pygame.draw.line(pantalla, c, [TransformX(0),TransformY(0)] , [TransformX(o.getX()), TransformY(o.getY())], a)
    makeCircle([TransformX(o.getX()),TransformY(o.getY())], 1)
    pygame.draw.line(pantalla, c, [TransformX(0),TransformY(o.getSide())] , [TransformX(o.getX()), TransformY(o.getY())], a)

    makeCircle([TransformX(0),TransformY(o.getSide())], 1)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makePlane(): #construye el plano cartesiano
    pfin = [ANCHO,ALTO/2] #ancho, alto
    pini = [0,ALTO/2]

    pi = [ANCHO/2, 0]
    pf = [ANCHO/2, ALTO]

    r1 = L(pini, pfin)
    r2 = L(pi, pf)

    #dibujamos el plano cartesiano
    imprime(r1, ROJO, 1)
    imprime(r2, ROJO, 1)

def makeCircle(p, r):
    pygame.draw.circle(pantalla, VERDE, p, r, 1)
    pygame.display.flip()

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

#dibuja el plano cartesiano
makePlane()

p = [0,40]
pr = Rote(p,pi/2)
makeCircle(Transform(p),1)
makeCircle(Transform(pr),1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
