class SpaceShipModule:

    def __init__(self, mass):
        self.mass = mass
        self.fuelNeeded = int(self.mass / 3) - 2

    def __str__(self):
        return "Mass: {0}, Fuel needed: {1}".format(self.mass, self.fuelNeeded)

    def countFuelForFuel(self):
        fuel = self.fuelNeeded
        fuelForFuel = 0
        while fuel > 3:
            fuelForFuel += fuel
            fuel = int(fuel / 3) - 2
        if fuel > 0:
            fuelForFuel += fuel
        return fuelForFuel