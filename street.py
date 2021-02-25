class Street:
  def __init__(self, id, name, lenght, intersections):
    self.id = id
    self.name = name
    self.lenght = lenght
    self.intersections = intersections

    print("Created street with id %s lenght %d and name %s" % (self.id, self.lenght, self.name))