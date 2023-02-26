import pygame, sys
from pygame.locals import *
class eventHandler:
    def __init__(self,model):
        self.model = model

    def handleEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                self.model.setPaddle1Velocity([0, -8])
            elif event.key == K_DOWN:
                self.model.setPaddle1Velocity([0, 8]) 
            elif event.key == K_w:
                self.model.setPaddle2Velocity([0, -8]) 
            elif event.key == K_s:
                self.model.setPaddle2Velocity([0, 8]) 
        elif event.type == KEYUP:
            if event.key == K_w or event.key == K_s:
                self.model.setPaddle2Velocity([0, 0])
            elif event.key == K_UP or event.key == K_DOWN:
                self.model.setPaddle1Velocity([0, 0])
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    def updatePosition(self):
        p1left, p1top = self.model.getPaddle1Position()           
        p2left, p2top = self.model.getPaddle2Position()
        p1velX, p1velY = self.model.getPaddle1Velocity()
        p2velX, p2velY = self.model.getPaddle2Velocity()        
        winlength, winwidth = self.model.getWindowParams()
        ball_x, ball_y = self.model.getBallPosition()
        ballv_x, ballv_y = self.model.getBallVelocity()
        radius = self.model.getBallRadius()
        left_score, right_score = self.model.getScore()
        paddlewidth, paddleheight = self.model.getPaddle1Dimension()
        if (p1top != 0 and p1velY < 0):
            self.model.setPaddle1Position((p1left, p1top+p1velY))
        elif p1top+paddleheight != winwidth and p1velY > 0:
            self.model.setPaddle1Position((p1left, p1top+p1velY))
        if (p2top != 0 and p2velY < 0):
            self.model.setPaddle2Position((p2left, p2top+p2velY))
        elif p2top+paddleheight != winwidth and p2velY > 0:
            self.model.setPaddle2Position((p2left, p2top+p2velY))
        if ball_y == winwidth - radius or ball_y == radius:
            self.model.setBallVelocity((ballv_x, -ballv_y))
        if ball_x == winlength or ball_x == 0:
            self.model.setBallVelocity((-ballv_x, ballv_y))
        
        if ball_x <= radius + paddlewidth and ball_y in range(p1top,p1top+paddleheight,1):
            self.model.setBallVelocity((-ballv_x, ballv_y))
        elif ball_x <= radius + paddlewidth:
            self.model.setScore((left_score, right_score+1))
            self.model.__init__(8, 80, 20, 600, 480)
        
        if ball_x >= winlength  - radius - paddlewidth and ball_y in range(p2top,p2top + paddleheight,1):
            self.model.setBallVelocity((-ballv_x, ballv_y))
        elif ball_x >= winlength - radius - paddlewidth:
            self.model.setScore((left_score+1, right_score))
            self.model.__init__(8, 80, 20, 600, 480)
        newball_x, newball_y = self.model.getBallPosition()
        newballv_x, newballv_y = self.model.getBallVelocity()
        self.model.setBallPosition((newball_x+newballv_x, newball_y+newballv_y))
                    
           
        
            
