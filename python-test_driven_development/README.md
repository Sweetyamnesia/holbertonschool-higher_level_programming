# 📘 Comprendre et Écrire des Tests Interactifs en Python

## 🔍 Qu’est-ce qu’un test interactif ?

Un **test interactif** en Python est un test que l’on peut exécuter directement depuis le terminal ou une interface, souvent via le module `doctest` ou en testant manuellement dans le shell Python. Ce type de test permet d’observer le comportement d’une fonction avec différentes entrées, comme un dialogue entre l'utilisateur et la machine.

Exemple :
```python
>>> from math import sqrt
>>> sqrt(4)
2.0
````

✅ Pourquoi les tests sont-ils importants ?

Les tests sont essentiels pour :

✅ Vérifier que le code fonctionne comme attendu.
🧪 Éviter les régressions lors des modifications.
🔄 Faciliter la maintenance du code.
🧠 Comprendre ce que le code est censé faire.
🔍 Trouver les erreurs cachées ou les cas limites.
🧾 Comment écrire des Docstrings pour créer des tests ?

En Python, on peut utiliser les docstrings pour inclure des exemples qui peuvent être testés automatiquement avec doctest.

Exemple :
````
def add(a, b):
    """
    Additionne deux nombres.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b
`````

Pour lancer les tests :
`````
python3 -m doctest -v nom_du_fichier.py
`````

📚 Comment documenter un module et une fonction ?

Pour un module (en haut du fichier) :

`````
"""
Module de calculs mathématiques simples.

Contient des fonctions pour additionner, soustraire, etc.
"""
`````

Pour une fonction :
`````
def multiply(a, b):
    """
    Multiplie deux nombres.

    Arguments :
    a -- premier nombre
    b -- second nombre

    Retourne :
    Le produit de a et b.

    >>> multiply(2, 3)
    6
    """
    return a * b
`````

⚙️ Quelles sont les options de base pour créer des tests ?

Avec `doctest`, quelques options utiles sont disponibles :

- `-v` : mode **verbeux**, affiche les résultats détaillés ligne par ligne.
- `+ELLIPSIS` : ignore une partie de la sortie, très utile si le résultat est partiellement imprévisible (ex : longues chaînes).
- `+NORMALIZE_WHITESPACE` : ignore les **différences d’espacement** (espaces ou tabulations).

Exemple :
`````
python3 -m doctest -v fichier.py
`````

🧪 Comment trouver les cas limites (edge cases) ?

Un **cas limite** (ou *edge case*) est une situation extrême ou inhabituelle qui pourrait faire planter ou mal fonctionner le programme.

Voici quelques exemples de cas à tester :

- Entrée vide : `""`, `[]`, `None`
- Valeurs très grandes ou très petites
- Types inattendus : par exemple une chaîne de caractères à la place d’un nombre
- Valeur égale à zéro ou négative
- Listes plus **courtes** ou plus **longues** que prévu
- Division par zéro
- Paramètres **manquants** ou **supplémentaires**

✅ Tester ces cas permet d’avoir un programme :
- plus **robuste**
- plus **fiable**
- mieux préparé aux situations imprévues

