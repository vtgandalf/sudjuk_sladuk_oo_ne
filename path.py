class Path:
    # Initializing
    def __init__(self, streets=[]):
        self.streets = streets

    def get_streets(self):
        return self.streets
    
    # Deleting (Calling destructor)
    def __del__(self):
        print('Destructor called, Path deleted.')
