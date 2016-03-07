#rectas y curvass
import libreria1
import pygame
import sys
import copy
import math
pi = 3.1415

ANCHO = 700
ALTO = 400
CENTRO = [ANCHO/2, ALTO/2]
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)

libreria1.makePlane()

'''
#funcion y = x**2 + 2
for i in range (-20,20):
    y1 = i**2 + 2
    y2 = (i+1)**2 + 2
    p1 = [i,y1]
    p2 = [(i+1),y2]
    libreria1.makeCircle(libreria1.Transform([i,y1]),1) #dibuja el punto
    libreria1.makeLine(VERDE, 1, p1, p2)

#Cardioide: r = a(1+cos(t))
# x = r cos (theta)
# y = r sen (theta)
a = 50
for t in range (0,360):
    #pasarlos a radianes
    r = a * (1 - math.cos(libreria1.DegToRad(t)))
    #pasarlos a cartesianas
    x = r*math.cos(libreria1.DegToRad(t))
    y = r*math.sin(libreria1.DegToRad(t))
    libreria1.makeCircle(libreria1.Transform([int(x),int(y)]),1)
'''

reloj = pygame.time.Clock()
r = 50
libreria1.makeCircle(libreria1.Transform([0,0]),r,ROJO) #dibuja el circulo fijo
for t in range (0,360):
    x = r*math.cos(libreria1.DegToRad(t))
    y = r*math.sin(libreria1.DegToRad(t))
    reloj.tick(150)
    libreria1.makeCircle(libreria1.Transform([int(x),int(y)]),2*r, VERDE)
    reloj.tick(150)
    libreria1.makeCircle(libreria1.Transform([int(x),int(y)]),1,BLANCO)
    reloj.tick(150)
    libreria1.makeCircle(libreria1.Transform([int(x),int(y)]),2*r,NEGRO)
    x2 = 3*r*math.cos(libreria1.DegToRad(t))
    y2 = 3*r*math.sin(libreria1.DegToRad(t))
    libreria1.makeCircle(libreria1.Transform([int(x2)+1,int(y2)]),1,ROJO)


'''centro_circulo = [100,0]
puntos = []
for i in range(0,2*pi):#generamos todos los puntos de un circulo y lo guardamos
    puntos = '''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
