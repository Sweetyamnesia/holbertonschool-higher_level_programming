# Programmation Orientée Objet en Python 3

## Introduction Générale

La programmation orientée objet (POO) est un paradigme basé sur l’idée de *regrouper des données* (attributs) et des *fonctions* (méthodes) dans des structures appelées **classes**. Une classe est un modèle ; ses instances (ou objets) sont les réalisations concrètes.

---

## Tout est objet

En Python, **tout est objet**, y compris les fonctions, les modules, et même les classes elles-mêmes. Cela signifie que les classes peuvent être manipulées comme n’importe quelle autre valeur.

---

## Classe minimale en Python

Voici un exemple de classe vide minimale :

```python
class Exemple:
    pass
```

Créer une instance :

```python
e = Exemple()
```

---

## Attributs

Les **attributs** sont les données associées à une instance. On peut les définir à la volée ou dans le constructeur `__init__`.

```python
class Personne:
    def __init__(self, nom):
        self.nom = nom
```

---

## Méthodes

Les **méthodes** sont des fonctions définies à l’intérieur d’une classe, prenant généralement `self` comme premier paramètre pour référencer l’instance courante.

---

## Méthode `__init__`

C’est le **constructeur** appelé automatiquement à la création d’un objet :

```python
class Animal:
    def __init__(self, espece):
        self.espece = espece
```

---

## Abstraction, Encapsulation et Masquage de l'information

- **Abstraction** : cacher les détails d’implémentation.
- **Encapsulation** : grouper les données et les méthodes qui y accèdent.
- **Masquage de l’information** : limiter l’accès direct à certaines données.

---

## Méthodes `__str__` et `__repr__`

- `__str__` : pour une représentation lisible par un humain.
- `__repr__` : pour une représentation destinée aux développeurs, souvent plus technique.

```python
def __str__(self):
    return f"Personne : {self.nom}"

def __repr__(self):
    return f"Personne(nom={self.nom!r})"
```

---

## Attributs publics, protégés et privés

Par convention :

- `nom` → **public**
- `_nom` → **protégé** (à ne pas modifier à l’extérieur, mais pas interdit)
- `__nom` → **privé** (nom mangling)

---

## Destructeur : `__del__`

Méthode appelée à la destruction de l’objet (rarement utilisée en pratique) :

```python
def __del__(self):
    print("Objet détruit")
```

---

## Attributs de classe vs d’instance

- **Instance** : propre à chaque objet (`self.attribut`)
- **Classe** : partagé par toutes les instances (`Class.attribut`)

```python
class Compteur:
    total = 0  # Attribut de classe
    def __init__(self):
        Compteur.total += 1
```

---

## `@classmethod` et `@staticmethod`

- **`@classmethod`** : méthode qui reçoit la classe (`cls`) comme premier argument.
- **`@staticmethod`** : méthode indépendante de l’instance et de la classe.

---

## Propriétés vs Getters/Setters

Python préfère les **propriétés** via le décorateur `@property` plutôt que les méthodes `get_` et `set_`.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, valeur):
        self._celsius = valeur
```

➡️ Cela permet d’accéder aux attributs comme s’ils étaient publics, tout en conservant le contrôle :

```python
t = Temperature(25)
t.celsius = 30
print(t.celsius)
```

---

## `str` vs `repr`

- `str(obj)` → lisible (pour l’utilisateur)
- `repr(obj)` → non ambigüe (pour les développeurs, idéalement `eval(repr(obj)) == obj`)

---
