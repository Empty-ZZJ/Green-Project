# coding=UTF-8
import pygame, sys
from settings import *
from level import Level
import os
current_path = os.path.dirname(__file__)
print("Hello World! 绿色守护者！")
print(os.getcwd())
os.chdir(os.getcwd())
class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('绿色守护者')
		self.clock = pygame.time.Clock()
		self.level = Level()
		main_sound = pygame.mixer.Sound('./audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
if __name__ == '__main__':
	game = Game()
	game.run()