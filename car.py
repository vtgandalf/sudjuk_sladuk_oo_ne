from path import Path

class Car:
    # Initializing
    def __init__(self, id, path, intersections):
        self.id = id
        self.path = path
        self.intersections = intersections

    def append_intersection(self, intersection):
        self.intersections.append(intersection)

    def remove_intersection(self, intersection):
        self.intersections.remove(intersection)

    def if_contain_intersection(self, intersection):
        if intersection in self.intersections:
            return True
        return False
        
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Car deleted.')

car = Car(0, Path(['street 1', 'street 2', 'street 3']), ['Intersection'])