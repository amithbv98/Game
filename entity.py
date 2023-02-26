class thing:
    def __init__(self, velocity: list[int, int], position: tuple((int,int))):
        self.velocity = velocity
        self.position = position
        
    def setPosition(self, position: list[int, int]):
        self.position = position
    
    def getPosition(self):
        return self.position
        
    def setVelocity(self, velocity: list[int, int]):
        self.velocity = velocity
        
    def getVelocity(self):
        return self.velocity

class ball(thing):
    def __init__(self, radius: int, velocity: list[int, int], position: tuple((int,int))):
        thing.__init__(self, velocity, position)
        self.radius = radius
        
    def setRadius(self, radius: int):
        self.radius = radius
    
    def getRadius(self):
        return self.radius
    
class paddle(thing):
    def __init__(self, dimensions: tuple((int, int)), velocity: list[int, int], position: tuple((int, int))):
        thing.__init__(self, velocity, position)
        self.dimensions = dimensions
       
    def setDimensions(self, dimensions):
        self.dimensions = dimensions
        
    def getDimensions(self):
        return self.dimensions