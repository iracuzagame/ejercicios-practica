import pygame
import random
import math

pygame.init()

pantalla = pygame.display.set_mode((800,600))

pygame.display.set_caption("Space Invader")
icono = pygame.image.load("C:/Users/User/Desktop/hacks python/ejercicios/space_invader/ufo.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("C:/Users/User/Desktop/hacks python/ejercicios/space_invader/espacio.jpg")

jugador = pygame.image.load("C:/Users/User/Desktop/hacks python/ejercicios/space_invader/rocket.png")
jugador_x = 368
jugador_y = 516
jugador_horizontal = 0

monster = []
monster_x = []
monster_y = []
monster_horizontal = []
monster_vertical = []
cantidad_monster = 8

for e in range(cantidad_monster):
    monster.append(pygame.image.load("C:/Users/User/Desktop/hacks python/ejercicios/space_invader/monster.png"))
    monster_x.append(random.randint(0, 768))
    monster_y.append(random.randint (50, 200))
    monster_horizontal.append(0.3)
    monster_vertical.append(50)

disparo = pygame.image.load("C:/Users/User/Desktop/hacks python/ejercicios/space_invader/bala.png")
disparo_x = 0
disparo_y = 516
disparo_horizontal = 0
disparo_vertical = 1
disparo_visible = False

puntaje = 0


def jugado(x, y):
    pantalla.blit(jugador, (x, y))

def enemigo(x, y, ene):
    pantalla.blit(monster[ene], (x, y))

def bala(x, y):
    global disparo_visible
    disparo_visible = True
    pantalla.blit(disparo, (x + 16, y + 10))

def colision(x1,y1,x2,y2):
    d = math.sqrt(math.pow(x2 - x1,2) + math.pow(y2 - y1,2))
    if d < 27:
        return True
    else:
        return False


se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0,0))

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta=False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_horizontal = -0.4
            if evento.key == pygame.K_RIGHT:
                jugador_horizontal = 0.4
            if evento.key == pygame.K_SPACE:
                if not disparo_visible:
                    disparo_x = jugador_x
                    bala(disparo_x, disparo_y)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_horizontal = 0

    jugador_x += jugador_horizontal
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    for e in range(cantidad_monster):
        monster_x[e] += monster_horizontal[e]

        if monster_x[e] <= 0:
            monster_horizontal[e] = 0.3
            monster_y[e] += monster_vertical[e]
        elif monster_x[e] >= 736:
            monster_horizontal[e] = -0.3
            monster_y[e] += monster_vertical[e]

        choque = colision(monster_x, monster_y, disparo_x, disparo_y)
        if choque:
            disparo_y = 500
            disparo_visible = False
            puntaje += 1
            print(puntaje)
            monster_x[e] = random.randint(0, 768)
            monster_y[e] = random.randint (50, 200)

        enemigo(monster_x[e], monster_y[e], e)


    if disparo_y <= -64:
        disparo_y = 500
        disparo_visible = False

    if disparo_visible:
        bala(disparo_x, disparo_y)
        disparo_y -= disparo_vertical




    jugado(jugador_x, jugador_y)
    
    pygame.display.update()

    

