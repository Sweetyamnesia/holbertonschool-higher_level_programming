# Python - Object Relational Mapping (ORM)

Ce projet présente les bases de la connexion et de la manipulation d'une base de données MySQL depuis un script Python, ainsi que les principes fondamentaux de l’ORM (Object Relational Mapping).

---

## Contenu

- **Connexion à une base de données MySQL depuis Python**
- **Exécution de requêtes SELECT pour récupérer des données**
- **Insertion de lignes dans une table MySQL via Python**
- **Compréhension de l’ORM (Object Relational Mapping)**
- **Mapping d’une classe Python à une table MySQL**

---

## Comment se connecter à une base MySQL depuis un script Python

On utilise généralement un connecteur comme [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/) ou [PyMySQL](https://pymysql.readthedocs.io/en/latest/) pour établir la connexion :

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="votre_mot_de_passe",
    database="nom_de_la_base"
)
cursor = conn.cursor()
````

Comment faire un SELECT dans une table MySQL depuis Python

Une fois connecté, on peut exécuter une requête SELECT et récupérer les résultats :
```python
query = "SELECT * FROM ma_table;"
cursor.execute(query)
results = cursor.fetchall()

for row in results:
    print(row)
```

Comment faire un INSERT dans une table MySQL depuis Python

Pour insérer des données, on prépare la requête puis on exécute :
```python
query = "INSERT INTO ma_table (col1, col2) VALUES (%s, %s);"
values = ("valeur1", "valeur2")
cursor.execute(query, values)
conn.commit()
```

Qu’est-ce que l’ORM ?

ORM (Object Relational Mapping) est une technique qui permet de mapper des classes et objets Python à des tables et enregistrements d’une base relationnelle. Cela facilite l’interaction avec la base de données en utilisant des objets Python au lieu d’écrire des requêtes SQL manuellement.

Comment mapper une classe Python à une table MySQL

Avec un ORM comme SQLAlchemy, on définit une classe qui représente une table, avec ses colonnes sous forme d’attributs :
```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
```

Ensuite, on peut manipuler la base via ces classes : créer, lire, modifier ou supprimer des objets Python, et les changements sont reflétés dans la base de données.
