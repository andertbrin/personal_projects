

# crie uma classe Car
class Car:
    # crie um método __init__
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    # crie um método que mostre o carro
    def describe_car(self):
        print(f"This car is a {self.year} {self.make} {self.model}.")


    # crie um método que mostre o odômetro using kilometers
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} kilometers on it.")


# crie duas instâncias da classe Car
car_1 = Car('Ford', 'Mustang', '2015')
car_2 = Car('Dodge', 'Viper', '2015')


# chame o método describe_car para cada instância
car_1.describe_car()
car_2.describe_car()

# altere o valor do odômetro de cada instância
car_1.odometer_reading = 23
car_2.odometer_reading = 34




