# Concepts fondamentaux en Python : Objets, Références et Mutabilité

Ce document couvre les bases essentielles de la gestion des objets et des variables en Python, notamment la différence entre objets et classes, la mutabilité, les références, et le comportement des fonctions.

---

## 🔹 Qu'est-ce qu'un objet ?

Un **objet** est une entité contenant à la fois des **données** (attributs) et des **comportements** (méthodes). En Python, **tout est objet** : nombres, chaînes, fonctions, classes, etc.

---

## 🔹 Quelle est la différence entre une classe et un objet (ou instance) ?

- Une **classe** est un plan (un modèle) qui définit la structure et le comportement des objets.
- Un **objet** (ou **instance**) est une occurrence concrète d’une classe.

```python
class Chien:
    def aboyer(self):
        print("Woof")

rex = Chien()  # rex est une instance (objet) de la classe Chien
```

## 🔹 Quelle est la différence entre un objet immuable et un objet mutable ?

**Immuable** : son contenu ne peut pas être modifié après sa création.
**Mutable** : son contenu peut être modifié.

## 🔹 Qu'est-ce qu'une référence ?

Une **référence** est un lien entre un nom de variable et un objet en mémoire. En Python, les variables ne contiennent pas directement les objets, mais des références à ceux-ci.

## 🔹 Qu'est-ce qu'une affectation (assignment) ?

**L’affectation** associe une référence à un nom de variable.
```python
x = [1, 2, 3]  # x est une référence vers une liste
```

## 🔹 Qu'est-ce qu'un alias ?

Un **alias** est un deuxième nom qui fait référence au même objet.
```python
a = [1, 2]
b = a  # b est un alias de a
```

## 🔹 Comment savoir si deux variables sont identiques ?

Utiliser l'opérateur `is` :
```python
a = [1, 2]
b = a
print(a is b)  # True
```

## 🔹 Comment savoir si deux variables pointent vers le même objet ?

Même chose : is vérifie si deux variables pointent vers le même objet en mémoire.

## 🔹 Comment afficher l'identifiant (adresse mémoire) d'une variable ?

Utilise la fonction `id()` :
```python
a = [1, 2]
print(id(a))  # Affiche l'identifiant (adresse mémoire CPython)
```

## 🔹 Qu'est-ce qui est mutable et immuable ?

Objets immuables :
int
float
str
tuple
frozenset
bool
Objets mutables :
list
dict
set
bytearray

## 🔹 Comment Python passe-t-il les variables aux fonctions ?

Python passe les références aux objets. Cela signifie :

Si l’objet est `mutable`, il peut être modifié à l’intérieur de la fonction.
Si l’objet est `immuable`, il ne peut pas être modifié (mais on peut créer un nouvel objet).

```python
def modifier(liste):
    liste.append(4)

a = [1, 2, 3]
modifier(a)
print(a)  # [1, 2, 3, 4] → l'objet a a été modifié
```

