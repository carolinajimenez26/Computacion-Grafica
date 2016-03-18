#Algoritmo DDA
import pygame
import sys
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
        x = self.pf[0]-self.pi[0]
        if(x != 0):
            return float((self.pf[1]-self.pi[1])/x)
        else :
            print "Pendiente indefinida"
            return

    def setPoints(self,pi,pf):
        self.pi = pi
        self.pf = pf

    def getPoints(self):
        return [self.pi, self.pf] #[[x1,y1],[x2,y2]]

    def getb(self): # b = y - mx
        self.pi[1] - self.getPendiente()*self.pi[0]

    def getEcuation(self): # y = mx + b
        return "y = " + str(self.getPendiente()) + "x + " + str(self.getb())

def swap(p1,p2):#intercambia dos puntos
    tmp = p1
    p1 = p2
    p2 = tmp
    return [p1,p2]

def DDA_X(recta, case):
    # case 0 : Xk+1 = Xk + 1/m
    # case 1 : Xk+1 = Xk + 1/(-m)
    if(case == 1):#ya no vamos de A hacia B, si no al contrario
        [A,B] = swap(recta.getPoints()[0],recta.getPoints()[1])
    while(True):
        pivote = recta.getPoints()[0] # recta.[x1,y1]
        libreria1.DrawPixel(pivote, AZUL)
        new_x = round( pivote[0] + (1/recta.getPendiente()) )
        new_y = round(recta.getPendiente()*new_x + recta.getb())
        new_point = [new_x,new_y]
        new_rect = R(pivote,new_point) #recta que se genera
        libreria1.DrawPixel(new_point, AZUL)
        if(new_x >= pivote[0]): #Xk+1 >= Xk
            return #parada
        pivote = new_rect #actualiza

def DDA_Y(recta, case):
    # case 0 : # Yk+1 = Yk + m
    # case 1 : # Yk+1 = Yk - m
    if(case == 1):#ya no vamos de A hacia B, si no al contrario
        [A,B] = swap(recta.getPoints()[0],recta.getPoints()[1])
    while(True):
        pivote = recta.getPoints()[0] # recta.[x1,y1]
        libreria1.DrawPixel(pivote, AZUL)
        new_y = round(pivote[1] + recta.getPendiente())
        new_x = round(( new_y - recta.getb() ) / recta.getPendiente())
        new_point = [new_x,new_y]
        new_rect = R(pivote,new_point) #recta que se genera
        libreria1.DrawPixel(new_point, AZUL)
        if(new_y <= pivote[1]): #Yk+1 <= Yk
            return #parada
        pivote = new_rect #actualiza


Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))

libreria1.makePlane()

recta = R([Ax,Ay],[Bx,By])

if(recta.getPendiente() <= 1): # m <= 1
    if(Ay > By):
        DDA_Y(recta,1) # Yk+1 = Yk - m
    else:
        DDA_Y(recta,0) # Yk+1 = Yk + m

else: # m > 1
    if(Ax < Bx):
        DDA_X(recta, 0) # Xk+1 = Xk + 1/m
    else:
        DDA_X(recta,1) # Xk+1 = Xk + 1/(-m)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
