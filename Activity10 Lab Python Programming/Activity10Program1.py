class Dog:
    animal = "dog"

    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

Rodger = Dog('pug', 'brown')
Buzu = Dog('billdog', 'black')

print("rodger details:")
print('rodger is a', Rodger.animal)
print('breed:', Rodger.breed)
print('colour:', Rodger.colour)

print("Buzu details:")
print('Buzu is a', Buzu.animal)
print('breed:', Buzu.breed)
print('colour:', Buzu.colour)