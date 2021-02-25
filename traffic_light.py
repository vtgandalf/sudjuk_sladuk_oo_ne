from enum import enum

class LightState(enum):
  RED = 1
  GREEN = 2

class TrafficLight:
  def __init__(self, id):
    self.id = id
    self.state = LightState.RED
    self.car_queue = []

    print("Created traffic light with id: %d" % (self.id))

  def add_car_to_queue(self, car_id):
    self.car_queue.append(car_id)

  def remove_car_from_queue(self, car_id):
    self.car_queue.remove(car_id)

