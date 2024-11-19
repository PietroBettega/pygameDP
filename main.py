import pygame as py
from pygame import mixer
from funcoes import tela_inicio, tela_fim, carregar_imagens_demonio, carregar_imagens_monstro
from config import screen, WIDTH, HEIGHT, FPS, clock, imagem_fundo

# Definição da classe Personagem
class Personagem(py.sprite.Sprite):
    def __init__(self, nome, nome_imagem, posicao_x, posicao_y, imagens):
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
        self.imagens = imagens

    def desenhar(self):
        personagem_img = self.imagens[self.state][self.current_image]
        screen.blit(personagem_img, (self.posicao_x, self.posicao_y))

    def update(self):
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
            self.current_image = (self.current_image + 1) % len(self.imagens[self.state])
            if self.current_image == 0:
                self.state = 'idle'
        elif self.last_img_change > 5:
            self.last_img_change = 0
            self.current_image = (self.current_image + 1) % len(self.imagens[self.state])

        # Movimentação horizontal
        self.posicao_x += self.x_speed
        margin = 300 if self.nome == 'Demon' else 255
        if self.posicao_x < -margin:
            self.posicao_x = -margin
        elif self.posicao_x + 864 > WIDTH + margin:
            self.posicao_x = WIDTH - 864 + margin

# Função de colisão para dano
def verificar_colisao(demon, mon):
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

# Função para desenhar a tela e as barras de vida
def limpa_screen(demon, mon):
    screen.blit(imagem_fundo, (0, 0))

    # Desenhando as barras de vida
    mon_health_ratio = mon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (50, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (50, 50, 500 * mon_health_ratio, 25))  # Barra de vida verde

    demon_health_ratio = demon.vida / 100
    py.draw.rect(screen, (255, 0, 0), (WIDTH - 550, 50, 500, 25))  # Barra de vida vermelha (fundo)
    py.draw.rect(screen, (0, 255, 0), (WIDTH - 550, 50, 500 * demon_health_ratio, 25))  # Barra de vida verde

    # Desenha os personagens
    if demon.vida > 0:
        demon.desenhar()
    if mon.vida > 0:
        mon.desenhar()

# Chamando a tela de início
tela_inicio(screen, WIDTH, HEIGHT)

# Carregar as imagens dos personagens
demon_images = carregar_imagens_demonio()
mon_images = carregar_imagens_monstro()

# Criando os personagens
demon = Personagem('Demon', 'demon_idle_1', 620, 100, demon_images)
mon = Personagem('Monstro', 'idle_1', -250, 200, mon_images)

# Loop principal do jogo
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

    demon.update()
    mon.update()
    verificar_colisao(demon, mon)
    limpa_screen(demon, mon)
    py.display.update()

# Fechar o jogo
tela_fim(screen, WIDTH, HEIGHT)
mixer.music.stop()
mixer.quit()
py.quit()