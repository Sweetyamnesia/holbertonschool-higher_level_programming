# 🐍 Héritage en Python

Ce document couvre les concepts fondamentaux et avancés de l'héritage en Python, y compris l'héritage multiple, les classes de base, les méthodes magiques, et les fonctions intégrées utiles comme `super()`, `isinstance()` ou `issubclass()`.

## 📚 Sommaire

- [Qu'est-ce que l'héritage ?](#quest-ce-que-lhéritage-)
- [Héritage multiple](#héritage-multiple)
- [Héritage en Python](#héritage-en-python)
- [Méthodes magiques et héritage](#méthodes-magiques-et-héritage)
- [Classe de base, superclasse ou classe parente](#classe-de-base-superclasse-ou-classe-parente)
- [Qu'est-ce qu'une sous-classe ?](#quest-ce-quune-sous-classe-)
- [Lister tous les attributs et méthodes](#lister-tous-les-attributs-et-méthodes)
- [Ajout d'attributs dynamiques](#ajout-dattributs-dynamiques)
- [Hériter d'une autre classe](#hériter-dune-autre-classe)
- [Héritage multiple en pratique](#héritage-multiple-en-pratique)
- [Classe par défaut : `object`](#classe-par-défaut--object-)
- [Redéfinir une méthode ou un attribut hérité](#redéfinir-une-méthode-ou-un-attribut-hérité)
- [Héritage et disponibilité des attributs](#héritage-et-disponibilité-des-attributs)
- [Objectif de l'héritage](#objectif-de-lhéritage)
- [Fonctions utiles : `isinstance`, `issubclass`, `type`, `super`](#fonctions-utiles--isinstance-issubclass-type-super)

---

## Qu'est-ce que l'héritage ?

L'héritage est un mécanisme permettant à une classe (dite **sous-classe**) d'acquérir les attributs et méthodes d'une autre classe (dite **superclasse**).

## Héritage multiple

Python autorise une classe à hériter de plusieurs classes de base, ce qui permet de combiner plusieurs comportements ou fonctionnalités.

```python
class A:
	pass

class B:
	pass

class C(A, B):
	pass
```

## Héritage en Python

Toutes les classes héritent implicitement de la classe object. Cela permet de garantir un comportement de base commun.

## Méthodes magiques et héritage

L’héritage permet de redéfinir les méthodes magiques (__init__, __str__, __repr__, etc.) pour modifier le comportement des objets.

## Classe de base, superclasse ou classe parente

Ce sont des synonymes désignant la classe dont hérite une autre classe.

## Qu'est-ce qu'une sous-classe ?

Une sous-classe est une classe qui hérite d'une autre. Elle peut étendre ou redéfinir les comportements de la superclasse.

## Lister tous les attributs et méthodes

Utilisez dir(obj) pour afficher tous les attributs et méthodes disponibles pour une instance ou une classe.

Ajout d'attributs dynamiques

Une instance peut recevoir de nouveaux attributs dynamiquement :

````
obj = MaClasse()
obj.nouvel_attribut = "valeur"
````

## Hériter d'une autre classe
```
class Volant:
	def voler(self):
		print("Je vole.")

class Nageant:
	def nager(self):
		print("Je nage.")

class Canard(Volant, Nageant):
	pass
```

## Héritage multiple en pratique
```
class Volant:
	def voler(self):
		print("Je vole.")

class Nageant:
	def nager(self):
		print("Je nage.")

class Canard(Volant, Nageant):
	pass
```

## Classe par défaut : objet

Toutes les classes en Python héritent de object si aucune autre classe n’est spécifiée.

## Redéfinir une méthode ou un attribut hérité

Une sous-classe peut redéfinir (override) une méthode pour personnaliser son comportement.
```
class Chat(Animal):
	def parler(self):
		print("Je miaule.")
````

## Héritage et disponibilité des attributs

Les attributs et méthodes publics de la classe parente sont disponibles dans la sous-classe, sauf s’ils sont masqués ou redéfinis.

## Objectif de l'héritage

L’héritage favorise la réutilisation de code, l'organisation hiérarchique et la spécialisation des comportements.

## Fonctions utiles : `isinstance`, `issubclass`, `type`, `super`

`isinstance(obj, Classe)` : Vérifie si `obj` est une instance de `Classe` ou de ses sous-classes.
`issubclass(SousClasse, SuperClasse)` : Vérifie si une classe hérite d’une autre.
`type(obj)` : Donne le type exact de l’objet.
`super()` : Permet d’appeler une méthode de la superclasse depuis une sous-classe.

```
class Animal:
	def parler(self):
		print("Animal parle")

class Chien(Animal):
	def parler(self):
		super().parler()
		print("Chien aboie")
````
