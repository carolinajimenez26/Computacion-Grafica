import pygame
import sys
import copy
import libreria1

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

def BresenhamCircle(xc,yc,r):#xcentro, ycentro, radio
    x = 0
    y = r
    p = 1 - r
    p_new = [[xc,yc],[x,y]]
    libreria1.DrawPixel(libreria1.Transform(p_new[0]), VERDE)
    libreria1.DrawPixel(libreria1.Transform(p_new[1]), VERDE)
    #se cicla hasta trazar todo un octante
    while (x < y) :
        x = x + 1
        if (p < 0) :
            p = p + 2*x + 1
        else :
            y = y - 1
            p = p + 2*(x - y) + 1

        libreria1.DrawPixel(libreria1.Transform([x,y]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-x,y]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([x,-y]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-x,-y]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([y,x]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-y,x]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([y,-x]), VERDE)
        libreria1.DrawPixel(libreria1.Transform([-y,-x]), VERDE)


libreria1.makePlane()

BresenhamCircle(0,0,100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
