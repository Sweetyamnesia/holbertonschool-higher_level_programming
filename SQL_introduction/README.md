# Introduction à MySQL et aux bases de données relationnelles

## 📌 Qu'est-ce qu'une base de données ?
Une base de données est un ensemble organisé de données structurées, généralement stockées électroniquement dans un système informatique. Elle permet de stocker, gérer et récupérer facilement les données.

## 📊 Qu'est-ce qu'une base de données relationnelle ?
Une base de données relationnelle (RDBMS - **Relational Database Management System**) stocke les données sous forme de tables, qui sont liées entre elles par des relations. Chaque table contient des lignes (enregistrements) et des colonnes (champs).

## 🧠 Que signifie SQL ?
**SQL** signifie **Structured Query Language**. C'est un langage utilisé pour interagir avec des bases de données relationnelles : création, modification, suppression et interrogation de données.

## 🐬 Qu'est-ce que MySQL ?
**MySQL** est un système de gestion de bases de données relationnelles open source. Il est basé sur SQL et largement utilisé dans le développement web et logiciel.

---

## 🛠️ Comment créer une base de données dans MySQL
```sql
CREATE DATABASE nom_de_la_base;
````

Pour utiliser cette base :
USE nom_de_la_base;

## 🧩 Que signifient DDL et DML ?

DDL (Data Definition Language) : Utilisé pour définir la structure de la base de données (ex. : CREATE, ALTER, DROP).
DML (Data Manipulation Language) : Utilisé pour manipuler les données (ex. : SELECT, INSERT, UPDATE, DELETE).

🏗️ Comment créer ou modifier une table

Créer une table
```sql
CREATE TABLE utilisateurs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nom VARCHAR(100),
  email VARCHAR(100)
);
```

Modifier une table
```sql
ALTER TABLE utilisateurs ADD COLUMN age INT;
```

🔍 Comment sélectionner des données depuis une table
```sql
SELECT * FROM utilisateurs;
SELECT nom, email FROM utilisateurs WHERE age > 18;
```

✍️ Comment insérer, mettre à jour ou supprimer des données

Insérer
```sql
INSERT INTO utilisateurs (nom, email, age)
VALUES ('Alice', 'alice@example.com', 25);
```

Mettre à jour
```sql
UPDATE utilisateurs SET age = 26 WHERE nom = 'Alice';
```

Supprimer
```sql
DELETE FROM utilisateurs WHERE nom = 'Alice';
```

🔄 Que sont les sous-requêtes (subqueries) ?

Une sous-requête est une requête imbriquée dans une autre requête SQL. Elle est souvent utilisée dans les clauses WHERE, FROM ou SELECT.
```sql
SELECT nom FROM utilisateurs
WHERE id IN (SELECT id_utilisateur FROM commandes WHERE total > 100);
```

🧮 Comment utiliser les fonctions MySQL
```sql
Fonctions courantes :
COUNT(), SUM(), AVG() : calculs
NOW(), CURDATE() : dates
UPPER(), LOWER() : chaînes de caractères

SELECT COUNT(*) FROM utilisateurs;
SELECT UPPER(nom) FROM utilisateurs;
SELECT AVG(age) FROM utilisateurs WHERE age IS NOT NULL;
```
