import pygame as py
from pygame import mixer
from funcoes import *
from animacoes import *
from config import *

#Tamanho da tela
WIDTH=1200
HEIGHT=700

#Criando personagens


    
#Loop do jogo

game=True
while game:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            game=False
        if event.type == py.KEYDOWN:
            #Direita
            if event.type == py.K_d:
                demon.state = 'walking'
                demon.x_speed=10
                demon.current_image = 0
            if event.type ==py.K_l:
                mon.state = 'walking'
                mon.x_speed=-10
                mon.current_image = 0
            #Esquerda
            if event.type == py.K_a:
                demon.state = 'walking'
                demon.x_speed=-10
                demon.current_image = 0
            if event.type ==py.K_j:
                mon.state = 'walking'
                mon.x_speed=10
                mon.current_image = 0

        if event.type == py.KEYUP:
            if event.type == py.K_d or py.K_a:
                demon.state = 'idle'
                demon.current_image = 0
            if event.type == py.K_l or py.K_j:
                mon.state = 'idle'
                mon.current_image = 0

    demon.update_demon()
    mon.update_mon()
    limpa_screen()
    py.display.update()


#Fechando jogo e música
