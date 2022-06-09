# ----- Importa e inicia pacotes
import pygame
import random

def fase3(window):
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
    LOOT_BOX_HEIGHT = 40
    LOOT_BOX_WIDTH = 40
    background = pygame.image.load('assets/img/background.png').convert()
    background_format = pygame.transform.scale(background,(WIDTH,HEIGHT))
    brick_branco = pygame.image.load('assets/img/bloco branco.png')
    brick_branco_format = pygame.transform.scale(brick_branco, (BRICK_WIDTH,BRICK_HEIGHT))
    brick_preto = pygame.image.load('assets/img/bloco preto.png')
    brick_preto_format = pygame.transform.scale(brick_preto,(BRICK_WIDTH,BRICK_HEIGHT))
    brick_vermelho = pygame.image.load('assets/img/bloco vermelho.png')
    brick_vermelho_format = pygame.transform.scale(brick_vermelho,(BRICK_WIDTH,BRICK_HEIGHT))
    prancha = pygame.image.load('assets/img/prancha.png')
    prancha_format = pygame.transform.scale(prancha, (PRANCHA_WIDTH,PRANCHA_HEIGHT))
    bola = pygame.image.load('assets/img/bola.png')
    bola_format = pygame.transform.scale(bola,(BOLA_WIDTH,BOLA_HEIGHT))
    lot_box = pygame.image.load('assets/img/loot.png').convert()
    lot_box_format = pygame.transform.scale(lot_box,(LOOT_BOX_WIDTH,LOOT_BOX_HEIGHT))
    hitt_sound = pygame.mixer.Sound('assets/img/sounds/hitt.wav')
    loot_sound = pygame.mixer.Sound('assets/img/sounds/loot.wav')
    prancha_sound = pygame.mixer.Sound('assets/img/sounds/pranchaa.wav')
    metal_sound = pygame.mixer.Sound('assets/img/sounds/metal.wav')
    dx = 8
    dy = 8
    x0 = BRICK_WIDTH*2
    y0 = BRICK_HEIGHT * 2
    i=23
    j=17


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
        def __init__(self,img,xx,yy):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = xx
            self.rect.y = yy
            self.speedx = 10
            self.speedy = 10

        def quique(self):
            self.speedy *= -1


        def update(self):
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        

    #--- cria classe loot
    class Loot(pygame.sprite.Sprite):
        def __init__(self,img,x0,y0):
            pygame.sprite.Sprite.__init__(self)
            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x0
            self.rect.y = y0
            self.speedy = 15
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

    all_bricks_preto = pygame.sprite.Group()
    all_bricks_branco = pygame.sprite.Group()
    all_bricks_vermelho = pygame.sprite.Group()
    all_bricks = pygame.sprite.Group()
    #----16 linhas
    #----17 colunas
    h = 0
    lista_des = [[[1,1,1,1,1,1,1],[5,7]],[[1,1,2,3,3,3,3,3,3,1,1],[3,11]],[[1,2,2,2,3,3,3,3,3,3,2,2,1],[2,13]],[[1,2,2,2,3,3,3,3,3,3,3,3,2,2,1],[1,15]],[[1,2,2,3,3,3,2,2,2,3,3,3,3,2,1],[1,15]],[[1,3,3,3,3,3,2,2,2,2,2,3,3,3,3,3,1],[0,17]],[[1,3,3,3,3,3,2,2,2,2,2,3,3,3,3,3,1],[0,17]],[[1,3,2,2,3,3,3,2,2,2,3,3,3,3,3,2,1],[0,17]],[[1,2,2,2,2,3,3,3,3,3,3,3,3,3,2,2,1],[0,17]],[[1,2,2,2,2,3,3,3,3,3,3,3,3,3,2,2,1],[0,17]],[[1,3,2,2,1,1,1,1,1,1,1,1,1,3,3,2,1],[0,17]],[[1,1,1,2,2,2,1,2,2,1,2,2,1,1,1],[1,15]],[[1,2,2,2,2,1,2,2,1,2,2,2,1],[2,13]],[[1,2,2,2,2,2,2,2,2,2,2,2,1],[2,13]],[[1,2,2,2,2,2,2,2,2,2,1],[3,11]],[[1,1,1,1,1,1,1,1,1],[4,9]]]
    for z in range (16):
        j = 1
        for k in range(lista_des[h][1][1]):
            if lista_des[h][0][j-1] == 1:
                brick_preto = Bricks(brick_preto_format,(x0+ lista_des[h][1][0]*dx+lista_des[h][1][0]*BRICK_WIDTH),y0)
                all_bricks_preto.add(brick_preto)
                all_sprites.add(brick_preto)
                all_bricks.add(brick_preto)
                x0+=BRICK_WIDTH + dx
            if lista_des[h][0][j-1] == 2:
                brick_branco = Bricks(brick_branco_format,(x0+ lista_des[h][1][0]*dx+lista_des[h][1][0]*BRICK_WIDTH),y0)
                all_bricks_branco.add(brick_branco)
                all_sprites.add(brick_branco)
                all_bricks.add(brick_branco)
                x0+=BRICK_WIDTH + dx
            if lista_des[h][0][j-1] == 3:
                brick_vermelho = Bricks(brick_vermelho_format,(x0+ lista_des[h][1][0]*dx+lista_des[h][1][0]*BRICK_WIDTH),y0)
                all_bricks_vermelho.add(brick_vermelho)
                all_sprites.add(brick_vermelho)
                all_bricks.add(brick_vermelho)
                x0+=BRICK_WIDTH + dx
            j+=1
        h+=1   
        x0 = BRICK_WIDTH*2
        y0+= BRICK_HEIGHT + dy




    #----Cria Jogaodor
    player = Prancha(prancha_format)
    all_sprites.add(player)

    #----Cria bola
    all_bolas=pygame.sprite.Group()
    bola = Bolinha(bola_format,300,700)
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
                STATE = 'Game_over'

            #----Verifica se apertou algo
            if event.type == pygame.KEYDOWN:
                #----altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx -= 16
                if event.key == pygame.K_RIGHT:
                    player.speedx += 16

            # Verifica se soltou
            if event.type == pygame.KEYUP:
                #----altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx += 16
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 16
        
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
        if hits:
            prancha_sound.play()
        for bola in hits:
            bola.quique()


        hits2 = pygame.sprite.groupcollide(all_bricks,all_bolas,True,False)
        if hits2:
            hitt_sound.play()
        for bloco in hits2:
            xx = bloco.rect.x
            yy = bloco.rect.y
            bloco.kill()
            # ---- Cria bolas novas aleatoriamente
            numx = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
            sort = random.choice(numx)
            if sort == 1:
                loot = Loot(lot_box_format,xx,yy)
                all_loot.add(loot)
                all_sprites.add(loot)
            for ball in hits2[bloco]:
                if abs(ball.rect.x - bloco.rect.right) <= 4 or abs(ball.rect.x - bloco.rect.left) <= 4:
                    ball.speedx *= -1
                else:
                    ball.quique()     

        hits5 = pygame.sprite.spritecollide(player,all_loot,True)
        if hits5:
            loot_sound.play()
        for t in  hits5:
            num = [1,2,3,4,5]
            rx = random.choice(num)
            nx = [200,300,400]
            ny = [500,600,700]
            for w in range(rx):
                bolanova = Bolinha(bola_format,random.choice(nx),random.choice(ny))
                all_bolas.add(bolanova) 
                all_sprites.add(bolanova)
                bolacount += 1 
        if all_bolas == 0:
            STATE = 'Game_over'
            game = False


    #---- Atualiza de acordo com os comandos
        all_sprites.update()

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_format, (0, 0)) # Preenche com a cor branca
        all_bolas.draw(window)
        all_sprites.draw(window)
        pygame.display.update()
        

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
    return STATE



