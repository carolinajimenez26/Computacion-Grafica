#Algoritmo Bresenham
import pygame
import sys
import copy
import libreria1
import Drawing_pixels_algorithms

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
NEGRO = (0,0,0)


'''Ax = int(input("Ax: "))
Ay = int(input("Ay: "))
Bx = int(input("Bx: "))
By = int(input("By: "))

#m = 0
Ax = 20
Ay = 20
Bx = 100
By = 20

#m < 1
# m = 0.5
Ax = 20
Ay = 30
Bx = 120
By = 80

# m = 0.9
Bx = 20
By = 10
Ax = 120
Ay = 100

# m = 1
Ax = 0
Ay = 0
Bx = 100
By = 100
'''

# m = 2.5
Ax = 20
Ay = 20
Bx = 60
By = 120

#Para que haga el swap
# m = -3.333
Ax = 50
Ay = 20
Bx = 20
By = 120
'''
#m indeterminado (x2-x1)=0
Ax = 20
Ay = 30
Bx = 20
By = 80

#Para que haga el swap
# m = -3.333
Ax = 50
Ay = 20
Bx = 20
By = 120'''

libreria1.makePlane()
libreria1.makeCircle(libreria1.Transform([Ax,Ay]),1,AZUL)
libreria1.makeCircle(libreria1.Transform([Bx,By]),1,AZUL)

recta = libreria1.R([Ax,Ay],[Bx,By])
print "Pendiente: " , recta.getPendiente()

Drawing_pixels_algorithms.Bresenham(recta)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
