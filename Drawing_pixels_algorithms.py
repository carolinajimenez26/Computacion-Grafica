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

<<<<<<< HEAD
=======

>>>>>>> 6b57d2fcbc81351f2a45fd66956e6d65919096b7
def DDA(recta):
    m = recta.getPendiente()
    parada = recta.getPoints()[1]
    x_new = recta.getPoints()[0][0]#inicializamos
    y_new = recta.getPoints()[0][1]
    print x_new , y_new
    p_new = libreria1.Transform([x_new,y_new])
    libreria1.DrawPixel(p_new,VERDE)
    if(m <= 1):#incrementa en X
        while(x_new <= parada[0]):
            x_new += 1
            y_new = y_new + m
            y_plotted = int(round(y_new + m))
            p_new = libreria1.Transform([x_new,y_plotted])
            libreria1.DrawPixel(p_new,VERDE)
    if(m > 1):#incrementa en Y
        while(y_new <= parada[1]):
            x_new = x_new + 1 / m
            x_plot = int(round(x_new + float(1 / m)))
            y_new += 1
            p_new = libreria1.Transform([x_plot,y_new])
            libreria1.DrawPixel(p_new,VERDE)
