#Algoritmo Bresenham
import pygame
import sys
import copy
import libreria1


ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

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
            return

    def setPoints(self,pi,pf):
        self.pi = pi
        self.pf = pf

    def getPoints(self):
        return [self.pi, self.pf] #[[x1,y1],[x2,y2]]

    def getb(self): # b = y - mx
        return self.pi[1] - self.getPendiente()*self.pi[0]

    def getEcuation(self): # y = mx + b
        return "y = " + str(self.getPendiente()) + "x + " + str(self.getb())


def swap(p1,p2):#intercambia dos puntos
    tmp = p1
    p1 = p2
    p2 = tmp
    return [p1,p2]

def Bresenham(recta):
    pass

'''Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))'''

Ax = 20
Ay = 20
Bx = 60
By = 120

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

recta = R([Ax,Ay],[Bx,By])
print "Pendiente: " , recta.getPendiente()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
