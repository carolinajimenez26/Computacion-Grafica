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
            print "plotted : " , p_new
            libreria1.DrawPixel(p_new,VERDE)
    if(m > 1):#incrementa en Y
        while(y_new <= parada[1]):
            x_new = x_new + 1 / m
            x_plot = int(round(x_new + float(1 / m)))
            y_new += 1
            print x_new , y_new
            p_new = libreria1.Transform([x_plot,y_new])
            libreria1.DrawPixel(p_new,VERDE)



Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))

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
By = 80'''

recta = libreria1.R([Ax,Ay],[Bx,By])
print "Pendiente: " , recta.getPendiente()

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

DDA(recta)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
