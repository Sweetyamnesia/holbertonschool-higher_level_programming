# Sérialisation et formats de données en Python

## 📌 Objectifs

Ce projet vise à comprendre et appliquer les concepts de sérialisation en Python, en explorant différents formats et leur utilisation dans des contextes réels.

### ✅ Concepts clés

- Expliquer les **différences et similarités entre marshaling et sérialisation**.
- Implémenter la **sérialisation dans un projet pratique en programmation**.
- Comprendre comment les **données sérialisées sont utilisées dans les applications web, bases de données et communications réseau**.
- Évaluer les **performances et compromis entre différents formats** tels que JSON, XML et les formats binaires.

---

## 📦 Sérialisation vs Marshaling

| Caractéristique     | Sérialisation                                    | Marshaling                                        |
|---------------------|-------------------------------------------------|--------------------------------------------------|
| **Définition**      | Transformation d’un objet en un format stockable ou transmissible | Préparation des données pour communication entre programmes ou processus |
| **Portabilité**     | Indépendante du langage (ex : JSON, XML)        | Souvent spécifique à un langage (ex : `marshal` Python) |
| **Interopérabilité**| Élevée (notamment JSON, XML)                      | Faible (usage interne ou langage spécifique)     |
| **Objectif**        | Stockage longue durée ou transmission             | Transfert temporaire de données durant l’exécution |
| **Cas d’usage**     | APIs, fichiers de configuration                   | Appels internes, Remote Procedure Calls (RPC)    |

✅ **Similarité** : les deux consistent à transformer des données en un format transférable ou stockable.

---

## 🛠️ Utilisation pratique de la sérialisation

### JSON
- Format : Texte, lisible par l’humain.
- Outils : module `json` de Python.
- Usage : APIs web, fichiers de configuration.

### XML
- Format : Texte, structure hiérarchique.
- Outils : module `xml.etree.ElementTree` de Python.
- Usage : systèmes anciens, documents, APIs SOAP.

### Binaire (Pickle)
- Format : Binaire compact.
- Outils : module `pickle` de Python.
- Usage : persistance d’objets Python, cache.

---

## 🌐 Sérialisation dans le monde réel

- **Applications web** : JSON est très utilisé pour l’échange de données via des APIs REST.
- **Bases de données** : données sérialisées stockées sous forme de blobs ou documents (ex : BSON dans MongoDB).
- **Communications réseau** : la sérialisation permet le transfert de données structurées entre clients et serveurs.

Exemple :
```python
import json

data = {"utilisateur": "Angela", "role": "admin"}
serialise = json.dumps(data)
print(serialise)  # -> {"utilisateur": "Angela", "role": "admin"}
