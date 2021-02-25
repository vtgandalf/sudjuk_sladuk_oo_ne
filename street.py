class Street:
  def __init__(self, id, lenght, intersections):
    self.id = id
    self.lenght = lenght
    self.intersections = intersections

    print("Created street with id %s and %d" % (self.id, self.lenght))