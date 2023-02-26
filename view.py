import model, pygame

class gameView:
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.surface = pygame.display.set_mode(self.model.getWindowParams())
        pygame.display.set_caption('pong')
        self.BLACK = (0,0,0)

    def updateView(self):
        self.surface.fill(self.BLACK)
        pad1Rect = pygame.Rect(self.model.getPaddle1Position(), self.model.getPaddle1Dimension())
        pygame.draw.rect(self.surface, (255,0,0), pad1Rect)
        pad2Rect = pygame.Rect(self.model.getPaddle2Position(), self.model.getPaddle2Dimension())
        pygame.draw.rect(self.surface, (255,0,0), pad2Rect)
        pygame.draw.circle(self.surface, (0, 0 ,255), self.model.getBallPosition(), self.model.getBallRadius())
        pygame.display.update()
