#Part 1
from abc import ABC, abstractmethod
class Aircraft(ABC):
  def __str__(self):
    return self.__class__.__name__

  @abstractmethod
  def speed(self):
    pass
#Part 2
class Airplane(Aircraft):
  def speed(self):
    print("Airplane speed: 150 mph")

class Helicopter(Aircraft):
  def speed(self):
    print("Helicopter speed: 120 mph")

#Part 3
h = Helicopter()
a = Airplane()
print(h)
a.speed()