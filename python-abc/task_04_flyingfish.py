#!/usr/bin/env python3

# Base class representing a fish
class Fish:
    def swim(self):
        # Method describing swimming behavior
        print("The fish is swimming!")

    def habitat(self):
        # Method describing where the fish lives
        print("The fish lives in water")


# Base class representing a bird
class Bird:
    def fly(self):
        # Method describing flying behavior
        print("The bird is flying")

    def habitat(self):
        # Method describing where the bird lives
        print("The bird lives in the sky")


# Class representing a flying fish that inherits from both Fish and Bird
class FlyingFish(Fish, Bird):
    def fly(self):
        # Override fly method to describe flying fish's flying
        print("The flying fish is soaring!")

    def swim(self):
        # Override swim method to describe flying fish's swimming
        print("The flying fish is swimming!")

    def habitat(self):
        # Override habitat method to describe the dual habitat of the flying fish
        print("The flying fish lives both in water and the sky!")


# Display the Method Resolution Order (MRO) for FlyingFish
FlyingFish.mro()