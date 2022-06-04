
# ----- Importa e inicia pacotes

from re import I
import pygame
import random

from sqlalchemy import false

pygame.init()

# ----- Gera tela principal
WIDTH = 960
HEIGHT = 1023
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Breaking Bricks')

# ---- Inicia assets
BRICK_WIDTH = 40
BRICK_HEIGHT = 30
PRANCHA_WIDTH = 100
PRANCHA_HEIGHT = 10
BOLA_WIDTH = 10
BOLA_HEIGHT = 10
LOOT_BOX_WIDTH = 20
LOOT_BOX_HEIGHT = 20
dx= 8
dy= 8
cor = (0,0,0)
background = pygame.image.load('assets/img/fundo1.jpg').convert()
background_format = pygame.transform.scale(background,(WIDTH,HEIGHT))
brick_vermelho = pygame.image.load('assets/img/Bloco vermelho.png')
brick_Vermelho_format = pygame.transform.scale(brick_vermelho, (BRICK_WIDTH,BRICK_HEIGHT))
brick_amarelo = pygame.image.load('assets/img/Bloco amarelo.png')
brick_amarelo_format = pygame.transform.scale(brick_amarelo, (BRICK_WIDTH,BRICK_HEIGHT))
brick_verde = pygame.image.load('assets/img/Bloco verde.png')
brick_verde_format = pygame.transform.scale(brick_verde, (BRICK_WIDTH,BRICK_HEIGHT))
brick_cor_de_pele = pygame.image.load('assets/img/cor_de_pele.png')
brick_cor_de_pele_format = pygame.transform.scale(brick_cor_de_pele, (BRICK_WIDTH,BRICK_HEIGHT))
brick_marrom = pygame.image.load('assets/img/brick_marrom.png')
brick_marrom_format = pygame.transform.scale(brick_marrom, (BRICK_WIDTH,BRICK_HEIGHT))
prancha = pygame.image.load('assets/img/prancha.png')
prancha_format = pygame.transform.scale(prancha, (PRANCHA_WIDTH,PRANCHA_HEIGHT))
bola = pygame.image.load('assets/img/bola.png')
bola_format = pygame.transform.scale(bola, (BOLA_WIDTH,BOLA_HEIGHT))
lot_box = pygame.image.load('assets/img/bola.png')
lot_box_format = pygame.transform.scale(lot_box,(LOOT_BOX_WIDTH,LOOT_BOX_HEIGHT))
font = pygame.font.SysFont(None, 48)
cor_prancha = (160,32,240)
itotal = 2
ibloc = itotal * BRICK_HEIGHT
icab1 = 1 
jcab1 = 7
icab2 = 3
jcab2 = 10
icab3 = 1
jcab3 = 7
ichap1 = 1
jchap1 = 5
ichap2 = 1
jchap2 = 9
icorp = 10
jcorp = 10
ipernas = 2
jpernas = 7
ipernas1 = 2
jpernas1 = 3

#---- Inicia estrutura de dados 
#---- define as novas classe
class Bricks(pygame.sprite.Sprite):
    def __init__(self,img,x0,y0):

        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x0
        self.rect.y = y0


class Prancha(pygame.sprite.Sprite):
    
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        #----Atualiza a velocidade 
        self.rect.x += self.speedx

        #Mantem dentro da tela principal
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Bolinha(pygame.sprite.Sprite):
    def __init__(self,img):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = 800
        vx=[10,-10]
        self.speedx = random.choice(vx)
        self.speedy = 10
        
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

    def quique(self):
        self.speedy = -self.speedy
    
#--- cria classe loot
class Loot(pygame.sprite.Sprite):
    def __init__(self,img,x0,y0):
        pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x0
        self.rect.y = y0
        self.speedy = 5
        self.speedx = 0
    def update(self):
        #----Atualiza a velocidade 
        self.rect.y += self.speedy

game=True
#----variavel para ajuste de velocidade
clock = pygame.time.Clock()
FPS=30

#----Criando um grupo com todas as sprites
all_sprites = pygame.sprite.Group()

#----Cria tijolos
lista_cor = [brick_verde_format, brick_amarelo_format,brick_Vermelho_format]
all_bricks_cor_de_pele = pygame.sprite.Group()
all_bricks_marrom = pygame.sprite.Group()
all_bricks_vermelho = pygame.sprite.Group()
all_bricks_verde = pygame.sprite.Group()
all_bricks_amarelo = pygame.sprite.Group()

#---- Desenho do Mario

for p in range(ichap1):
    gapx = BRICK_WIDTH * 8 + dx
    gapy = BRICK_HEIGHT * 2  
    for k in range(jchap1):
        bloco_vermelho = Bricks(brick_Vermelho_format,gapx,gapy) 
        all_bricks_vermelho.add(bloco_vermelho)
        gapx += BRICK_WIDTH + dx
    gapy += BRICK_HEIGHT

for p in range(ichap2):
    gapx = BRICK_WIDTH * 7 
    gapy += dy  
    for k in range(jchap2):
        bloco_vermelho = Bricks(brick_Vermelho_format,gapx,gapy) 
        all_bricks_vermelho.add(bloco_vermelho)
        gapx += BRICK_WIDTH + dx
    gapy += BRICK_HEIGHT

for p in range(icab1):
    gapxx = BRICK_WIDTH * 7
    for w in range(3):
        bloco_marrom = Bricks(brick_marrom_format,gapxx,gapy+dy)
        all_bricks_marrom.add(bloco_marrom)
        gapxx += BRICK_WIDTH + dx
    gapx = BRICK_WIDTH * 11 - 2 * dx
    gapy += dy  
    for k in range(jcab1 - 3):
        bloco_cor_de_pele = Bricks(brick_cor_de_pele_format,gapx,gapy) 
        all_bricks_cor_de_pele.add(bloco_cor_de_pele)
        gapx += BRICK_WIDTH + dx
    xx = BRICK_WIDTH * 13
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy)
    all_bricks_marrom.add(bloco_marrom)
    gapy += BRICK_HEIGHT
xx = BRICK_WIDTH * 13
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 6 - dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 7 
bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
all_bricks_cor_de_pele.add(bloco_cor_de_pele)
xx = BRICK_WIDTH * 8 + dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 9 + 2*dx
for j in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx
xx = BRICK_WIDTH * 14 + dx 
for j in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 6 - dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 7 
bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
all_bricks_cor_de_pele.add(bloco_cor_de_pele)
xx = BRICK_WIDTH * 8 + dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 9 + dx+dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 11 - 2* dx 
for j in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx
xx = BRICK_WIDTH * 14 + dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 15 + 2*dx 
for j in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 6 - dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 7 
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx = BRICK_WIDTH * 8 + dx 
for h in range(4):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx  
xx = BRICK_WIDTH * 13  
for l in range(4):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx  
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 8 + dx
for n in range(7):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 7 
for l in range(2):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx  
xx = BRICK_WIDTH * 9 + 2* dx
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
xx = BRICK_WIDTH * 10 + 3*dx 
for l in range(2):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx  
xx = BRICK_WIDTH * 13 
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
gapy += BRICK_HEIGHT + dy 
xx = BRICK_WIDTH * 6 - dx 
for l in range(3):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx 
xx = BRICK_WIDTH * 9 + 2* dx
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
xx = BRICK_WIDTH * 11 - 2* dx 
for l in range(2):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx 
xx = BRICK_WIDTH * 13 
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
xx = BRICK_WIDTH * 14 + dx
for l in range(3):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx 
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 4 + 3*dx
for l in range(4):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx
for k in range(4):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
for l in range(4):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx

gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 4 + 3*dx
for n in range(2):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx += BRICK_WIDTH + dx
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
xx += BRICK_WIDTH + dx
bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
all_bricks_cor_de_pele.add(bloco_cor_de_pele)
xx += BRICK_WIDTH + dx 
for n in range(2):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
all_bricks_cor_de_pele.add(bloco_cor_de_pele)
xx += BRICK_WIDTH + dx
bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
all_bricks_vermelho.add(bloco_vermelho)
xx += BRICK_WIDTH + dx
bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
all_bricks_marrom.add(bloco_marrom)
xx += BRICK_WIDTH + dx
for n in range(2):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 4 + 3* dx
for n in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
for n in range(6):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
for n in range(3):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 4 + 3* dx
for n in range(2):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
for n in range(8):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
for n in range(2):
    bloco_cor_de_pele= Bricks(brick_cor_de_pele_format,xx,gapy+dy)
    all_bricks_cor_de_pele.add(bloco_cor_de_pele)
    xx += BRICK_WIDTH + dx 
gapy += BRICK_HEIGHT + dy 
xx = BRICK_WIDTH * 7
for n in range(3):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
xx = BRICK_WIDTH * 13
for n in range(3):
    bloco_vermelho = Bricks(brick_Vermelho_format,xx,gapy+dy)
    all_bricks_vermelho.add(bloco_vermelho)
    xx += BRICK_WIDTH + dx
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 6 - dx 
for l in range(3):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx
xx = BRICK_WIDTH * 14 + dx
for l in range(3):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx
gapy += BRICK_HEIGHT + dy
xx = BRICK_WIDTH * 5 - 2* dx 
for l in range(4):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx
xx = BRICK_WIDTH * 14 + dx
for l in range(4):
    bloco_marrom = Bricks(brick_marrom_format,xx,gapy+dy)
    all_bricks_marrom.add(bloco_marrom)
    xx += BRICK_WIDTH + dx





#----Cria Jogaodor
player = Prancha(prancha_format)
all_sprites.add(player)

#----Cria bola
all_bolas=pygame.sprite.Group()
bola = Bolinha(bola_format)
all_sprites.add(bola)
all_bolas.add(bola)
bolacount = 1

#---Cria loot
all_loot = pygame.sprite.Group()

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

        #----Verifica se apertou algo
        if event.type == pygame.KEYDOWN:
            #----altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 12
            if event.key == pygame.K_RIGHT:
                player.speedx += 12

           # Verifica se soltou
        if event.type == pygame.KEYUP:
            #----altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 12
            if event.key == pygame.K_RIGHT:
                player.speedx -= 12
       
    for bola in all_bolas:   
        if bola.rect.y >= HEIGHT - BOLA_HEIGHT:
            bola.kill()  
            bolacount -= 1
            if bolacount == 0:
                game = False
        if bola.rect.y <= 0:
            bola.speedy = -bola.speedy
        if bola.rect.x >= WIDTH - BOLA_WIDTH:
            bola.speedx = -bola.speedx
        if bola.rect.x <= 0:
            bola.speedx = -bola.speedx  

    hits = pygame.sprite.spritecollide(player,all_bolas,False)
    for bola in hits:
        bola.quique()


    hits2 = pygame.sprite.groupcollide(all_bricks_vermelho,all_bolas,True,False)
    for bloco in hits2:

        xx = bloco.rect.x
        yy = bloco.rect.y
        bloco.kill()
        # ---- Cria bolas novas aleatoriamente
        numx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
        sort = random.choice(numx)
        if sort == 1:
            loot = Loot(lot_box_format,xx,yy)
            all_loot.add(loot)
            all_sprites.add(loot)
        for ball in hits2[bloco]:
            ball.quique()        
    hits3 = pygame.sprite.groupcollide(all_bricks_cor_de_pele,all_bolas,False,False)
    for bloco in hits3:
        xx = bloco.rect.x
        yy = bloco.rect.y
        brick_vermelho_replace = Bricks(brick_Vermelho_format,xx,yy)
        all_bricks_vermelho.add(brick_vermelho_replace)
        all_sprites.add(brick_vermelho_replace)
        bloco.kill()
        for ball in hits3[bloco]:
            ball.quique() 

    hits4 = pygame.sprite.groupcollide(all_bricks_marrom,all_bolas,False,False)
    for bloco in hits4:
        xx = bloco.rect.x
        yy = bloco.rect.y
        brick_cor_de_pele_replace = Bricks(brick_cor_de_pele_format,xx,yy)
        all_bricks_cor_de_pele.add(brick_cor_de_pele_replace)
        all_sprites.add(brick_cor_de_pele_replace)
        bloco.kill()
        for bola in hits4[bloco]:
            bola.quique() 
            
    hits5 = pygame.sprite.spritecollide(player,all_loot,True)
    for t in  hits5:
        bolanova = Bolinha(bola_format)
        all_bolas.add(bolanova) 
        all_sprites.add(bolanova)
        bolacount += 1
        


    





#---- Atualiza de acordo com os comandos
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_format, (0, 0)) # Preenche com a cor branca
    all_bricks_verde.draw(window)
    all_bricks_amarelo.draw(window)
    all_bricks_vermelho.draw(window)
    all_bricks_cor_de_pele.draw(window)
    all_bricks_marrom.draw(window)
    all_bolas.draw(window)
    all_sprites.draw(window)
    pygame.display.update()

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


