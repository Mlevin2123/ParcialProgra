import pygame
import time
import random

# Inicialización de Pygame
pygame.init()

# Colores
blanco = (255, 255, 255)
amarillo = (255, 255, 102)
negro = (0, 0, 0)
rojo = (213, 50, 80)
verde = (0, 255, 0)
azul = (50, 153, 213)

# Dimensiones de la pantalla
ancho_pantalla = 800
alto_pantalla = 400

pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))
pygame.display.set_caption('Snake con Pygame')

# Velocidad del reloj
reloj = pygame.time.Clock()
velocidad_snake = 5


# Tamaño de la serpiente
tamaño_snake = 10

# Fuentes
fuente = pygame.font.SysFont("bahnschrift", 25)
fuente_puntuacion = pygame.font.SysFont("comicsansms", 35)

def puntuacion(puntaje):
    valor = fuente_puntuacion.render("Puntos: " + str(puntaje), True, amarillo)
    pantalla.blit(valor, [0, 0])

def nuestra_snake(tamaño_snake, lista_snake):
    for x in lista_snake:
        pygame.draw.rect(pantalla, negro, [x[0], x[1], tamaño_snake, tamaño_snake])

def mensaje(msg, color):
    mensaje = fuente.render(msg, True, color)
    pantalla.blit(mensaje, [ancho_pantalla / 100, alto_pantalla / 5])

def juego():
    game_over = False
    game_cerrado = False

    x1 = ancho_pantalla / 2
    y1 = alto_pantalla / 2

    x1_cambio = 0
    y1_cambio = 0

    lista_snake = []
    longitud_snake = 1

    comida_x = round(random.randrange(0, ancho_pantalla - tamaño_snake) / 10.0) * 10.0
    comida_y = round(random.randrange(0, alto_pantalla - tamaño_snake) / 10.0) * 10.0

    while not game_over:

        while game_cerrado:
            pantalla.fill(azul)
            mensaje("Perdiste! Presiona C para jugar de nuevo o Q para salir", rojo)
            puntuacion(longitud_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_cerrado = False
                    if event.key == pygame.K_c:
                        juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_cambio = -tamaño_snake
                    y1_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    x1_cambio = tamaño_snake
                    y1_cambio = 0
                elif event.key == pygame.K_UP:
                    y1_cambio = -tamaño_snake
                    x1_cambio = 0
                elif event.key == pygame.K_DOWN:
                    y1_cambio = tamaño_snake
                    x1_cambio = 0

        if x1 >= ancho_pantalla or x1 < 0 or y1 >= alto_pantalla or y1 < 0:
            game_cerrado = True
        x1 += x1_cambio
        y1 += y1_cambio
        pantalla.fill(azul)
        pygame.draw.rect(pantalla, verde, [comida_x, comida_y, tamaño_snake, tamaño_snake])
        lista_snake.append([x1, y1])
        if len(lista_snake) > longitud_snake:
            del lista_snake[0]

        for x in lista_snake[:-1]:
            if x == [x1, y1]:
                game_cerrado = True

        nuestra_snake(tamaño_snake, lista_snake)
        puntuacion(longitud_snake - 1)

        pygame.display.update()

        if x1 == comida_x and y1 == comida_y:
            comida_x = round(random.randrange(0, ancho_pantalla - tamaño_snake) / 10.0) * 10.0
            comida_y = round(random.randrange(0, alto_pantalla - tamaño_snake) / 10.0) * 10.0
            longitud_snake += 1

        reloj.tick(velocidad_snake)

    pygame.quit()
    quit()

juego()
