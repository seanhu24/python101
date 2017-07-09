class Vehicle:
    """ doc string"""

    def __init__(self, color, doors, tires):
        """ contructor"""
        self.color=color
        self.doors=doors
        self.tires=tires

    def brake(self):
        """ stop"""
        return "Braking"

    def drive(self):
        """ drive"""
        return "Driving"