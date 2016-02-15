#punto en x = cos (angulo)
#punto en y = sen (angulo)
import pygame
import sys
import math
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0) #rgb
VERDE = (0,255,0)
AZUL = (0,0,255)

#con sen y cos me saca los puntos pero como si comenzara en 0,0; por lo tanto
#debo trasladarlo al vertice (v.x + cos, v.y + sen)

class A:#Angulo
    def __init__(self,a,v): #angulo y vertice (el vertice lo recibe con coordenadas cartesianas)
        self.a = a
        self.v = v

    def setVertex(self, v): #recibe el vertice sin traslacion
        self.v = v

    def getX(self): #cos(a) + v.x , Sin traslacion al plano normal
        return math.cos(self.a) + self.v[0]

    def getY(self): #sen(a) + v.y , Sin traslacion al plano normal
        return math.sin(self.a) + self.v[1]

    def getAngle(self):
        return self.a

    def getVertex(self):
        return self.v

    def setAngle(self, a):
        self.a = a

    def setRadius(self,r):
        self.r = r

    def getRadius(self):
        return self.v[0] - CENTRO[0]

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
    return x - CENTRO[0]

def AntiTransformY(y):
    return CENTRO[1] + y

def imprime(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def imprimeAngulo(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    v = o.getVertex()
    pygame.draw.line(pantalla, c, [AntiTransformX(v[0]),AntiTransformY(v[1])] , [AntiTransformX(o.getX()), AntiTransformY(o.getY())], a)
    pygame.draw.line(pantalla, c, [AntiTransformX(v[0]),AntiTransformY(v[1])] , [AntiTransformX(o.getX()), AntiTransformY(o.getY() - o.getY())], a)
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

angulo = A(pi/4,[10,10])
makeCircle([TransformX(10),TransformY(10)], 1)
imprimeAngulo(angulo,AZUL,1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
