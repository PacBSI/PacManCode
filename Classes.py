# Arquivos com classes PacMan
# Autores: Antonio Jorge / Igor Camilo / Edvan Soares / Breno Ferys
# -*- coding: utf-8 -*-

import pygame
import sys, os

PONTOS_INICIAIS = 0
NUM_VIDAS = 3
PONTOS_CANETA = 10

class Coordenada:
	def __init__ (self, x ,y):
		self.x = int(x)
		self.y = int(y)


class Imagem:
	def __init__(self, arquivo, comprimento, altura,x ,y):
		
		self.arquivo = str(arquivo)
		self.comprimento = int(comprimento)
		self.altura = int(altura)
		self.coordenada = Coordenada(x, y)
		
class Personagem:
	def __init__(self,nome,x, y, arquivo, comprimento,altura):
		
		self.nome = str(nome)
		self.imagem = Imagem(arquivo, comprimento, altura, x, y)
	
	def andar(self, deslocx, deslocy):
		self.x = self.x + deslocx
		self.y = self.y + deslocy


class Aluno(Personagem):
	def __init__(self,nome, x, y, arquivo, comprimento,altura):
		Personagem.__init__(self, nome, x, y, arquivo,comprimento,altura)
		self.pontos = PONTOS_INICIAIS
		self.vidas = NUM_VIDAS
		
	def ganhar_pontos(self):
		self.pontos = self.pontos + PONTOS_CANETA 

	def perda_vida(self):
		self.vidas = self.vidas - 1

	def esta_morto(self):
		if self.vidas == 0:
			return True
		else:
			return False

class Professor(Personagem):
	def __init__(self, nome, x, y, arquivo, comprimento,altura):
		Personagem.__init__(self, nome,x,y)
		self.imagem_prof = Imagem(arquivo, comprimento,altura,x,y)
		self.status = False
		

	def morte_professor(self):
		self.status = True

class Tempo:
	def __init__(self, tempo):
		self.tempo = tempo

	def d_tempo(self,tempo):
		self.tempo = self.tempo + tempo



class Caneta():
	def __init__(self,arquivo, comprimento, altura,x ,y):
		self.imagem_caneta = Imagem(arquivo, comprimento, altura,x ,y)
		self.coordenada_caneta =Coordenada(x, y)
		self.pontos_caneta = PONTOS_CANETA
		

class Som:
	def __init__(self, arquivo):
		self.arqSom = arquivo

class Musica:
	def __init__(self, arquivo):
		self.arqMus = arquivo

class Obstaculo:
	def __init__(self, arquivo, comprimento, altura, x, y):
		self.imagem_obst = Imagem(arquivo, comprimento, altura,x ,y)
		self.coordenada_obst = (x, y)


