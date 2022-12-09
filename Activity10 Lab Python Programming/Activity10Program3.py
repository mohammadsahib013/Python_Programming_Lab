class bus:
    def __init__(self, speed, model, mileage):
        self.speed = speed
        self.model = model
        self.mileage = mileage

    def display(self):
        print('vehicle max speed is', self.speed)
        print('vehicle model is', self.model)
        print('vehicle mileage is', self.mileage)

class derived(bus):
    def __init__(self, speed, model, mileage, colour, regno):
        self.colour = colour
        self.regno = regno
        bus.__init__(self, speed,  model, mileage)

    def disp(self):
        print('vehicle colour is', self.colour )
        print('vehicle registration is', self.regno )

vehicle = derived('180kmph', 2022, '24km', 'black', '12N09042')
vehicle.display()
vehicle.disp()       
