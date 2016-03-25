
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
pistas = (165, 165, 204)

# Fondo
alto_fondo = 600
ancho_fondo = 800
tamano_fondo = (ancho_fondo, alto_fondo)

# Inicializa PyGame
pygame.init()

# Fuentes
titulos = pygame.font.SysFont("monospace", 60, italic=True)
palabras_menu = pygame.font.SysFont("monospace", 17)
numeros_sudoku = pygame.font.SysFont("monospace", 30, bold=True)
numeros = pygame.font.SysFont("fuentes/numeros.ttf", 25)

# Define la pantalla principal y el titulo de la pantalla
fondo = pygame.display.set_mode(tamano_fondo)
pygame.display.set_caption("Sudoku Chevere")
ruta_imagen_fondo = os.path.join('imagenes', 'fondo.png')
imagen_fondo = pygame.image.load(ruta_imagen_fondo).convert()

# Icono del programa
ruta_imagen_logo = os.path.join('imagenes', 'logo.png')
icono = pygame.image.load(ruta_imagen_logo).convert()
pygame.display.set_icon(icono)

# Cuadros por segundos a los que se refresca la pantalla
fps = 30

# ______________________________ Clases ______________________________________#


class Juego():
    """Donde se corre el juego."""

    tablero_solucion = []
    tablero_juego = [['0'for x in range(9)] for y in range(9)]
    fuente = palabras_menu
    color = negro
    tiempo = [0,0]
    puntaje = 0
    errores = 0
    jugador = ''
    modo = 0
    archivo = os.path.join('tableros', '')
    dificultad = ''

    def __init__(self, nombre_archivo):
        self.archivo = os.path.join('tableros', nombre_archivo)
        self.tablero_solucion = self.cargar_tablero()
        self.tablero_juego = self.copia_numeros()
        # QUITAR
        print("Tablero Solucion")
        self.imprimir(self.tablero_solucion)
        print("Tablero Juego")
        self.imprimir(self.tablero_juego)

    def cargar_tablero(self):
        """Carga los numeros del tablero del Sudoku de un archivo '.txt'."""
        fila = []
        numeros_tablero = []
        temp = 'lol'
        with open(self.archivo, 'r') as archivo:
            while temp != '':
                temp = archivo.readline()
                for i in range(len(temp)):
                    if temp[i] in '123456789' and temp[i - 1] != '*':
                        fila.append(temp[i])
                    if temp[i] == '*':
                        fila.append(temp[i] + temp[i + 1])
                numeros_tablero.append(fila)
                fila = []
            numeros_tablero.remove(numeros_tablero[9])
            archivo.closed
            return numeros_tablero

    def copia_numeros(self):
        """Crea la matriz a ser utilizada en el juego."""
        for x in range(9):
            for y in range(9):
                if '*' in self.tablero_solucion[x][y] or '#' in self.tablero_solucion[x][y]:
                    self.tablero_juego[x][y] = self.tablero_solucion[x][y]
        return self.tablero_juego

    def dibuja_numero(self, tablero):
        """Dibuja la matriz del juego en pantalla."""
        for x in range(self.modo):
            for y in range(self.modo):
                if self.tablero_juego[x][y] == '0':
                    pass
                elif '*' in self.tablero_juego[x][y]:
                    temp = self.fuente.render(self.tablero_juego[x][y][1], True, self.color)
                    pos_matriz = (y, x)
                    pos_coordenado = celdas_coord(pos_matriz, tablero)
                    # Crea el resaltado en las pistas
                    resaltado = pygame.Surface((tablero.celda, tablero.celda))
                    resaltado.fill(pistas)
                    resaltado.set_alpha(100)
                    fondo.blit(resaltado, pos_coordenado)
                    # Desplazamiento de los numeros
                    pos_coordenado = (pos_coordenado[0]+10, pos_coordenado[1]+5)
                    fondo.blit(temp, pos_coordenado)
                elif self.tablero_juego[x][y] in '123456789':
                    temp = self.fuente.render(self.tablero_juego[x][y], True, self.color)
                    pos = (y, x)
                    pos_coordenado = celdas_coord(pos, tablero)
                    # Desplazamiento de los numeros
                    pos_coordenado = (pos_coordenado[0]+10, pos_coordenado[1]+5)
                    fondo.blit(temp, pos_coordenado)
        pygame.display.update()

    def imprimir(self, mat):
        print ("   "," ".join([str(x) for x in range(len(mat))]))
        print ("_"," ".join(['_' for x in range(len(mat)+1)]))
        for i,x in enumerate(mat):
            print (i,'|'," ".join(x))


class Rectangulo():
    """Rectangulos de PyGame, solo tienen las x,y de la esquina superior izquierda."""

    margen_x = 0
    margen_y = 0


class Imagen(Rectangulo):
    """Variables necesarias para cualquier imagen que se quiera dibujar."""

    ruta = os.path.join('imagenes', 'nueva_partida.png')
    imagen = pygame.image.load(ruta)
    imagen.set_colorkey(negro)

    def indica_ruta(self):
        self.imagen = pygame.image.load(self.ruta)
        self.imagen.convert()
        self.imagen.set_colorkey(blanco)


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

    def renderizar(self):
        """Renderiza el texto, para poder ser mostrado en pantalla."""
        self.renderizado = self.fuente.render(self.texto, self.antialias, self.color)
        return None


class Texto(Boton):
    """Variables para blitear imagenes."""

    fuente = palabras_menu
    antialias = True
    color = negro
    renderizado = None

# ___________________________ Fin Clases _____________________________________#


# _____________________________ Valores iniciales ____________________________#

# #################################################
# Gato trabajador
gato = Imagen()
gato.margen_x = 236
gato.margen_y = 50
gato.ruta = os.path.join('imagenes', 'gato.jpg')
gato.indica_ruta()

# Estamos trabajando
trabajando = Texto()
trabajando.texto = '¿Qué haces por aquí?'
trabajando.fuente = titulos
trabajando.color = negro
trabajando.margen_x = 30
trabajando.margen_y = 500
trabajando.renderizar()
# ###################################################

# Partida
partida = Juego('sudoku.txt')
partida.jugador = ''
partida.fuente = numeros_sudoku
partida.color = negro
partida.modo = 9
#partida.inicial('sudoku.txt')

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
tablero6.margen_x = 150
tablero6.margen_y = 200
tablero6.lineas = 6

# Nombre del jugador
nombre = Texto()
nombre.texto = ''
nombre.fuente = titulos
nombre.color = negro
nombre.margen_x = 230
nombre.margen_y = 250
nombre.renderizar()

# ____________________ INICIO IMAGENES _______________________________________

# Texto de bienvenida
bienvenida = Imagen()
bienvenida.ancho = 520
bienvenida.alto = 100
bienvenida.margen_x = 140
bienvenida.margen_y = 100
bienvenida.ruta = os.path.join('imagenes', 'introduzca_nombre.png')
bienvenida.indica_ruta()
texto = "introduzca_nombre"

# Texto de Elegir Dificultades
elegir_dificultadtxt = Texto()
elegir_dificultadtxt.texto = 'Elegir Dificultad'
elegir_dificultadtxt.fuente = titulos
elegir_dificultadtxt.color = negro
elegir_dificultadtxt.margen_x = 200
elegir_dificultadtxt.margen_y = 10
elegir_dificultadtxt.renderizar()

# Texto de Elegir Tablero
elegir_tablerotxt = Texto()
elegir_tablerotxt.texto = 'Elegir Tablero'
elegir_tablerotxt.fuente = titulos
elegir_tablerotxt.color = negro
elegir_tablerotxt.margen_x = 200
elegir_tablerotxt.margen_y = 10
elegir_tablerotxt.renderizar()

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


# _____________________ Botones de elegir dificultad _________________

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
menu.margen_y = 485
menu.ruta = os.path.join('imagenes', 'menu_principal.png')
menu.indica_ruta()
texto = "Menu"

#_____________________  FIN de Botones de elegir dificultad _________________


#_____________________ Botones para elegir tablero __________________________
# Tablero 6x6
t6x6 = Boton()
t6x6.ancho = 150
t6x6.alto = 30
t6x6.margen_x = 130
t6x6.margen_y = 150
t6x6.ruta = os.path.join('imagenes', '6x6.png')
t6x6.indica_ruta()
texto = "6x6"

#Tablero 9x9
t9x9 = Boton()
t9x9.ancho = 150
t9x9.alto = 30
t9x9.margen_x = 570
t9x9.margen_y = 150
t9x9.ruta = os.path.join('imagenes', '9x9.png')
t9x9.indica_ruta()
texto = "t9x9"

# ____________________ FIN IMAGENES _______________________________________


# _________________________ Inicio de Funciones ______________________________#

# Funcion donde corre el juego del Sudoku
# Carga el tablero
def juego_sudoku(nombre, tablero):
    # Carga los datos del tablero
    nombre = cargar_tablero(nombre)

    # Muestra los numeros en el tablero


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
                elegir_tablero(partida)
                dificultad = False
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
                dificultad = False
            if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
                dificultad = False
            if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
                dificultad = False
            if click[0] == 1 and cajas[4].collidepoint(mouse[0], mouse[1]):
                dificultad = False
                menu_juego(datos_menu[0], datos_menu[1], datos_menu[2], datos_menu[3])

        pygame.display.update()

def elegir_tablero(partida):
    tablero = True
    cajas = [
    pygame.Rect(t6x6.margen_x, t6x6.margen_y, t6x6.ancho, t6x6.alto),
    pygame.Rect(t9x9.margen_x, t9x9.margen_y, t9x9.ancho, t9x9.alto),
    ]

    while tablero:

        # Dibuja los botones del menu
        fondo.blit(imagen_fondo, (0, 0))
        fondo.blit(elegir_tablerotxt.renderizado, (elegir_tablerotxt.margen_x, elegir_tablerotxt.margen_y))
        dibuja_boton(t6x6)
        dibuja_boton(t9x9)

        for event in pygame.event.get():
            # Variables a verificar
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            # Sale del juego
            if event.type == pygame.QUIT:
                cerrar()
            # Reacciona si se pasa por encima de la opcion (FALTAN IMG HOVER)
            if cajas[0].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, (azul), (t6x6.margen_x, t6x6.margen_y, t6x6.ancho, t6x6.alto))
            if cajas[1].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (t9x9.margen_x, t9x9.margen_y, t9x9.ancho, t9x9.alto))
            # Acciona si le dan click a cualquier botón
            if click[0] == 1 and cajas[0].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                main(tablero6)
                tablero = False
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                main(tablero9)
                tablero = False
        pygame.display.update()



# Crea los botones del menu
def dibuja_boton(opcion):
    """Funcion que dibuja los botones del menu"""
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
                dibuja_tablero(tablero9, negro, imagen_fondo, sudoku)
                menu = False
            if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
                menu = False
            if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
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
    if tablero.lineas == 9:
        for i in range(0, 400, (3 * tablero.celda)):
            # Horizontales
            pygame.draw.line(fondo, color,
                            (i + tablero.margen_x, tablero.margen_y),
                            (i + tablero.margen_x, 360 + tablero.margen_y), 3)
            # Verticales
            pygame.draw.line(fondo, color,
                    (tablero.margen_x, i + tablero.margen_y),
                    (tablero.ancho + tablero.margen_x, i + tablero.margen_y), 3)
    elif tablero.lineas == 6:
        # Horizontales
        for i in range(0, 400, (3 * tablero.celda)):
            pygame.draw.line(fondo, color,
                            (i + tablero.margen_x, tablero.margen_y),
                            (i + tablero.margen_x, 360 + tablero.margen_y), 3)
            # Verticales
        for i in range(0, 400, (2 * tablero.celda)):
            pygame.draw.line(fondo, color,
                    (tablero.margen_x, i + tablero.margen_y),
                    (tablero.ancho + tablero.margen_x, i + tablero.margen_y), 3)

    return


# mousex, mousey = pygame.mouse.get_pos() necesario para que funcione
def celdas_coord(pos, tablero):
    """Pasa del sistema del juego al sistema coordenado celdas."""
    izquierda = (pos[0] * tablero.celda) + tablero.margen_x
    arriba = (pos[1] * tablero.celda) + tablero.margen_y
    return (izquierda, arriba)


# mousex, mousey = pygame.mouse.get_pos() Necesario para que funcione
def coord_celdas(mouse, tablero):
    """Pasa del sistema coordenado celdas, al sistema coordenado del juego."""
    for x in range(9):
        for y in range(9):
            pos = (x, y)
            izquierda, arriba = celdas_coord(pos, tablero)
            caja = pygame.Rect(izquierda, arriba, tablero.celda, tablero.celda)
            if caja.collidepoint(mouse[0], mouse[1]):
                return (x, y)
    return (None, None)


def cerrar():
    """Cierra el programa."""
    pygame.quit()
    sys.exit()


# Permite el ingreso de texto
def input_texto(nombre, titulo):
    """Permite el ingreso de texto desde el GUI"""
    ingreso = True
    # Crea el fondo
    fondo.blit(imagen_fondo, (0, 0))
    dibuja_boton(bienvenida)
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
        dibuja_boton(bienvenida)
        nombre.renderizar()
        fondo.blit(nombre.renderizado, (nombre.margen_x, nombre.margen_y))
        pygame.display.update()


# Guarda la partida
def guardar_partida(nombre, numeros_tablero):
    """Guarda los numeros del tablero del Sudoku de un archivo '.txt'."""
    with open(nombre + ".txt", 'w') as archivo:
        for linea in numeros_tablero:
            archivo.write(linea)
    archivo.closed

# Donde se corre el juego ahora si si si
def main(tablero):
    global partida, negro, imagen_fondo, sudoku, fps

    # INICIAL
    # Se limpia la pantalla (queda: fondo blanco, titulo)
    actualiza_pantalla_juego(tablero)
    pygame.display.update()
    # Crea el reloj
    reloj = pygame.time.Clock()
    contador = 0
    reloj_contador = [0, 0]

   # Ciclo principal
    while True:
        for evento in pygame.event.get():
            # Variables a verificar
            if evento.type == QUIT:
                cerrar()
            if evento.type == MOUSEBUTTONUP:
                mouse = pygame.mouse.get_pos()
                mouse_celdas = coord_celdas(mouse, tablero)
                if mouse_celdas[0] != None:
                    if len(partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]]) == 1:
                        print(mouse_celdas)
                        mouse = celdas_coord(mouse_celdas, tablero)
                        # Resalta la celda seleccionada
                        resaltado = pygame.Surface((tablero.celda, tablero.celda))
                        resaltado.fill(azul)
                        resaltado.set_alpha(150)
                        fondo.blit(resaltado, mouse)
                        # Resalta la fila y la columna de la celda selecionada
                        # Filas
                        pygame.draw.line(fondo, rojo,
                            (tablero.margen_x + 2, mouse[1]),
                            (tablero.margen_x + tablero.ancho - 2, mouse[1]), 2)
                        pygame.draw.line(fondo, rojo,
                            (tablero.margen_x + 2, mouse[1] + tablero.celda),
                            (tablero.margen_x + tablero.ancho - 2, mouse[1] + tablero.celda), 2)
                        # Columnas
                        pygame.draw.line(fondo, rojo,
                            (mouse[0], tablero.margen_y + 2),
                            (mouse[0], tablero.ancho + tablero.margen_y - 2), 2)
                        pygame.draw.line(fondo, rojo,
                            (mouse[0] + tablero.celda, tablero.margen_y + 2),
                            (mouse[0] + tablero.celda, tablero.ancho + tablero.margen_y - 2), 2)
                        # Actualiza la pantalla
                        pygame.display.update((tablero.margen_x, tablero.margen_y, tablero.ancho, tablero.ancho))
                        introduce_numero(tablero, mouse_celdas)
                else:
                    print('mamalo mucho')# Quitar
                    pass
                    pygame.display.update()
        contador += reloj.tick() / 1000
        contador = tiempo_juego(reloj_contador, contador)
        # Se actualiza la pantalla (queda: fondo blanco, titulo)
        # Dibujar numero cambiado
        #partida.dibuja_numero(tablero)
        dibuja_tablero(tablero, negro, imagen_fondo, sudoku)
        pygame.display.update((tablero.margen_x, tablero.margen_y, tablero.ancho, tablero.ancho))

def tiempo_juego(reloj, contador):
    reloj[1] += contador
    if reloj[1] > 59:
        reloj[0] += 1
        reloj[1] -= 59
    contador = 0
    partida.tiempo = reloj
    return contador



def introduce_numero(tablero, mouse_celdas):
    ciclo = True
    while ciclo:
        for evento in pygame.event.get():
            if evento.type == QUIT:
                cerrar()
            if evento.type == KEYDOWN:
                if evento.unicode.isnumeric() and evento.unicode != '0':
                    if evento.unicode == partida.tablero_solucion[mouse_celdas[1]][mouse_celdas[0]]:
                        partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] = evento.unicode
                        actualiza_pantalla_juego(tablero)
                        ciclo = False
                    else:
                        print('TE EQUIVOCASTE MENOR!')
                        actualiza_pantalla_juego(tablero)
                        ciclo = False
                if evento.unicode == '\r':
                    actualiza_pantalla_juego(tablero)
                    ciclo = False
                if evento.unicode == '\x08':
                    partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] = '0'
                    actualiza_pantalla_juego(tablero)
                    ciclo = False
        pygame.display.update((tablero.margen_x-5, tablero.margen_y-5, tablero.ancho+10, tablero.ancho+10))

def actualiza_pantalla_juego(tablero):
    global fondo, imagen_fondo, sudoku, negro
    # Muestra el fondo, titulo, tablero y numeros del Sudoku
    limpia_pantalla(fondo, imagen_fondo, sudoku)
    partida.dibuja_numero(tablero)
    dibuja_tablero(tablero, negro, imagen_fondo, sudoku)
    # Muestra el nombre del jugador
    nombre = numeros.render('Jugador: ' + partida.jugador, True, negro)
    fondo.blit(nombre, (600, 200))
    # Muestra el tiempo de la partida
    tiempo = numeros.render('Tiempo: {0:0>2.0f}:{1:0>2.0f}'.format(partida.tiempo[0], partida.tiempo[1]), True, negro)
    fondo.blit(tiempo, (600, 230))
    #Lista de rectangulos a actualizar en pantalla
    #lista = (nombre + tiempo)
    pygame.display.update()




# ########################################################
def lindo_gatito(gato, imagen_fondo, trabajando):
    """Dibuja un lindo gatito."""
    fondo.blit(imagen_fondo, (0, 0))
    fondo.blit(gato.imagen, (gato.margen_x, gato.margen_y))
    fondo.blit(trabajando.renderizado, (trabajando.margen_x, trabajando.margen_y))

    pygame.display.update()
######################################################


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
partida.jugador = nombre.texto
menu_juego(fondo, blanco, azul, sudoku)
# Dibuja el tablero

    # PROCESAMIENTO DE EVENTOS DEBAJO DE ESTA LINEA

    # PROCESAMIENTO DE EVENTOS ENCIMA DE ESTA LINEA

    # LOGICA DEL JUEGO DEBAJO DE ESTA LINEA

    # LOGICA DEL JUEGO ENCIMA DE ESTA LINEA

    # DIBUJO DE LA NUEVA PANTALLA

    # Se actualiza todo lo hecho en el codigo
pygame.display.update()
    # Limitamos los FPS
