# Manipulation du DOM en JavaScript

Ce dépôt explique les bases de la manipulation du DOM (Document Object Model) en JavaScript. Il couvre les sélections d'éléments HTML, la modification de leur contenu ou de leur style, la gestion des événements, ainsi que les requêtes HTTP via `XMLHttpRequest` et l'API Fetch.


## Comment sélectionner des éléments HTML en JavaScript

```js
// Par ID
const element = document.getElementById("mon-id");

// Par classe
const elements = document.getElementsByClassName("ma-classe");

// Par nom de balise
const tags = document.getElementsByTagName("div");

// Avec querySelector (CSS selector)
const elem = document.querySelector(".ma-classe");

// Avec querySelectorAll (plusieurs éléments)
const allElems = document.querySelectorAll("div.exemple");
```

## Différences entre les sélecteurs par ID, classe et nom de balise

| Sélecteur     | Méthode JavaScript         | Unicité  | Type de retour        |
| ------------- | -------------------------- | -------- | --------------------- |
| ID            | `getElementById()`         | Unique   | Élément unique        |
| Classe        | `getElementsByClassName()` | Multiple | Collection d’éléments |
| Nom de balise | `getElementsByTagName()`   | Multiple | Collection d’éléments |

## Modifier le style d’un élément HTML
```javascript
const element = document.getElementById("mon-id");
element.style.color = "red";
element.style.backgroundColor = "yellow";
```

## Obtenir et mettre à jour le contenu d’un élément HTML
```javascript
// Obtenir le texte
const texte = element.textContent;

// Mettre à jour le texte
element.textContent = "Nouveau contenu";

// Obtenir HTML interne
const html = element.innerHTML;

// Mettre à jour HTML interne
element.innerHTML = "<strong>Texte en gras</strong>";
```

## Modifier le DOM
```javascript
// Créer un nouvel élément
const nouveauParagraphe = document.createElement("p");
nouveauParagraphe.textContent = "Paragraphe ajouté dynamiquement";

// Ajouter à la page
document.body.appendChild(nouveauParagraphe);

// Supprimer un élément
const aSupprimer = document.getElementById("supprimer-moi");
aSupprimer.remove();
```

## Faire une requête avec XMLHttpRequest
```javascript
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.exemple.com/donnees", true);
xhr.onload = function () {
  if (xhr.status === 200) {
    console.log(xhr.responseText);
  }
};
xhr.send();
```

## Faire une requête avec Fetch API
```javascript
fetch("https://api.exemple.com/donnees")
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Erreur :", error));
```

## Écouter / lier des événements du DOM
```javascript
document.addEventListener("DOMContentLoaded", function () {
  console.log("Le DOM est entièrement chargé");
});
```

## Écouter / lier des événements utilisateur
```javascript
const bouton = document.getElementById("mon-bouton");
bouton.addEventListener("click", function () {
  alert("Bouton cliqué !");
});
```