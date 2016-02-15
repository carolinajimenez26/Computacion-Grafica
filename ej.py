#http://sabia.tic.udc.es/gc/Contenidos%20adicionales/trabajos/ProgramacionVideoJuegos/PyGame/modules/draw/ejemplo.html
import pygame, sys
from pygame.locals import *

#Pinta un cuadrado en la pantalla. En la posicion (30,30)
#Tiene 100 pixeles de lado y el grosor de su linea es 2
def pintarCuadrado():
    pygame.draw.rect(screen, (255,255,255), pygame.Rect((30,30),(100,100)), 2)

#Pinta un poligono de 5 lados en la pantalla. listPuntos es
#la lista de puntos en la que estan definidos los vertices por orden.
#No se indica el parametro width para que la figura este rellena
def pintarPoligono():
    listPuntos = [(200, 30),(250, 80),(225, 130),(175, 130),(150 ,80)]
    pygame.draw.polygon(screen, (255,0,255), listPuntos)

#Pinta un circulo en la pantalla. El centro del circulo sera el
#punto (320, 80). Tendra 50 pixeles de radio y 2 pixeles de borde.
def pintarCirculo():
    pygame.draw.circle(screen, (0,255,255), (320, 80), 50, 2)

#Pinta una elipse en pantalla. La elipse estara inscrita en un rectangulo
#de 100x70 pixeles y comenzara en la posicion (390,45). Tendra 3 pixeles
#de borde
def pintarElipse():
    pygame.draw.ellipse(screen, (255,255,0), pygame.Rect((390,45),(100,70)), 3)

#Pinta un Arco en pantalla de 2.5 radianes. Empieza en el angulo 0 y acaba el 2.5.
#El arco estara inscrito en un rectangulo de 100*100 pixeles y que comienza en la
#posicion (510,30). Tendra 3 pixeles de borde
def pintarArco():
    pygame.draw.arc(screen, (255,0,0), pygame.Rect((510,30),(100,100)), 0, 2.5, 3)

#Pinta una linea en pantalla que va desde la posicion (630,30) hasta la
#posicion (730, 130). Tendra 6 pixeles de anchura
def pintarLinea():
    pygame.draw.line(screen, (0,255,0), (630,30), (730,130), 6)

#Pinta una serie de lineas continuas en pantalla. listPuntos es un array de tuplas
#ordenadas con las posiciones de los vertices. No sera cerrada y tendra un borde de
#1 pixel
def pintarLineas():
    listPuntos = [(750, 60),(770, 30),(750, 100),(740, 40),
                  (800 ,80), (820, 10), (800, 60), (850, 130)]
    pygame.draw.lines(screen, (20,100,150), False, listPuntos,1)

#Pinta una linea en pantalla con anti-aliasing, que va desde la posicion (870,30)
#hasta la posicion (970,130)
def pintarAalinea():
    pygame.draw.aaline(screen, (150,20,50), (870,30), (970, 130), False)

#Pinta una serie de lineas continuas en pantalla con antialiasing.
#listPuntos es un array de tuplas ordenadas con las posiciones de
#los vertices. No sera cerrada.
def pintarAalineas():
    listPuntos = [(990, 60),(1010, 30),(990, 100),(980, 40),(1040 ,80),
                  (1060, 10), (1040, 60), (1090, 130)]
    pygame.draw.aalines(screen, (0,140,100), False, listPuntos, False)


#--------------------------Programa Principal-----------------------------------#

pygame.init()

#Se crea una variable para guardar las dimensiones de la ventana
tam = (1120,160)
#Se crea la ventana con las dimensiones indicadas y se guarda la superficie
#devuelta en la variable screen
screen = pygame.display.set_mode((tam))
#Se le pone un titulo a la ventana
pygame.display.set_caption("Ejemplo modulo Draw")

#Bucle infinito que mantendra los modulos actualizados y la aplicaciones en
#constante ejecucion
while 1:
    #Bucle que comprueba eventos y mira si se ordeno salir del programa
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()

    #Se borra la pantalla pintandola a negro en cada ciclo
    screen.fill((0,0,0))
    #Sobre la pantalla borrada se pintan las figuras
    pintarCuadrado()
    pintarPoligono()
    pintarCirculo()
    pintarArco()
    pintarElipse()
    pintarLinea()
    pintarLineas()
    pintarAalinea()
    pintarAalineas()
    #Se actualiza el contenido de la pantalla
    pygame.display.flip()
