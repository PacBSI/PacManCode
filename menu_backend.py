#coding: utf-8
from Classes import *
import pygame
from pygame.locals import *
import sys

pygame.init()
# ------------------- * Menu * --------------------
#musicas do jogo

musica_menu = Musica("musica_menu.mp3") # classe pra criar musica

musica_fase_tut= Musica("tema.mp3")
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
pac_down3 = Imagem("pac_down3.png",10 ,10)
pac_left1 = Imagem("pac_left1.png",10 ,10)
pac_left2 = Imagem("pac_left2.png",10 ,10)
pac_left3 = Imagem("pac_left3.png",10 ,10)
pac_up1 = Imagem("pac_up1.png",10 ,10)
pac_up2 = Imagem("pac_up2.png",10 ,10)
pac_up3 = Imagem("pac_up3.png",10 ,10)
pac_right1 = Imagem("pac1.png",10 ,10)
pac_right2 = Imagem("pac2.png",10 ,10)
pac_right3 = Imagem("pac3.png",10 ,10)

     # --- imagens inimigos


botao_play = Imagem("play.png",100 ,100) # imagem passou a ser chamado botão 
botao_play_selec = Imagem("play_selec.png",100 ,100)
botao_play_focus = Imagem("play_focus.png",100 ,100)
botao_exit = Imagem("exit.png",400 ,400)
botao_exit_selec = Imagem("exit_selec.png",400 ,400)
botao_exit_focus = Imagem("exit_focus.png",400 ,400)

img_menu = Imagem("first_stage.png",0,0) #DEFINIR IMAGEM DO MENU
img_menu2 = Imagem("fundo.png",265,145)
img_fase_tut = Imagem("first_stage.png",0 ,0) 
img_fase_1 = Imagem("arquivo","posx" ,"posy")
img_fase_2 = Imagem("arquivo","posx" ,"posy")
img_fase_3 = Imagem("arquivo","posx" ,"posy")
img_fase_4 = Imagem("arquivo","posx" ,"posy")
img_fase_5 = Imagem("arquivo","posx" ,"posy")

# ----- FUNÇÕES MENU  ----------- 
play = pygame.image.load(botao_play.arquivo)
play_s = pygame.image.load(botao_play_selec.arquivo)
play_f = pygame.image.load(botao_play_focus.arquivo)
sair = pygame.image.load(botao_exit.arquivo)
sair_s = pygame.image.load(botao_exit_selec.arquivo)
sair_f = pygame.image.load(botao_exit_focus.arquivo)

screen = pygame.display.set_mode((tela.x, tela.y))
tela_menu = pygame.image.load(img_menu.arquivo)
fundo_menu = pygame.image.load(img_menu2.arquivo)
FPS = 15

def menu():
    pygame.init()
    while True:

        screen.blit(tela_menu,(0,0)) # TEM QUE SE FAZER A TELA DO MENU
        screen.blit(fundo_menu,(img_menu2.coordenada.x,img_menu2.coordenada.y))
        screen.blit(play,(botao_play.coordenada.x,botao_play.coordenada.y))
        screen.blit(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y))
        # FALTA OS OUTROS BOTÕES 
        pygame.display.update()

        Instrucoes()

def pos_mouse(img_botao,pos_botao,pos_mouse):
    
    posx= pos_botao[0] 
    posy = pos_botao[1]
    side_x, side_y = img_botao.get_size() 
    dx = posx + side_x 
    dy = posy + side_y 
    if pos_mouse[0] > posx and pos_mouse[0] < dx and pos_mouse[1] > posy and pos_mouse[1] < dy: 
        return True
    return False
        
def Instrucoes():
    pygame.init()

    while True:
        fpsTime = pygame.time.Clock()
        pmouse = pygame.mouse.get_pos() #Retorna a posicao do mouse

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
    
        #pmouse = pygame.mouse.get_pos() #Retorna a posicao do mouse

        
        if pos_mouse(play,(botao_play.coordenada.x,botao_play.coordenada.y),pmouse) == True:
            if event.type == MOUSEMOTION:
                screen.blit(play_f,(botao_play_focus.coordenada.x,botao_play_focus.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                    
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                screen.blit(play_s,(botao_play_selec.coordenada.x,botao_play_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                    
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                screen.blit(play_s,(botao_play_selec.coordenada.x,botao_play_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                tutorial()
        else:
            screen.blit(play,(botao_play.coordenada.x,botao_play.coordenada.y))
            pygame.display.flip()
            pygame.display.update()
        
        
        if pos_mouse(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y),pmouse) == True:
            if event.type == MOUSEMOTION:
                screen.blit(sair_f,(botao_exit_focus.coordenada.x,botao_exit_focus.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                    
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                screen.blit(sair_s,(botao_exit_selec.coordenada.x,botao_exit_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                    
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                screen.blit(sair_s,(botao_exit_selec.coordenada.x,botao_exit_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                pygame.quit()
                sys.exit()
        else:
            screen.blit(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y))
            pygame.display.flip()
            pygame.display.update()
        
        
         
        pygame.display.flip()
        
        pygame.display.update()
        fpsTime.tick(FPS)




# ---------- * Jogo / Backend * --------------------------
    # -------- Fase Tutorial ----------#
def tutorial():
    pygame.init()
    FPS = 15
    fpsTime = pygame.time.Clock()
    som = pygame.mixer.Sound("coin.wav")
    # Musica de fundo
    pygame.mixer.init()
    pygame.mixer.music.load(musica_fase_tut.arqMus)
    pygame.mixer.music.play()

    screen = pygame.display.set_mode((tela.x, tela.y))
    fundo = pygame.image.load(img_fase_tut.arquivo)
    pac1 = pygame.image.load(pac_right1.arquivo)
    pac2 = pygame.image.load(pac_right2.arquivo)
    pac3 = pygame.image.load(pac_right3.arquivo)
    pacman = 1
    x = 10
    y = 10
    direcao = None
    while True:
        # Animação do pacman
        screen.blit(fundo,(0,0))
        if pacman == 1:
            screen.blit(pac1,(x,y))
            pacman += 1
        elif pacman == 2:
            screen.blit(pac2,(x,y))
            pacman += 1
        elif pacman == 3:
            screen.blit(pac3,(x,y))
            pacman += 1
        elif pacman == 4:
            screen.blit(pac2,(x,y))
            pacman -= 3
            
           
        #Captura de teclas
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

        # Movimentação do pacman e alteração nas imagens conforme direção que ele anda
        if direcao == "down":
            pac1 = pygame.image.load(pac_down1.arquivo)
            pac2 = pygame.image.load(pac_down2.arquivo)
            pac3 = pygame.image.load(pac_down3.arquivo)
            y += 8
            if y >= 550:
                direcao = None
                
        elif direcao == "up":
            pac1 = pygame.image.load(pac_up1.arquivo)
            pac2 = pygame.image.load(pac_up2.arquivo)
            pac3 = pygame.image.load(pac_up3.arquivo)
            y -= 8
            if y <= 9:
                direcao = None
                    
        elif direcao == "left":
            pac1 = pygame.image.load(pac_left1.arquivo)
            pac2 = pygame.image.load(pac_left2.arquivo)
            pac3 = pygame.image.load(pac_left3.arquivo)
            x -= 8
            if x <= 9:
                direcao = None
                
        if direcao == "right":
            pac1 = pygame.image.load(pac_right1.arquivo)
            pac2 = pygame.image.load(pac_right2.arquivo)
            pac3 = pygame.image.load(pac_right3.arquivo)
            x += 8
            if x >= 750:
                direcao = None
               
         
        pygame.display.update()
        fpsTime.tick(FPS)

menu()
        
