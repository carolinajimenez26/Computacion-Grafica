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

            while(times != 0):
                y+= 5
                pto = [x,y]
                pantalla.fill(BLANCO)
                pantalla.blit(obj,pto)
                reloj.tick(60)
                pygame.display.flip()

                if(y >= alto + marco[3]):
                    y = marco[3]*-1
                    times -= 1

        if(case == 1):#izq a derecha
            x = 0
            y = alto/2 - marco[3] / 2
            pto = [x,y]
            pantalla.blit(obj,pto)
            pygame.display.flip()

            while(times != 0):
                x+= 5
                pto = [x,y]
                pantalla.fill(BLANCO)
                pantalla.blit(obj,pto)
                reloj.tick(60)
                pygame.display.flip()

                if(x >= ancho + marco[2]):
                    x = marco[2]*-1
                    times -= 1

        if(case == 2):#derecha a izq
            x = ancho
            y = alto/2 - marco[3] / 2
            pto = [x,y]
            pantalla.blit(obj,pto)
            pygame.display.flip()

            while(times != 0):
                x-= 5
                pto = [x,y]
                pantalla.fill(BLANCO)
                pantalla.blit(obj,pto)
                reloj.tick(60)
                pygame.display.flip()

                if(x <= 0 - marco[2]):
                    x = ancho
                    times -= 1

        if(case == 3):#abajo a a arriba
            x = ancho/2 - marco[2] / 2
            y = alto
            pto = [x,y]
            pantalla.blit(obj,pto)
            pygame.display.flip()

            while(times != 0):
                y-= 5
                pto = [x,y]
                pantalla.fill(BLANCO)
                pantalla.blit(obj,pto)
                reloj.tick(60)
                pygame.display.flip()

                if(y <= 0 - marco[3]):
                    y = alto + marco[3]
                    times -= 1


pantalla = pygame.display.set_mode([ancho,alto])
pantalla.fill(BLANCO)

balon = pygame.image.load('../imagenes/balon.png').convert_alpha()
marco =  balon.get_rect()
print "Ancho:" , marco[2] , "Alto:" , marco[3]

reloj = pygame.time.Clock()

terminar = False

move(balon, 0, 3)

while (not terminar):

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            terminar = True
