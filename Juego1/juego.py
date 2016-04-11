import pygame

#constantes
WIDTH = 640
HIGH = 512

if __name__ == '__main__':
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])

	background = pygame.image.load('Background.png').convert()
	SCREEN.blit(background, [0,0]) #posiciona la imagen desde ese punto

	pygame.mouse.set_visible(False)#para que no se vea el mouse

	pos = pygame.mouse.get_pos()
	xship = pos[0]
	yship = pos[1]
	ship = pygame.image.load('Enemy1.png').convert_alpha()#lo posiuciona donde esta el mouse
	SCREEN.blit(ship, [xship,yship])#pone la imagen en la pantalla

	pygame.display.flip()
	end = False

	while not end:
		pos = pygame.mouse.get_pos()
		xship = pos[0]
		yship = pos[1]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True

		SCREEN.blit(background, [0,0])#hay que poner siempre el background
		SCREEN.blit(ship, [xship,yship])#se mueve a medida que se mueva el mouse
		pygame.display.flip()
