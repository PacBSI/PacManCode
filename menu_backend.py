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
pac_down1 = Imagem("pac_down1.png",10 ,10) # lembrar de ver comp e alt da img
pac_down2 = Imagem("pac_down2.png",10 ,10)
pac_left1 = Imagem("pac_left1.png",10 ,10)
pac_left2 = Imagem("pac_left2.png",10 ,10)
pac_up1 = Imagem("pac_up1.png",10 ,10)
pac_up2 = Imagem("pac_up2.png",10 ,10)
pac_right1 = Imagem("pac1.png",10 ,10)
pac_right2 = Imagem("pac2.png",10 ,10)

     # --- imagens inimigos


botao_play = Imagem("arquivo",posx ,posy) # imagem passou a ser chamado botão 
botao_instruc = Imagem("arquivo",posx ,posy)
botao_voltar = Imagem("arquivo",posx ,posy)
botao_exit = Imagem("arquivo",posx ,posy)

img_fase_tut = Imagem("first_stage.png",0 ,0) # lembrar de ver comp e alt da img
img_fase_1 = Imagem("arquivo",posx ,posy)
img_fase_2 = Imagem("arquivo",posx ,posy)
img_fase_3 = Imagem("arquivo",posx ,posy)
img_fase_4 = Imagem("arquivo",posx ,posy)
img_fase_5 = Imagem("arquivo",posx ,posy)

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
    # -------- Fase Tutorial ----------#
FPS = 10
fpsTime = pygame.time.Clock()

screen = pygame.display.set_mode((tela.x, tela.y))
fundo = pygame.image.load(img_fase_tut.arquivo)
pac1 = pygame.image.load(pac_right1.arquivo)
pac2 = pygame.image.load(pac_right2.arquivo)
pacman = 1
x = 10
y = 10
direcao = None
while True:
    
    screen.blit(fundo,(0,0))

    if pacman == 1:
        screen.blit(pac1,(x,y))
        pacman += 1
    elif pacman == 2:
        screen.blit(pac2,(x,y))
        pacman -= 1
        
       
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
        pac1 = pygame.image.load(pac_down1.arquivo)
        pac2 = pygame.image.load(pac_down2.arquivo)
        y += 12
        if y >= 550:
            direcao = "up"
            
    elif direcao == "up":
        pac1 = pygame.image.load(pac_up1.arquivo)
        pac2 = pygame.image.load(pac_up2.arquivo)
        y -= 12
        if y <= 9:
            direcao = "down"
                
    elif direcao == "left":
        pac1 = pygame.image.load(pac_left1.arquivo)
        pac2 = pygame.image.load(pac_left2.arquivo)
        x-=12
        if x <= 9:
            direcao = "right"
            
    if direcao == "right":
        pac1 = pygame.image.load(pac_right1.arquivo)
        pac2 = pygame.image.load(pac_right2.arquivo)
        x+=12
        if x >= 750:
            direcao = "left"
           
     
    pygame.display.update()
    fpsTime.tick(FPS)

        
