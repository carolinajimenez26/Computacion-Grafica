import pygame
import sys
import math

#constantes
ANCHO = 700
ALTO = 400

#colores
ROJO = (255,0,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)
VERDE = (0,255,0)

#pantalla
pygame.init()
pantalla = pygame.display.set_mode([ANCHO,ALTO])

#centro
centro=[ANCHO/2,ALTO/2]

#plano cartesiano
pygame.draw.line(pantalla, ROJO, [0,ALTO/2], [ANCHO,ALTO/2], 2)
pygame.draw.line(pantalla, ROJO, [ANCHO/2,0], [ANCHO/2,ALTO], 2)

#transformacion
def transformada(punto):
	nx = centro[0]+punto[0]
	ny = centro[1]-punto[1]
	return (nx,ny)

#tranformada lista de puntos
def translista(lista):
	aux = []
	for obj in lista:
		aux.append(transformada(obj))
	return aux

#matriz escalamineto
def escalamiento(punto, escalar):
	nx = punto[0]*escalar
	ny = punto[1]*escalar
	return (nx,ny)

#escalar lista puntos
def esclstpuntos(lst, escalar):
	aux = []
	for punto in lst:
		aux.append(escalamiento(punto, escalar))
	return aux

#triangulo
vertices = [[25,0],[40,0],[0,40]]
pygame.draw.polygon(pantalla, VERDE, translista(vertices), 2)
pygame.draw.polygon(pantalla, AZUL, translista(esclstpuntos(vertices, 0.5)), 2)

#####################
pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit(0)
