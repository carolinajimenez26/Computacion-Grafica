#Algoritomos para dibujar pixeles
import pygame
import sys
import copy
import libreria1

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

def DDA(recta):

    m = recta.getPendiente()
    print "m : " , m

    if(recta.getPoints()[0][1] > recta.getPoints()[1][1] or recta.getPoints()[0][0] > recta.getPoints()[1][0]): #Ay > By or Ax > Bx
        [A,B] = libreria1.swap(recta.getPoints()[0],recta.getPoints()[1])
        recta.setPoints(A,B)

    parada = recta.getPoints()[1]
    x_new = recta.getPoints()[0][0]#inicializamos
    y_new = recta.getPoints()[0][1]
    p_new = libreria1.Transform([x_new,y_new])
    libreria1.DrawPixel(p_new,VERDE)

    if(m <= 1):#incrementa en X

        '''if(recta.getPoints()[0][0] > recta.getPoints()[1][0]):
            m *= -1'''

        while(x_new <= parada[0]):
            libreria1.DrawPixel(p_new,VERDE)
            print "plotted : " , libreria1.AntiTransform(p_new)
            x_new += 1
            y_new = y_new + m
            y_plotted = int(round(y_new + m))
            p_new = libreria1.Transform([x_new,y_plotted])

    if(m > 1):#incrementa en Y

        '''if(recta.getPoints()[0][1] > recta.getPoints()[1][1]):
            m *= -1'''

        while(y_new <= parada[1]):
            x_new = x_new + 1 / m
            x_plot = int(round(x_new + float(1 / m)))
            y_new += 1
            print x_new , y_new
            p_new = libreria1.Transform([x_plot,y_new])
            libreria1.DrawPixel(p_new,VERDE)


def Bresenham(recta):

    if(recta.getPoints()[0][0] > recta.getPoints()[1][0]): # Ax > Bx
        print "Ax : " , recta.getPoints()[0][0]
        print "Bx : " , recta.getPoints()[1][0]
        [A,B] = libreria1.swap(recta.getPoints()[0],recta.getPoints()[1])
        print "new A : " , A
        print "new B : " , B
        recta.setPoints(A,B)

    parada = recta.getPoints()[1]
    x_new = recta.getPoints()[0][0]#inicializamos
    y_new = recta.getPoints()[0][1]
    p_new = libreria1.Transform([x_new,y_new])
    libreria1.DrawPixel(p_new,VERDE)

    d_y =  recta.getPoints()[1][1] - recta.getPoints()[0][1] #y2-y1
    d_x =  recta.getPoints()[1][0] - recta.getPoints()[0][0] #x2-x1
    c = 2*d_y + 2*d_x*recta.getb() - d_x

    if(recta.getPendiente() >= 0 and recta.getPendiente() <= 1): #  pendiente tiende a ser horizontal
        while(x_new <= parada[0]): #xk <= xfinal

            pk = 2*d_y*x_new - 2*d_x*y_new + c #criterio de decision

            if(pk > 0) : #d1 > d2
                # hay que pintar (xk+1,yk)
                y_new += 1 #innecesario de poner

            #else : #d1 < d2
                # hay que pintar (xk+1,yk+1)

            x_new += 1
            p_new = libreria1.Transform([x_new,y_new])
            libreria1.DrawPixel(p_new,VERDE)

    if(recta.getPendiente() > 1): #  pendiente tiende a ser mas vertical que horizontal
        #ARREGLAR
        c = 2*d_x + 2*d_y*recta.getb() - d_y

        while(y_new <= parada[1]): #yk <= yfinal

            pk = 2*d_x*x_new - 2*d_y*y_new + c #criterio de decision

            if(pk < 0) :
                # hay que pintar (xk+1,yk+1)
                x_new += 1 #innecesario de poner

            #else :
                # hay que pintar (xk,yk+1)

            y_new += 1
            p_new = libreria1.Transform([x_new,y_new])
            libreria1.DrawPixel(p_new,VERDE)

    if(recta.getPendiente() <= 0): #pendientes negativas
        print "pendiente negativa"
        pass
