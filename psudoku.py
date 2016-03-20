
# Librerias
import pygame, sys, time
from pygame.locals import *

# Colores
blanco = (255,255,255)
negro = (0,0,0)
gris = (84,84,84)
azul = (47, 86, 233)


# Valores globales
tamaño_fondo = (800, 600)
tamaño_tablero = 360
assert(tamaño_tablero % 9 == 0), "El tablero tiene que ser multiplo de 9"
tablero = (tamaño_tablero, tamaño_tablero)
celda = int(tablero[0] / 9) # Tamaño de cada celda en el tablero
margen_x = 200 # Margen que tiene el tablero horizontalmente
margen_y = 100 # Margen que tiene el tablero verticalmente
pos_titulo = ((margen_x+(3*celda)),(margen_y-60)) # Posicion del título
pos_menu = (pos_titulo[0]+30, pos_titulo[1]+120) # Posición del Menu
lineas = 9 # Numero de lineas tanto verticales como horizontales


########################## Inicio de Funciones #################################

# Menu
def Menu(fondo,negro,pos_titulo, OpcionFont):
	OpcionBack = (205,197,191)

	# Crea opcion1 (Crear Nueva Partida)
	Nva_partida = OpcionFont.render('Nueva partida', True, negro,OpcionBack)
	Fondo_Op = Nva_partida.get_rect()
	pos_nvapartida = (pos_titulo[0]+30, pos_titulo[1]+120)
	Fondo_Op.center = (pos_nvapartida)
	fondo.blit(Nva_partida,pos_nvapartida)

	# Creea opcion2 (Descargar Partida existente)
	Des_partida = OpcionFont.render('Cargar partida', True, negro,OpcionBack)
	pos_despartida = (pos_nvapartida[0]-4, pos_nvapartida[1]+60)
	Fondo_Op.center = (pos_despartida)
	fondo.blit(Des_partida,pos_despartida)

	# Creea opcion3 (Records)
	Records = OpcionFont.render('Tabla de Records', True, negro,OpcionBack)
	pos_record = (pos_despartida[0]-10, pos_despartida[1]+60)
	Fondo_Op.center = (pos_record)
	fondo.blit(Records,pos_record)

	# Creea opcion4 (Reglas)
	Reglas = OpcionFont.render('Como Jugar', True, negro,OpcionBack)
	pos_regla = (pos_record[0]+30, pos_record[1]+60)
	Fondo_Op.center = (pos_regla)
	fondo.blit(Reglas,pos_regla)	

	# Creea opcion5 (Salir)
	Salir = OpcionFont.render('Salir', True, negro,OpcionBack)
	pos_salir = (pos_regla[0]+25, pos_regla[1]+60)
	Fondo_Op.center = (pos_salir)
	fondo.blit(Salir,pos_salir)

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

# Pasa de las coordenadas de fondo a las celdas de tablero 
#mousex, mousey = pygame.mouse.get_pos() necesario para que funcione
def celdas_coord(x, y, celda, margenx, margeny):
	izquierda = (x * celda) + margenx
	arriba = (y * celda) + margeny
	return (izquierda, arriba)

# Pasas de las celdas de tablero a las coordenadas de fondo 
# mousex, mousey = pygame.mouse.get_pos() Necesario para que funcione
def coord_celdas(xmouse, ymouse, celda, margenx, margeny):
	for x in range(9):
		for y in range(9):
			izquierda, arriba = celdas_coord(x, y, celda, margenx, margeny)
			caja = pygame.Rect(izquierda, arriba, celda, celda)
			if caja.collidepoint(xmouse, ymouse):
				print (x,y)
				return (x, y)
	return (None, None)

# Carga los datos del tablero a un arreglo 2D
def cargar_tablero(nombre):
	with open(nombre+".txt", 'r') as archivo:
		numeros_tablero = archivo.readlines()
	archivo.closed

# Guarda la partida
def guardar_partida(numeros_tablero):
	with open(nombre+".txt", 'w') as archivo:
		for linea in numeros_tablero:
			archivo.write(linea)
	archivo.closed



############################# Fin de Funciones #################################

# Inicializa PyGame
pygame.init()
# Fuentes
titulos = pygame.font.SysFont("monospace", 60, italic=True)
palabras_menu = pygame.font.SysFont("monospace", 17)

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
# Crea menu
Menu(fondo,negro,pos_titulo, palabras_menu)
#Dibuja el tablero

while True:
	evento = pygame.event.poll()
	if evento.type == QUIT:
		pygame.quit()
		sys.exit()
	elif evento.type == MOUSEBUTTONUP:
		click.play() # Reproduce el sonido click
		dibuja_tablero(fondo, negro, tablero, celda, margen_x, margen_y)
	pygame.display.update()