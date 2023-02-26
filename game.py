import pygame, model, view, controller

class pong:
	def __init__(self):
		self.model = model.gameState(8, 80, 20, 600, 400)
		self.controller = controller.eventHandler(self.model)
		self.view = view.gameView(self.model)
		self.fps = pygame.time.Clock()
		
	def startGameLoop(self):
		while True:
			for event in pygame.event.get():
				self.controller.handleEvent(event)
			self.controller.updatePosition()
			self.view.updateView()
			self.fps.tick(60)
				