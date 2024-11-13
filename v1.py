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

def tela_inicio():
    # Carrega a imagem de fundo da tela inicial
    imagem_fundo_inicio = py.image.load("assets/Inicio.webp")
    imagem_fundo_inicio = py.transform.scale(imagem_fundo_inicio, (WIDTH, HEIGHT))
    # Parâmetros do botão
    botao_largura = 300
    botao_altura = 80
    botao_x = WIDTH // 2 - botao_largura // 2
    botao_y = HEIGHT // 2 + 100
    fonte = py.font.Font(None, 74)
    fonte_botao = py.font.Font(None, 50)

    esperando = True
    while esperando:
        screen.blit(imagem_fundo_inicio, (0, 0))  # Fundo
        texto = fonte.render("Batalha das Feras", True, (255, 255, 255))
        screen.blit(texto, (WIDTH // 2 - texto.get_width() // 2, HEIGHT // 2 - 150))

        # Botão
        py.draw.rect(screen, (0, 128, 0), (botao_x, botao_y, botao_largura, botao_altura))
        texto_botao = fonte_botao.render("Iniciar Jogo", True, (255, 255, 255))
        screen.blit(texto_botao, (botao_x + botao_largura // 2 - texto_botao.get_width() // 2, botao_y + botao_altura // 2 - texto_botao.get_height() // 2))
        py.display.update()

        # Verificar eventos para interação com o botão
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            if event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                # Verificar se o clique foi no botão
                if botao_x <= mouse_x <= botao_x + botao_largura and botao_y <= mouse_y <= botao_y + botao_altura:
                    esperando = False  # Inicia o jogo

# Função para a Tela de Fim com imagem de fundo e encerramento ao clicar
def tela_fim():
    # Carrega a imagem de fundo da tela final
    imagem_fundo_fim = py.image.load("assets/Tela fim.webp")
    imagem_fundo_fim = py.transform.scale(imagem_fundo_fim, (WIDTH, HEIGHT))
    
    screen.blit(imagem_fundo_fim, (0, 0))
    py.display.update()

    # Esperar qualquer clique para fechar o jogo
    esperando = True
    while esperando:
        for event in py.event.get():
            if event.type == py.QUIT or event.type == py.MOUSEBUTTONDOWN:
                esperando = False  # Fecha o jogo
    py.quit()

# Chamando a tela de início
tela_inicio()

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
class Personagem:
    def __init__(self, nome, nome_imagem, posicao_x, posicao_y):
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
        self.hit_tempo=0

    def desenhar_demonio(self):
        personagem_demon = demon_images[self.state][self.current_image]
        screen.blit(personagem_demon, (self.posicao_x, self.posicao_y))

    def desenhar_monstro(self):
        personagem_mon = mon_images[self.state][self.current_image]
        screen.blit(personagem_mon, (self.posicao_x, self.posicao_y))

    def update_demon(self):
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
        # Aplicar movimento horizontal
        self.posicao_x += self.x_speed
        # Impedir de sair da tela
        if self.posicao_x < 0:
            self.posicao_x = 0
        elif self.posicao_x + 864 > WIDTH:  # 864 é a largura do personagem demon
            self.posicao_x = WIDTH - 864

        # Movimento vertical (pulo)
        if not self.no_chao:
            self.y_speed += 1  # Gravidade
            self.posicao_y += self.y_speed
            # Verificar se tocou o chão
            if self.posicao_y >= 100:  # Posição inicial no chão
                self.posicao_y = 100
                self.no_chao = True
                self.y_speed = 0

    def update_mon(self):
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

        # Aplicar movimento horizontal
        self.posicao_x += self.x_speed
        # Impedir de sair da tela
        if self.posicao_x < 0:
            self.posicao_x = 0
        elif self.posicao_x + 768 > WIDTH:  # 768 é a largura do personagem mon
            self.posicao_x = WIDTH - 768

        # Movimento vertical (pulo)
        if not self.no_chao:
            self.y_speed += 1  # Gravidade
            self.posicao_y += self.y_speed
            # Verificar se tocou o chão
            if self.posicao_y >= 200:  # Posição inicial no chão
                self.posicao_y = 200
                self.no_chao = True
                self.y_speed = 0

# Função de colisão para dano
def verificar_colisao():
    if abs(demon.posicao_x - mon.posicao_x) < 100:  # Distância mínima para colisão
        if demon.state == 'beating' and mon.state != 'hit':
            mon.state = 'hit'
            mon.current_image = 0
            mon.hit_tempo=0
        elif mon.state == 'beating' and demon.state != 'hit':
            demon.state = 'hit'
            demon.current_image = 0
            demon.hit_tempo=0

# Aplicando os personagens
mon = Personagem('Monstro', 'idle_1', -250, 200)
demon = Personagem('Demon', 'demon_idle_1', 620, 100)

# Funções do jogo
def limpa_screen():
    screen.blit(imagem_fundo, (0, 0))
    mon.desenhar_monstro()
    demon.desenhar_demonio()

# Loop do jogo
game = True
while game:
    clock.tick(FPS)
    for event in py.event.get():
        if event.type == py.QUIT:
            game = False
        if event.type == py.KEYDOWN:
            # Movimentos
            if event.key == py.K_LEFT:
                demon.state = 'walking'
                demon.x_speed = -10
                demon.current_image = 0
            if event.key == py.K_d:
                mon.state = 'walking'
                mon.x_speed = 10
                mon.current_image = 0
            if event.key == py.K_RIGHT:
                demon.state = 'walking'
                demon.x_speed = 10
                demon.current_image = 0
            if event.key == py.K_a:
                mon.state = 'walking'
                mon.x_speed = -10
                mon.current_image = 0
            # Pulo
            if event.key == py.K_w and mon.no_chao:
                mon.y_speed = -15  # Força do pulo
                mon.no_chao = False
            if event.key == py.K_UP and demon.no_chao:
                demon.y_speed = -15
                demon.no_chao = False
            # Ataque
            if event.key == py.K_SPACE:
                demon.state = 'beating'
                demon.current_image = 0
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
tela_fim()
mixer.music.stop()
mixer.quit()
py.quit()

