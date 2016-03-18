
import pygame
import sys
import libreria1

VERDE = (0,255,0)
ANCHO = 700
ALTO = 400

pantalla = pygame.display.set_mode([ANCHO,ALTO])

for i in range(0,100):
    #libreria1.DrawPixel([i,i], VERDE)
    pantalla.set_at([i,i],VERDE)
    libreria1.makeCircle([i,i],1,VERDE)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
