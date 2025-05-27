# Python 3 : Programmation Orientée Objet (OOP)

Ce document fournit un aperçu des concepts avancés de la programmation orientée objet (OOP) en Python 3, ainsi que des ressources utiles pour approfondir chaque sujet.

## Sommaire

- [Abstract Classes](#abstract-classes)
- [Interfaces et Duck Typing](#interfaces-et-duck-typing)
- [Héritage des Classes de Base Standard](#héritage-des-classes-de-base-standard)
- [Redéfinition de Méthodes (Method Overriding)](#redéfinition-de-méthodes-method-overriding)
- [Héritage Multiple](#héritage-multiple)
- [Mixins](#mixins)
- [Ressources Complémentaires](#ressources-complémentaires)

---

## Abstract Classes

Comprendre et utiliser les classes abstraites pour définir des interfaces communes tout en imposant un niveau minimal d’implémentation dans les sous-classes.

➡️ Utilisation du module `abc` (`Abstract Base Classes`) pour créer des classes abstraites.

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```

## Interfaces et Duck Typing

Maîtriser les interfaces et le duck typing afin de garantir qu’un objet respecte un contrat ou protocole sans avoir besoin d’une hiérarchie explicite de classes.

"If it looks like a duck and quacks like a duck, it’s a duck."

```
class Duck:
    def quack(self):
        print("Quack!")

def make_it_quack(thing):
    thing.quack()
```

## Héritage des Classes de Base Standard

Étendre des classes de base comme list, dict, ou des itérateurs pour créer des structures de données personnalisées avec un comportement spécialisé.

```
class CustomList(list):
    def sum(self):
        return sum(self)
```

## Redéfinition de Méthodes (Method Overriding)

Modifier ou étendre le comportement des méthodes d'une classe parente dans une classe enfant.

```
class Parent:
    def greet(self):
        print("Hello")

class Child(Parent):
    def greet(self):
        print("Hi, I’m the child")
```

## Héritage Multiple

Comprendre et utiliser l’héritage multiple pour former des relations complexes entre classes. Utiliser avec précaution à cause de la complexité potentielle (ex. résolution de méthode via MRO).

```
class A:
    def do_something(self):
        print("A")

class B:
    def do_something(self):
        print("B")

class C(A, B):
    pass

c = C()
c.do_something()  # Affiche "A" à cause de MRO
```

## Mixins

Utiliser les mixins pour composer des comportements réutilisables entre classes non liées, sans avoir à créer de hiérarchie complexe.

```
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person(JsonMixin):
    def __init__(self, name):
        self.name = name
```
