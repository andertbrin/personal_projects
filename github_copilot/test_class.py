

# crie uma classe
class Car:
    # crie um método __init__
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0
        self.gas_tank_size = 0
        self.gas_tank_capacity = 0
        self.gas_tank_level = 0
        self.gas_tank_level_percentage = 0


    # crie um método que mostre o carro
    def describe_car(self):
        print(f'This is a {self.year} {self.make} {self.model}.')

    # crie um método que mostre o odômetro
    def read_odometer(self):
        print(f'This car has {self.odometer_reading} miles on it.')

    # crie um método que altere o nivel de combustível
    def fill_gas_tank(self):
        self.gas_tank_level = self.gas_tank_capacity
        print(f'The gas tank is now full.')


# crie duas instâncias da classe car
car_1 = Car('Ford', 'Mustang', '2018')
car_2 = Car('Toyota', 'Corolla', '2019')


# chame o método describe_car para cada instância
car_1.describe_car()
car_2.describe_car()

