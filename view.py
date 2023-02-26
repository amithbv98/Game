import model, pygame

class gameView:
    def __init__(self, model):
        self.model = model
        pygame.init()
        self.surface = pygame.display.set_mode(self.model.getWindowParams())
        pygame.display.set_caption('pong')
        self.BLACK = (0,0,0)

    def updateView(self):
        window_length, window_width = self.model.getWindowParams()
        self.surface.fill(self.BLACK)
        pad1Rect = pygame.Rect(self.model.getPaddle1Position(), self.model.getPaddle1Dimension())
        pygame.draw.line(self.surface, (255,255,0), [window_length // 2, 0],[window_length // 2, window_width], 1)
        pygame.draw.rect(self.surface, (255,0,0), pad1Rect)
        pad2Rect = pygame.Rect(self.model.getPaddle2Position(), self.model.getPaddle2Dimension())
        pygame.draw.rect(self.surface, (255,0,0), pad2Rect)
        pygame.draw.circle(self.surface, (0, 0 ,255), self.model.getBallPosition(), self.model.getBallRadius())
        left_score, right_score = self.model.getScore()
        self.updateScore(left_score, (40, 10))
        self.updateScore(right_score, (480, 10))
        pygame.display.update()

    def updateScore(self, score, position):
        font = pygame.font.SysFont("Comic Sans MS", 20)
        score = font.render("Score :"+str(score), 1, (0, 255, 0))
        self.surface.blit(score, position)
