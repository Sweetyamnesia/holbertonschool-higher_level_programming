# 📂 Python Input/Output Guide

Ce guide vous explique les bases des opérations d'entrée/sortie (Input/Output) en Python, notamment la manipulation de fichiers, la gestion du JSON, et l'utilisation des paramètres en ligne de commande.

---

## 📝 Lecture et écriture de fichiers

### 🔓 Comment ouvrir un fichier

```python
file = open("example.txt", "r")  # Modes : "r" (lecture), "w" (écriture), "a" (ajout), "b" (binaire)
````

✍️ Écrire du texte dans un fichier

with open("example.txt", "w") as file:
    file.write("Bonjour, monde !")

📖 Lire tout le contenu d’un fichier

with open("example.txt", "r") as file:
    content = file.read()
    print(content)

📄 Lire un fichier ligne par ligne

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

🎯 Déplacer le curseur dans un fichier

file = open("example.txt", "r")
file.seek(0)        # Déplace le curseur au début du fichier
position = file.tell()  # Donne la position actuelle du curseur
file.close()

✅ S’assurer qu’un fichier est fermé après utilisation
Utilisez toujours le mot-clé with :

with open("example.txt", "r") as file:
    content = file.read()
# Le fichier est automatiquement fermé ici

🔒 Le mot-clé with

Le mot-clé with permet de gérer automatiquement les ressources. Il garantit que le fichier est fermé correctement, même en cas d'erreur :

with open("example.txt", "r") as file:
    print(file.read())


🧬 JSON en Python

❓ Qu’est-ce que JSON
JSON (JavaScript Object Notation) est un format léger d’échange de données, très utilisé pour transmettre des données entre un serveur et une application web.

📦 Sérialisation
Convertir une structure Python en chaîne JSON :

import json

data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)
print(json_str)  # {"name": "Alice", "age": 30}


📥 Désérialisation
Convertir une chaîne JSON en structure Python :

json_str = '{"name": "Alice", "age": 30}'
data = json.loads(json_str)
print(data["name"])  # Alice


🧠 Accéder aux paramètres de la ligne de commande

Utilisez le module sys :

import sys

print("Nom du script:", sys.argv[0])
print("Paramètres:", sys.argv[1:])


Exécution depuis la console :

python script.py arg1 arg2
