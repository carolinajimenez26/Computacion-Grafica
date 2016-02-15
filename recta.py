
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


class R:#recta
    def __init__(self,pi,pf): #recibe los puntos como si el centro fuera 0,0
        self.pi = pi
        self.pf = pf

    def setInitialPoint(self, pi): #recibe el punto inicial sin traslacion
        self.pi = pi

    def setFinalPoint(self, pf): #recibe el punto final sin traslacion
        self.pf = pf

    def setInitialPointTranslate(self, pi): #recibe punto inicial trasladado
        self.pi_ = pi

    def setFinalPointTranslate(self, pf):#recibe punto final trasladado
        self.pf_ = pf

    def getInitialPointTranslate(self):#retorna el punto inicial trasladado
        return Transform(self.pi)

    def getFinalPointTranslate(self):#retorna el punto final trasladado
        return Transform(self.pf)

    def getPi(self):#retorna el punto inicial sin traslacion
        return self.pi

    def getPf(self):#retorna el punto final sin traslacion
        return self.pf

    def getPendiente(self): #(y2-y1)/(x2-x1)
        x = (self.pi[1] - self.pi[0])
        if x == 0 :
            return 0
        else :
            return (self.pf[1] - self.pf[0])/x

    def getb(self): # b = y - mx
        return self.pf[0] - self.getPendiente()*self.pi[0]

    def getEcuation(self):
        return "y = " + str(self.getPendiente()) + "x + " + str(self.getb())

    def getY(self,x): #dado x se --- en la ecuacion de la recta y se retorna y
        return self.getPendiente()*x + self.getb()

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

def AntiTransform(x): #transforma un punto del plano cartesiano a la pantalla
    return CENTRO[0] - x

def AntiTransformY(y):
    return CENTRO[1] + y

def imprimeRecta(o, c, a): #objeto, color, ancho
    pygame.draw.line(pantalla, c, [X_MIN,AntiTransformY(o.getY(TransformX(X_MIN)))], [X_MAX,AntiTransformY(o.getY(TransformX(X_MAX)))], a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

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


print "Punto A:"
ax = raw_input("ax: ")
ay = raw_input("ay: ")

print "Punto B:"
bx = raw_input("bx: ")
by = raw_input("by: ")

A = [int(ax), int(ay)]
B = [int(bx), int(by)]

pygame.init()

pantalla = pygame.display.set_mode([ANCHO,ALTO])

pygame.draw.circle(pantalla, ROJO, [TransformX(A),TransformY(B)], 2, 1)

#dibuja el plano cartesiano
makePlane()


recta = R(A,B)
#imprimeRecta(recta, AZUL, 3)

print "Ecuacion de la recta: " , recta.getEcuation()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONUP:
            x,y = event.pos
            print "x: ", x, " y: ", y
