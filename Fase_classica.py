
# ----- Importa e inicia pacotes
import pygame
import random

def fase2(window):
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
    brick_rosa = pygame.image.load('assets/img/bloco rosa.png')
    brick_rosa_format = pygame.transform.scale(brick_rosa, (BRICK_WIDTH,BRICK_HEIGHT))
    brick_roxo = pygame.image.load('assets/img/bloco roxo.png')
    brick_roxo_format = pygame.transform.scale(brick_roxo,(BRICK_WIDTH,BRICK_HEIGHT))
    brick_vermelho = pygame.image.load('assets/img/bloco vermelho escuro.png')
    brick_vermelho_format = pygame.transform.scale(brick_vermelho,(BRICK_WIDTH,BRICK_HEIGHT))
    brick_cinza = pygame.image.load('assets/img/brick_cinza.png')
    brick_cinza_format = pygame.transform.scale(brick_cinza, (BRICK_WIDTH,BRICK_HEIGHT))
    prancha = pygame.image.load('assets/img/prancha.png')
    prancha_format = pygame.transform.scale(prancha, (PRANCHA_WIDTH,PRANCHA_HEIGHT))
    bola = pygame.image.load('assets/img/bola.png')
    bola_format = pygame.transform.scale(bola,(BOLA_WIDTH,BOLA_HEIGHT))
    lot_box = pygame.image.load('assets/img/loot.png')
    lot_box_format = pygame.transform.scale(lot_box,(LOOT_BOX_WIDTH,LOOT_BOX_HEIGHT))
    hitt_sound = pygame.mixer.Sound('assets/img/sounds/hitt.wav')
    loot_sound = pygame.mixer.Sound('assets/img/sounds/loot.wav')
    prancha_sound = pygame.mixer.Sound('assets/img/sounds/pranchaa.wav')
    metal_sound = pygame.mixer.Sound('assets/img/sounds/metal.wav')
    dx = 8
    dy = 8
    x0 = BRICK_WIDTH*2
    y0 = BRICK_HEIGHT * 2
    i=10
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
            vx=[10,-10]
            self.speedx = random.choice(vx)
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

    class Invencible_Bricks(pygame.sprite.Sprite):
        def __init__(self,x0,y0):

            pygame.sprite.Sprite.__init__(self)
            self.image = brick_cinza_format
            self.rect = self.image.get_rect()
            self.rect.x = x0
            self.rect.y = y0
        

    game=True
    #----variavel para ajuste de velocidade
    clock = pygame.time.Clock()
    FPS=30

    #----Criando um grupo com todas as sprites
    all_sprites = pygame.sprite.Group()

    #----Cria tijolos
    all_bricks_vermelho = pygame.sprite.Group()
    all_bricks_rosa = pygame.sprite.Group()
    all_bricks_roxo = pygame.sprite.Group()
    listaimg = [brick_rosa_format,brick_vermelho_format,brick_roxo_format]
    for z in range (i):
        rimg = random.choice(listaimg)
        for k in range (j):
            brick=Bricks(rimg,x0,y0)
            if rimg == brick_rosa_format:
                all_bricks_rosa.add(brick)
                all_sprites.add(brick)
            elif rimg == brick_roxo_format:
                all_bricks_roxo.add(brick)
                all_sprites.add(brick)
            else:
                all_bricks_vermelho.add(brick)
                all_sprites.add(brick)
            x0+=BRICK_WIDTH + dx
        x0 = BRICK_WIDTH*2
        y0+= BRICK_HEIGHT + dy


    all_brick_cinza = pygame.sprite.Group()
    for l in range (j):
        bloco_cinza = Invencible_Bricks(x0,y0)
        all_brick_cinza.add(bloco_cinza)
        all_sprites.add(bloco_cinza)
        x0 +=BRICK_WIDTH + dx

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
                    STATE = 'Game_over'
                    game = False
                    
            if bola.rect.y <= 0:
                bola.speedy = -bola.speedy
            if bola.rect.x >= WIDTH - BOLA_WIDTH:
                bola.speedx = -bola.speedx
            if bola.rect.x <= 0:
                bola.speedx = -bola.speedx  

        hits = pygame.sprite.spritecollide(player,all_bolas,False)
        for bola in hits:
            prancha_sound.play()
            bola.quique()


        hits2 = pygame.sprite.groupcollide(all_bricks_rosa,all_bolas,True,False)
        for bloco in hits2:
            hitt_sound.play()
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
                if abs(ball.rect.x - bloco.rect.right) <= 6 or abs(ball.rect.x - bloco.rect.left) <= 6:
                    ball.speedx *= -1
                else:
                    ball.quique()
        hits3 = pygame.sprite.groupcollide(all_bricks_roxo,all_bolas,False,False)
        for bloco in hits3:
            hitt_sound.play()
            xx = bloco.rect.x
            yy = bloco.rect.y
            bloco.kill()
            brick_rosa_replace = Bricks(brick_rosa_format,xx,yy)
            all_bricks_rosa.add(brick_rosa_replace)
            all_sprites.add(brick_rosa_replace)
            for ball in hits3[bloco]:
                if abs(ball.rect.x - bloco.rect.right) <= 6 or abs(ball.rect.x - bloco.rect.left) <= 6:
                    ball.speedx *= -1
                else:
                    ball.quique()

        hits4 = pygame.sprite.groupcollide(all_bricks_vermelho,all_bolas,False,False)
        for bloco in hits4:
            hitt_sound.play()
            xx = bloco.rect.x
            yy = bloco.rect.y
            bloco.kill()
            brick_vermelho_replace = Bricks(brick_roxo_format,xx,yy)
            all_bricks_roxo.add(brick_vermelho_replace)
            all_sprites.add(brick_vermelho_replace)
            
            for ball in hits4[bloco]:
                if abs(ball.rect.x - bloco.rect.right) <= 6 or abs(ball.rect.x - bloco.rect.left) <= 6:
                    ball.speedx *= -1
                else:
                    ball.quique()
            
        hits5 = pygame.sprite.spritecollide(player,all_loot,True)
        if hits5:
            loot_sound.play()
        for t in  hits5:
            num = [1,2,3]
            rx = random.choice(num)
            nx = [200,300,400]
            ny = [500,600,700,300,400]
            for w in range(rx):
                bolanova = Bolinha(bola_format,random.choice(nx),random.choice(ny))
                all_bolas.add(bolanova) 
                all_sprites.add(bolanova)
                bolacount += 1
        hits6 = pygame.sprite.groupcollide(all_brick_cinza,all_bolas,False,False)
        for bloco in hits6:
            metal_sound.play()
            for ball in hits6[bloco]:
                ball.quique()
   
            


        





    #---- Atualiza de acordo com os comandos
        all_sprites.update()

        # ----- Gera sa??das
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_format, (0, 0)) # Preenche com a cor branca
        all_bolas.draw(window)
        all_sprites.draw(window)
        pygame.display.update()

    return STATE



