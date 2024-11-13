import pygame as py
from pygame import mixer

# Tamanho da tela
WIDTH = 1200
HEIGHT = 700

# Iniciando jogo e música
py.init()
mixer.init()

# Abrindo a Tela e Música
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Batalha das Feras")
mixer.music.load("assets/background_music.mp3")
mixer.music.set_volume(0.7)
mixer.music.play(-1)
imagem_fundo = py.image.load("assets/PyGame Fundo.webp")
imagem_fundo = py.transform.scale(imagem_fundo, (WIDTH, HEIGHT))

# Animação demon
demon_images = {}
img_list = []
for i in range(1, 7):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo idle/01_demon_idle/demon_idle_{i}.png").convert_alpha(), (864, 480)))
demon_images['idle'] = img_list
img_list = []
for i in range(1, 13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo andando/02_demon_walk/demon_walk_{i}.png").convert_alpha(), (864, 480)))
demon_images['walking'] = img_list
img_list = []
for i in range(1, 16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo batendo/03_demon_cleave/demon_cleave_{i}.png").convert_alpha(), (864, 480)))
demon_images['beating'] = img_list
img_list = []
for i in range(1, 23):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo morte/05_demon_death/demon_death_{i}.png").convert_alpha(), (864, 480)))
demon_images['death'] = img_list
img_list = []
for i in range(1, 6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Demo tomando/04_demon_take_hit/demon_take_hit_{i}.png").convert_alpha(), (864, 480)))
demon_images['hit'] = img_list

# Animação mon
mon_images = {}
img_list = []
for i in range(1, 16):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon idle/idle/idle_{i}.png").convert_alpha(), (768, 448)))
mon_images['idle'] = img_list
img_list = []
for i in range(1, 13):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon andando/walk/walk_{i}.png").convert_alpha(), (768, 448)))
mon_images['walking'] = img_list
img_list = []
for i in range(1, 8):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon batendo1/1atk/1atk_{i}.png").convert_alpha(), (768, 448)))
mon_images['beating'] = img_list
img_list = []
for i in range(1, 12):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon morte/death/death_{i}.png").convert_alpha(), (768, 448)))
mon_images['death'] = img_list
img_list = []
for i in range(1, 6):
    img_list.append(py.transform.scale(py.image.load(f"assets/Mon tomando/hurt/hurt_{i}.png").convert_alpha(), (768, 448)))
mon_images['hit'] = img_list

# Clock
FPS = 30
clock = py.time.Clock()

# Criando personagens
class Personagem(py.sprite.Sprite):
    def __init__(self, nome, nome_imagem, posicao_x, posicao_y):
        super().__init__()
        self.nome = nome
        self.nome_imagem = nome_imagem
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.state = 'idle'
        self.x_speed = 0
        self.y_speed = 0
        self.current_image = 1
        self.last_img_change = 0
        self.no_chao = True
        self.hit_duracao = 10
        self.hit_tempo = 0
        self.vida = 100

    def desenhar_demonio(self):
        personagem_demon = demon_images[self.state][self.current_image]
        screen.blit(personagem_demon, (self.posicao_x, self.posicao_y))

    def desenhar_monstro(self):
        personagem_mon = mon_images[self.state][self.current_image]
        screen.blit(personagem_mon, (self.posicao_x, self.posicao_y))

    def update_demon(self):
        if self.vida <= 0:
            self.state = 'death'
            return
        self.last_img_change += 1
        if self.state == 'hit':
            self.hit_tempo += 1
            if self.hit_tempo >= self.hit_duracao:
                self.state = 'idle'
                self.hit_tempo = 0
            return
        if self.state == 'beating' and self.last_img_change > 1:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(demon_images[self.state])
            if self.current_image == 0:
                self.state = 'idle'
        elif self.last_img_change > 5:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(demon_images[self.state])

        # Aplicar movimento horizontal com nova margem
        self.posicao_x += self.x_speed
        margin = 300  # Margem adicional para movimento nas bordas da tela
        if self.posicao_x < -margin:
            self.posicao_x = -margin
        elif self.posicao_x + 864 > WIDTH + margin:
            self.posicao_x = WIDTH - 864 + margin

    def update_mon(self):
        if self.vida <= 0:
            self.state = 'death'
            return
        self.last_img_change += 1
        if self.state == 'hit':
            self.hit_tempo += 1
            if self.hit_tempo >= self.hit_duracao:
                self.state = 'idle'
                self.hit_tempo = 0
            return
        if self.state == 'beating' and self.last_img_change > 2:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(mon_images[self.state])
            if self.current_image == 0:
                self.state = 'idle'
        elif self.last_img_change > 5:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(mon_images[self.state])

        # Aplicar movimento horizontal com nova margem
        self.posicao_x += self.x_speed  
        margin = 255  # Margem adicional para movimento nas bordas da tela
        if self.posicao_x < -margin:
            self.posicao_x = -margin
        elif self.posicao_x + 768 > WIDTH + margin:
            self.posicao_x = WIDTH - 768 + margin

# Função de colisão para dano
def verificar_colisao():
    if demon.vida > 0 and mon.vida > 0:
        if abs(demon.posicao_x - mon.posicao_x) < 300:
            if demon.state == 'beating' and mon.state != 'hit':
                mon.state = 'hit'
                mon.current_image = 0
                mon.hit_tempo = 0
                mon.vida -= 6
            elif mon.state == 'beating' and demon.state != 'hit':
                demon.state = 'hit'
                demon.current_image = 0
                demon.hit_tempo = 0
                demon.vida -= 9

# Aplicando os personagens
mon = Personagem('Monstro', 'idle_1', -250, 200)
demon = Personagem('Demon', 'demon_idle_1', 620, 100)

# Funções do jogo
def limpa_screen():
    screen.blit(imagem_fundo, (0, 0))
    
    # Desenhando as barras de vida
    # Barra de vida do monstro
    mon_health_ratio = mon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (50, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (50, 50, 500 * mon_health_ratio, 25))  # Barra de vida verde
    
    # Barra de vida do demônio
    demon_health_ratio = demon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (WIDTH - 550, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (WIDTH - 550, 50, 500 * demon_health_ratio, 25))  # Barra de vida verde
    
    # Desenha os personagens
    if demon.vida > 0:
        demon.desenhar_demonio()
    if mon.vida > 0:
        mon.desenhar_monstro()

# Loop do jogo
game = True
while game:
    clock.tick(FPS)
    
    # Termina o jogo se um dos personagens estiver morto
    if demon.vida <= 0 or mon.vida <= 0:
        game = False
    
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False
        if event.type == py.KEYDOWN:
            if demon.vida > 0:
                if event.key == py.K_LEFT:
                    demon.state = 'walking'
                    demon.x_speed = -10
                    demon.current_image = 0
                if event.key == py.K_RIGHT:
                    demon.state = 'walking'
                    demon.x_speed = 10
                    demon.current_image = 0
                if event.key == py.K_SPACE:
                    demon.state = 'beating'
                    demon.current_image = 0
            if mon.vida > 0:
                if event.key == py.K_d:
                    mon.state = 'walking'
                    mon.x_speed = 10
                    mon.current_image = 0
                if event.key == py.K_a:
                    mon.state = 'walking'
                    mon.x_speed = -10
                    mon.current_image = 0
                if event.key == py.K_r:
                    mon.state = 'beating'
                    mon.current_image = 0

        if event.type == py.KEYUP:
            if event.key in [py.K_LEFT, py.K_RIGHT]:
                demon.state = 'idle'
                demon.x_speed = 0
                demon.current_image = 0
            if event.key in [py.K_d, py.K_a]:
                mon.state = 'idle'
                mon.x_speed = 0
                mon.current_image = 0

    demon.update_demon()
    mon.update_mon()
    verificar_colisao()
    limpa_screen()
    py.display.update()

# Fechando jogo e música
mixer.music.stop()
mixer.quit()
py.quit()
