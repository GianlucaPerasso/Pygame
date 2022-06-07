import pygame

pygame.init()


# ----- Gera tela principal
WIDTH = 960
HEIGHT = 1023
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Breaking Bricks')

background = pygame.image.load('assets/img/background.png').convert_alpha()
background_format = pygame.transform.scale(background,(WIDTH,HEIGHT))
font = pygame.font.Font('assets/font/04B_30__.TTF', 60)
titulo = font.render('BREAKING BRICKS',True,(0,0,0))
font2 = pygame.font.Font('assets/font/04B_30__.TTF', 30)
sub_titulo = font2.render('Aperte qualquer botao para comecar',True,(255,255,255))
game = True

# ===== Loop principal =====
while game:
 
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

   
    

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(background_format, (0, 0))
    window.blit(titulo, (100, 100))
    window.blit(sub_titulo, (100, 200))
    # Desenhando meteoros

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

