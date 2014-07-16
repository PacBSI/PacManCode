#coding: utf-8
from Classes import *
import pygame
from pygame.locals import *
import sys

pygame.init()
# ------------------- * Menu * --------------------
#musicas do jogo

musica_menu = Musica("musica_menu.mp3") 

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
pygame.display.set_caption("PacBSI")
    
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

     # --- imagens  botão
botao_play = Imagem("play.png",276 ,200)  
botao_play_selec = Imagem("play_selec.png",276 ,200)
botao_play_focus = Imagem("play_focus.png",276 ,200)
botao_exit = Imagem("exit.png",276 ,280)
botao_exit_selec = Imagem("exit_selec.png",276 ,280)
botao_exit_focus = Imagem("exit_focus.png",276 ,280)
img_pause = Imagem("pause1.png",276,200)
botao_voltar = Imagem("voltar1.png",276,280)
botao_voltar_focus = Imagem("voltar2.png",276,280)
botao_voltar_selec = Imagem("voltar3.png",276,280)
img_sair = Imagem("pacsair.png",140,110)
botao_sim = Imagem("sim1.png",200,300)
botao_sim_focus = Imagem("sim2.png",200,300)
botao_sim_selec = Imagem("sim3.png",200,300)
botao_nao = Imagem("nao1.png",430,300)
botao_nao_focus = Imagem("nao2.png",430,300)
botao_nao_selec = Imagem("nao3.png",430,300)

    # ---Imagens fases e menu
img_menu = Imagem("first_stage.png",0,0) 
img_menu2 = Imagem("fundo.png",265,145)
img_fase_tut = Imagem("first_stage.png",0 ,0) 
img_fase_1 = Imagem("arquivo","posx" ,"posy")
img_fase_2 = Imagem("arquivo","posx" ,"posy")
img_fase_3 = Imagem("arquivo","posx" ,"posy")
img_fase_4 = Imagem("arquivo","posx" ,"posy")
img_fase_5 = Imagem("arquivo","posx" ,"posy")
    
    # --- imagens obstaculos
img_block = Imagem("block.png",60,50)
img_blockg = Imagem("block2.png",540,190)
img_carros = Imagem("carros.png",540,50)
img_logo = Imagem("logo.png",540,460)

# ----- FUNÇÕES E IMAGENS DO MENU  ----------- 
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
    global event

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
                exit()

        else:
            screen.blit(sair,(botao_exit.coordenada.x,botao_exit.coordenada.y))
            pygame.display.flip()
            pygame.display.update()
        
        
        pygame.display.update()
        fpsTime.tick(FPS)
# -------- Função para pausar
def pause():
    pygame.init()
    pause = pygame.image.load(img_pause.arquivo)
    voltar = pygame.image.load(botao_voltar.arquivo)
    voltar_f = pygame.image.load(botao_voltar_focus.arquivo)
    voltar_s = pygame.image.load(botao_voltar_selec.arquivo)
    global event
    
    while True:
        fpsTime = pygame.time.Clock()
        pmouse = pygame.mouse.get_pos() #Retorna a posicao do mouse
        screen.blit(pause,(img_pause.coordenada.x,img_pause.coordenada.y))
        screen.blit(voltar,(botao_voltar.coordenada.x,botao_voltar.coordenada.y))

        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit()
               pygame.quit()


        if pos_mouse(voltar,(botao_voltar.coordenada.x,botao_voltar.coordenada.y),pmouse) == True:
            if event.type == MOUSEMOTION:
                screen.blit(voltar_f,(botao_voltar_focus.coordenada.x,botao_voltar_focus.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                        
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                screen.blit(voltar_s,(botao_voltar_selec.coordenada.x,botao_voltar_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                        
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                screen.blit(voltar_s,(botao_voltar_selec.coordenada.x,botao_voltar_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                pygame.mouse.set_pos((0,0))
                return True
                break

        pygame.display.flip()
        
        pygame.display.update()
        fpsTime.tick(FPS)
    
# ------- Função para sair 
def exit():
    pacsair = pygame.image.load(img_sair.arquivo)
    sim = pygame.image.load(botao_sim.arquivo)
    sim_f = pygame.image.load(botao_sim_focus.arquivo)
    sim_s = pygame.image.load(botao_sim_selec.arquivo)
    nao = pygame.image.load(botao_nao.arquivo)
    nao_f = pygame.image.load(botao_nao_focus.arquivo)
    nao_s = pygame.image.load(botao_nao_selec.arquivo)
    global event
    
    while True:
        fpsTime = pygame.time.Clock()
        pmouse = pygame.mouse.get_pos() #Retorna a posicao do mouse
        screen.blit(pacsair,(img_sair.coordenada.x,img_sair.coordenada.y))
        screen.blit(sim,(botao_sim.coordenada.x,botao_sim.coordenada.y))
        screen.blit(nao,(botao_nao.coordenada.x,botao_nao.coordenada.y))

        for event in pygame.event.get():
            if event.type == QUIT:
               sys.exit()
               pygame.quit()


        if pos_mouse(sim,(botao_sim.coordenada.x,botao_sim.coordenada.y),pmouse) == True:
            if event.type == MOUSEMOTION:
                screen.blit(sim_f,(botao_sim_focus.coordenada.x,botao_sim_focus.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                        
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                screen.blit(sim_s,(botao_sim_selec.coordenada.x,botao_sim_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                        
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                screen.blit(sim_s,(botao_sim_selec.coordenada.x,botao_sim_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                sys.exit()
                pygame.quit()

        if pos_mouse(nao,(botao_nao.coordenada.x,botao_nao.coordenada.y),pmouse) == True:
            if event.type == MOUSEMOTION:
                screen.blit(nao_f,(botao_nao_focus.coordenada.x,botao_nao_focus.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                            
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                screen.blit(nao_s,(botao_nao_selec.coordenada.x,botao_nao_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                            
            elif event.type == MOUSEBUTTONUP and event.button == 1:
                screen.blit(nao_s,(botao_nao_selec.coordenada.x,botao_nao_selec.coordenada.y))
                pygame.display.flip()
                pygame.display.update()
                pygame.mouse.set_pos((0,0))
                return True
                break

        pygame.display.flip()
        pygame.display.update()
        fpsTime.tick(FPS)


# ---------- Colisões ----------
def colisao(img1,img2,(x1,y1),(x2,y2)):
    rect1 = img1.get_rect()
    rect2 = img2.get_rect()
    rect1.x, rect1.y = x1,y1
    rect2.x, rect2.y = x2,y2

    colidiu = rect1.colliderect(rect2)
    if colidiu == True:
        return True

    else:
        return False


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
    #pygame.mixer.music.play()

    screen = pygame.display.set_mode((tela.x, tela.y))
    fundo = pygame.image.load(img_fase_tut.arquivo)
    block = pygame.image.load(img_block.arquivo)
    blockg = pygame.image.load(img_blockg.arquivo)
    carros = pygame.image.load(img_carros.arquivo)
    logo = pygame.image.load(img_logo.arquivo)

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
            elif keys[K_p]:
                direcao = None
                pause()
                continue
            elif keys[K_q]:
                direcao = None
                exit()




        # Movimentação do pacman e alteração nas imagens conforme direção que ele anda
        if direcao == "down":
            pac1 = pygame.image.load(pac_down1.arquivo)
            pac2 = pygame.image.load(pac_down2.arquivo)
            pac3 = pygame.image.load(pac_down3.arquivo)
            y += 8
            if y >= 550:
                direcao = "up"

                
        elif direcao == "up":
            pac1 = pygame.image.load(pac_up1.arquivo)
            pac2 = pygame.image.load(pac_up2.arquivo)
            pac3 = pygame.image.load(pac_up3.arquivo)
            y -= 8
            if y <= 9:
                direcao = "down"
                    
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
                direcao = "left"

        if colisao(pac1,block,(x,y),(60,50)) or colisao(pac2,block,(x,y),(60,50)) or colisao(pac3,block,(x,y),(60,50)):
            direcao = None

        if colisao(pac1,block,(x,y),(60,190)) or colisao(pac2,block,(x,y),(60,190)) or colisao(pac3,block,(x,y),(60,190)):
            direcao = None

        if colisao(pac1,block,(x,y),(60,325)) or colisao(pac2,block,(x,y),(60,325)) or colisao(pac3,block,(x,y),(60,325)):
            direcao = None

        if colisao(pac1,block,(x,y),(60,460)) or colisao(pac2,block,(x,y),(60,460)) or colisao(pac3,block,(x,y),(60,460)):
            direcao = None

        if colisao(pac1,block,(x,y),(300,50)) or colisao(pac2,block,(x,y),(300,50)) or colisao(pac3,block,(x,y),(300,50)):
            direcao = None

        if colisao(pac1,block,(x,y),(300,190)) or colisao(pac2,block,(x,y),(300,190)) or colisao(pac3,block,(x,y),(300,190)):
            direcao = None

        if colisao(pac1,block,(x,y),(300,325)) or colisao(pac2,block,(x,y),(300,325)) or colisao(pac3,block,(x,y),(300,325)):
            direcao = None

        if colisao(pac1,block,(x,y),(300,460)) or colisao(pac2,block,(x,y),(300,460)) or colisao(pac3,block,(x,y),(300,460)):
            direcao = None

        if colisao(pac1,carros,(x,y),(540,50)) or colisao(pac2,carros,(x,y),(540,50)) or colisao(pac3,block,(x,y),(540,50)):
            direcao = None

        if colisao(pac1,blockg,(x,y),(540,190)) or colisao(pac2,blockg,(x,y),(540,190)) or colisao(pac3,blockg,(x,y),(540,190)):
            direcao = None

        if colisao(pac1,logo,(x,y),(540,460)) or colisao(pac2,logo,(x,y),(540,460)) or colisao(pac3,logo,(x,y),(540,460)):
            direcao = None
             
         
        pygame.display.update()
        fpsTime.tick(FPS)

menu()
        
