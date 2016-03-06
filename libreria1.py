#libreria primer parcial Computacion Grafica
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
BLANCO = (255,255,255)

class V:#vector
    def __init__(self,pi,pf):#pi = x1,y1, pf = x2,y2
        self.pf = pf
        self.pi = pi
        self.m = self.getMagnitud(pi,pf)

    def getPoints(self): #[(x1,y1),(x2,y2)]
        return [self.pi,self.pf]

    def getMagnitud(self):
        return self.m

    def setPoints(self, pi, pf):
        self.pi = pi
        self.pf = pf

    def getMagnitud(self, pi, pf):#sqrt((x2-x1)**2+(y2-y1)**2)
        return math.sqrt((pf[0]-pi[0])**2+(pf[1]-pi[1])**2)

    def setMagnitud(self, m):
        self.m = m

    def Draw(self):#dibuja el vector
        p = self.getPoints()
        makeLine(BLANCO, 1, p[0], p[1])

class A:#Angulo
    def __init__(self,a,v): #angulo y vertice (el vertice lo recibe con coordenadas cartesianas)
        self.a = a
        self.v = v
        self.r = 100 #inicialmente

    def getPoints(self):# x = rcos (theta), y = rsin(theta)
        return [int(self.getRadius()*math.cos(self.getAngle())), int(self.getRadius()*math.sin(self.a))]

    def getAngle(self):
        return self.a

    def setAngle(self, a):
        self.a = a

    def getVertex(self):
        return self.v

    def setVertex(self, v): #recibe el vertice sin traslacion
        self.v = v

    def setRadius(self,r):
        self.r = r

    def getRadius(self): #como no nos dan ningun lado fijo, entonces lo fijamos nosotros
        return self.r

def DrawPolygon(points):#cantidad de puntos en la figura
    for i in range(1,points + 1):
        makeCircle(Transform(Polares(100,(2*pi/points)*i)),2)
        p1 = Polares(100,(2*pi/points)*i)
        p2 = Polares(100,(2*pi/points)*(i+1))
        makeLine(AZUL, 1, p1, p2)

def makeLine(c, a, p1, p2): #color, ancho, puntos
    pygame.draw.line(pantalla, c, Transform(p1), Transform(p2), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makePlane(): #construye el plano cartesiano
    pygame.draw.line(pantalla, ROJO, [0,ALTO/2], [ANCHO,ALTO/2], 2)
    pygame.draw.line(pantalla, ROJO, [ANCHO/2,0], [ANCHO/2,ALTO], 2)
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

def translateToCenter(p, pivote): #se translada al centro
    return [p[0]-pivote[0],p[1]-pivote[1]]

def translateToPoint(p, pivote):#se translada a un punto
    return [p[0]+pivote[0],p[1]+pivote[1]]

#escalar un punto
def scale(point, scale):
	nx = point[0]*scale
	ny = point[1]*scale
	return (nx,ny)

pygame.init()
pantalla = pygame.display.set_mode([ANCHO,ALTO])

#dibuja el plano cartesiano
makePlane()

v = V([50,50],[100,100])
v.Draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
