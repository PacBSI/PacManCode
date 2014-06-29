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
pac_down1 = Imagem("pac_down1.png",10 ,10) 
pac_down2 = Imagem("pac_down2.png",10 ,10)
pac_left1 = Imagem("pac_left1.png",10 ,10)
pac_left2 = Imagem("pac_left2.png",10 ,10)
pac_up1 = Imagem("pac_up1.png",10 ,10)
pac_up2 = Imagem("pac_up2.png",10 ,10)
pac_right1 = Imagem("pac1.png",10 ,10)
pac_right2 = Imagem("pac2.png",10 ,10)

     # --- imagens inimigos


botao_play = Imagem("play.png",100 ,100) # imagem passou a ser chamado botão 
botao_instruc = Imagem("instrucao.png",posx ,posy)
botao_voltar = Imagem("voltar.png",posx ,posy)
botao_exit = Imagem("exit.png",400 ,400)

img_menu = Imagem("arquivo",0,0) #DEFINIR IMAGEM DO MENU
img_fase_tut = Imagem("first_stage.png",0 ,0) 
img_fase_1 = Imagem("arquivo",posx ,posy)
img_fase_2 = Imagem("arquivo",posx ,posy)
img_fase_3 = Imagem("arquivo",posx ,posy)
img_fase_4 = Imagem("arquivo",posx ,posy)
img_fase_5 = Imagem("arquivo",posx ,posy)

# ----- FUNÇÕES MENU  ----------- 
play = pygame.image.load(botao_play.arquivo)
sair = pygame.image.load(botao_exit.arquivo)
tela_menu = pygame.image.load(img_menu.arquivo)
FPS = 15

def menu():
    
    while True:

        screen.blit(tela_menu,(0,0)) # TEM QUE SE FAZER A TELA DO MENU
        screen.blit(play,(botao_play.coordenada.x,botao_play.coordenada.y))
        screen.blit(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y))
        # FALTA OS OUTROS BOTÕES 
        pygame.display.update()

        Instrucoes()

def pos_mouse(img_botao,pos_botao,pos_mouse):
    
    posx= pos_botao[0] 
    posy = pos_botao[1]
    side_x, side_y = img_botao.get_size() 
    dx = img_x + side_x 
    dy = img_y + side_y 
    if pos_mouse[0] > posx and pos_mouse[0] < dx and pos_mouse[1] > posy and pos_mouse[1] < dy: 
        return True
    return False
        
def Instrucoes():
    

    while True:
        fpsTime = pygame.time.Clock()
    
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        pmouse = pygame.mouse.get_pos() #Retorna a posicao do mouse
        
        if mouse(play,(botao_play.coordenada.x,botao_play.coordenada.y),pmouse) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
               tutorial()
        if mouse(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y),pmouse) == True:
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
               pygame.quit()
               sys.exit()
        else:
            continue
         
        pygame.display.flip()
        
        pygame.display.update()
        fpsTime.tick(FPS)




# ---------- * Jogo / Backend * --------------------------
    # -------- Fase Tutorial ----------#
def tutorial():
    FPS = 15
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

        
