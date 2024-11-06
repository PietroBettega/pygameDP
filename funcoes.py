import pygame as py
from config import *
from animacoes import *


def limpa_screen():
    imagem_fundo=py.image.load("assets/PyGame Fundo.webp")
    imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))
    screen.blit(imagem_fundo,(0,0))

    mon.desenhar_demonio()
    demon.desenhar_monstro()

class Personagem:
    def __init__(self,nome,nome_imagem, posicao_x,posicao_y):
        self.nome = nome
        self.nome_imagem = nome_imagem
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.state = 'idle'
        self.x_speed=0
        self.current_image = 1
        self.last_img_change = 0

    def desenhar_demonio(self):
        # print(self.nome, self.current_image)
        personagem_demon = demon_images[self.state][self.current_image]
        screen.blit(personagem_demon, (self.posicao_x,self.posicao_y))

    def update_demon(self):
        self.last_img_change += 1
        if self.last_img_change > 5:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(demon_images[self.state])

        
    def desenhar_monstro(self):
        # print(self.nome, self.current_image)
        personagem_mon = mon_images[self.state][self.current_image]
        screen.blit(personagem_mon, (self.posicao_x,self.posicao_y))

    def update_mon(self):
        self.last_img_change += 1
        if self.last_img_change > 2:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(mon_images[self.state])
    #Atualiza posição
    self.posicao_x= self.posicao_x + self.x_speed
    if self.posicao_x < 0:
        self.posicao_x=0
        self.state = 'idle'
    if self.posicao_x > 950:
        self.posicao_x = 950
        self.state = 'idle'