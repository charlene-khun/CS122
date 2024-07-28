#Part 1
class Vehicle:
  def __init__(self, brand = "BMW", model = "430i", year = 2020):
    self.__brand = brand
    self.__model = model
    self.__year = year
  def start(self):
    print("Vehicle started")
  def stop(self):
    print("Vehicle stopped")
  def accelerate(self):
    print("Vehicle accelerated")
  def displayInfo(self):
      print("Brand:" + str(self.__brand))
      print("Model:" + str(self.__model))
      print("Year:" + str(self.__year))


#Part 2
class Bike(Vehicle):
  def __init__(self, brand, model, year):
    super().__init__(brand, model, year)
    self.displayInfo()

#Part 3
class Car(Vehicle):
  def __init__(self, brand, model, year, numberofDoors):
    super().__init__(brand, model, year)
    self.__numberOfDoors = numberofDoors
  def displayInfo(self):
    super().displayInfo()
    print("Number of Doors:", self.__numberOfDoors)

#Part 4
class ElectricCar(Car):
  def __init__(self, brand, model, year, numberofDoors, batteryCapacity):
    super().__init__(brand, model, year, numberofDoors)
    self.__batteryCapacity = batteryCapacity
  def charging(self):
    print("Charging electric car")
  def displayInfo(self):
    super().displayInfo()
    print("Battery Capacity:" + self.__batteryCapacity)

#Part 5
bike1 = Bike("Santa Cruz", "Model 5", 2024)
bike1.start()
print("")

electricCar1 = ElectricCar("Tesla", "Model X", 2022, numberofDoors = 4, batteryCapacity = "80%")
electricCar1.displayInfo()
electricCar1.charging()