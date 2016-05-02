import pygame
import sys
ANCHO = 700
ALTO = 400

ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
BLANCO = (255,255,255)

class Enemy(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, x,y,w,h,surface,color):
    	pygame.sprite.Sprite.__init__(self)
        self.y = y
        self.x = x
        self.w = w
        self.h = h
        self.color = color
        self.surface = surface
        pygame.draw.rect(surface, color, (x,y,w,h))

    def update(self):#se mueve hacia los lados
        #self.surface.fill(BLANCO)
        pygame.draw.rect(self.surface, self.color, (self.x,self.y,self.w,self.h))

class Player(pygame.sprite.Sprite): #Hereda de la clase sprite
    def __init__(self, x,y,w,h,surface,color):
    	pygame.sprite.Sprite.__init__(self)
        #pygame.surface(weight,high) #OJOOOOOOOOOOO
        self.y = y
        self.x = x
        self.w = w
        self.h = h
        self.color = color
        self.surface = surface
        self.speed = 1
        self.stop = False
        self.i = h #este controla el alto de su salto
        pygame.draw.rect(surface, color, (x,y,w,h))

    def moveLeft(self):
        if(self.x - self.speed > 0 + self.w):
            self.x -= self.speed

    def moveRight(self):
        if(self.x + self.speed < ANCHO - self.w):
            self.x += self.speed

    def moveUp(self):
        if(self.stop == False):
            self.y -= self.speed
            self.i -= 1 #se le acaba el salto
        if(self.i <= 0): #debe comenzar a bajar
            self.i = self.h
            self.Gravity()

    def Stop(self,b):
        self.stop = b
        if(b):
            self.i = self.h

    def Gravity(self):
        self.grav = True
        if(self.y >= 0 - self.h): #para que no pase del piso self.grav = False
            self.y += 0.3

    def update(self):#se mueve hacia los lados
        #self.surface.fill(BLANCO)
        pygame.draw.rect(self.surface, self.color, (self.x,self.y,self.w,self.h))


def checkCollision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        return True
    else:
        return False

def main():
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    reloj = pygame.time.Clock()

    #------------Listas de sprites--------------
    ls_todos = pygame.sprite.Group()
    ls_jugador = pygame.sprite.Group()
    ls_plataforma = pygame.sprite.Group()

    #-------------Jugadores--------------------------
    jugador = Player(ANCHO/5-25,ALTO-50,25,50,pantalla,ROJO)
    ls_todos.add(jugador)
    ls_jugador.add(jugador)

    #--------------Plataformas--------------------------
    plataforma1 = Enemy(ANCHO/5-25,ALTO-100,50,25,pantalla,VERDE)
    ls_todos.add(plataforma1)
    ls_plataforma.add(plataforma1)

    plataforma2 = Enemy(ANCHO/5+25,ALTO-100,50,25,pantalla,AZUL)
    ls_todos.add(plataforma2)
    ls_plataforma.add(plataforma2)

    flag_space = False #Este controla que siga subiendo cuando se le presiona una sola vez el espacio

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            jugador.moveLeft()
            pantalla.fill(BLANCO)
            jugador.update()

        if keys[pygame.K_RIGHT]:
            jugador.moveRight()
            pantalla.fill(BLANCO)
            jugador.update()

        if keys[pygame.K_SPACE]:
            jugador.moveUp()
            pantalla.fill(BLANCO)
            jugador.update()
            flag_space = True

        else:
            jugador.Gravity()

        """if(flag_space):
            jugador.moveUp()
            pantalla.fill(BLANCO)
            jugador.update()"""

        """for p in ls_plataforma:
            if(checkCollision(jugador,p)):
                jugador.Stop(True)#no lo deja mover""""

        ls_todos.update()
        ls_plataforma.update()
        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':

	main()
