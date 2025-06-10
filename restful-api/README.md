# RESTful API - Projet d’apprentissage

## Introduction

Dans le monde en constante évolution du développement logiciel, savoir communiquer et transférer des données efficacement entre systèmes est essentiel. Ce projet explore le domaine des **RESTful APIs**, qui sont une pierre angulaire des services web modernes.

L’architecture REST (Representational State Transfer) définit un ensemble de contraintes pour garantir un système de communication **scalable**, **sans état** et **cacheable**. Cette approche facilite l’intégration de services web, les rendant accessibles à une large gamme d’applications.

---

## Objectifs pédagogiques

- **Bases HTTP/HTTPS**  
  Comprendre les principes fondamentaux du protocole web principal, les méthodes utilisées et la différence entre les versions sécurisées et non sécurisées.

- **Consommation d’API via la ligne de commande**  
  Apprendre à interagir avec des APIs en utilisant des outils simples en ligne de commande, base pour des interactions plus avancées.

- **Consommation d’API avec Python**  
  Exploiter Python pour effectuer des requêtes API et manipuler les données récupérées.

- **Développement d’API avec `http.server`**  
  Comprendre comment créer une API simple en Python à partir des modules intégrés, pour acquérir les bases.

- **Développement d’API avec Flask**  
  Approfondir la création d’API avec Flask, un micro-framework léger, en se concentrant sur le routage, la gestion des données et la montée en charge.

- **Sécurité et authentification des API**  
  Aborder la protection des échanges et l’accès sécurisé aux ressources.

- **Normes & documentation avec OpenAPI**  
  Maintenir une documentation claire et standardisée pour garantir la compréhension et la maintenabilité de l’API.

---

## Importance des RESTful APIs

Dans notre ère numérique interconnectée, les APIs RESTful sont omniprésentes. Elles font le lien entre différentes applications et systèmes, traduisant les requêtes en actions concrètes, récupérant ou modifiant des données.

Exemples d’utilisation :  
- Partage de données entre plateformes de réseaux sociaux et agences publicitaires  
- Communication entre systèmes industriels pour l’automatisation  

Maîtriser la consommation, le développement, la sécurisation et la documentation des APIs est une compétence clé mêlant technique et conception.

---

## Diagramme conceptuel d’une API REST

```text
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database


### Composants

- **Client** : Le demandeur, souvent un navigateur ou une application.  
- **Serveur Web** : Gère la requête entrante, agit comme intermédiaire vers l’API.  
- **Serveur API** : Traite la logique métier et les requêtes.  
- **Base de données** : Stocke les données consultées ou modifiées.

---

### Flux

1. Le client envoie une requête HTTP/HTTPS au serveur web.  
2. Le serveur web transmet la requête au serveur API.  
3. Le serveur API traite la requête et interagit avec la base de données si nécessaire.  
4. Le serveur API renvoie la réponse au serveur web.  
5. Le serveur web retourne la réponse finale au client.
