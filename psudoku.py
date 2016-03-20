
# Librerias
import pygame, sys, time
from pygame.locals import *

# Colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (84,84,84)


# Valores globales
tamaño_fondo = (800, 600)
tamaño_tablero = 360
assert(tamaño_tablero % 9 == 0), "El tablero tiene que ser multiplo de 9"
tablero = (tamaño_tablero, tamaño_tablero)
celda = int(tablero[0] / 9) # Tamaño de cada celda en el tablero
margen_x = 200
margen_y = 100
pos_titulo = ((margen_x+(3*celda)),(margen_y-60))


########################## Inicio de Funciones #################################

# Dibuja las lineas que delimitan el tablero
def dibuja_tablero(fondo, color, tablero, celda, margenx, margeny):
	#Variables de verificación
	x_veri = 0
	y_veri = 0
	i_veri = 0
	# Dibuja las lineas horizontales
	for x in range(0, 400, celda):
		pygame.draw.line(fondo, color, (x+margenx, margeny), (x+margenx,tablero[0]+margeny))
		x_veri = x_veri + 1
	# Dibuja las lineas verticales
	for y in range(0, 400, celda):
		pygame.draw.line(fondo, color, (margenx,y+margeny), ((tablero[0]+margenx),(y+margeny)))
		y_veri = y_veri + 1
	# Verificación del dibujo del tablero
	assert(x_veri == 10), "Tienen que haber 10 líneas horizontales"
	assert(y_veri == 10), "Tienen que haber 10 líneas verticales"
	# Resalta las regiones del tablero
	for i in range(0, 400, (3*celda)):
		pygame.draw.line(fondo, color, (i+margenx,+margeny), (i+margenx,360+margeny), 3) # Horizontales
		pygame.draw.line(fondo, color, (margenx,i+margeny), (tablero[0]+margenx,i+margeny), 3) # Verticales
		i_veri = i_veri + 1
	# Verificación del dibujo de las regiones
	assert(i_veri == 4), "Tienen que haber 9 regiones"
	return None

"""NO FUNCIONA"""
# Pasa de las coordenadas de fondo a las celdas de tablero 
def celdas_coord(x, y, celda, margenx, margeny):
	izquierda = x * celda + margenx
	arriba = y * celda + margeny
	return (izquierda, arriba)

"""NO FUNCIONA"""
# Pasas de las celdas de tablero a las coordenadas de fondo 
def coord_celdas(x, y, celda, margenx, margeny):
	for x in range(10):
		for y in range(10):
			izquierda, arriba = celdas_coord(x, y, celda, margenx, margeny)
			caja = pygame.Rect(izquierda, arriba, celda, celda)
	if caja.collidepoint(x, y):
		return (x, y)
	else:
		return (None, None)

############################# Fin de Funciones #################################

# Inicializa PyGame
pygame.init()

# Fuentes
titulos = pygame.font.SysFont("monospace", 40, italic=True)

# Sonidos
click = pygame.mixer.Sound('click.wav')

################################################################################
#                           Inicio del programa                                #
################################################################################

# Crea la pantalla
pygame.display.set_caption('Sudoku Chevere')
fondo = pygame.display.set_mode(tamaño_fondo)
fondo.fill(blanco)
# Crea el titulo 'Sudoku'
sudoku = titulos.render("Sudoku", 2, negro)
fondo.blit(sudoku, pos_titulo)
#Dibuja el tablero
dibuja_tablero(fondo, negro, tablero, celda, margen_x, margen_y)

while True:
	evento = pygame.event.poll()
	if evento.type == QUIT:
		pygame.quit()
		sys.exit()
	elif evento.type == MOUSEBUTTONUP:
		click.play() # Reproduce el sonido click
	pygame.display.update()