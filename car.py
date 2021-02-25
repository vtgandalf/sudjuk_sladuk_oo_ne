from path import Path

class Car:
    # Initializing
    def __init__(self, id, path, intersections):
        self.id = id
        self.path = path
        self.intersections = intersections

    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Car deleted.')

car = Car(0, Path(['street 1', 'street 2', 'street 3']), ['Intersection'])