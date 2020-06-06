# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    # Parent class
    pass

class FlightVehicle(Vehicle):
    # Has Vehicle as base class
    # Child to Vehicle
    pass

class Starship(FlightVehicle):
    # Has FlightVehicle as base
    # Child to FlightVehicle, grandchild to Vehicle
    pass

class Airplane(FlightVehicle):
    # Has FlightVehicle as base
    # Child to FlightVehicle, grandchild to Vehicle
    pass

class GroundVehicle(Vehicle):
    # Has Vehicle as base class
    # Child to Vehicle
    pass

class Car(GroundVehicle):
    # Has GroundVehicle as base
    # Child to GroundVehicle, grandchild to Vehicle
    pass

class Motorcycle(GroundVehicle):
    # Has GroundVehicle as base
    # Child to GroundVehicle, grandchild to Vehicle
    pass
