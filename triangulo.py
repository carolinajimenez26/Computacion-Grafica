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


class T:#Triangulo
    def __init__(self,a,l1,l2): #angulo, lados
        self.a = a
        self.l1 = l1
        self.l2 = l2

    def getX(self): #cos(a) + v.x , Sin traslacion al plano normal
        return int(self.getRadius()*math.cos(self.getAngle()))

    def getY(self): #y = rsen(a)
        return int(self.getRadius()*math.sin(self.getAngle()))

    def getAngle(self):
        return self.a
        #return math.arctan(self.getY()/self.getX())

    def setAngle(self, a): #en radianes
        self.a = a

    def setRadius(self,l2):
        self.l2 = l2

    def getRadius(self): #como no nos dan ningun lado fijo, entonces lo fijamos nosotros
        return self.l2

    def getSide(self):
        return self.l1

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


def TransformX(x): #transforma un punto de la pantalla al plano cartesiano
    return CENTRO[0] + x

def TransformY(y):
    return CENTRO[1] - y

def AntiTransformX(x): #transforma un punto del plano cartesiano a la pantalla
    return CENTRO[0] - x

def AntiTransformY(y):
    return CENTRO[1] + y

def imprime(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def imprimeTriangulo(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, [AntiTransformX(0),AntiTransformY(0)] , [AntiTransformX(0), AntiTransformY(o.getSide())], a)
    print "p1:" , [AntiTransformX(0),AntiTransformX(0)]
    makeCircle([AntiTransformX(0),AntiTransformX(0)], 1) #Dibuja el punto del vertice
    pygame.draw.line(pantalla, c, [AntiTransformX(0),AntiTransformY(0)] , [AntiTransformX(o.getX()), AntiTransformY(o.getY())], a)
    makeCircle([AntiTransformX(o.getX()),AntiTransformY(o.getY())], 1)
    pygame.draw.line(pantalla, c, [AntiTransformX(0),AntiTransformY(o.getSide())] , [AntiTransformX(o.getX()), AntiTransformY(o.getY())], a)
    makeCircle([AntiTransformX(0),AntiTransformY(o.getSide())], 1)
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

def makeCircle(p, r): #recibe un punto de la pantalla, no hay que trasladarlo
    pygame.draw.circle(pantalla, VERDE, p, r, 1)
    pygame.display.flip()

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

#dibuja el plano cartesiano
makePlane()

triangulo = T(pi/3,10,20) #angulo, lados
imprimeTriangulo(triangulo,AZUL,1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
