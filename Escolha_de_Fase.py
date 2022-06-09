
import pygame

def escolha_de_fase(window):
    pygame.init()

    # ----- Gera tela principal
    WIDTH = 960
    HEIGHT = 1023
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Breaking Bricks')

    background = pygame.image.load('assets/img/background.png').convert_alpha()
    background_format = pygame.transform.scale(background,(WIDTH,HEIGHT))
    font = pygame.font.Font('assets/font/04B_30__.TTF', 60)
    titulo = font.render('Escolha a Fase',True,(255,255,255))
    font2 = pygame.font.Font('assets/font/04B_30__.TTF', 40)
    Fase1 = font2.render('Fase 1 [1] ',True,(0,0,0))
    fase2 = font2.render('Fase 2 [2] ',True,(0,0,0))
    fase3 = font2.render('Fase 3 [3] ',True,(0,0,0))

    rodando = True

    # ===== Loop principal =====
    while rodando:
    
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                STATE = 'QUIT'
                rodando = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    STATE = 'Fase_1'
                    rodando = False
                if event.key == pygame.K_2:
                    STATE = 'Fase_2'
                    rodando = False
                if event.key == pygame.K_3:
                    STATE = 'Fase_3'
                    rodando = False
    
        

        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(background_format, (0, 0))
        window.blit(titulo, (100, 100))
        window.blit(Fase1, (100, 300))
        window.blit(fase2, (100, 400))
        window.blit(fase3, (100, 500))
    
        # Desenhando meteoros

        pygame.display.update()  # Mostra o novo frame para o jogador

    return STATE