"""Un super Sudoku que no funciona."""

# Librerias
import sys
import os.path
# import time
import pygame
from pygame import *

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (84, 84, 84)
azul = (47, 86, 233)
rojo = (255, 0, 0)

# Fondo
alto_fondo = 600
ancho_fondo = 800
tamano_fondo = (ancho_fondo, alto_fondo)

# Inicializa PyGame
pygame.init()

# Fuentes
titulos = pygame.font.SysFont("monospace", 60, italic=True)
palabras_menu = pygame.font.SysFont("monospace", 17)

# Define la pantalla principal y el título de la pantalla
fondo = pygame.display.set_mode(tamano_fondo)
pygame.display.set_caption("Sudoku Chevere")
ruta_imagen_fondo = os.path.join('imagenes', 'fondo.png')
imagen_fondo = pygame.image.load(ruta_imagen_fondo).convert()


# Icono del programa
ruta_imagen_logo = os.path.join('imagenes', 'logo.png')
icono = pygame.image.load(ruta_imagen_logo).convert()
pygame.display.set_icon(icono)

# ______________________________ Clases ______________________________________#


class Rectangulo():
    """Rectangulos de PyGame, solo tienen las x,y de la esquina superior izquierda."""

    margen_x = 0
    margen_y = 0


class Imagen(Rectangulo):
    """Variables necesarias para cualquier imagen que se quiera dibujar."""

    ruta = os.path.join('imagenes', 'nueva_Partida.png')
    imagen = pygame.image.load(ruta)

    def indica_ruta(self):
    	self.imagen = pygame.image.load(self.ruta)


class Bloques(Rectangulo):
    """Variables necesarias para crear los Rect en PyGame."""

    ancho = 0
    alto = 0


class Tablero(Bloques):
    """Clase hija de Bloques, donde se agrega celdas y lineas de un tablero."""

    celda = 0
    lineas = 0


class Boton(Imagen):
    """Clase hija de Bloques, para cargar imagenes."""

    texto = ""


class Texto(Imagen):
    """Variables para blitear imagenes."""

    texto = ''
    fuente = palabras_menu
    antialias = True
    color = negro
    renderizado = None

    def renderizar(self):
        """Renderiza el texto, para poder ser mostrado en pantalla."""
        self.renderizado = self.fuente.render(self.texto, self.antialias, self.color)
        return None

# ___________________________ Fin Clases _____________________________________#


# _____________________________ Valores iniciales ____________________________#

# Tablero 9x9
tablero9 = Tablero()
tablero9.ancho = 360
tablero9.alto = tablero9.ancho
tablero9.celda = int(tablero9.ancho / 9)
tablero9.margen_x = 200
tablero9.margen_y = 180
tablero9.lineas = 9

# Tablero 6x6
tablero6 = Tablero()
tablero6.ancho = 360
tablero6.alto = tablero9.ancho
tablero6.celda = int(tablero9.ancho / 6)
tablero6.margen_x = 200
tablero6.margen_y = 200
tablero6.lineas = 6

# Nombre del jugador
nombre = Texto()
nombre.texto = ''
nombre.fuente = palabras_menu
nombre.color = negro
nombre.margen_x = 0
nombre.margen_y = 200
nombre.renderizar()

# Texto de bienvenida
bienvenida = Texto()
bienvenida.texto = 'Bienvenido a Sudoku Chevere, por favor introduzca su nombre'
bienvenida.fuente = palabras_menu
bienvenida.color = negro
bienvenida.margen_x = 0
bienvenida.margen_y = 0
bienvenida.renderizar()

# Texto de Elegir Dificultades
elegir_dificultadtxt = Texto()
elegir_dificultadtxt.texto = 'Elegir Dificultad'
elegir_dificultadtxt.fuente = titulos
elegir_dificultadtxt.color = negro
elegir_dificultadtxt.margen_x = 200
elegir_dificultadtxt.margen_y = 10
elegir_dificultadtxt.renderizar()

# Titulo 'Sudoku'
sudoku = Imagen()
sudoku.margen_x = 150
sudoku.margen_y = 10
sudoku.ruta = os.path.join('imagenes', 'sudoku.png')
sudoku.indica_ruta()


# ________Inicio Botones del Menu__________________________
# Nueva partida
nueva_Partida = Boton()
nueva_Partida.ancho = 150
nueva_Partida.alto = 30
nueva_Partida.margen_x = 320
nueva_Partida.margen_y = 185
nueva_Partida.ruta = os.path.join('imagenes', 'nueva_partida.png')
nueva_Partida.indica_ruta()
texto = "Nueva Partida"

# Cargar partida
cargar_partida = Boton()
cargar_partida.ancho = 150
cargar_partida.alto = 30
cargar_partida.margen_x = 320
cargar_partida.margen_y = 260
cargar_partida.ruta = os.path.join('imagenes', 'cargar_partida.png')
cargar_partida.indica_ruta()
texto = "Cargar Partida"

# Records
records = Boton()
records.ancho = 150
records.alto = 30
records.margen_x = 320
records.margen_y = 335
records.ruta = os.path.join('imagenes', 'records.png')
records.indica_ruta()
texto = "Records"

# Ayuda
ayuda = Boton()
ayuda.ancho = 150
ayuda.alto = 30
ayuda.margen_x = 320
ayuda.margen_y = 410
ayuda.ruta = os.path.join('imagenes', 'reglas.png')
ayuda.indica_ruta()
texto = "Ayuda"

# Salir
salir = Boton()
salir.ancho = 150
salir.alto = 30
salir.margen_x = 320
salir.margen_y = 485
salir.ruta = os.path.join('imagenes', 'salir.png')
salir.indica_ruta()
texto = "Salir"

# ____________________ FIN de botones del menu _______________


#_____________________ Botones de elegir dificultad _________________

# Entrenamiento
entrenamiento = Boton()
entrenamiento.ancho = 150
entrenamiento.alto = 30
entrenamiento.margen_x = 320
entrenamiento.margen_y = 185
entrenamiento.ruta = os.path.join('imagenes', 'entrenamiento.png')
entrenamiento.indica_ruta()
texto = "Entrenamiento"

# Facil
facil = Boton()
facil.ancho = 150
facil.alto = 30
facil.margen_x = 320
facil.margen_y = 260
facil.ruta = os.path.join('imagenes', 'facil.png')
facil.indica_ruta()
texto = "Facil"

# Dificil
dificil = Boton()
dificil.ancho = 150
dificil.alto = 30
dificil.margen_x = 320
dificil.margen_y = 335
dificil.ruta = os.path.join('imagenes', 'dificil.png')
dificil.indica_ruta()
texto = "Dificil"

# Extremo
extremo = Boton()
extremo.ancho = 150
extremo.alto = 30
extremo.margen_x = 320
extremo.margen_y = 410
extremo.ruta = os.path.join('imagenes', 'extremo.png')
extremo.indica_ruta()
texto = "Extremo"

# Menu: Si, volvemos al menu principal.
menu = Boton()
menu.ancho = 150
menu.alto = 30
menu.margen_x = 320
menu.margen_y = 410
menu.ruta = os.path.join('imagenes', 'menu_principal.png')
menu.indica_ruta()
texto = "Menu"

#_____________________  FIN de Botones de elegir dificultad _________________


# Cuadros por segundos a los que se refresca la pantalla
fps = 30


# _________________________ Inicio de Funciones ______________________________#

# Funcion para elegir dificultades
def elegir_dificultad(datos_menu):
	dificultad = True
	global menu
	cajas = [
    pygame.Rect(entrenamiento.margen_x, entrenamiento.margen_y, entrenamiento.ancho, entrenamiento.alto),
    pygame.Rect(facil.margen_x, facil.margen_y, facil.ancho, facil.alto),
    pygame.Rect(dificil.margen_x, dificil.margen_y, dificil.ancho, dificil.alto),
    pygame.Rect(extremo.margen_x, extremo.margen_y, extremo.ancho, extremo.alto),
    pygame.Rect(menu.margen_x, menu.margen_y, menu.ancho, menu.alto)
        ]

	while dificultad:

        # Dibuja los botones del menu
		fondo.blit(imagen_fondo, (0, 0))
		fondo.blit(elegir_dificultadtxt.renderizado, (elegir_dificultadtxt.margen_x, elegir_dificultadtxt.margen_y))
		dibuja_boton(entrenamiento)
		dibuja_boton(facil)
		dibuja_boton(dificil)
		dibuja_boton(extremo)
		dibuja_boton(menu)

		for event in pygame.event.get():
            # Variables a verificar
			mouse = pygame.mouse.get_pos()
			click = pygame.mouse.get_pressed()
            # Sale del juego
			if event.type == pygame.QUIT:
				cerrar()
            # Reacciona si se pasa por encima de la opcion (FALTAN IMG HOVER)
			if cajas[0].collidepoint(mouse[0], mouse[1]):
				pygame.draw.rect(fondo, (azul), (entrenamiento.margen_x, entrenamiento.margen_y, entrenamiento.ancho, entrenamiento.alto))
                #fondo.blit(opcion.imagen, (opcion.margen_x - 15, opcion.margen_y - 22))
			if cajas[1].collidepoint(mouse[0], mouse[1]):
				pygame.draw.rect(fondo, azul, (facil.margen_x, facil.margen_y, facil.ancho, facil.alto))
			if cajas[2].collidepoint(mouse[0], mouse[1]):
				pygame.draw.rect(fondo, azul, (dificil.margen_x, dificil.margen_y, dificil.ancho, dificil.alto))
			if cajas[3].collidepoint(mouse[0], mouse[1]):
				pygame.draw.rect(fondo, azul, (extremo.margen_x, extremo.margen_y, extremo.ancho, extremo.alto))
			if cajas[4].collidepoint(mouse[0], mouse[1]):
				pygame.draw.rect(fondo, azul, (menu.margen_x, menu.margen_y, menu.ancho, menu.alto))

			if click[0] == 1 and cajas[0].collidepoint(mouse[0], mouse[1]):
				click_sonido.play()
				#elegir_dificultad()
				dificultad = False
			if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
				click_sonido.play()
				#dibuja_tablero(tablero9, negro)
				dificultad = False
			if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
				click_sonido.play()
				#dibuja_tablero(tablero9, negro)
				dificultad = False
			if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
				click_sonido.play()
				#dibuja_tablero(tablero9, negro)
				dificultad = False
			if click[0] == 1 and cajas[4].collidepoint(mouse[0], mouse[1]):
				dificultad = False
				menu_juego(datos_menu)


	


		pygame.display.update()



# Crea los botones del menu
def dibuja_boton(opcion):
    """Funcion que dibuja los botones del menu"""
    pygame.draw.rect(fondo, (blanco), (opcion.margen_x, opcion.margen_y, opcion.ancho, opcion.alto))
    fondo.blit(opcion.imagen, (opcion.margen_x - 15, opcion.margen_y - 22))


# Dibuja el menú principal
def menu_juego(fondo, blanco, azul, sudoku):
    """Funcion que muestra el menu en la pantalla."""
    datos_menu = (fondo,blanco,azul,sudoku)
    menu = True
    # Ciclo principal
    while menu:
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Almacena todas las opciones del menú en un arreglo
        cajas = [
    pygame.Rect(nueva_Partida.margen_x, nueva_Partida.margen_y, nueva_Partida.ancho, nueva_Partida.alto),
    pygame.Rect(cargar_partida.margen_x, cargar_partida.margen_y, cargar_partida.ancho, cargar_partida.alto),
    pygame.Rect(records.margen_x, records.margen_y, records.ancho, records.alto),
    pygame.Rect(ayuda.margen_x, ayuda.margen_y, ayuda.ancho, ayuda.alto),
    pygame.Rect(salir.margen_x, salir.margen_y, salir.ancho, salir.alto)
        ]

        # Dibuja los botones del menu
        fondo.blit(imagen_fondo, (0, 0))
        fondo.blit(sudoku.imagen, (sudoku.margen_x, sudoku.margen_y))
        dibuja_boton(nueva_Partida)
        dibuja_boton(cargar_partida)
        dibuja_boton(records)
        dibuja_boton(ayuda)
        dibuja_boton(salir)

        for event in pygame.event.get():
            # Variables a verificar
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # Sale del juego
            if event.type == pygame.QUIT:
                cerrar()
            # Reacciona si se pasa por encima de la opcion (FALTAN IMG HOVER)
            if cajas[0].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, (azul), (nueva_Partida.margen_x, nueva_Partida.margen_y, nueva_Partida.ancho, nueva_Partida.alto))
                #fondo.blit(opcion.imagen, (opcion.margen_x - 15, opcion.margen_y - 22))
            if cajas[1].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (cargar_partida.margen_x, cargar_partida.margen_y, cargar_partida.ancho, cargar_partida.alto))
            if cajas[2].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (records.margen_x, records.margen_y, records.ancho, records.alto))
            if cajas[3].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (ayuda.margen_x, ayuda.margen_y, ayuda.ancho, ayuda.alto))
            if cajas[4].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (salir.margen_x, salir.margen_y, salir.ancho, salir.alto))

            if click[0] == 1 and cajas[0].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                menu = elegir_dificultad(datos_menu)
                #menu = False
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                dibuja_tablero(tablero9, negro)
                menu = False
            if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                dibuja_tablero(tablero9, negro)
                menu = False
            if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                dibuja_tablero(tablero9, negro)
                menu = False
            if click[0] == 1 and cajas[4].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                cerrar()

        pygame.display.update()

# Limpia la pantalla
def limpia_pantalla(fondo, imagen_fondo, sudoku):# Arreglar entrada al tener la clase texto
    """Limpia de la pantalla todos los graficos que ya no son necesarios."""
    # Pone el fondo
    fondo.blit(imagen_fondo, (0, 0))
    # Crea el titulo 'Sudoku'
    fondo.blit(sudoku.imagen, (sudoku.margen_x, sudoku.margen_y))


def dibuja_tablero(tablero, color, imagen_fondo, sudoku):
    """Dibuja las lineas que delimitan las celdas y el tablero."""
    # Se limpia la pantalla (queda: fondo blanco, titulo)
    limpia_pantalla(fondo, imagen_fondo, sudoku)
    # Variables de verificación
    x_veri = -1
    y_veri = -1
    # Dibuja las lineas horizontales
    for x in range(0, 400, tablero.celda):
        pygame.draw.line(fondo, color,
                    (x + tablero.margen_x, tablero.margen_y),
                    (x + tablero.margen_x, tablero.ancho + tablero.margen_y))
        x_veri = x_veri + 1
    # Dibuja las lineas verticales
    for y in range(0, 400, tablero.celda):
        pygame.draw.line(fondo, color,
                (tablero.margen_x, y + tablero.margen_y),
                ((tablero.ancho + tablero.margen_x), (y + tablero.margen_y)))
        y_veri = y_veri + 1
    # Verificación del dibujo del tablero
    assert(x_veri == tablero.lineas), "Faltan líneas horizontales"
    assert(y_veri == tablero.lineas), "Faltan líneas verticales"
    # Resalta las regiones del tablero
    for i in range(0, 400, (3 * tablero.celda)):
        # Horizontales
        pygame.draw.line(fondo, color,
                        (i + tablero.margen_x, tablero.margen_y),
                        (i + tablero.margen_x, 360 + tablero.margen_y), 3)
        # Verticales
        pygame.draw.line(fondo, color,
                (tablero.margen_x, i + tablero.margen_y),
                (tablero.ancho + tablero.margen_x, i + tablero.margen_y), 3)

    return None


# mousex, mousey = pygame.mouse.get_pos() necesario para que funcione
def celdas_coord(x, y, celda, margenx, margeny):
    """Pasa del sistema del juego al sistema coordenado celdas."""
    izquierda = (x * celda) + margenx
    arriba = (y * celda) + margeny
    return (izquierda, arriba)


# mousex, mousey = pygame.mouse.get_pos() Necesario para que funcione
def coord_celdas(xmouse, ymouse, celda, margenx, margeny):
    """Pasa del sistema coordenado celdas, al sistema coordenado del juego."""
    for x in range(9):
        for y in range(9):
            izquierda, arriba = celdas_coord(x, y, celda, margenx, margeny)
            caja = pygame.Rect(izquierda, arriba, celda, celda)
            if caja.collidepoint(xmouse, ymouse):
                print (x, y)
                return (x, y)
    return (None, None)


def cerrar():
    """Cierra el programa."""
    pygame.quit()
    sys.exit()


# Permite el ingreso de texto
def input_texto(nombre, titulo):
    """NO FUNCIONA."""
    ingreso = True
    # Crea el fondo
    fondo.blit(imagen_fondo, (0, 0))
    fondo.blit(titulo.renderizado, (titulo.margen_x, titulo.margen_y))
    pygame.display.update()

    while ingreso:
        # Guarda el nombre en el string
        for evento in pygame.event.get():
            if evento.type == KEYDOWN:
                if evento.unicode.isalpha() or evento.unicode.isnumeric():
                    nombre.texto += evento.unicode
                if evento.key == K_BACKSPACE:
                    nombre.texto = nombre.texto[:-1]
                if evento.key == K_SPACE:
                    nombre.texto += ' '
                if evento.key == K_RETURN:
                    ingreso = False
                if evento.key == K_CLEAR:
                    nombre.texto = ''
            if evento.type == QUIT:
                    cerrar()
            else:
                pass

        # Escribe el nombre ingresado en pantalla
        fondo.blit(imagen_fondo, (0, 0))
        fondo.blit(titulo.renderizado, (titulo.margen_x, titulo.margen_y))
        nombre.renderizar()
        fondo.blit(nombre.renderizado, (nombre.margen_x, nombre.margen_y))
        pygame.display.update()

    """texto = fuente.render(nombre, 1, negro)
    # Arreglar posicion
    fondo.blit(texto, (0, 0))"""


# Carga los datos del tablero a un arreglo 2D
def cargar_tablero(nombre):
    """Carga los numeros del tablero del Sudoku de un archivo '.txt'."""
    with open(nombre + ".txt", 'r') as archivo:
        numeros_tablero = archivo.readlines()
    archivo.closed
    return numeros_tablero


# Guarda la partida
def guardar_partida(nombre, numeros_tablero):
    """Guarda los numeros del tablero del Sudoku de un archivo '.txt'."""
    with open(nombre + ".txt", 'w') as archivo:
        for linea in numeros_tablero:
            archivo.write(linea)
    archivo.closed


# _____________________________ Fin de Funciones _____________________________#


# Velocidad de refrescamiento de la pantalla
reloj = pygame.time.Clock()

# Sonidos
click_sonido = pygame.mixer.Sound('click.wav')

# ____________________________________________________________________________#
#                           Inicio del programa                               #
# ____________________________________________________________________________#

# ------ Ciclo principal del programa --------------
fondo.blit(imagen_fondo, (0, 0))
input_texto(nombre, bienvenida)
menu_juego(fondo, blanco, azul, sudoku)
# Dibuja el tablero
while True:

    # PROCESAMIENTO DE EVENTOS DEBAJO DE ESTA LINEA
    for evento in pygame.event.get():
        # Cierra el programa
        if evento.type == QUIT:
            cerrar()
        # Dibuja el tablero si hay un click"""
        #if evento.type == MOUSEBUTTONUP:
            # Reproduce el sonido click
            #dibuja_tablero(tablero9, negro)
        # Entrada del nombre del usuario (ARREGLAR DONDE VA LUEGO)"""
        if evento.type == KEYUP and evento.key != 'backspace':
            tecla = pygame.key.name(evento.key)
            nombre += input_texto(tecla, palabras_menu, (0, 0))
            print(nombre)
        if evento.type == KEYUP and evento.key == 'backspace':
            nombre -= nombre[:-1]
            print(nombre)
    # PROCESAMIENTO DE EVENTOS ENCIMA DE ESTA LINEA

    # LOGICA DEL JUEGO DEBAJO DE ESTA LINEA

    # LOGICA DEL JUEGO ENCIMA DE ESTA LINEA

    # DIBUJO DE LA NUEVA PANTALLA

    # Se actualiza todo lo hecho en el codigo
    pygame.display.update()
    # Limitamos los FPS
    reloj.tick(fps)
