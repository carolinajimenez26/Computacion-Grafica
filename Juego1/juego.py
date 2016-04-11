import pygame

#constantes
WIDTH = 640
HIGH = 512

if __name__ == '__main__':
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	reloj = pygame.time.Clock()

	background = pygame.image.load('Background.png').convert()

	pygame.mouse.set_visible(False)#para que no se vea el mouse

	pos = pygame.mouse.get_pos()

	#----------------JUGADOR-------------------------
	ship = pygame.image.load('Player.png').convert_alpha()#lo posiuciona donde esta el mouse
	ship_x = pos[0]
	ship_y = pos[1]
	ship_frame =  ship.get_rect()

	#----------------ENEMIGO-------------------------
	enemy = pygame.image.load('Enemy1.png').convert_alpha()#lo posiuciona donde esta el mouse
	enemy_x = 50
	enemy_y = 50
	enemy_frame =  enemy.get_rect()

	#----------------BALA-------------------------
	bullet = pygame.image.load('mano.png').convert_alpha()
	bullet_x = ship_x
	bullet_y = ship_y
	bullet_frame =  bullet.get_rect()
	bullet_sound = pygame.mixer.Sound('Warble.mp3')

	pygame.display.flip()
	end = False
	disparo = False
	while not end:
		#accion
		pos = pygame.mouse.get_pos()
		ship_x = pos[0]
		ship_y = pos[1]
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				disparo = True;
				bullet_x = ship_x
				bullet_y = ship_y
				bullet_sound.play()
		#reaccion
		if disparo :
			if bullet_y < HIGH :
				bullet_y -=5
			else :
				disparo = False

		SCREEN.blit(background, [0,0])
		SCREEN.blit(ship, [ship_x,ship_y])
		SCREEN.blit(enemy ,[enemy_x,enemy_y])
		SCREEN.blit(bullet ,[bullet_x,bullet_y])
		pygame.display.flip()
		reloj.tick(60)
