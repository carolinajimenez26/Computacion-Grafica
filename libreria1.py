#libreria primer parcial Computacion Grafica
import pygame
import sys
import math
import copy
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)

pantalla = pygame.display.set_mode([ANCHO,ALTO])

class R:#recta
    def __init__(self,pi,pf): #recibe los puntos
        self.pi = pi # [x1,y1]
        self.pf = pf # [x2,y2]

    def getPendiente(self): # m = (y2-y1)/(x2-x1)
        x = float(self.pf[0])-float(self.pi[0])
        if(x != 0):
            y = float(self.pf[1])-float(self.pi[1])
            return float(y/x)
        else :
            print "Pendiente indefinida"
            return float('Inf') #tiende a infinito, no es infinito

    def setPoints(self,pi,pf):
        self.pi = pi
        self.pf = pf

    def getPoints(self):
        return [self.pi, self.pf] #[[x1,y1],[x2,y2]]

    def getb(self): # b = y - mx
        return self.pi[1] - self.getPendiente()*self.pi[0]

    def getEcuation(self): # y = mx + b
        return "y = " + str(self.getPendiente()) + "x + " + str(self.getb())

class V:#vector
    def __init__(self,pi,pf):#pi = x1,y1, pf = x2,y2
        self.pf = pf
        self.pi = pi
        #self.m = self.getMagnitud(pi,pf)

    def getPoints(self): #[(x1,y1),(x2,y2)]
        return [self.pi,self.pf]

    def setPoints(self, pi, pf):
        self.pi = pi
        self.pf = pf

    def getMagnitud(self):#sqrt((x2-x1)**2+(y2-y1)**2)
        return math.sqrt((self.pf[0]-self.pi[0])**2+(self.pf[1]-self.pi[1])**2)

    def setMagnitud(self, m):
        self.m = m

    def Draw(self, color):#dibuja el vector
        p = self.getPoints()
        makeLine(color, 1, p[0], p[1])

    def scale(self, s):#se escala el vector
        p = self.getPoints()
        self.setPoints(scale(p[0],s),scale(p[1],s))

    def moveTo(self,pivote):
        p = self.getPoints()
        self.setPoints(moveToPoint(p[0],pivote),moveToPoint(p[1],pivote))

    def returnTo(self,pivote):
        p = self.getPoints()
        self.setPoints(moveToCenter(p[0],pivote),moveToCenter(p[1],pivote))

    def Rote(self, angle): #rota los puntos del vector
        p = self.getPoints() #[pi,pf] = [(x1,y1),(x2,y2)]
        self.setPoints(Rote(p[0],angle),Rote(p[1],angle))

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

    def Draw(self, color):
        p = self.getPoints()
        makeLine(color, 1, p[0], p[1])
        makeLine(color, 1, p[0], p[2])
        makeLine(color, 1, p[1], p[2])

class A:#Angulo
    def __init__(self,a,v): #angulo y vertice (el vertice lo recibe con coordenadas cartesianas)
        self.a = a
        self.v = v
        self.r = 100 #inicialmente

    def getPoints(self):# x = rcos (theta), y = rsin(theta)
        #p1 = [int(self.getRadius()*math.cos(self.getAngle())), int(self.getRadius()*math.sin(self.a))]
        p2 = [self.getVertex()[0] + self.getRadius(), self.getVertex()[1]]
        p1 = Rote(p2,self.getAngle())
        return [p1,p2]

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

    def Draw(self, color):
        p = self.getPoints() #[(x1,y1),(x2,y2)]
        makeLine(color, 1, self.getVertex(), p[0])
        makeLine(color, 1, self.getVertex(), p[1])

def oppositeVector(v):#el opuesto de un vector
    p = v.getPoints()[1] #si esta en el origen no nos interesa el pi
    v.setPoints(v.getPoints()[0],[p[0]*-1,p[1]*-1])
    return v

def VectorAdd(v1,v2):#Suma de vectores (Deben tener vertice en el centro)
    pv1 = v1.getPoints()[1] #Nos interesa solo el punto final. [(v1_x,v1_y)]
    pv2 = v2.getPoints()[1] #[(v2_x,v2_y)]
    p = [(pv1[0]+pv2[0]),(pv1[1]+pv2[1])] #[(v1_x+v2_x2),(v1_y1+v2_y2)]
    v = V(v1.getPoints()[0],p)
    #v.Draw(BLANCO)
    #parallelogramMethod(v1,v2,v) #para que lo muestre graficamente
    return v

def VectorSub(v1,v2):#Suma de vectores (Deben tener vertice en el centro)
    #v1 + (-v2)
    v2_copy = copy.deepcopy(v2)
    return oppositeVector(v2_copy)

def parallelogramMethod(v1,v2,v):#crea los otros vectores que son el resultado de la suma de v1 y v2
    pv1 = v1.getPoints() #[(x1,y1),(x2,y2)]
    pv2 = v2.getPoints()
    pv = v.getPoints()
    v1_ = V(pv1[1],pv[1]) #inicia donde termina v1 y termina donde termina v
    #v1_.Draw(AZUL)
    v2_ = V(pv2[1],pv[1])
    #v2_.Draw(AZUL)
    return [v1_,v2_]

def DrawPolygon(points):#cantidad de puntos en la figura
    for i in range(1,points + 1):
        makeCircle(Transform(Polar(100,(2*pi/points)*i)),2)
        p1 = Polar(100,(2*pi/points)*i)
        p2 = Polar(100,(2*pi/points)*(i+1))
        makeLine(AZUL, 1, p1, p2)

def makeLine(c, a, p1, p2): #color, ancho, puntos
    pygame.draw.line(pantalla, c, Transform(p1), Transform(p2), a)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makePlane(): #construye el plano cartesiano
    pygame.draw.line(pantalla, ROJO, [0,ALTO/2], [ANCHO,ALTO/2], 2)
    pygame.draw.line(pantalla, ROJO, [ANCHO/2,0], [ANCHO/2,ALTO], 2)
    pygame.display.flip() #actualizar la pantalla, funcion de refresco

def makeCircle(p, r, color): #recibe un punto de la pantalla, no hay que trasladarlo
    pygame.draw.circle(pantalla, color, p, r, 1)
    pygame.display.flip()

def Transform(p): #transforma un punto de la pantalla al plano cartesiano
    return [(CENTRO[0] + p[0]), (CENTRO[1] - p[1])]

def AntiTransform(p): #transforma un punto del plano cartesiano a la pantalla
    return [p[0] - CENTRO[0], CENTRO[1] - p[1]]

def Rote(p,a): #puntos, angulo. Retorna un punto
    return [float(p[0]*math.cos(a) - p[1]*math.sin(a)), float(p[0]*math.sin(a) + p[1]*math.cos(a))]

def moveToCenter(p, pivote): #se translada al centro
    return [ int(p[0] - pivote[0]), int(p[1] - pivote[1]) ]

def moveToPoint(p, pivote):#se translada a un punto
    return [ int(p[0] + pivote[0]), int(p[1] +  pivote[1]) ]

#escalar un punto
def scale(point, scale):
	nx = point[0]*scale
	ny = point[1]*scale
	return [nx,ny]

def Polar(r, a):#radio y angulo. x = rcos(theta), y = rsin(theta)
    return [int(r*math.cos(a)), int(r*math.sin(a))]

def RadToDeg(r):#radianes a grados
    return r*(180/pi)

def DegToRad(d):#grados a radianes
    return d*(pi/180)

def DrawPixel(p,color):
    pantalla.set_at(p,color)
    pygame.display.flip()

def swap(p1,p2):#intercambia dos puntos
    tmp = p1
    p1 = p2
    p2 = tmp
    return [p1,p2]
