u""".

Descripción: Juego de un Sudoku con una GUI, que permite al usuario utilizar el
programa (juego) donde posee un primer paso para introducir su nombre, luego un
menú en el cual se le presentan varias opciones el juego del Sudoku como tal con
varios niveles de dificultad, una tabla con las mejores puntuaciones.

    1- Introducir Nombre
    2- Opciones en el menú:
        2.1- Partida nueva
        2.2- Cargar partida ya existente
        2.3- Mostrar la tabla de records
        2.4- Mostrar la ayuda
        2.5- Salir del juego
    3- Dificultada del juego:
        3.1- Entrenamiento
        3.2- Fácil
        3.3- Difícil
        3.4- Muy Difícil
    4- Elegir partida (seleccionar tablero):
        4.1- Cargar tablero
        4.2- Elegir archivo solución
    5- Tablero con tiempo, puntaje y opción de salir y guardar
    6- Records muestra el puntaje de los jugadores por cada nivel
    7- Ayuda presenta las reglas del juego y el como jugarlo

    Al iniciar la partida, debe se debe visualizar el tiempo y el puntaje

    Nivel Entrenamiento:
        Tablero 6x6 o 9x9
        Solo el tiempo sin puntaje

Autores:
    Mariano Rodríguez 12-10892
    Pablo Gonzalez 13-10575

Última modificación:
        28/03/2016
"""

# Librerias
import sys
import datetime
import os.path
import random
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
titulos = pygame.font.SysFont("monospace", 40, italic=True)
palabras_menu = pygame.font.SysFont("monospace", 17)
numeros_sudoku = pygame.font.SysFont("monospace", 30, bold=True)
error_txt = pygame.font.SysFont("monospace", 50, bold=True)
ayuda_txt = pygame.font.SysFont("monospace", 20, bold=True)
numeros = pygame.font.SysFont("fuentes/numeros.ttf", 30)
nombre_victoria = pygame.font.SysFont("monospace", 50, bold=True)

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
# Contador de veces que pasas un score en especifico
cont = 1
# Dummy del puntaje
pto = 0
# ______________________________ Clases ______________________________________#


class Juego():
    """Donde se corre el juego."""

    modo = 0
    ruta = ''
    color = negro
    tiempo = [0, 0]
    puntaje = 0
    nayuda = 0
    errores = 0
    jugador = ''
    nivel = 0
    niveles = [0, 0, 0, 0]
    archivo = os.path.join('tableros', '')
    dificultad = 0
    fuente = palabras_menu
    tablero_solucion = []
    tablero_juego = []
    fuente = ''


class Rectangulo():
    """Rectangulos de PyGame."""

    margen_x = 0
    margen_y = 0


class Imagen(Rectangulo):
    """Variables necesarias para cualquier imagen que se quiera dibujar."""

    ruta = os.path.join('imagenes', 'nueva_partida.png')
    imagen = pygame.image.load(ruta)
    imagen.set_colorkey(negro)

    def indica_ruta(self):
        """Indica la ruta del archivo."""
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
        self.renderizado = self.fuente.render(self.texto, self.antialias,
                                                self.color)
        return None


class Texto(Boton):
    """Variables para blitear imagenes."""

    fuente = palabras_menu
    antialias = True
    color = negro
    renderizado = None


class Records():
    """Records."""

    nombres = []
    puntajes = []
    level = ''


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

# Elija las casillas para la solucion
eleccion_casilla = Texto()
eleccion_casilla.texto = 'Elija casillas para la solución'
eleccion_casilla.fuente = titulos
eleccion_casilla.color = negro
eleccion_casilla.margen_x = 30
eleccion_casilla.margen_y = 500
eleccion_casilla.renderizar()
# ###################################################

# Partida
partida = Juego()
partida.modo = 0
partida.ruta = ''
partida.color = negro
partida.tiempo = [0, 0]
partida.puntaje = 0
partida.errores = 0
partida.nayuda = 0
partida.jugadas = 0
partida.jugador = ''
partida.nivel = ''
partida.niveles = 'e'
partida.archivo = ''
partida.fuente = numeros_sudoku
partida.tablero_solucion = []
partida.tablero_juego = [['0'for x in range(partida.modo)]
                         for y in range(partida.modo)]

# Puntaje_alto
puntaje_alto = Records()
puntaje_alto.nombres = []
puntaje_alto.puntajes = []
puntaje_alto.level = ''

# Tablero 9x9
tablero9 = Tablero()
tablero9.ancho = 360
tablero9.alto = tablero9.ancho
tablero9.celda = int(tablero9.ancho / 9)
tablero9.margen_x = 200
tablero9.margen_y = 190
tablero9.lineas = 9
tablero9.fuente = pygame.font.SysFont("monospace", 30, bold=True)

# Tablero 6x6
tablero6 = Tablero()
tablero6.ancho = 360
tablero6.alto = tablero6.ancho
tablero6.celda = int(tablero6.ancho / 6)
tablero6.margen_x = 200
tablero6.margen_y = 190
tablero6.lineas = 6
tablero6.fuente = pygame.font.SysFont("monospace", 40, bold=True)

# Nombre del jugador
nombre = Texto()
nombre.texto = ''
nombre.fuente = titulos
nombre.color = negro
nombre.margen_x = 230
nombre.margen_y = 250
nombre.renderizar()

# Records
puntaje_alto = Records()


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

# Texto de Elegir Tablero
error = Texto()
error.texto = '¡ERROR!'
error.fuente = error_txt
error.color = negro
error.margen_x = 570
error.margen_y = 400
error.renderizar()

# Texto de Maximo de ayuda
max_ayuda = Texto()
max_ayuda.texto = '¡Ayudas\n agotadas! :('
max_ayuda.fuente = ayuda_txt
max_ayuda.color = negro
max_ayuda.margen_x = 570
max_ayuda.margen_y = 400
max_ayuda.renderizar()

# Texto de No Ayuda
no_ayuda = Texto()
no_ayuda.texto = ('Accion no permitida')
no_ayuda.fuente = ayuda_txt
no_ayuda.color = negro
no_ayuda.margen_x = 570
no_ayuda.margen_y = 400
no_ayuda.renderizar()

# Titulo 'Sudoku'
sudoku = Imagen()
sudoku.margen_x = 150
sudoku.margen_y = 10
sudoku.ruta = os.path.join('imagenes', 'sudoku.png')
sudoku.indica_ruta()

# Titulo '¡Victoria!'
victoria = Imagen()
victoria.margen_x = 90
victoria.margen_y = 200
victoria.ruta = os.path.join('imagenes', 'victoria.png')
victoria.indica_ruta()

# Texto completo de las reglas
reglas = Imagen()
reglas.margen_x = 0
reglas.margen_y = 0
reglas.ruta = os.path.join('imagenes', 'ayuda_reglas.png')
reglas.indica_ruta()

# Titulo 'Has perdido'
derrota = Imagen()
derrota.margen_x = 90
derrota.margen_y = 230
derrota.ruta = os.path.join('imagenes', 'derrota.png')
derrota.indica_ruta()

# Texto de Cargar partida
nombre_del_archivo = Boton()
nombre_del_archivo.ancho = 150
nombre_del_archivo.alto = 30
nombre_del_archivo.margen_x = 140
nombre_del_archivo.margen_y = 100
nombre_del_archivo.ruta = os.path.join('imagenes', 'nombre_del_archivo.png')
nombre_del_archivo.indica_ruta()
texto = "Nombre del Archivo: "

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

# Boton de Elegir Dificultades
elegir_dificultadtxt = Boton()
elegir_dificultadtxt.ancho = 260
elegir_dificultadtxt.alto = 30
elegir_dificultadtxt.margen_x = 160
elegir_dificultadtxt.margen_y = 60
elegir_dificultadtxt.ruta = os.path.join('imagenes', 'elegir_dificultad.png')
elegir_dificultadtxt.indica_ruta()
texto = "Entrenamiento"


# Entrenamiento
entrenamiento = Boton()
entrenamiento.ancho = 260
entrenamiento.alto = 30
entrenamiento.margen_x = 280
entrenamiento.margen_y = 185
entrenamiento.ruta = os.path.join('imagenes', 'entrenamiento.png')
entrenamiento.indica_ruta()
texto = "Entrenamiento"

# Facil
facil = Boton()
facil.ancho = 150
facil.alto = 30
facil.margen_x = 280
facil.margen_y = 260
facil.ruta = os.path.join('imagenes', 'facil.png')
facil.indica_ruta()
texto = "Facil"

# Dificil
dificil = Boton()
dificil.ancho = 150
dificil.alto = 30
dificil.margen_x = 280
dificil.margen_y = 335
dificil.ruta = os.path.join('imagenes', 'dificil.png')
dificil.indica_ruta()
texto = "Dificil"

# Extremo
extremo = Boton()
extremo.ancho = 150
extremo.alto = 30
extremo.margen_x = 280
extremo.margen_y = 410
extremo.ruta = os.path.join('imagenes', 'extremo.png')
extremo.indica_ruta()
texto = "Extremo"

# Menu: Si, volvemos al menu principal.
menu = Boton()
menu.ancho = 150
menu.alto = 30
menu.margen_x = 280
menu.margen_y = 485
menu.ruta = os.path.join('imagenes', 'menu_principal.png')
menu.indica_ruta()
texto = "Menu"

# _____________________  FIN de Botones de elegir dificultad _________________


# _____________________ Botones para elegir tablero __________________________

# Boton de Elegir Tablero
elegir_tablerotxt = Boton()
elegir_tablerotxt.ancho = 260
elegir_tablerotxt.alto = 30
elegir_tablerotxt.margen_x = 160
elegir_tablerotxt.margen_y = 60
elegir_tablerotxt.ruta = os.path.join('imagenes', 'elegir_tablero.png')
elegir_tablerotxt.indica_ruta()
texto = "Entrenamiento"

# Tablero 6x6
t6x6 = Boton()
t6x6.ancho = 100
t6x6.alto = 30
t6x6.margen_x = 130
t6x6.margen_y = 250
t6x6.ruta = os.path.join('imagenes', '6x6.png')
t6x6.indica_ruta()
texto = "6x6"

# Tablero 9x9
t9x9 = Boton()
t9x9.ancho = 105
t9x9.alto = 30
t9x9.margen_x = 570
t9x9.margen_y = 250
t9x9.ruta = os.path.join('imagenes', '9x9.png')
t9x9.indica_ruta()
texto = "t9x9"
# _______________________ FIN  de Botones para elegir tablero _________________

# _____________________ Botones para el juego principal ____________________

# Verificar Sudoku
verificar_sudoku = Boton()
verificar_sudoku.ancho = 130
verificar_sudoku.alto = 30
verificar_sudoku.margen_x = 30
verificar_sudoku.margen_y = 175
verificar_sudoku.ruta = os.path.join('imagenes', 'verificar_sudoku.png')
verificar_sudoku.indica_ruta()
texto = "Verificar Sudoku"

# Solucion
solucion = Boton()
solucion.ancho = 130
solucion.alto = 30
solucion.margen_x = 10
solucion.margen_y = 185
solucion.ruta = os.path.join('imagenes', 'solucion.png')
solucion.indica_ruta()
texto = "Solucion"

# Menu Principal
menu_main = Boton()
menu_main.ancho = 150
menu_main.alto = 30
menu_main.margen_x = 20
menu_main.margen_y = 285
menu_main.ruta = os.path.join('imagenes', 'volver.png')
menu_main.indica_ruta()
texto = "Menu"

# Salir
salir_main = Boton()
salir_main.ancho = 150
salir_main.alto = 30
salir_main.margen_x = 10
salir_main.margen_y = 385
salir_main.ruta = os.path.join('imagenes', 'salir.png')
salir_main.indica_ruta()
texto = "Salir"

# ___________________________  FIN de Botones Juego Principal_________________#

# ___________________________ Botones de Victoria _____________________________#

# Salir
salir_victoria = Boton()
salir_victoria.ancho = 150
salir_victoria.alto = 30
salir_victoria.margen_x = 500
salir_victoria.margen_y = 450
salir_victoria.ruta = os.path.join('imagenes', 'salir.png')
salir_victoria.indica_ruta()
texto = "Salir"

# Menu Principal
volver_menu = Boton()
volver_menu.ancho = 150
volver_menu.alto = 30
volver_menu.margen_x = 100
volver_menu.margen_y = 450
volver_menu.ruta = os.path.join('imagenes', 'volver_menu.png')
volver_menu.indica_ruta()
texto = "Menu"

# ________________________ FIN Botones de Victoria ___________________________#

# ________________________ Botones de Preguntar _______________________________#

# Si
si = Boton()
si.ancho = 150
si.alto = 30
si.margen_x = 150
si.margen_y = 450
si.ruta = os.path.join('imagenes', 'si.png')
si.indica_ruta()
texto = "Si"

# No
no = Boton()
no.ancho = 150
no.alto = 30
no.margen_x = 530
no.margen_y = 450
no.ruta = os.path.join('imagenes', 'no.png')
no.indica_ruta()
texto = "No"

# _________________________ Inicio de Funciones ______________________________#
"""
# Elige la carpeta para el guardado del record
def records_elige_nivel(puntaje_alto, partida):
    Define el nivel que se acaba de jugar para cargar el record.
    if partida.nivel == 'e':
        puntaje_alto.level = 'entrenamiento.txt'
    if partida.nivel == 'f':
        puntaje_alto.level = 'facil.txt'
    if partida.nivel == 'p':
        puntaje_alto.level = 'dificil.txt'
    if partida.nivel == 'x':
        puntaje_alto.level = 'extremo.txt'

# Abre la carpeta de los records
def records_cargar(puntaje_alto):
    '''Carga los datos.'''
    with open(os.path.join('records', puntaje_alto.level), 'r') as f:
        archivo = f.readlines()
        for x in range(0, len(archivo), 2):
            puntaje_alto.nombres += archivo[x]
            puntaje_alto.puntajes += archivo[x + 1]
    f.closed

# Agreg el puntaje actual a los records
def records_agregar(puntaje_alto, puntaje_actual):
    u'''Elimina el puntaje más bajo, por el nuevo más alto.'''
    for x in range(len(puntaje_alto.puntajes)):
        temp = puntaje_alto.puntajes[x]
        if puntaje_actual <= int(temp):
            pass
        elif puntaje_actual > int(temp):
            puntaje_alto.puntajes[len(puntaje_alto.puntajes) - 1]=puntaje_actual
            break

# Ordena los records
def records_ordenar(puntaje_alto):
    Ordena la lista.
    ordenado = False
    while not ordenado:
        ordenado = True
        for x in range(len(puntaje_alto.puntajes) - 1):
            if int(puntaje_alto.puntajes[x + 1])>int(puntaje_alto.puntajes[x]):
                ordenado = False
                puntaje_alto.puntajes[x + 1], puntaje_alto.puntajes[x] = \
                puntaje_alto.puntajes[x], puntaje_alto.puntajes[x + 1]

# Guarda los records nuevos
def records_guardar(puntaje_alto):
    '''Guarda los puntajes en un archivo '.txt'.'''
    with open(os.path.join('records', puntaje_alto.level), 'w') as f:
        for x in range(len(puntaje_alto.puntajes)):
            f.write(puntaje_alto.nombres)
            f.write('\n')
            f.write(puntaje_alto.puntajes)
            f.write('\n')
            f.write(puntaje_alto.level)
            f.write('\n')

# Compara el puntaje de la partida con los guardados anteriormente
def records_posicionar(puntaje_alto, puntaje_actual):
    '''Compara el puntaje de la partida con los guardados.'''
    for x in range(len(puntaje_alto.puntajes)):
        if puntaje_alto.puntajes == puntaje_actual:
            return x
        else:
            return ("Esta por debajo de {}".format(len(puntaje_alto.puntajes)))
"""
# Imprime  en el terminal por motivos de verificacion
def imprimir(mat):
    """Impresion bonita de matrices."""
    print ("   ", " ".join([str(x) for x in range(len(mat))]))
    print ("_", " ".join(['_' for x in range(len(mat) + 1)]))
    for i, x in enumerate(mat):
        print (i, '|', " ".join(x))

# Define el tablero 6x6 ó 9x9
def definicion_tablero(partida):
    """Dibuja el tablero."""
    if partida.modo == 9:
        partida.ruta = 'tableros/9x9/'
        # Elige un archivo txt solución al azar
        partida.archivo = random.choice(os.listdir(partida.ruta))
        # Define la matriz solución
        partida.tablero_solucion = cargar_tablero(partida)
        # Define la matriz de juego
        partida.tablero_juego = copia_numeros(partida)
        # Imprime en el terminal para verificacion
        print("Tablero Solucion")
        imprimir(partida.tablero_solucion)
        print("Tablero Juego")
        imprimir(partida.tablero_juego)
    if partida.modo == 6:
        partida.ruta = 'tableros/6x6/'
        partida.archivo = random.choice(os.listdir(partida.ruta))
        partida.tablero_solucion = cargar_tablero(partida)
        partida.tablero_juego = copia_numeros(partida)
        # Imprime en el terminal para verificacion
        print("Tablero Solucion")
        imprimir(partida.tablero_solucion)
        print("Tablero Juego")
        imprimir(partida.tablero_juego)


# Hace la matriz Solucion
def cargar_tablero(partida):
    """Carga los numeros del tablero del Sudoku de un archivo '.txt'."""
    # Inicio del arreglo
    fila = []
    # Inicio del arreglo
    numeros_tablero = []
    # Inicio del string
    temp = 'lol'
    with open(partida.ruta + partida.archivo, 'r') as f:
        while temp != '':
            temp = f.readline()
            for i in range(len(temp)):
                if temp[i] in '123456789' and temp[i - 1] != '*':
                    fila.append(temp[i])
                if temp[i] == '*':
                    fila.append(temp[i] + temp[i + 1])
            numeros_tablero.append(fila)
            fila = []
        numeros_tablero.remove(numeros_tablero[partida.modo])
        f.closed
        return numeros_tablero


# Crea la matriz donde se realiza el Juego
def copia_numeros(partida):
    """Crea la matriz a ser utilizada en el juego."""
    # Inicio de la matriz juego
    partida.tablero_juego = [['0'for x in range(partida.modo)]
                                for y in range(partida.modo)]
    for x in range(partida.modo):
        for y in range(partida.modo):
            if '*' in partida.tablero_solucion[x][y] or '#' in partida.tablero_solucion[x][y]:
                partida.tablero_juego[x][y] = partida.tablero_solucion[x][y]
    return partida.tablero_juego

# Dibuja la matriz Juego donde se desarrolla el juego
def dibuja_numero(tablero, partida):
    """Dibuja la matriz del juego en pantalla."""
    for x in range(partida.modo):
        for y in range(partida.modo):
            if partida.tablero_juego[x][y] == '0':
                pass
            elif '*' in partida.tablero_juego[x][y]:
                temp = tablero.fuente.render(partida.tablero_juego[x][y][1], True, partida.color)
                pos_matriz = (y, x)
                pos_coordenado = celdas_coord(pos_matriz, tablero)
                # Crea el resaltado en las pistas
                resaltado = pygame.Surface((tablero.celda, tablero.celda))
                resaltado.fill(pistas)
                resaltado.set_alpha(100)
                fondo.blit(resaltado, pos_coordenado)
                # Desplazamiento de los numeros
                pos_coordenado = (pos_coordenado[0] + 10, pos_coordenado[1] + 5)
                fondo.blit(temp, pos_coordenado)
            elif partida.tablero_juego[x][y] in '123456789':
                temp = tablero.fuente.render(partida.tablero_juego[x][y], True,
                                                 partida.color)
                pos = (y, x)
                pos_coordenado = celdas_coord(pos, tablero)
                # Desplazamiento de los numeros
                pos_coordenado = (pos_coordenado[0] + 10, pos_coordenado[1] + 5)
                fondo.blit(temp, pos_coordenado)
    pygame.display.update(tablero.margen_x - 5, tablero.margen_y - 5,
                            tablero.ancho + 10, tablero.ancho+10)

# Funcion para elegir dificultades
def elegir_dificultad(datos_menu,partida):
    dificultad = True
    global menu
    cajas = [
    pygame.Rect(entrenamiento.margen_x, entrenamiento.margen_y, entrenamiento.ancho, entrenamiento.alto),
    pygame.Rect(facil.margen_x + 90, facil.margen_y, facil.ancho - 60, facil.alto),
    pygame.Rect(dificil.margen_x + 80, dificil.margen_y, dificil.ancho - 30, dificil.alto),
    pygame.Rect(extremo.margen_x + 60, extremo.margen_y, extremo.ancho, extremo.alto),
    pygame.Rect(menu.margen_x, menu.margen_y, menu.ancho + 80, menu.alto)
        ]

    while dificultad:

        # Dibuja los botones del menu
        fondo.blit(imagen_fondo, (0, 0))
        dibuja_boton(elegir_dificultadtxt)
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
            if cajas[1].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (facil.margen_x + 90, facil.margen_y, facil.ancho - 60, facil.alto))
            if cajas[2].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (dificil.margen_x + 80, dificil.margen_y, dificil.ancho - 30, dificil.alto))
            if cajas[3].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (extremo.margen_x + 60, extremo.margen_y, extremo.ancho, extremo.alto))
            if cajas[4].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (menu.margen_x, menu.margen_y, menu.ancho + 80, menu.alto))

            if click[0] == 1 and cajas[0].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                partida.nivel = 'e'
                partida.puntaje = 0
                partida.nayuda = 0
                partida.errores = 0
                elegir_tablero(partida)
                dificultad = False
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                partida.nivel = 'f'
                partida.puntaje = 0
                partida.modo = 6
                partida.nayuda = 0
                partida.errores = 0
                definicion_tablero(partida)
                main(tablero6)
                dificultad = False
            if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                if partida.niveles > 'e':
                    partida.nivel = 'p'
                    partida.puntaje = 0
                    partida.modo = 9
                    partida.nayuda = 0
                    partida.errores = 0
                    definicion_tablero(partida)
                    main(tablero9)
                    dificultad = False
                elif partida.niveles <= 'e':
                    pass
            if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
                if partida.niveles > 'f':
                    click_sonido.play()
                    partida.nivel = 'x'
                    partida.puntaje = 0
                    partida.modo = 9
                    partida.nayuda = 0
                    partida.errores = 0
                    definicion_tablero(partida)
                    main(tablero9)
                    dificultad = False
                elif partida.niveles <= 'f':
                    pass
            if click[0] == 1 and cajas[4].collidepoint(mouse[0], mouse[1]):
                dificultad = False
                menu_juego(datos_menu[0], datos_menu[1], datos_menu[2], datos_menu[3])

        pygame.display.update()

# Elegir estilo 6x6 o 9x9
def elegir_tablero(partida):
    tableros = True
    cajas = [
    pygame.Rect(t6x6.margen_x, t6x6.margen_y, t6x6.ancho, t6x6.alto),
    pygame.Rect(t9x9.margen_x, t9x9.margen_y, t9x9.ancho, t9x9.alto),
    ]

    while tableros:

        # Dibuja los botones del menu
        fondo.blit(imagen_fondo, (0, 0))
        dibuja_boton(elegir_tablerotxt)
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
                partida.modo = 6
                definicion_tablero(partida)
                main(tablero6)
                tableros = False
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                partida.modo = 9
                definicion_tablero(partida)
                main(tablero9)
                tableros = False
        pygame.display.update()

# Crea los botones
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
    pygame.Rect(ayuda.margen_x + 40, ayuda.margen_y - 5, ayuda.ancho - 50, ayuda.alto),
    pygame.Rect(salir.margen_x + 30, salir.margen_y, salir.ancho, salir.alto - 5)
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
            if cajas[1].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (cargar_partida.margen_x, cargar_partida.margen_y, cargar_partida.ancho, cargar_partida.alto))
            if cajas[2].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (records.margen_x, records.margen_y, records.ancho, records.alto))
            if cajas[3].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (ayuda.margen_x + 40, ayuda.margen_y - 5, ayuda.ancho - 50, ayuda.alto))
            if cajas[4].collidepoint(mouse[0], mouse[1]):
                pygame.draw.rect(fondo, azul, (salir.margen_x + 40, salir.margen_y, salir.ancho - 50, salir.alto))

            if click[0] == 1 and cajas[0].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                partida.tiempo = [0, 0]
                menu = elegir_dificultad(datos_menu, partida)
            if click[0] == 1 and cajas[1].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                cargar_archivo(partida)
                if partida.modo == 6:
                    main(tablero6)
                if partida.modo == 9:
                    main(tablero9)
            if click[0] == 1 and cajas[2].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                lindo_gatito(gato, imagen_fondo, trabajando)
                menu = False
            if click[0] == 1 and cajas[3].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                ayuda_reglas()
                menu = False
            if click[0] == 1 and cajas[4].collidepoint(mouse[0], mouse[1]):
                click_sonido.play()
                cerrar()

        pygame.display.update()

# Limpia la pantalla
def limpia_pantalla(fondo, imagen_fondo, sudoku):
    """Limpia de la pantalla todos los graficos que ya no son necesarios."""
    # Pone el fondo
    fondo.blit(imagen_fondo, (0, 0))
    # Crea el titulo 'Sudoku'
    fondo.blit(sudoku.imagen, (sudoku.margen_x, sudoku.margen_y))

# Dibuja el tablero
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

# mousex, mousey = pygame.mouse.get_pos() necesario para que funcione
def celdas_coord(pos, tablero):
    """Pasa del sistema del juego al sistema coordenado celdas."""
    izquierda = (pos[0] * tablero.celda) + tablero.margen_x
    arriba = (pos[1] * tablero.celda) + tablero.margen_y
    return (izquierda, arriba)

# mousex, mousey = pygame.mouse.get_pos() Necesario para que funcione
def coord_celdas(mouse, tablero):
    """Pasa del sistema coordenado celdas, al sistema coordenado del juego."""
    global partida
    for x in range(partida.modo):
        for y in range(partida.modo):
            pos = (x, y)
            izquierda, arriba = celdas_coord(pos, tablero)
            caja = pygame.Rect(izquierda, arriba, tablero.celda, tablero.celda)
            if caja.collidepoint(mouse[0], mouse[1]):
                return (x, y)
    return (None, None)

# Pregunta si quiere guardar
def ask_guardar(partida):
    ask = True
    fondo.blit(imagen_fondo, (0, 0))
    question = titulos.render('¿Desea guardar antes de salir?', True, negro)
    fondo.blit(question, (50, 170))
    cajas = [
    pygame.Rect(si.margen_x, si.margen_y, si.ancho, si.alto),
    pygame.Rect(no.margen_x, no.margen_y, no.ancho, no.alto)
    ]
    dibuja_boton(si)
    dibuja_boton(no)
    pygame.display.update()
    while ask:
        dibuja_boton(si)
        dibuja_boton(no)
        mouse = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                cerrar()
            if evento.type == MOUSEBUTTONUP:
                if cajas[0].collidepoint(mouse[0], mouse[1]):
                    guardar_partida(partida)
                    cerrar()
                if cajas[1].collidepoint(mouse[0], mouse[1]):
                    cerrar()
        pygame.display.update()

# Cierra el juego
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
    # Asigna el nombre del jugador
    partida.jugador = nombre.texto

# Guarda la partida
def guardar_partida(partida):
    fecha = datetime.datetime.now()
    i = 0
    p_guardada = 'partida' + str(i) + '_' + fecha.strftime('%d') + fecha.strftime('%m') + fecha.strftime('%y') + '.txt'
    existe = os.path.exists('partidas/' + p_guardada)
    while existe == True:
        i += 1
        p_guardada = 'partida' + str(i) + '_' + fecha.strftime('%d') + fecha.strftime('%m') + fecha.strftime('%y') + '.txt'
        existe = os.path.exists('partidas/'+ p_guardada)
    with open('partidas/' + p_guardada, 'w') as archivo:
        archivo.write(str(partida.modo))
        archivo.write('\n')
        for i in range(partida.modo):
            for j in range(partida.modo):
                archivo.write(partida.tablero_juego[i][j])
            archivo.write('\n')
        archivo.write(partida.jugador)
        archivo.write('\n')
        archivo.write(str(partida.nivel))
        archivo.write('\n')
        archivo.write(str(partida.niveles))
        archivo.write('\n')
        archivo.write(str(partida.puntaje))
        archivo.write('\n')
        archivo.write(str(partida.tiempo[0]))
        archivo.write('\n')
        archivo.write(str(partida.tiempo[1]))
        archivo.write('\n')
        archivo.write(str(partida.errores))
        archivo.write('\n')
        archivo.write(str(partida.nayuda))
        archivo.write('\n')
        archivo.write(str(partida.jugadas))
        archivo.write('\n')
        archivo.write(partida.ruta)
        archivo.write('\n')
        archivo.write(partida.archivo)
        archivo.write('\n')
        archivo.closed


# Cargar la partida (Mejorar)
def cargar_archivo(partida):
    """Permite el ingreso de texto desde el GUI"""
    cargar = True
    # Crea el fondo
    fondo.blit(imagen_fondo, (0, 0))
    dibuja_boton(nombre_del_archivo)
    pygame.display.update()
    nombre.texto = ''

    while cargar:
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
                    cargar = False
                if evento.key == K_CLEAR:
                    nombre.texto = ''
                if evento.unicode == '_':
                    nombre.texto += '_'
            if evento.type == QUIT:
                    cerrar()
            else:
                pass

        # Escribe el nombre ingresado en pantalla
        fondo.blit(imagen_fondo, (0, 0))
        dibuja_boton(nombre_del_archivo)
        nombre.renderizar()
        fondo.blit(nombre.renderizado, (nombre.margen_x, nombre.margen_y))
        pygame.display.update()
    # Asigna el nombre del Tablero_Juego
    p_cargada = nombre.texto
    with open('partidas/' + p_cargada + '.txt', 'r') as archivo:
        fila = []
        partida.tablero_juego = []
        temp = archivo.readlines()
        # Define el tip ode tablero
        partida.modo = int(temp[0])
        # Carga el tablero
        for j in range(1, (partida.modo + 1)):
            linea = temp[j]
            for i in range(len(linea)):
                if linea[i] in '0123456789' and linea[i - 1] != '*':
                    fila.append(linea[i])
                if linea[i] == '*':
                    fila.append(linea[i] + linea[i + 1])
            partida.tablero_juego.append(fila)
            fila = []
        # Carga el Nombre
        partida.jugador = temp[partida.modo + 1][:-1]
        # Carga el nivel
        partida.nivel = temp[partida.modo + 2][:-1]
        # Carga los niveles pasados
        partida.niveles = temp[partida.modo + 3][:-1]
        # Carga el puntaje
        partida.puntaje = int(temp[partida.modo + 4])
        # Carga el tiempo (minutos)
        partida.tiempo[0] = int(temp[partida.modo + 5])
        # Carga el tiempo (minutos)
        partida.tiempo[1] = float(temp[partida.modo + 6][:-1])
        # Carga los errores
        partida.errores = int(temp[partida.modo + 7])
        # Carga los cantidad de veces que ha pedido soluciones
        partida.nayuda = int(temp[partida.modo + 8])
        # Carga la cantidad de jugadas
        partida.jugadas = int(temp[partida.modo + 9])
        # Carga la ruta del archivo solucion
        partida.ruta = temp[partida.modo + 10][:-1]
        # Carga el archivo para la solucion
        partida.archivo = temp[partida.modo + 11][:-1]
    archivo.closed
    partida.tablero_solucion = cargar_tablero(partida)
    print("Tablero Solucion")
    imprimir(partida.tablero_solucion)
    print("Tablero Juego")
    imprimir(partida.tablero_juego)


# Refresca el timer (Mejorar)
def refresca_tiempo(partida):
        Surf_tiempo = pygame.Surface((150,20))
        Surf_tiempo.blit(imagen_fondo, (0,0))
        tiempo = numeros.render('Tiempo: {0:0>2.0f}:{1:0>2.0f}'.format(partida.tiempo[0], partida.tiempo[1]), True, negro)
        Surf_tiempo.blit(tiempo,(0,0))
        fondo.blit(Surf_tiempo, (600,200))


# Donde se corre el juego
def main(tablero):
    global partida, negro, imagen_fondo, sudoku, fps, cont,  pto
    # INICIAL
    # Se limpia la pantalla (queda: fondo blanco, titulo)
    actualiza_pantalla_juego(tablero)
    pygame.display.update()
    # Crea el reloj
    reloj = pygame.time.Clock()
    contador = 0
    # Cajas de opciones del Juego Principal (main)
    cajas = [
    pygame.Rect(solucion.margen_x, solucion.margen_y, solucion.ancho, solucion.alto),
    pygame.Rect(menu_main.margen_x, menu_main.margen_y, menu_main.ancho, menu_main.alto),
    pygame.Rect(salir_main.margen_x, salir_main.margen_y, salir_main.ancho, salir_main.alto)
    ]
    Surf_tiempo = pygame.Surface((150,20))
    cubiertas = 0 # Inicio casillas cubiertas
    valido = 0 # Inicio de la variable que define el numero valido introducido
    # Inicio de la var que cuenta la cantidad de veces que se ha llegado a 3000
    if partida.puntaje == 0:
        cont = 1
    # Dummy de puntaje
    pto = partida.puntaje
   # Ciclo principal
    while True:

        refresca_tiempo(partida)
        mouse = pygame.mouse.get_pos()
        # Dibuja los botones de las opciones
        if partida.nivel < 'x':
            dibuja_boton(solucion)
            dibuja_boton(menu_main)
            dibuja_boton(salir_main)
        elif partida.nivel == 'x':
            dibuja_boton(verificar_sudoku)
            dibuja_boton(menu_main)
            dibuja_boton(salir_main)

        for evento in pygame.event.get():
            refresca_tiempo(partida)
            # Variables a verificar
            if evento.type == QUIT:
                cerrar()
            if evento.type == MOUSEBUTTONDOWN:
                mouse_celdas = coord_celdas(mouse, tablero)
                if mouse_celdas[0] != None:
                    if len(partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]]) == 1:
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

                        # Resaltado de los numero iguales al seleccionado
                        if partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] != '0':
                            for i in range(partida.modo):
                                for j in range(partida.modo):
                                    if partida.tablero_juego[i][j][-1] == partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]]:
                                        resaltado = pygame.Surface((tablero.celda, tablero.celda))
                                        resaltado.fill(azul)
                                        resaltado.set_alpha(150)
                                        iguales = celdas_coord((j,i),tablero)
                                        fondo.blit(resaltado, iguales)

                        # Actualiza la pantalla
                        pygame.display.update()
                        # Permite al usuario introducir un numero. Regresa el numero para calculo de puntaje
                        valido = introduce_numero(tablero, mouse_celdas)
                        # Cuenta el numero de casillas cubiertas
                        cubiertas = casillas_cubiertas(partida)
                        # Calculo de puntaje
                        calculo_puntaje(partida, valido, cubiertas)
                        actualiza_pantalla_juego(tablero)
                        # Verifica si el usuario gana o no
                        verificacion(partida,tablero)
                else:
                    pass
                if partida.nivel < 'x':
                    if cajas[0].collidepoint(mouse[0], mouse[1]):
                        ayuda_solucion(tablero,partida)
                        actualiza_pantalla_juego(tablero)
                    if cajas[1].collidepoint(mouse[0], mouse[1]):
                        menu_juego(fondo, blanco, azul, sudoku)
                    if cajas[2].collidepoint(mouse[0], mouse[1]):
                        ask_guardar(partida)
                        cerrar()
                elif partida.nivel == 'x':
                    if cajas[0].collidepoint(mouse[0], mouse[1]):
                        verificar_matriz(partida, tablero)
                        calculo_puntaje(partida, valido, cubiertas)
                        pto = partida.puntaje
                        actualiza_pantalla_juego(tablero)
                        # Verifica si el usuario gana o no
                        verificacion(partida,tablero)
                        actualiza_pantalla_juego(tablero)
                    if cajas[1].collidepoint(mouse[0], mouse[1]):
                        menu_juego(fondo, blanco, azul, sudoku)
                    if cajas[2].collidepoint(mouse[0], mouse[1]):
                        ask_guardar(partida)
                        cerrar()


                    pygame.display.update()
        contador += reloj.tick() / 1000
        contador = tiempo_juego(partida.tiempo, contador)
        # Se actualiza la pantalla (queda: fondo blanco, titulo)
        # Dibujar numero cambiado
        #partida.dibuja_numero(tablero)
        dibuja_tablero(tablero, negro, imagen_fondo, sudoku)
        pygame.display.update()
        tablero.margen_x, tablero.margen_y, tablero.ancho, tablero.ancho

# Creación del Timer del juego
def tiempo_juego(reloj, contador):
    reloj[1] += contador
    if reloj[1] > 59:
        reloj[0] += 1
        reloj[1] -= 59
    contador = 0
    partida.tiempo = reloj
    return contador

# Permite al usuario agregar numeros al tablero
def introduce_numero(tablero, mouse_celdas):
    ciclo = True
    while ciclo:
        refresca_tiempo(partida)
        for evento in pygame.event.get():
            refresca_tiempo(partida)
            if evento.type == QUIT:
                cerrar()
            if evento.type == KEYDOWN:
                partida.jugadas += 1
                if evento.unicode.isnumeric() and evento.unicode != '0':
                    if evento.unicode == partida.tablero_solucion[mouse_celdas[1]][mouse_celdas[0]]:
                        partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] = evento.unicode
                        actualiza_pantalla_juego(tablero)
                        ciclo = False
                        return int(partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]])
                    else:
                        # Contador de errores (Niveles Fácil y Difícil)
                        if partida.nivel < 'x':
                            partida.errores+= 1
                        # Resta por nivel (Fácil)
                        if partida.nivel == 'f':
                            partida.puntaje = partida.puntaje - 50
                        # Resta por error (Difícil)
                        if partida.nivel  == 'p':
                            partida.puntaje = partida.puntaje - 100
                        # Si es dificil o extremo dejo que escriba el  numero invalido 
                        if partida.nivel == 'p' or partida.nivel == 'x':
                            partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] = evento.unicode
                            actualiza_pantalla_juego(tablero)
                        # Si es facil o entrenamiento lo evito y aviso el error
                        elif partida.nivel == 'p' or partida.nivel == 'e' or partida.nivel == 'f':
                            fondo.blit(error.renderizado, (error.margen_x, error.margen_y))
                            pygame.display.update()
                            pygame.time.delay(1000)
                            actualiza_pantalla_juego(tablero)
                        return 0
                        ciclo = False
                if evento.unicode == '\r':
                    actualiza_pantalla_juego(tablero)
                    return 0
                    ciclo = False
                if evento.unicode == '\x08':
                    partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] = '0'
                    actualiza_pantalla_juego(tablero)
                    return 0
                    ciclo = False
        pygame.display.update((tablero.margen_x-5, tablero.margen_y-5, tablero.ancho+10, tablero.ancho+10))

# Actualiza la Pantalla del juego
def actualiza_pantalla_juego(tablero):
    global partida, fondo, imagen_fondo, sudoku, negro, pto 
    # Muestra el fondo, titulo, tablero y numeros del Sudoku
    limpia_pantalla(fondo, imagen_fondo, sudoku)
    dibuja_numero(tablero, partida)
    dibuja_tablero(tablero, negro, imagen_fondo, sudoku)
    # Muestra el nombre del jugador
    nombre = numeros.render('Jugador: ' + partida.jugador, True, negro)
    fondo.blit(nombre, (200, 150))
    # A partir de fácil para arriba muestra el puntaje
    if partida.nivel > 'e':
        errores = numeros.render('N° Errores: ' + str(partida.errores), True, negro)
        fondo.blit(errores, (600, 260))
        if partida.nivel < 'x':
            puntos = numeros.render('Puntos: ' + str(partida.puntaje), True, negro)
            fondo.blit(puntos, (600, 230))
        elif partida.nivel == 'x':
            puntos = numeros.render('Puntos: ' + str(pto), True, negro)
            fondo.blit(puntos, (600, 230))
    # Muestra el tiempo de la partida
    refresca_tiempo(partida)
    pygame.display.update()

# Muestra al usuario las soluciones del área que seleccione
def ayuda_solucion(tablero,partida):
    ayuda = True
    pistas = []
    if partida.nivel == 'f' and partida.nayuda == 3:
        fondo.blit(max_ayuda.renderizado, (max_ayuda.margen_x, max_ayuda.margen_y))
        pygame.display.update()
        pygame.time.delay(1500)
        ayuda = False

    if partida.nivel == 'p':
        fondo.blit(no_ayuda.renderizado, (no_ayuda.margen_x, no_ayuda.margen_y))
        pygame.display.update()
        pygame.time.delay(1500)
        ayuda = False

    while ayuda == True:
        mouse = pygame.mouse.get_pos()
        for evento in pygame.event.get():
                # Variables a verificar
                if evento.type == QUIT:
                    cerrar()
                if evento.type == MOUSEBUTTONUP:
                    mouse_celdas = coord_celdas(mouse, tablero)
                    if partida.nivel == 'f' and len(pistas) == 1:
                        pass  
                    elif mouse_celdas[0] != None:
                        if len(partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]]) == 1 and partida.tablero_juego[mouse_celdas[1]][mouse_celdas[0]] == '0':
                            dibuja_boton(solucion)
                            mouse = celdas_coord(mouse_celdas, tablero)
                            # Resalta la celda seleccionada
                            resaltado = pygame.Surface((tablero.celda, tablero.celda))
                            resaltado.fill(azul)
                            resaltado.set_alpha(150)
                            fondo.blit(resaltado, mouse)
                            pistas.append([mouse_celdas[1],mouse_celdas[0]])
                            pygame.display.update(mouse,(tablero.celda,tablero.celda))
                        else:
                            pass
                if evento.type == KEYDOWN:
                    if evento.key == K_ESCAPE:
                        ayuda = False
                    if evento.key == K_RETURN:
                        if len(pistas) != 0:
                            partida.jugadas+= 1
                            partida.nayuda+= 1                            
                            for i in range(len(pistas)):
                                partida.tablero_juego[pistas[i][0]][pistas[i][1]] = partida.tablero_solucion[pistas[i][0]][pistas[i][1]]
                                ayuda = False
                        else:
                            ayuda = False
                            pass

# Centa la cantidad de casillas llenas en el tablero
def casillas_cubiertas(partida):
    cubiertas = 0
    for x in range(partida.modo):
        for y in range(partida.modo):
            if partida.tablero_juego[x][y] != '0':
                    cubiertas += 1
    return cubiertas

# Calcula puntaje (CONSTRUIR)
def calculo_puntaje(partida, valido,  cubiertas):
    global cont
    fjugada = 15 # Inicio de factor jugada
    fcobertura = 31 # Inicio de factor cobertura
    if valido != 0:
        # Modificacion por jugada de fjugada y fcobertura (facil)
        if partida.nivel == 'f' and partida.jugadas % 5 == 0:
            fjugada = fjugada - (1 * (partida.jugadas//5))
            fcobertura = fcobertura - (2 * (partida.jugadas//5))

        # Modifica cada 3000 puntos el fjugada y el fcobertura (fácil)
        if partida.nivel == 'f' and partida.puntaje // 3000 == cont:
            fjugada += 5
            fcobertura += 5
            cont += 1

        # Modificacion por jugada de fjugada y fcobertura (difícil y muy difícil)
        if (partida.nivel == 'p' or partida.nivel == 'x') and partida.jugadas % 5 == 0:
            fjugada = fjugada - (2 * (partida.jugadas//5))
            fcobertura = fcobertura - (3 * (partida.jugadas//5))

        # Modifica cada 4500 puntos el fjugada y el fcobertura (difícil y muy difícil)
        if (partida.nivel == 'p' or partida.nivel == 'x') and partida.puntaje // 4500 == cont:
            fjugada += 5
            fcobertura += 5
            cont += 1

        # Solo disminuye hasta 1
        if fjugada < 1:
            fjugada = 1

        # Solo disminuye hasta 1
        if fcobertura < 1:
            fcobertura = 1

        # Cálculo del puntaje
        pjugada = valido * fjugada
        pcobertura = cubiertas * fcobertura
        pactual = pjugada + pcobertura
        partida.puntaje += pactual

# Verifica si el usuario gana o pierde
def verificacion(partida,tablero):
    ganar = True
    for i in range(partida.modo):
        for j in range(partida.modo):
            if partida.tablero_juego != partida.tablero_solucion:
                ganar = False
                pass

    # Pantalla de Ganador
    if ganar == True:
        pygame.time.delay(2000)
        if partida.nivel == 'x':
            if partida.nayuda == 1 and partida.errores == 0:
                partida.puntaje += 5000
            if partida.errores > 0 and partida.errores < 4:
                partida.puntaje += 1500
        # Muestra el texto con la pantalla final
        fondo.blit(imagen_fondo, (0, 0))
        winner = nombre_victoria.render('¡' + partida.jugador + '!', True, negro)
        fondo.blit(winner, (180,90))
        points = nombre_victoria.render('Puntaje: ' + str(partida.puntaje), True, negro)
        fondo.blit(points, (victoria.margen_x, victoria.margen_y + 120))
        fondo.blit(victoria.imagen, (victoria.margen_x, victoria.margen_y))
        cajas = [
        pygame.Rect(volver_menu.margen_x, volver_menu.margen_y, volver_menu.ancho, volver_menu.alto),
        pygame.Rect(salir_victoria.margen_x, salir_victoria.margen_y, salir_victoria.ancho, salir_victoria.alto)
        ]
        mouse = pygame.mouse.get_pos()
        while True:
            dibuja_boton(volver_menu)
            dibuja_boton(salir_victoria)
            winner = nombre_victoria.render('¡' + partida.jugador + '!', True, negro)
            fondo.blit(winner, (180,90))
            mouse = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    cerrar()
                if evento.type == MOUSEBUTTONUP:
                    if cajas[0].collidepoint(mouse[0], mouse[1]):
                        menu_juego(fondo,blanco,azul,sudoku)
                        break
                    if cajas[1].collidepoint(mouse[0], mouse[1]):
                        cerrar()
                        break
            pygame.display.update()
        # Promocion de acceso a niveles
        if partida.niveles < partida.nivel:
            partida.niveles = partida.nivel
            pygame.display.update()
    # Pantalla de Perdedor
    if ganar == False and ((partida.nivel == 'f' and partida.errores == 5) or (partida.nivel == 'p' and partida.errores == 3) \
        or (partida.nivel == 'x' and (partida.errores > 3 or partida.nayuda == 3))):
        fondo.blit(imagen_fondo, (0, 0))
        fondo.blit(derrota.imagen, (derrota.margen_x, derrota.margen_y))
        cajas = [
        pygame.Rect(volver_menu.margen_x, volver_menu.margen_y, volver_menu.ancho, volver_menu.alto),
        pygame.Rect(salir_victoria.margen_x, salir_victoria.margen_y, salir_victoria.ancho, salir_victoria.alto)
        ]
        mouse = pygame.mouse.get_pos()
        while True:
            dibuja_boton(volver_menu)
            dibuja_boton(salir_victoria)
            mouse = pygame.mouse.get_pos()
            for evento in pygame.event.get():
                if evento.type == QUIT:
                    cerrar()
                if evento.type == MOUSEBUTTONUP:
                    if cajas[0].collidepoint(mouse[0], mouse[1]):
                        menu_juego(fondo, blanco, azul, sudoku)
                        break
                    if cajas[1].collidepoint(mouse[0], mouse[1]):
                        cerrar()
                        break
            pygame.display.update()
    else:
        pass

# Funcion "verificar sudoku" del nivel Extremo
def verificar_matriz(partida,tablero):
    partida.nayuda += 1
    error_actual = 0
    for i in range(partida.modo):
        for j in range(partida.modo):
            if partida.tablero_juego[i][j] != partida.tablero_solucion[i][j] and partida.tablero_juego[i][j] != '0':
                coord = celdas_coord((j,i),tablero)
                resaltado = pygame.Surface((tablero.celda, tablero.celda))
                resaltado.fill(rojo)
                resaltado.set_alpha(150)
                fondo.blit(resaltado,coord)                
                error_actual += 1
    partida.errores += error_actual
    partida.puntaje = partida.puntaje - (error_actual * 100)
    pygame.display.update()

# Muestra las reglas y como jugar al usuario
def ayuda_reglas():
    global fondo, imagen_fondo, sudoku

    limpia_pantalla(fondo, imagen_fondo, sudoku)
    fondo.blit(reglas.imagen, (reglas.margen_x, reglas.margen_y))
    cajas = [
    pygame.Rect(menu_main.margen_x, menu_main.margen_y, menu_main.ancho, menu_main.alto)
    ]
    dibuja_boton(menu_main)
    while True:
        pygame.display.update()
        mouse = pygame.mouse.get_pos()
        for evento in pygame.event.get():
            if evento.type == QUIT:
                cerrar()
            if evento.type == MOUSEBUTTONDOWN:
                if cajas[0].collidepoint(mouse[0], mouse[1]):
                    menu_juego(fondo, blanco, azul, sudoku)


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
#victoria_snd = pygame.mixer.Sound('gaelica.mp3')

# ____________________________________________________________________________#
#                           Inicio del programa                               #
# ____________________________________________________________________________#

# ------ Ciclo principal del programa --------------
fondo.blit(imagen_fondo, (0, 0))
input_texto(nombre, bienvenida)
menu_juego(fondo, blanco, azul, sudoku)
    # Se actualiza todo lo hecho en el codigo
pygame.display.update()
    # Limitamos los FPS
