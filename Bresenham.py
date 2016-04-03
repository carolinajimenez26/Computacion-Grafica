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


def Bresenham(recta):

    if(recta.getPoints()[0][0] > recta.getPoints()[1][0]): # Ax > Bx
        [A,B] = libreria1.swap(recta.getPoints()[0],recta.getPoints()[1])
        recta.setPoints(A,B)

    parada = recta.getPoints()[1]
    x_new = recta.getPoints()[0][0]#inicializamos
    y_new = recta.getPoints()[0][1]
    p_new = libreria1.Transform([x_new,y_new])
    libreria1.DrawPixel(p_new,VERDE)

    d_y =  recta.getPoints()[1][1] - recta.getPoints()[0][1] #y2-y1
    d_x =  recta.getPoints()[1][0] - recta.getPoints()[0][0] #x2-x1
    c = 2*d_y + 2*d_x*recta.getb() - d_x

    if(m > 0 and m < 1): # 0 < m < 1

        while(x_new <= parada[0]): #xk <= xfinal

            pk = 2*dy*x_new - 2*d_x*y_new + c #criterio de decision

            if(pk < 0) : #d1 < d2
                # hay que pintar (xk+1,yk)
                y_new += 0 #innecesario de poner

            else : #d1 > d2
                # hay que pintar (xk+1,yk+1)
                y_new += 1

            x_new += 1
            p_new = libreria1.Transform([x_new,y_new])
            libreria1.DrawPixel(p_new,VERDE)


'''Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))'''

Ax = 20
Ay = 20
Bx = 60
By = 120

'''
#m < 1
Ax = 20
Ay = 30
Bx = 120
By = 80

#m > 1
Ax = 10
Ay = 20
Bx = 80
By = 120

#m indeterminado (x2-x1)=0
Ax = 20
Ay = 30
Bx = 20
By = 80

#cPara que haga el swap
Ax = 50
Ay = 20
Bx = 20
By = 120'''

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

recta = libreria1.R([Ax,Ay],[Bx,By])
print "Pendiente: " , recta.getPendiente()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
