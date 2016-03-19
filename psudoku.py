

# Librerias
import pygame
import sys
from pygame.locals import *

# Colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (84,84,84)



# Funciones

#def Menu():


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

while True:
	event = pygame.event.poll()
	if event.type == QUIT:
		break
	pygame.display.update()