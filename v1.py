import pygame as py

#Tamanho da tela
WIDTH=1200
HEIGHT=700

#Iniciando
py.init()

#Abrindo a Tela

screen=py.display.set_mode((WIDTH,HEIGHT))
py.display.set_caption("Batalha das Feras")

#Funções do jogo

def limpa_screen():
    imagem_fundo=py.image.load("C:/Users/pbett/OneDrive/Área de Trabalho/DESIGN DE SOFTWARE 1B/DP desoft/imagensjogo/ancient-eastern-scene-character-platform-background_1023080-6686.jpg")
    imagem_fundo=py.transform.scale()

#Loop do jogo

game=True
while game:
    for event in py.event.get():
        if event.type == py.QUIT:
            game=False

    limpa_screen()



#Fechando
py.quit()