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
mixer.music.load("background_music.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)

#Clock

FPS=30
clock=py.time.Clock()

#Criando personagens
class Personagem:
    def __init__(self,nome,nome_imagem, posicao_x,posicao_y):
        self.nome = nome
        self.nome_imagem = nome_imagem
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y

#Aplicando os personagens

personagem_nightborne = ('NightBorne','NightBorne',100, 300)
personagem_demon = ('Demon','boss_demon_slime_FREE_v1.0', 600, 300)



#Funções do jogo

def limpa_screen():
    imagem_fundo=py.image.load("PyGame Fundo.webp")
    imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))
    screen.blit(imagem_fundo,(0,0))

    personagem_imagem = py.image.load(r'')
    screen.blit(personagem_imagem, (100,300))



#Funções do jogo

def limpa_screen():
    imagem_fundo=py.image.load("PyGame Fundo.webp")
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