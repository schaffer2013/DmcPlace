class Pixel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.value=False
        #print(str(self.x)+ " " + str(self.y)+ " " + str(self.value))
        
    def printValue(self):
        print(self.value)
