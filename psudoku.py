

# Librerias
import pygame, sys
from pygame.locals import *	

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Funciones

# Dibuja las lineas que separan los numeros, las regiones del tablero y el fondo
# de la pantalla
def dibuja_tablero (color1, color2):
	# Crea el fondo blanco del tablero
	DISPLAYSURF = pygame.display.fill(color1)

	# Crea las lineas divisorias de los numeros
	for x in range(0, 800, 30):
		pygame.draw.line(DISPLAYSURF, color2, (x,0), (x,600))
	# Crea las lineas divisorias de las regiones y delimitadoras del tablero



################################################################################
#                           Inicio del programa                                #
################################################################################


# Inicializa PyGame
pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Sudoku Chevere')
while True: # main game loop
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			pygame.display.update()