#!/usr/bin/env python3

# Mixin that provides swimming ability
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Mixin that provides flying ability
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class inherits both swimming and flying abilities via mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
