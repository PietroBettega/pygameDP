import pygame as py
from pygame import mixer

#Tamanho da tela
WIDTH=1200
HEIGHT=700

#Iniciando jogo e música
py.init()
mixer.init()

#Abrindo a Tela e Música

screen=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Batalha das Feras")
mixer.music.load("C:/Users/pbett/OneDrive/Área de Trabalho/DESIGN DE SOFTWARE 1B/DP desoft/imagensjogo/background_music.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#Clock

FPS=30
clock=py.time.Clock()

#Funções do jogo

def limpa_screen():
    imagem_fundo=py.image.load("C:/Users/pbett/OneDrive/Área de Trabalho/DESIGN DE SOFTWARE 1B/DP desoft/imagensjogo/ancient-eastern-scene-character-platform-background_1023080-6686.jpg")
    imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))
    screen.blit(imagem_fundo,(0,0))

#Loop do jogo

game=True
while game:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            game=False

    limpa_screen()
    py.display.update()


#Fechando jogo e música
mixer.music.stop()
mixer.quit()
py.quit()