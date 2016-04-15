import pygame
import random

WIDTH = 640
HIGH = 512

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
	def __init__(self, img, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.pos = pos
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def getRect(self):
		return self.rect

	def getPos(self):
		return [self.x,self.y]

	def setPos(self,pos):
		self.x = pos[0]
		self.y = pos[1]
		self.rect.x = pos[0]
		self.rect.y = pos[1]

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
	def __init__(self, img, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.pos = pos
		self.rect.x = pos[0]
		self.rect.y = pos[1]
		self.x = pos[0]
		self.y = pos[1]
		self.vidas = 5

	def getRect(self):
		return self.rect

	def getPos(self):
		return [self.x,self.y]

	def setPos(self,pos):
		self.x = pos[0]
		self.y = pos[1]
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def getVidas(self):
		return vidas

	def setVidas(self,vidas):
		self.vidas = vidas


class Bullet(pygame.sprite.Sprite): #Hereda de la clase sprite
	def __init__(self, img, pos): #img para cargar, y su padre(de donde debe salir la bala)
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img).convert_alpha()
		self.rect = self.image.get_rect()
		self.pos = pos
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def getRect(self):
		return self.rect

	def getPos(self):
		return [self.x,self.y]

	def setPos(self,pos):
		self.x = pos[0]
		self.y = pos[1]
		self.rect.x = pos[0]
		self.rect.y = pos[1]

	def update(self):
		self.rect.y -= 5 #dispara hacia arriba

if __name__ == '__main__':
	pygame.init()
	SCREEN = pygame.display.set_mode([WIDTH,HIGH])
	reloj = pygame.time.Clock()

	background = pygame.image.load('Background.png').convert()

	pygame.mouse.set_visible(False)#para que no se vea el mouse

	pos = pygame.mouse.get_pos()#recibe donde esta ubicado el mouse
	ls_all = pygame.sprite.Group()
	ls_impactos = pygame.sprite.Group()
	#----------------JUGADOR-------------------------
	ship = Player('Player.png',pos)
	ls_all.add(ship)

	#----------------ENEMIGOS-------------------------
	ls_enemies = pygame.sprite.Group()
	for i in range(0,5):
		enemy = Enemy('Enemy1.png',[0,0])
		ls_enemies.add(enemy)
		ls_all.add(enemy)
		enemy.rect.x = random.randrange(WIDTH - 20)
		enemy.rect.y = random.randrange(HIGH - 20)
		#ls_enemies.draw(SCREEN)#posiciona los enemigos

	#----------------BALA-------------------------
	ls_bullet = pygame.sprite.Group()


	#--------------SONIDO---------------------------
	bullet_sound = pygame.mixer.Sound('Warble.mp3')


	#-----------------EMPIEZA-------------------

	pygame.display.flip()
	end = False
	disparo = False
	while not end:
		#accion
		pos = pygame.mouse.get_pos()
		ship.setPos(pos)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				disparo = True;
				#bullet.setPos(ship.getPos())#la bala inicia donde esta el jugador
				bullet_sound.play()#suena disparo
		#reaccion
		if disparo :
			bullet = Bullet('mano.png',[0,0])
			bullet.rect.x = pos[0]
			bullet.rect.y = pos[1]
			ls_bullet.add(bullet)
			ls_all.add(bullet)
			disparo = False


		SCREEN.blit(background, [0,0])

		for b in ls_bullet:
			ls_impactos = pygame.sprite.spritecollide(b, ls_enemies, True)
			for impacto in ls_impactos:
				ls_bullet.remove(b)
				ls_all.remove(b)
				#puntos += 1

		#------------IMPRIME EN PANTALLA--------------
		ls_all.update()
		ls_all.draw(SCREEN)
		pygame.display.flip()
		reloj.tick(60)

		#---------------COLISION----------------------
		ls_choque = pygame.sprite.spritecollide(ship, ls_enemies, False)
		for elements in ls_choque:
			print "choque"
			#ship.setVidas(ship.getVidas()-1)#le quita una vida
