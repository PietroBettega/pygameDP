import pygame as py
from pygame import mixer

# Tamanho da tela
WIDTH = 1200
HEIGHT = 700

# Iniciando o Pygame e o mixer
py.init()
mixer.init()

# Abrindo a Tela e Música
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Batalha das Feras")
mixer.music.load("assets/background_music.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
imagem_fundo = py.image.load("assets/PyGame Fundo.webp")
imagem_fundo = py.transform.scale(imagem_fundo, (WIDTH, HEIGHT))  # Garantir que seja uma superfície válida

# Clock
FPS = 30
clock = py.time.Clock()
