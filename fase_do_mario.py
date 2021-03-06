
# ----- Importa e inicia pacotes

import pygame
import random

def fase1(window):
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
    LOOT_BOX_WIDTH = 40
    LOOT_BOX_HEIGHT = 40
    dx= 8
    dy= 8
    background = pygame.image.load('assets/img/background.png').convert()
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
    lot_box = pygame.image.load('assets/img/loot.png')
    lot_box_format = pygame.transform.scale(lot_box,(LOOT_BOX_WIDTH,LOOT_BOX_HEIGHT))
    hitt_sound = pygame.mixer.Sound('assets/img/sounds/hitt.wav')
    loot_sound = pygame.mixer.Sound('assets/img/sounds/loot.wav')
    prancha_sound = pygame.mixer.Sound('assets/img/sounds/pranchaa.wav')
    icab1 = 1 
    jcab1 = 7
    ichap1 = 1
    jchap1 = 5
    ichap2 = 1
    jchap2 = 9


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
    bola = Bolinha(bola_format,350,600)
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
            # ----- Verifica consequ??ncias
            if event.type == pygame.QUIT:
                game = False

            #----Verifica se apertou algo
            if event.type == pygame.KEYDOWN:
                #----altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx -= 18
                if event.key == pygame.K_RIGHT:
                    player.speedx += 18

            # Verifica se soltou
            if event.type == pygame.KEYUP:
                #----altera a velocidade.
                if event.key == pygame.K_LEFT:
                    player.speedx += 18
                if event.key == pygame.K_RIGHT:
                    player.speedx -= 18
        
        for bola in all_bolas:   
            if bola.rect.y >= HEIGHT - BOLA_HEIGHT:
                bola.kill()  
                bolacount -= 1
                if bolacount == 0:
                    game = False
                    STATE = 'Game_over'
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


        hits2 = pygame.sprite.groupcollide(all_bricks_vermelho,all_bolas,True,False)
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
        hits3 = pygame.sprite.groupcollide(all_bricks_cor_de_pele,all_bolas,False,False)
        if hits3:
            hitt_sound.play()
        for bloco in hits3:
            xx = bloco.rect.x
            yy = bloco.rect.y
            brick_vermelho_replace = Bricks(brick_Vermelho_format,xx,yy)
            all_bricks_vermelho.add(brick_vermelho_replace)
            all_sprites.add(brick_vermelho_replace)
            bloco.kill()
            for ball in hits3[bloco]:
                if abs(ball.rect.x - bloco.rect.right) <= 5 or abs(ball.rect.x - bloco.rect.left) <= 5:
                    ball.speedx *= -1
                else:
                    ball.quique()

        hits4 = pygame.sprite.groupcollide(all_bricks_marrom,all_bolas,False,False)
        if hits4:
            hitt_sound.play()
        for bloco in hits4:
            xx = bloco.rect.x
            yy = bloco.rect.y
            brick_cor_de_pele_replace = Bricks(brick_cor_de_pele_format,xx,yy)
            all_bricks_cor_de_pele.add(brick_cor_de_pele_replace)
            all_sprites.add(brick_cor_de_pele_replace)
            bloco.kill()
            for ball in hits4[bloco]:
                if abs(ball.rect.x - bloco.rect.right) <= 5 or abs(ball.rect.x - bloco.rect.left) <= 5:
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
            ny = [500,600,700,400,300]
            for w in range(rx):
                bolanova = Bolinha(bola_format,random.choice(nx),random.choice(ny))
                all_bolas.add(bolanova) 
                all_sprites.add(bolanova)
                bolacount += 1
        if all_bricks_cor_de_pele == 0:
            STATE = 'Game_over'
            game = False
            


        





    #---- Atualiza de acordo com os comandos
        all_sprites.update()

        # ----- Gera sa??das
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

    return STATE

