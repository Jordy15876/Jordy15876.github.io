class Vehicle(object):
  def __init__(self, make, color):
    self.make = make
    self.color = color

  def info(self):
    print("This car is a {}, the color is {}.".format(self.make, self.color))

class DriverlessCar(Vehicle):
  def __init__(self, make, color, top_speed, object_detected):
    super(DriverlessCar, self).__init__(make, color)
    self.top_speed = top_speed
    self.objected_detected = object_detected

  def drive(self):
    print ("The car is driving at {}km/h, and it can detect objects {} metres away.".format(self.top_speed, self.objected_detected))

car = DriverlessCar("NIssan Skyline", "Black", 200, 80)

car.info()
car.drive()