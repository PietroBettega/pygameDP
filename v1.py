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
imagem_fundo=py.image.load("assets/PyGame Fundo.webp")
imagem_fundo=py.transform.scale(imagem_fundo,(WIDTH,HEIGHT))


#Animação demon
demon_images = {}
img_list = []
for i in range(1,7):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo idle/01_demon_idle/demon_idle_{i}.png").convert_alpha(),
        (864,480)))
demon_images['idle'] = img_list
img_list = []
for i in range(1,13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo andando/02_demon_walk/demon_walk_{i}.png").convert_alpha(),
        (864,480)))
demon_images['walking'] = img_list
for i in range(1,16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo batendo/03_demon_cleave/demon_cleave_{i}.png").convert_alpha(),
        (864,480)))
demon_images['beating'] = img_list
for i in range(1,23):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo morte/05_demon_death/demon_death_{i}.png").convert_alpha(),
        (864,480)))
demon_images['death'] = img_list
for i in range(1,6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo tomando/04_demon_take_hit/demon_take_hit_{i}.png").convert_alpha(),
        (864,480)))
demon_images['hit'] = img_list

#Animando mon
mon_images = {}
img_list = []
for i in range(1,16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon idle/idle/idle_{i}.png").convert_alpha(),
        (768,448)))
mon_images['idle'] = img_list
img_list = []
for i in range(1,13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon andando/walk/walk_{i}.png").convert_alpha(),
        (768,448)))
mon_images['walking'] = img_list
for i in range(1,8):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon batendo/1atk/1atk_{i}.png").convert_alpha(),
        (768,448)))
mon_images['beating'] = img_list
img_list = []
for i in range(1,12):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon morte/death/death_{i}.png").convert_alpha(),
        (768,448)))
mon_images['death'] = img_list
for i in range(1,6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon tomando/hurt/hurt_{i}.png").convert_alpha(),
        (768,448)))
mon_images['hit'] = img_list



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
        self.state = 'idle'
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

#Aplicando os personagens

mon = Personagem('Monstro','idle_1',-250, 200)
demon = Personagem('Demon','demon_idle_1', 620, 100)



#Funções do jogo

def limpa_screen():
    
    screen.blit(imagem_fundo,(0,0))
    mon.desenhar_monstro()
    demon.desenhar_demonio()
    
#Loop do jogo

game=True
while game:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            game=False
        # if event.type == py.KEYDOWN:
        #     #se apertou esquerda
        #     demon.state = 'walking'
        #     demon.current_image = 0
        # if event.type == py.KEYUP:
        #     demon.state = 'idle'
        #     demon.current_image = 0

    demon.update_demon()
    mon.update_mon()
    limpa_screen()
    py.display.update()


#Fechando jogo e música
mixer.music.stop()
mixer.quit()
py.quit()