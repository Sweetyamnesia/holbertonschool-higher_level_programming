
# Fondamentaux de Python : Contrôle de flux, fonctions, et plus

Ce document présente les concepts essentiels de la programmation en Python, en mettant l'accent sur le contrôle de flux, les fonctions, la portée des variables, et la syntaxe générale.

---

## 📌 Pourquoi l'indentation est-elle importante en Python ?

Python utilise **l'indentation** pour définir les blocs de code. Contrairement à d'autres langages qui utilisent des accolades (`{}`), Python repose sur une indentation cohérente (généralement 4 espaces).

Exemple :
```python
if True:
    print("Ceci est correctement indenté")
```

Une mauvaise indentation provoque une erreur `IndentationError`.

---

## ✅ Les instructions `if` et `if ... else`

Utilisées pour l'exécution conditionnelle :
```python
if condition:
    # faire quelque chose
elif autre_condition:
    # faire autre chose
else:
    # cas par défaut
```

---

## 💬 Les commentaires

Les commentaires documentent le code et sont ignorés par l'interpréteur.

- Ligne unique : `# Ceci est un commentaire`
- Multiligne (non officiel) : triple guillemets (utilisés souvent pour les docstrings)

---

## 🎯 Affectation de valeurs à des variables

L'affectation se fait avec l'opérateur `=` :
```python
x = 5
nom = "Alice"
```

---

## 🔁 Les boucles : `while` et `for`

### Boucle `while` :
Exécutée tant qu'une condition est vraie.
```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### Boucle `for` :
Itère sur une séquence (liste, chaîne, etc.).
```python
for i in range(5):
    print(i)
```

---

## 🛑 Les instructions `break` et `continue`

- `break` : interrompt la boucle prématurément
- `continue` : saute l'itération en cours et passe à la suivante

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

## ✨ Clause `else` sur les boucles

S'exécute uniquement si la boucle **se termine sans `break`** :
```python
for i in range(3):
    print(i)
else:
    print("Boucle terminée sans interruption.")
```

---

## 🔃 L’instruction `pass`

Instruction vide. Utilisée comme **placeholder** :
```python
def ma_fonction():
    pass
```

---

## 📏 Utilisation de `range()`

Génère une séquence de nombres :
```python
range(5)         # de 0 à 4
range(1, 6)      # de 1 à 5
range(0, 10, 2)  # nombres pairs de 0 à 8
```

---

## 🧩 Fonctions

Définies avec `def` :
```python
def saluer(nom):
    print(f"Bonjour, {nom}")
```

---

## ⏎ Retour d'une fonction sans `return`

Une fonction sans `return` explicite retourne automatiquement `None`.

---

## 🌍 Portée des variables

- **Locale** : définie à l’intérieur d’une fonction
- **Globale** : définie en dehors de toute fonction
- Pour modifier une variable globale depuis une fonction, utiliser le mot-clé `global`

---

## 🐍 Qu’est-ce qu’un traceback ?

Un traceback est un message d’erreur indiquant **où et pourquoi une exception s’est produite**.

Exemple :
```text
Traceback (most recent call last):
  File "exemple.py", line 1, in <module>
    print(variable_inconnue)
NameError: name 'variable_inconnue' is not defined
```

---

## ➕ Les opérateurs arithmétiques

| Opérateur | Description          | Exemple    |
|----------|----------------------|------------|
| `+`      | Addition              | `a + b`    |
| `-`      | Soustraction          | `a - b`    |
| `*`      | Multiplication        | `a * b`    |
| `/`      | Division              | `a / b`    |
| `//`     | Division entière      | `a // b`   |
| `%`      | Modulo (reste)        | `a % b`    |
| `**`     | Puissance             | `a ** b`   |

---