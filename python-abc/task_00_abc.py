#!/usr/bin/env python3
from abc import ABC, abstractmethod  # Import tools to define abstract base classes


# Abstract base class representing a generic animal
class Animal(ABC):

    @abstractmethod
    def sound(self):
        # Abstract method that must be implemented by any subclass
        # Should return the sound the animal makes
        pass


# Dog class inheriting from Animal
class Dog(Animal):
    def sound(self):
        # Implementation of the sound method for a dog
        return "Bark"


# Cat class inheriting from Animal
class Cat(Animal):
    def sound(self):
        # Implementation of the sound method for a cat
        return "Meow"
