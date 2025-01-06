class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along")


my_car = Vehicle("Telsa", "Model 3")

print(my_car.model)
print(my_car.make)
my_car.moves()


# inheritance

class Airplane(Vehicle):
    def __init__(self, make, model,id):
        super().__init__(make, model)
        self.id = id
    def moves(self):
        print("Flies along")

class Truck(Vehicle):
    def moves(self):
        print("Rumbles along")

class GolfCart(Vehicle):
   pass


cessna = Airplane("Cessna", "Skybank","poo")
mack = Truck("truck Cessna", "Skybank")
golf = GolfCart("gokf Cessna", "Skybank")

cessna.moves()

mack.moves()

golf.moves()