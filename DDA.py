#Algoritmo DDA
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

def DDA_X(recta, case):
    print "DDA_X"
    print "A1: " ,  recta.getPoints()[0]
    print "B1: " ,  recta.getPoints()[1]
    # case 0 : Xk+1 = Xk + 1/m
    # case 1 : Xk+1 = Xk + 1/(-m)
    print "CASO:" , case
    if(case == 1):#ya no vamos de A hacia B, si no al contrario
        [A,B] = swap(recta.getPoints()[0],recta.getPoints()[1])
        recta.setPoints(A,B)
    parada = recta.getPoints()[1]
    print "punto de llegada: " , parada
    while(True):
        pivote = recta.getPoints()[0] # recta.[x1,y1]
        print "pivote: " , pivote
        #libreria1.DrawPixel(pivote, AZUL)
        libreria1.makeCircle(libreria1.Transform(pivote),1,VERDE)
        new_x = int(round( pivote[0] + (1/recta.getPendiente()) ))
        new_y = int(round(recta.getPendiente()*new_x + recta.getb()))
        new_point = [new_x,new_y]
        print "New point: " , new_point
        libreria1.makeCircle(libreria1.Transform(new_point),1,VERDE)
        #ibreria1.DrawPixel(new_point, AZUL)
        print "new_x: " , new_x
        print "parada[0]: " , parada[0]
        if(new_x >= parada[0]): #Xk+1 >= Xk
            return #parada
        print "parada: " , parada
        print "new_y: " , new_y
        recta.setPoints([new_x,new_y],recta.getPoints()[1]) #actualiza

def DDA_Y(recta, case):
    print "DDA_Y"
    print "A1: " ,  recta.getPoints()[0]
    print "B1: " ,  recta.getPoints()[1]
    # case 0 : # Yk+1 = Yk + m
    # case 1 : # Yk+1 = Yk - m
    print "CASO:" , case
    i = 0
    if(case == 0):#ya no vamos de A hacia B, si no al contrario
        #print "A: " , recta.getPoints()[0] , "B: " , recta.getPoints()[1]
        [A,B] = swap(recta.getPoints()[0],recta.getPoints()[1])
        recta.setPoints(A,B)
        print "A: " , A , "B: " , B
    parada = recta.getPoints()[1]
    print "punto de llegada: " , parada
    while(True):
        pivote = recta.getPoints()[0] # recta.[x1,y1]
        #libreria1.DrawPixel(pivote, AZUL) #NO QUIERE SERVIR
        libreria1.makeCircle(libreria1.Transform(pivote),1,VERDE)
        print "pivote: " , pivote
        new_y = int(round(pivote[1] + recta.getPendiente()))
        new_x = int(round(( int(new_y) - recta.getb() ) / recta.getPendiente()))
        new_point = [new_x,new_y]
        #libreria1.DrawPixel(new_point, AZUL)
        print "New point: " , new_point
        libreria1.makeCircle(libreria1.Transform(new_point),1,VERDE)
        if(new_y <= parada[1] ):#or i == 10): #Yk+1 <= Yk
            return #parada
        print "parada: " , parada
        print "new_y: " , new_y
        recta.setPoints([new_x,new_y],recta.getPoints()[1]) #recta = new_rect
        i+=1


'''Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))'''
'''Ax = 20
Ay = 20
Bx = 60
By = 120'''

#Funcionando:
'''Ax = 20
Ay = 120
Bx = 50
By = 20

Bx = 20
By = 120
Ax = 50
Ay = 20'''

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

recta = R([Ax,Ay],[Bx,By])
print "Pendiente: " , recta.getPendiente()
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
