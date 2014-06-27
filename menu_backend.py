from Classes import *
import pygame
from pygame.locals import *

pygame.init()
# ------------------- * Menu * --------------------
#musicas do jogo

musica_menu = Musica("musica_menu.mp3") # classe pra criar musica

musica_fase_tut= Musica("nome do arquivo")
musica_fase_1= Musica("nome do arquivo")
musica_fase_2= Musica("nome do arquivo")
musica_fase_3= Musica("nome do arquivo")
musica_fase_4= Musica("nome do arquivo")
musica_fase_5= Musica("nome do arquivo")

#Sons
som_inicio_jogo = Som("play.mp3")
som_mudanca_opcao = Som("arq som")
som_press_opcao = Som("arq press")
som_coleta = Som("arq")
som_morreu = Som("arq")
som_coleta_bonus = Som("arq")


#Imagens / tela
tela = Coordenada(800,600)
pygame.display.set_caption("PacMan BSI")
    
    # imagem personagem
img_personagem_stop = Imagem("aaa.png", "", "",10 ,10) # lembrar de ver comp e alt da img
img_personagem_mov1 = Imagem("arquivo", "comprimento", "altura",posx ,posy)

     # --- imagens inimigos


botao_play = Imagem("arquivo", "comprimento", "altura",posx ,posy) # imagem passou a ser chamado botão 
botao_instruc = Imagem("arquivo", "comprimento", "altura",posx ,posy)
botao_voltar = Imagem("arquivo", "comprimento", "altura",posx ,posy)
botao_exit = Imagem("arquivo", "comprimento", "altura",posx ,posy)

img_fase_tut = Imagem("first_stage.png", 800, 600,0 ,0) # lembrar de ver comp e alt da img
img_fase_1 = Imagem("arquivo", "comprimento", "altura",posx ,posy)
img_fase_2 = Imagem("arquivo", "comprimento", "altura",posx ,posy)
img_fase_3 = Imagem("arquivo", "comprimento", "altura",posx ,posy)
img_fase_4 = Imagem("arquivo", "comprimento", "altura",posx ,posy)
img_fase_5 = Imagem("arquivo", "comprimento", "altura",posx ,posy)

# ----- Funções menu

def verificaMouse(img_botao,pos_botao,pos_mouse):#mudar variáveis
    img_x, img_y = pos_botao 
    img_w, img_h = img_botao.get_size() 
    varia_x = img_x + img_w 
    varia_y = img_y + img_h 
    if pos_mouse[0] > img_x and pos_mouse[0] < varia_x and pos_mouse[1] > img_y and pos_mouse[1] < varia_y: 
        return True
    return False
        
def Instrucoes():
    
    imagem_instrucoes = Imagem("arquivo", "comprimento", "altura",posx ,posy)
    
    while True:
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        xy = pygame.mouse.get_pos() #Recupera a posicao do mouse

        screen.blit(imagem_instrucoes,(0,0))
        
        if verificaMouse(botao_voltar,(46,531),xy) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
               # MenuInicial()
               # Cliquesom.play()
         
        pygame.display.flip()
        
    pygame.display.update()
    fpsTime.tick(FPS)






# ---------- * Jogo / Backend * --------------------------

FPS = 30
fpsTime = pygame.time.Clock()

screen = pygame.display.set_mode((tela.x,tela.y))
fundo = pygame.image.load(img_fase_tut.arquivo)
personagem = pygame.image.load(img_personagem_stop.arquivo)
#x = 10
#y = 10
direcao = None
while True:
    screen.blit(fundo,(0,0))
    screen.blit(personagem,(img_personagem_stop.coordenada.x,img_personagem_stop.coordenada.y))
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if keys[K_DOWN]:
            direcao = "down"
        elif keys[K_UP]:
            direcao = "up"
        elif keys[K_LEFT]:
            direcao = "left"
        elif keys[K_RIGHT]:
            direcao = "right"
        elif keys[K_ESCAPE]:
            direcao = None
    
    if direcao == "down":
        img_personagem_stop.coordenada.y += 4
    if direcao == "up":
        img_personagem_stop.coordenada.y -= 4
    if direcao == "left":
        img_personagem_stop.coordenada.x -= 4
    if direcao == "right":
        img_personagem_stop.coordenada.x += 4
        
