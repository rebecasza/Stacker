import os
import sys
import pygame
import time
from numpy import *
from pygame.locals import *

def setupTela():

    pygame.init()
    pygame.display.set_caption("Bem vindo! Stacker Game by Rebeca Souza - IFSP")

    global screen
    screen = pygame.display.set_mode((500,500))

    global empty
    global tower

    empty = pygame.image.load('empty.png').convert()
    tower = pygame.image.load('tower.png').convert()

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)

####################################################################

def updateTela():
    posX = 0
    posY = 0

    if not Coluna_1:
        for i in range(5):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
    else:
        blocosTower = len(Coluna_1)
        blocosEmpty = 5 - blocosTower

        for i in range(blocosEmpty):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
        for i in range(blocosTower):
            screen.blit(tower,(posX,posY))
            posY = posY + 100

    posX = 100
    posY = 0
    if not Coluna_2:
        for i in range(5):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
    else:
        blocosTower = len(Coluna_2)
        blocosEmpty = 5 - blocosTower

        for i in range(blocosEmpty):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
        for i in range(blocosTower):
            screen.blit(tower,(posX,posY))
            posY = posY + 100

    posX = 200
    posY = 0
    if not Coluna_3:
        for i in range(5):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
    else:
        blocosTower = len(Coluna_3)
        blocosEmpty = 5 - blocosTower

        for i in range(blocosEmpty):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
        for i in range(blocosTower):
            screen.blit(tower,(posX,posY))
            posY = posY + 100

    posX = 300
    posY = 0
    if not Coluna_4:
        for i in range(5):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
    else:
        blocosTower = len(Coluna_4)
        blocosEmpty = 5 - blocosTower

        for i in range(blocosEmpty):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
        for i in range(blocosTower):
            screen.blit(tower,(posX,posY))
            posY = posY + 100

    posX = 400
    posY = 0
    if not Coluna_5:
        for i in range(5):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
    else:
        blocosTower = len(Coluna_5)
        blocosEmpty = 5 - blocosTower

        for i in range(blocosEmpty):
            screen.blit(empty,(posX,posY))
            posY = posY + 100
        for i in range(blocosTower):
            screen.blit(tower,(posX,posY))
            posY = posY + 100

####################################################################


def movBloco():

    tamanhos =[len(Coluna_1),len(Coluna_2),len(Coluna_3),len(Coluna_4),len(Coluna_5)]
    maximaTorre = max(tamanhos)
    blocoHorizontal = 4 - maximaTorre
    global possY
    global possX
    possY = 0
    possX = 0
    direcao = 0

    for i in range(blocoHorizontal):
        screen.blit(empty,(possX,possY))
        possY = possY + 100

    while True:
        if direcao == 0:
            screen.blit(empty,(0,possY))
            screen.blit(empty,(100,possY))
            screen.blit(empty,(200,possY))
            screen.blit(empty,(300,possY))
            screen.blit(empty,(400,possY))
            screen.blit(tower,(possX,possY))
            if possX == 500:
                direcao = 1
        else:
            screen.blit(empty,(0,possY))
            screen.blit(empty,(100,possY))
            screen.blit(empty,(200,possY))
            screen.blit(empty,(300,possY))
            screen.blit(empty,(400,possY))
            screen.blit(tower,(possX,possY))
            if possX == 0:
                direcao = 0
        time.sleep(100.0 / 1000.0)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit();
                sys.exit();
            if event.type == pygame.KEYDOWN:
                return possX

        if direcao == 0:
            possX = possX + 100
        else:
            possX = possX - 100


if __name__ == '__main__':
    setupTela()
pygame.display.update()
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
posY = 0
pygame.mixer.music.load('song.mp3')
pygame.mixer.music.play(-1)
global Coluna_1
global Coluna_2
global Coluna_3
global Coluna_4
global Coluna_5
Coluna_1 = []
Coluna_2 = []
Coluna_3 = []
Coluna_4 = []
Coluna_5 = []

updateTela()

while True:

    updateTela()
    posX = movBloco()/100
    print(posX)

    if posX == 1:
        Coluna_1.append(1)
    elif posX == 2:
        Coluna_2.append(1)
    elif posX == 3:
        Coluna_3.append(1)
    elif posX == 4:
        Coluna_4.append(1)
    elif posX == 5:
        Coluna_5.append(1)
    else:
        a = 0