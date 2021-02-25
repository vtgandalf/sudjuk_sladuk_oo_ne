from traffic_light import TrafficLight

class Intersection:
  def __init__(self, id, lights, schedule):
    self.id = id
    self.queue = None
    self.lights = lights
    self.scheduler = schedule
    print("Created an intersection with id %d " %(self.id))
