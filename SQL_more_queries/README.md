# Guide MySQL - Concepts et commandes essentielles

Ce document présente les notions clés et commandes courantes pour gérer une base de données MySQL, notamment la création d’utilisateurs, la gestion des privilèges, les clés primaires et étrangères, les contraintes, et les requêtes avancées.

---

## Comment créer un nouvel utilisateur MySQL

Pour créer un nouvel utilisateur dans MySQL, on utilise la commande suivante :

```sql
CREATE USER 'nom_utilisateur'@'hôte' IDENTIFIED BY 'mot_de_passe';
```

Exemple :  
```sql
CREATE USER 'user1'@'localhost' IDENTIFIED BY 'password123';
```

---

## Gestion des privilèges pour un utilisateur

Pour attribuer des privilèges à un utilisateur sur une base de données ou une table :

```sql
GRANT ALL PRIVILEGES ON nom_base.* TO 'nom_utilisateur'@'hôte';
FLUSH PRIVILEGES;
```

Exemple :  
```sql
GRANT SELECT, INSERT ON ma_base.ma_table TO 'user1'@'localhost';
FLUSH PRIVILEGES;
```

---

## Qu’est-ce qu’une clé primaire (PRIMARY KEY) ?

La clé primaire est une colonne (ou un ensemble de colonnes) qui identifie de manière unique chaque ligne d’une table.  
- Elle ne peut pas contenir de valeurs NULL.  
- Chaque valeur doit être unique.

Exemple :  
```sql
CREATE TABLE utilisateurs (
    id INT PRIMARY KEY,
    nom VARCHAR(100)
);
```

---

## Qu’est-ce qu’une clé étrangère (FOREIGN KEY) ?

Une clé étrangère est une colonne (ou un groupe de colonnes) dans une table qui fait référence à la clé primaire d’une autre table. Elle assure l’intégrité référentielle entre les tables.

Exemple :  
```sql
CREATE TABLE commandes (
    id INT PRIMARY KEY,
    utilisateur_id INT,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id)
);
```

---

## Contraintes NOT NULL et UNIQUE

- `NOT NULL` : empêche une colonne d’avoir des valeurs NULL (obligatoire d’avoir une valeur).  
- `UNIQUE` : assure que toutes les valeurs de la colonne sont différentes (pas de doublons).

Exemple :  
```sql
CREATE TABLE produits (
    id INT PRIMARY KEY,
    code_produit VARCHAR(50) NOT NULL UNIQUE
);
```

---

## Récupérer des données depuis plusieurs tables en une seule requête

On utilise généralement les **JOIN** pour combiner des lignes de plusieurs tables selon une condition.

Exemple d’INNER JOIN :  
```sql
SELECT utilisateurs.nom, commandes.id
FROM utilisateurs
JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

---

## Qu’est-ce qu’une sous-requête (subquery) ?

Une sous-requête est une requête SQL imbriquée dans une autre. Elle est utilisée pour récupérer des données qui serviront à une requête principale.

Exemple :  
```sql
SELECT nom FROM utilisateurs
WHERE id IN (SELECT utilisateur_id FROM commandes WHERE montant > 100);
```

---

## Les opérateurs JOIN et UNION

- **JOIN** : combine les colonnes de tables différentes selon une condition.  
  Types courants : INNER JOIN, LEFT JOIN, RIGHT JOIN, FULL JOIN.

- **UNION** : combine les résultats de plusieurs requêtes SELECT, en empilant les lignes (mêmes colonnes requises).

Exemple JOIN :  
```sql
SELECT utilisateurs.nom, commandes.date
FROM utilisateurs
JOIN commandes ON utilisateurs.id = commandes.utilisateur_id;
```

Exemple UNION :  
```sql
SELECT nom FROM clients
UNION
SELECT nom FROM fournisseurs;
```