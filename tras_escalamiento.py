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
    def __init__(self,p1,p2,p3): #puntos
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def getPoints(self):#recibe los tres puntos que construye el triangulo
        return [self.p1,self.p2,self.p3]

    def setPoints(self,p):#recibe lista de puntos [(x1,y1),(x2,y2),(x3,y3)]
        self.p1 = p[0]
        self.p2 = p[1]
        self.p3 = p[2]

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

def imprime(o, c, a): #objeto, color, ancho (esta funcion es para el plano cartesiano)
    pygame.draw.line(pantalla, c, o.getInitialPoint(), o.getFinalPoint(), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makeCircle(p, r): #recibe un punto de la pantalla, no hay que trasladarlo
    pygame.draw.circle(pantalla, VERDE, p, r, 1)
    pygame.display.flip()

def Transform(p): #transforma un punto de la pantalla al plano cartesiano
    return [(CENTRO[0] + p[0]), (CENTRO[1] - p[1])]

def AntiTransform(p): #transforma un punto del plano cartesiano a la pantalla
    return [(CENTRO[0] - p[0]),(CENTRO[1] + p[1])]

def Rote(p,a): #puntos, angulo. Retorna un punto
    return [int(p[0]*math.cos(a) - p[1]*math.sin(a)), int(p[0]*math.sin(a) + p[1]*math.cos(a))]

def imprimeTriangulo(o, c, a): #objeto, color, ancho
    p = o.getPoints()
    makeCircle(Transform(p[0]), 1)
    makeCircle(Transform(p[1]), 1)
    makeCircle(Transform(p[2]), 1)
    pygame.draw.line(pantalla, c, Transform(p[0]), Transform(p[1]), a)
    pygame.draw.line(pantalla, c, Transform(p[0]), Transform(p[2]), a)
    pygame.draw.line(pantalla, c, Transform(p[2]), Transform(p[1]), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def Mult(point, escalar):
    return [point[0]*escalar, point[1]*escalar]

def Escalamiento(p,s):#puntos y el escalar
    return [Mult(p[0],s),Mult(p[1],s),Mult(p[2],s)]

def Rest(p1,p2):
    return [p1[0]-p2[0],p1[1]-p2[1]]

def Translacion(p1,p2,p3):# puntos a transladar
    return [Rest(p1,p2),Rest(p2,p2),Rest(p3,p2)]

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

#dibuja el plano cartesiano
makePlane()

p1 = [12,20]
p2 = [0,30]
p3 = [30,30]

triangulo = T(p1,p2,p3)
imprimeTriangulo(triangulo,VERDE,1)

puntos_trasladados = Translacion(p1,p2,p3)
triangulo_trasladado = T(puntos_trasladados[0],puntos_trasladados[1],puntos_trasladados[2])
imprimeTriangulo(triangulo_trasladado,ROJO,1)


puntos = Escalamiento([[0,0],[0,30],[30,30]],5)
triangulo_escalado = T(puntos[0],puntos[1], puntos[2])
imprimeTriangulo(triangulo_escalado,AZUL,1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
