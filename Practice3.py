mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
J = len(mytuple)
i = 0
while i < J:
    print(next(myit))
    i += 1


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    x = self.a
    self.a += 1
    return x
myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
  print(x)


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Drive!")
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Sail!")
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")     
for x in (car1, boat1, plane1):
  x.move()


class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print(f"{self.brand} {self.model}: Drive!")
  def __str__(self):
    return f"Car: {self.brand} {self.model}"
class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print(f"{self.brand} {self.model}: Sail!")
  def __str__(self):
    return f"Boat: {self.brand} {self.model}"
class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print(f"{self.brand} {self.model}: Fly!")
  def __str__(self):
    return f"Plane: {self.brand} {self.model}"
car1 = Car("Ford", "Mustang") 
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")
print(car1)  
print(boat1)
print(plane1)
for x in (car1, boat1, plane1):
  x.move()


class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  def move(self):
    print("Move!")
class Car(Vehicle):
  pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")
class Plane(Vehicle):
  def move(self):
    print("Fly!")
car1 = Car("Ford", "Mustang") 
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747") 
for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()