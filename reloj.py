import pygame
import sys

reloj = pygame.time.Clock()
con = 0
veces = 0
seguir = True
while seguir:
    con+=1
    reloj.tick(10)
    if con%10 == 0:
        print "Hola"
        veces+=1
    if veces == 5:
        seguir = False
