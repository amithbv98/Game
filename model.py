import entity
class gameState():
    def __init__(self, paddle_width, paddle_height, ball_radius, window_length, window_width):
        self.paddle1 = entity.paddle([paddle_width, paddle_height], [0,0], (0, window_width//2 - paddle_height//2))
        self.paddle2 = entity.paddle([paddle_width, paddle_height], [0,0], [window_length - paddle_width, window_width//2 - paddle_height//2])
        self.ball = entity.ball(ball_radius, [0,0], [window_length//2, window_width//2])        
        self.window_length = window_length
        self.window_width = window_width
        self.setBallVelocity((1,1))
        
    def setPaddle1Position(self, position):
        self.paddle1.setPosition(position)
    
    def getPaddle1Position(self):
        return self.paddle1.getPosition()

    def setPaddle2Position(self, position):
        self.paddle2.setPosition(position)
    
    def getPaddle2Position(self):
        return self.paddle2.getPosition()
        
    def setPaddle1Velocity(self, velocity):
        self.paddle1.setVelocity(velocity)
       
    def getPaddle1Velocity(self):
        return self.paddle1.getVelocity()
    
    def setPaddle2Velocity(self, velocity):
        self.paddle2.setVelocity(velocity)
    
    def getPaddle2Velocity(self):
        return self.paddle2.getVelocity()
   
    def setBallPosition(self, position):
        self.ball.setPosition(position)
    
    def setBallVelocity(self, velocity):
        self.ball.setVelocity(velocity)
    
    def getBallPosition(self):
        return self.ball.getPosition()
    
    def getBallVelocity(self):
        return self.ball.getVelocity()
        
    def setPaddle1Dimension(self, dimension):
        self.paddle1.setDimension(dimension)
    
    def getPaddle1Dimension(self):
        return self.paddle1.getDimensions()
        
    def setPaddle2Dimension(self, dimension):
        self.paddle2.setDimension(dimension)
    
    def getPaddle2Dimension(self):
        return self.paddle2.getDimensions()
        
    def setBallRadius(self, radius):
        self.ball.setRadius(radius)
    
    def getBallRadius(self):
        return self.ball.getRadius()
        
    def getWindowParams(self):
        return self.window_length, self.window_width
    
    
    
        
        