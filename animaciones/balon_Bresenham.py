import pygame
import sys
#from ..libreria1 import *
#import imp
#libreria1 = imp.load_source('libreria1.py', 'home/carolinajimenez26/Documentos/U/Sexto semestre/Computacion-Grafica/libreria1.py')
#foo.MyClass()
import libreria1

ancho = 700
alto = 400

BLANCO = (255,255,255)


def Bresenham(recta, obj):

    if(recta.getPoints()[0][0] > recta.getPoints()[1][0]): # Ax > Bx
        [A,B] = libreria1.swap(recta.getPoints()[0],recta.getPoints()[1])
        recta.setPoints(A,B)

    parada = recta.getPoints()[1]
    x_new = recta.getPoints()[0][0]#inicializamos
    y_new = recta.getPoints()[0][1]
    p_new = libreria1.Transform([x_new,y_new])

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
            pantalla.fill(BLANCO)
            pantalla.blit(obj,p_new)
            reloj.tick(60)
            pygame.display.flip()

pantalla = pygame.display.set_mode([ancho,alto])
pantalla.fill(BLANCO)

balon = pygame.image.load('imagenes/balon.png').convert_alpha()
marco =  balon.get_rect()

reloj = pygame.time.Clock()

#m < 1
# m = 0.5
Ax = 20
Ay = 30
Bx = 120
By = 80

recta = libreria1.R([Ax,Ay],[Bx,By])

Bresenham(recta, balon)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
