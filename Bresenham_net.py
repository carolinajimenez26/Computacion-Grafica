#http://myslide.es/documents/algoritmo-dda-bresenham-java.html
import pygame
import sys
import copy
import libreria1

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

def Bresenham(x0,y0,x1,y1):

    dx = (x1 - x0)
    dy = (y1 - y0)
    #determinar que punto usar para empezar, cual para terminar
    if (dy < 0) :
        dy = -1*dy
        stepy = -1
    else :
        stepy = 1
    if (dx < 0) :
        dx = -1*dx
        stepx = -1
    else :
        stepx = 1
    x = x0
    y = y0
    p_new = [[x0, y0], [x0, y0]]
    p1 = libreria1.Transform(p_new[0])
    p2 = libreria1.Transform(p_new[1])
    p_new = [p1,p2]
    libreria1.DrawPixel(p1, VERDE)
    libreria1.DrawPixel(p2, VERDE)
    #se cicla hasta llegar al extremo de la linea
    if(dx>dy) :
        p = 2*dy - dx
        incE = 2*dy
        incNE = 2*(dy-dx)
        while (x != x1) :
            x = x + stepx
            if (p < 0) :
                p = p + incE
            else :
                y = y + stepy
                p = p + incNE
            p_new = [x, y]
            p1 = libreria1.Transform(p_new)
            libreria1.DrawPixel(p1, VERDE)

    else :
        p = 2*dx - dy
        incE = 2*dx
        incNE = 2*(dx-dy)
        while (y != y1) :
            y = y + stepy
            if (p < 0) :
                p = p + incE
            else :
                x = x + stepx
                p = p + incNE

            p_new = [x, y]
            p1 = libreria1.Transform(p_new)
            libreria1.DrawPixel(p1, VERDE)


# m = -3.333
Ax = 50
Ay = 20
Bx = 20
By = 120

'''#m < 1
# m = 0.5
Ax = 20
Ay = 30
Bx = 120
By = 80

# m = 1
Ax = 0
Ay = 0
Bx = 100
By = 100

# m = 2.5
Ax = 20
Ay = 20
Bx = 60
By = 120

#m indeterminado (x2-x1)=0
Ax = 20
Ay = 30
Bx = 20
By = 80
'''

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

Bresenham(Ax,Ay,Bx,By)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
