import pygame as py
from funcoes import *
from funcoes import Personagem


# #Tamanho da tela

WIDTH=1200
HEIGHT=700

#Clock

FPS=30
clock=py.time.Clock()

# Abrindo a Tela e Música

screen=py.display.set_mode((WIDTH,HEIGHT))

# Monstros 

mon = Personagem('Monstro','idle_1',-250, 200)
demon = Personagem('Demon','demon_idle_1', 620, 100)