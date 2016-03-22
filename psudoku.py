
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
    ancho = 0
    largo = 0
    margen_x = 0
    margen_y = 0


class Tablero(Bloques):
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

# _________________________ Inicio de Funciones ______________________________#


# Dibuja las lineas que delimitan el tablero
def dibuja_tablero(tablero, color):
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


# Pasa de las coordenadas de fondo a las celdas de tablero
# mousex, mousey = pygame.mouse.get_pos() necesario para que funcione
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
                print (x, y)
                return (x, y)
    return (None, None)


# Cierra el programa
def cerrar():
    pygame.quit()
    sys.exit()


# Permite el ingreso de texto
def input_texto(fps, fuente, pos_nombre, reloj):
    """NO FUNCIONA"""
    # Inicializando
    nombre = []
    alfabeto = 'abcdefghijklmnopqrstuvwxyz0987654321'
    # Obtiene los eventos
    evento = pygame.event.get()
    # Velocidad de refrescamiento de la pantalla
    reloj.tick(fps)
    # Cierra el programa si presionan cerrar
    for x in evento:
        if x.type == QUIT:
            cerrar()
    # Ingresos de letras al string
    for x in evento:
        if x.type == KEYDOWN:
            if x.key == K_BACKSPACE:
                # Borra lo ultimo ingresado
                nombre = nombre[:-1]
            elif x.key == K_SPACE:
                # Agrega un espacio
                nombre += [' ']
            elif x.key == K_BACKSPACE:
                print(nombre)# Quitar
                # Sale de la funcion
                return
            elif pygame.key.name(x.key) in alfabeto:
                nombre += pygame.key.name(x.key)
                print(nombre)
    # Imprime lo ingresado en pantalla


# Carga los datos del tablero a un arreglo 2D
def cargar_tablero(nombre):
    with open(nombre + ".txt", 'r') as archivo:
        numeros_tablero = archivo.readlines()
    archivo.closed
    return numeros_tablero


# Guarda la partida
def guardar_partida(nombre, numeros_tablero):
    with open(nombre + ".txt", 'w') as archivo:
        for linea in numeros_tablero:
            archivo.write(linea)
    archivo.closed


# Limpia la pantalla
def limpia_pantalla(pantalla, fondo):
    fondo.blit(pantalla, (0, 0))

# _____________________________ Fin de Funciones _____________________________#

# Inicializa PyGame
pygame.init()
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
pygame.display.set_caption('Sudoku Chevere')
fondo = pygame.display.set_mode(tamano_fondo)
fondo.fill(blanco)
# Crea el titulo 'Sudoku'
sudoku = titulos.render("Sudoku", 2, negro)
fondo.blit(sudoku, (0, 0))# Arreglar la posicion

# Dibuja el tablero

while True:
    evento = pygame.event.poll()
    if evento.type == QUIT:
        cerrar()
    elif evento.type == MOUSEBUTTONUP:
        # Reproduce el sonido click
        click.play()
        dibuja_tablero(tablero9, negro)
    pygame.display.update()
