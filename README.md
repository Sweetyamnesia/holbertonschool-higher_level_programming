# holbertonschool-higher_level_programming

# Apprendre les bases de Python 🐍

Ce projet introduit les bases essentielles de Python, adaptées aux débutants. Il aborde l'utilisation de l'interpréteur Python, la manipulation de chaînes de caractères, l'affichage avec `print`, le slicing et l'indexation, ainsi que les bonnes pratiques de style de code.

---

## 🔧 Comment utiliser l'interpréteur Python

### Lancer l'interpréteur
```bash
python3
```

## Executer un script en Python
```bash
python3 mon_script.py
```

## 🖨️ Afficher du texte et des variables avec print()
# Affichage simple
```bash
print("Bonjour le monde")

# Affichage de variables
nom = "Alice"
age = 25
print("Nom:", nom)
print(f"{nom} a {age} ans.")  # Utilisation de f-strings
```

## 🔤 Utiliser les chaînes de caractères (strings)
```bash
texte = "Python est amusant"

# Longueur
print(len(texte))  # 17

# Majuscules / minuscules
print(texte.upper())      # "PYTHON EST AMUSANT"
print(texte.lower())      # "python est amusant"

# Concaténation
salutation = "Bonjour"
nom = "Bob"
print(salutation + " " + nom)  # "Bonjour Bob"
```

## 🔍 Indexation et slicing

# Indexation (positions des caractères)
```bash
mot = "Python"
print(mot[0])   # P
print(mot[-1])  # n (dernier caractère)
```

# Slicing (extraire une sous-partie)
```bash
print(mot[0:2])   # Py
print(mot[2:])    # thon
print(mot[:3])    # Pyt
print(mot[::2])   # Pto (un caractère sur deux)
```

## 🎨 Style de code Python (PEP 8) et pycodestyle
# PEP 8
PEP 8 est le guide de style officiel de Python. Il recommande :

4 espaces pour l'indentation
Des noms de variables explicites en minuscule_avec_underscores
Des lignes de max 79 caractères
Une ligne vide entre les fonctions
Pas d'espaces inutiles autour des opérateurs ou dans les parenthèses

# Vérifier son code avec pycodestyle
```bash
pip install pycodestyle
pycodestyle mon_script.py
```
## 📁 Exemple de structure simple
```bash
.
├── 0-hello.py         # Utilisation de print
├── 1-string.py        # Manipulation de chaînes
├── 2-slicing.py       # Slicing et indexation
└── README.md
```
