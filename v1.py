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
mixer.music.load("assets/background_music.mp3")
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

    def desenhar_demonio(self):
        #personagem_demon = py.image.load("assets/Demo idle/01_demon_idle/demon_idle_1.png")
        personagem_demon=py.transform.scale(py.image.load("assets/Demo idle/01_demon_idle/demon_idle_1.png").convert_alpha(),
        (864,480))
        screen.blit(personagem_demon, (self.posicao_x,self.posicao_y))

    def desenhar_monstro(self):
        #personagem_mon = py.image.load("assets/Mon idle/idle/idle_1.png")
        personagem_mon=py.transform.scale(py.image.load("assets/Mon idle/idle/idle_1.png").convert_alpha(),
        (768,448))
        screen.blit(personagem_mon, (self.posicao_x,self.posicao_y))
#Aplicando os personagens

mon = Personagem('Monstro','idle_1',600, 150)
demon = Personagem('Demon','demon_idle_1', -220, 240)



#Funções do jogo

def limpa_screen():
    imagem_fundo=py.image.load("assets/PyGame Fundo.webp")
    imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))
    screen.blit(imagem_fundo,(0,0))

    mon.desenhar_demonio()
    demon.desenhar_monstro()
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