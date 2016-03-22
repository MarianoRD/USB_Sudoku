"""Un super Sudoku que no funciona."""

# Librerias
import sys
# import time
import pygame
from pygame import *

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
gris = (84, 84, 84)
azul = (47, 86, 233)

# ______________________________ Clases ______________________________________#


class Bloques():
    """Variables necesarias para crear los Rect en PyGame."""

    ancho = 0
    largo = 0
    margen_x = 0
    margen_y = 0


class Tablero(Bloques):
    """Clase hija de Bloques, donde se agrega celdas y lineas de un tablero."""

    celda = 0
    lineas = 0


# ___________________________ Fin Clases _____________________________________#


# _____________________________ Valores iniciales ____________________________#
# Fondo
tamano_fondo = (800, 600)

# Tablero 9x9
tablero9 = Tablero()
tablero9.ancho = 360
tablero9.largo = tablero9.ancho
tablero9.celda = int(tablero9.ancho / 9)
tablero9.margen_x = 200
tablero9.margen_y = 100
tablero9.lineas = 9

# Tablero 6x6
tablero6 = Tablero()
tablero6.ancho = 360
tablero6.largo = tablero9.ancho
tablero6.celda = int(tablero9.ancho / 6)
tablero6.margen_x = 200
tablero6.margen_y = 100
tablero6.lineas = 6

# Cuadros por segundos a los que se refresca la pantalla
fps = 30

# Nombre del jugador
nombre = ''

# _________________________ Inicio de Funciones ______________________________#

# Limpia la pantalla
def limpia_pantalla(fondo, color_fondo, color_letras):# Arreglar entrada al tener la clase texto
    """Limpia de la pantalla todos los graficos que ya no son necesarios."""
    # Llena la pantalla de blanco
    fondo.fill(blanco)
    # Crea el titulo 'Sudoku'
    sudoku = titulos.render("Sudoku", 2, negro)
    fondo.blit(sudoku, (0, 0))# Arreglar la posicion


def dibuja_tablero(tablero, color):
    """Dibuja las lineas que delimitan las celdas y el tablero."""
    # Se limpia la pantalla (queda: fondo blanco, titulo)
    limpia_pantalla(fondo, blanco, negro)

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
def input_texto(tecla, fuente, pos_nombre):
    """NO FUNCIONA."""
    """# Se limpia la pantalla (queda: fondo blanco, titulo)
    limpia_pantalla(fondo, blanco, negro)"""
    # Inicializando
    nombre = ''
    alfabeto = 'abcdefghijklmnopqrstuvwxyz0987654321'
    # Almacena el nombre en string
    if tecla == 'space':
        nombre += ' '
    elif tecla == 'return' or tecla == 'escape':
        return
    elif tecla == 'backspace':
        nombre = nombre[:-1]
    elif tecla in alfabeto:
        nombre += tecla

    # Imprime lo ingresado en pantalla
    """texto = fuente.render(nombre, 1, negro)
    fondo.blit(texto, (0, 0))# Arreglar posicion]"""
    return nombre


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

# Inicializa PyGame
pygame.init()
# Velocidad de refrescamiento de la pantalla
reloj = pygame.time.Clock()
# Fuentes
titulos = pygame.font.SysFont("monospace", 60, italic=True)
palabras_menu = pygame.font.SysFont("monospace", 17)
# Sonidos
click = pygame.mixer.Sound('click.wav')

# ____________________________________________________________________________#
#                           Inicio del programa                               #
# ____________________________________________________________________________#

# Crea la pantalla
fondo = pygame.display.set_mode(tamano_fondo)
pygame.display.set_caption('Sudoku Chevere')
limpia_pantalla(fondo, blanco, negro)


# ------ Ciclo principal del programa --------------
while True:

    # PROCESAMIENTO DE EVENTOS DEBAJO DE ESTA LINEA
    for evento in pygame.event.get():
        # Cierra el programa
        if evento.type == QUIT:
            cerrar()
        # Dibuja el tablero si hay un click
        """if evento.type == MOUSEBUTTONUP:
            # Reproduce el sonido click
            click.play()
            dibuja_tablero(tablero9, negro)
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
