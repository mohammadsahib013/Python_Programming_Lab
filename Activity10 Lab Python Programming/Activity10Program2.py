class Dog:
    animal = 'dog'

    def __init__(self, breed):
        self.breed=breed

    def setcolour(self,colour):
        self.colour=colour

    def getcolour(self):
        return self.colour

rodger = Dog('pug')
rodger.setcolour('Brown')
print(rodger.getcolour())

