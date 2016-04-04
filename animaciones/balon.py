import pygame
import sys

alto = 500
ancho = 500

BLANCO =(250,250,250)

def move(obj, case, times):

    if(case == 0): #arriba a abajo
        x = ancho/2 - marco[2] / 2
        y = 0
        pto = [x,y]
        pantalla.blit(obj,pto)
        pygame.display.flip()
        print "ciclo : " , times*marco[3]
        for i in range (0,times*marco[3]):
            print "i : " , i
            y+= 5
            pto = [x,y]
            pantalla.fill(BLANCO)
            pantalla.blit(obj,pto)
            reloj.tick(60)
            pygame.display.flip()

            if(y >= alto + marco[3]):
                y = 0

    if(case == 1):#izq a derecha
        x = 0
        y = alto/2 - marco[3] / 2
        pto = [x,y]
        pantalla.blit(obj,pto)
        pygame.display.flip()

        for i in range (0,times):
            x+= 5
            pto = [x,y]
            pantalla.fill(BLANCO)
            pantalla.blit(obj,pto)
            reloj.tick(60)
            pygame.display.flip()

            if(x >= ancho + marco[2]):
                x = 0

    if(case == 2):#derecha a izq
        x = 0
        y = alto/2 - marco[3] / 2
        pto = [x,y]
        pantalla.blit(obj,pto)
        pygame.display.flip()

        for i in range (0,times):
            x+= 5
            pto = [x,y]
            pantalla.fill(BLANCO)
            pantalla.blit(obj,pto)
            reloj.tick(60)
            pygame.display.flip()

            if(x >= ancho + marco[2]):
                x = 0

    if(case == 3):#abajo a a arriba
        x = 0
        y = alto/2 - marco[3] / 2
        pto = [x,y]
        pantalla.blit(obj,pto)
        pygame.display.flip()

        for i in range (0,times):
            x+= 5
            pto = [x,y]
            pantalla.fill(BLANCO)
            pantalla.blit(balon,pto)
            reloj.tick(60)
            pygame.display.flip()

            if(x >= ancho + marco[2]):
                x = 0


pantalla = pygame.display.set_mode([ancho,alto])
pantalla.fill(BLANCO)

balon = pygame.image.load('../imagenes/balon.png').convert_alpha()
marco =  balon.get_rect()
print "Ancho:" , marco[2] , "Alto:" , marco[3]

reloj = pygame.time.Clock()

terminar = False

while (not terminar):

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            terminar = True
        else :
            move(balon, 1, 10)
