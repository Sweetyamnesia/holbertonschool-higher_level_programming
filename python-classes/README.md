# Python - Classes et Objets

## Programmation Orientée Objet (POO)

La **programmation orientée objet (OOP)** est un paradigme de programmation qui organise le code autour des objets et des classes plutôt que des fonctions et des logiques. Elle permet de modéliser des entités du monde réel avec des attributs (données) et des comportements (méthodes).

## "First-class everything"

En Python, tout est objet, même les types, fonctions et classes. Cela signifie que les fonctions peuvent être passées comme arguments, retournées par d'autres fonctions, et assignées à des variables.

## Qu'est-ce qu'une classe ?

Une **classe** est un plan (ou template) permettant de créer des objets. Elle définit les attributs et les méthodes que ses objets auront.

```python
class Chien:
    def __init__(self, nom):
        self.nom = nom

    def aboyer(self):
        print(f"{self.nom} aboie !")
```

## Qu'est-ce qu'un objet et une instance ?

Un **objet** est une instance concrète d'une classe. Créer un objet signifie instancier une classe.

```python
rex = Chien("Rex")
rex.aboyer()  # Rex aboie !
```

## Différence entre classe, objet et instance

* **Classe** : le plan.
* **Objet / Instance** : une réalisation concrète de ce plan. Les termes *objet* et *instance* sont souvent interchangeables.

## Qu'est-ce qu'un attribut ?

Un **attribut** est une variable attachée à une instance ou une classe.

```python
rex.nom  # 'Rex' est un attribut de l'objet rex
```

## Attributs publics, protégés et privés

* **Public** : accessible partout (par défaut).
* **Protégé (\_attribut)** : convention indiquant qu'il ne doit être utilisé que dans la classe ou ses sous-classes.
* **Privé (\_\_attribut)** : rend l'attribut difficilement accessible de l'extérieur (name mangling).

```python
class Exemple:
    def __init__(self):
        self.public = 1
        self._protege = 2
        self.__prive = 3
```

## self

`self` est une référence à l'instance courante de la classe. Il doit être le premier paramètre de chaque méthode d'instance.

## Qu'est-ce qu'une méthode ?

Une **méthode** est une fonction définie à l'intérieur d'une classe. Elle agit généralement sur les attributs de l'instance.

## Méthode spéciale **init**

`__init__` est un constructeur appelé automatiquement lors de la création d'une instance. Il initialise les attributs.

```python
class Voiture:
    def __init__(self, marque):
        self.marque = marque
```

## Abstraction, encapsulation et masquage d'information

* **Abstraction** : cacher les détails complexes et montrer uniquement l'essentiel.
* **Encapsulation** : regrouper les données et les méthodes dans une seule unité (classe).
* **Masquage d'information** : rendre certaines parties internes inaccessibles directement (via attributs privés).

## Propriété (property)

Une **property** permet de contrôler l'accès à un attribut comme s'il s'agissait d'une variable, tout en permettant l'ajout de logique.

```python
class Personne:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, valeur):
        if valeur < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self._age = valeur
```

## Différence entre attribut et propriété

* Un **attribut** est une simple variable.
* Une **propriété** permet de définir des accesseurs personnalisés tout en gardant une syntaxe d'accès par point.

## Manière pythonique de faire des getters et setters

Utiliser le décorateur `@property` pour créer des getters/setters sans compromettre la syntaxe naturelle.

## Création dynamique d'attributs

On peut créer dynamiquement de nouveaux attributs pour une instance à tout moment :

```python
objet.nouvel_attribut = 42
```

## Liaison d'attributs aux objets et classes

* Attributs d'**instance** : définis dans `__init__` via `self`.
* Attributs de **classe** : définis directement dans le corps de la classe.

```python
class Exemple:
    attribut_classe = 10

    def __init__(self):
        self.attribut_instance = 20
```

## **dict** d'une classe ou d'une instance

* `instance.__dict__` contient les attributs de l'objet sous forme de dictionnaire.
* `Classe.__dict__` contient les méthodes, attributs de classe, etc.

```python
print(objet.__dict__)
```

## Recherche d'attributs par Python

Python cherche les attributs dans l'ordre suivant (MRO - Method Resolution Order) :

1. L'objet lui-même
2. Sa classe
3. Les classes parentes

## La fonction getattr()

`getattr(objet, nom_attribut, valeur_par_défaut)` permet d'accéder dynamiquement à un attribut.

```python
nom = getattr(objet, "nom", "inconnu")
```
