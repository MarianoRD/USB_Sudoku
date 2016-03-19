
# Librerias
import pygame, sys
from pygame.locals import *

# Colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (84,84,84)


# Valores iniciales
tablero = (360, 360)



# Funciones

# Dibuja las lineas que delimitan el tablero
def dibuja_tablero(fondo, color):
	celda = 40 # Tamaño de cada celda en el tablero
	# Dibuja las lineas horizontales
	for x in range(0, 400, celda):
		pygame.draw.line(fondo, color, (x,0), (x,360))
	# Dibuja las lineas verticales
	for y in range(0, 400, celda):
		pygame.draw.line(fondo, color, (0,y), (360,y))
	# Resalta las regiones del tablero
	for x in range(0, 400, (3*celda)):
		pygame.draw.line(fondo, color, (x,0), (x,360), 3) # Horizontales
		pygame.draw.line(fondo, color, (0,x), (360,x), 3) # Verticales
	return None

# Lleva la cuenta de cuanto tiempo lleva el jugador resolviendo el Sudoku



################################################################################
#                           Inicio del programa                                #
################################################################################


# Inicializa PyGame
pygame.init()

# Fuentes
fuente = pygame.font.SysFont("monospace",15)

# Crea la pantalla
pygame.display.set_caption('Sudoku Chevere')
fondo = pygame.display.set_mode((800, 600))
fondo.fill(blanco)
dibuja_tablero(fondo, negro)

while True:
	evento = pygame.event.poll()
	if evento.type == QUIT:
		pygame.quit()
		sys.exit()
	pygame.display.update()