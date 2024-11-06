import pygame as py
from funcoes import Personagem
from pygame import mixer


# #Tamanho da tela

WIDTH=1200
HEIGHT=700

#Clock

FPS=30
clock=py.time.Clock()

# Abrindo a Tela e Música

py.init()
mixer.init()

screen=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Batalha das Feras")
mixer.music.load("assets/background_music.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
imagem_fundo=py.image.load("assets/PyGame Fundo.webp")
imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))

# Monstros 

mon = Personagem('Monstro','idle_1',-250, 200)
demon = Personagem('Demon','demon_idle_1', 620, 100)
