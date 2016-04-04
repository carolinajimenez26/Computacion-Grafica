import pygame
import sys

alto = 500
ancho = 500

BLANCO =(250,250,250)

pantalla = pygame.display.set_mode([ancho,alto])
pantalla.fill(BLANCO)

balon = pygame.image.load('../imagenes/balon.png').convert_alpha()
marco =  balon.get_rect()
print marco, "Ancho:" , marco[2] , "Alto:" , marco[3]

#x = ancho/2 - marco[2] / 2
#y = 0

x = 0
y = alto/2 - marco[3]/2

pto = [x,y]

pantalla.blit(balon,pto)
pygame.display.flip()

reloj = pygame.time.Clock()

pygame.display.flip()

terminar = False

while (not terminar):

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            terminar = True

    #arriba a abajo
    '''y+= 5
    pto = [x,y]
    pantalla.fill(BLANCO)
    pantalla.blit(balon,pto)
    reloj.tick(60)
    pygame.display.flip()

    if(y >= alto + marco[3]):
        y = 0
    '''
    #izq a derecha
    x+= 5
    pto = [x,y]
    pantalla.fill(BLANCO)
    pantalla.blit(balon,pto)
    reloj.tick(60)
    pygame.display.flip()

    if(x >= ancho + marco[2]):
        x = 0
