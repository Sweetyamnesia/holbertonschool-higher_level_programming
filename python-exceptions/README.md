# Exceptions en Python

## 🐍 Pourquoi la programmation Python est-elle géniale ?

Python est un langage simple, lisible et puissant. Il permet de développer rapidement des applications grâce à sa syntaxe claire, ses nombreuses bibliothèques intégrées, et une communauté très active. Il est utilisé dans de nombreux domaines : web, data science, intelligence artificielle, automatisation, etc.

## ⚠️ Différence entre erreurs et exceptions

- **Erreurs** : Problèmes qui apparaissent souvent à l'exécution et qui interrompent immédiatement le programme si non traités.
- **Exceptions** : Un type particulier d'erreur que Python peut gérer via un mécanisme spécifique (try/except).

## ❓ Qu’est-ce qu’une exception et comment l’utiliser ?

Une **exception** est un événement qui se produit pendant l'exécution du programme et qui interrompt le flux normal des instructions. Python permet de gérer ces situations en utilisant les blocs `try`, `except`, `else` et `finally`.

Exemple :

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division par zéro interdite.")
````

🕒 Quand devons-nous utiliser les exceptions ?

On utilise les exceptions pour :

Gérer des erreurs inattendues (fichiers manquants, division par zéro, connexions échouées, etc.).
Empêcher un plantage brutal du programme.
Proposer des messages d’erreurs compréhensibles à l’utilisateur.
✅ Comment gérer correctement une exception ?

Utilise les blocs try et except pour entourer le code susceptible de générer une exception. Tu peux également gérer plusieurs types d'exceptions spécifiques.

```
try:
    with open("data.txt") as file:
        data = file.read()
except FileNotFoundError:
    print("Fichier introuvable.")
```

🎯 Pourquoi attraper les exceptions ?

Attraper une exception permet :

D’éviter un arrêt brutal du programme.
D’améliorer l’expérience utilisateur avec des messages clairs.
De permettre une reprise de contrôle sur l’exécution du programme.
📌 Comment lever une exception intégrée ?

Tu peux utiliser le mot-clé raise pour déclencher une exception manuellement.

```
age = -5
if age < 0:
    raise ValueError("L'âge ne peut pas être négatif.")
````

🧹 Quand faut-il nettoyer après une exception ?

Utilise le bloc finally pour exécuter du code quoi qu’il arrive, par exemple pour fermer un fichier ou une connexion réseau.

```
try:
    file = open("data.txt")
    # Lecture ou traitement
except Exception as e:
    print("Une erreur est survenue :", e)
finally:
    file.close()
```
