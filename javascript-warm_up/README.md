# Introduction à la programmation JavaScript

Ce document présente les bases de la programmation en JavaScript, un langage puissant et très utilisé pour le développement web.

---

## Pourquoi la programmation JavaScript est incroyable

JavaScript est un langage polyvalent qui permet de rendre les pages web interactives, de créer des applications côté client et serveur, et bénéficie d'un écosystème riche et dynamique. Il est simple à apprendre tout en étant très puissant.

---

## Comment exécuter un script JavaScript

- Dans un navigateur web, on peut inclure un script JavaScript dans une page HTML avec la balise `<script>`.
- En dehors du navigateur, on peut utiliser Node.js pour exécuter des fichiers `.js` en ligne de commande :  
```bash
node monScript.js
```

Comment créer des variables et des constantes

Variables : valeurs modifiables, déclarées avec `let` ou `var`.
Constantes : valeurs fixes, déclarées avec `const`.
```javascript
let age = 25;
const pi = 3.14;
```

Différences entre var, const et let

`var` : portée globale ou fonctionnelle, hoisting (remontée de déclaration), moins utilisé aujourd’hui.
`let` : portée de bloc, plus sûr et recommandé pour les variables modifiables.
`const` : portée de bloc, variable immuable (sa référence ne peut pas changer).
Les types de données disponibles en JavaScript

Types primitifs : string, number, boolean, null, undefined, symbol, bigint.
Types complexes : object (tableaux, objets, fonctions).

Utilisation des instructions if et if ... else
```javascript
if (condition) {
  // bloc exécuté si la condition est vraie
} else {
  // bloc exécuté sinon
}
```

Utilisation des commentaires
```javascript
Commentaire sur une ligne : // Ceci est un commentaire
Commentaire sur plusieurs lignes :

/*
  Ceci est un commentaire
  sur plusieurs lignes
*/
```

Affectation de valeurs aux variables
```javascript
let x;
x = 10;          // assignation simple
let y = 20;      // déclaration avec assignation
```

Utilisation des boucles `while` et `for`

Boucle while :
```javascript
while (condition) {
  // instructions à répéter
}
```

Boucle for :
```javascript
for (let i = 0; i < 5; i++) {
  // instructions à répéter
}
```

Utilisation des instructions `break` et `continue`

`break` : quitte la boucle immédiatement.
`continue` : saute l’itération en cours et passe à la suivante.

Qu’est-ce qu’une fonction et comment l’utiliser

Une fonction est un bloc de code réutilisable, définie ainsi :
```javascript
function maFonction(param) {
  // code
  return param * 2;
}

let resultat = maFonction(5);
```

Que renvoie une fonction sans instruction return

Une fonction sans return renvoie automatiquement undefined.

Portée des variables (scope)

Variables var ont une portée globale ou locale à la fonction.
Variables let et const ont une portée limitée au bloc { ... } où elles sont déclarées.
Opérateurs arithmétiques et leur utilisation

Addition : +
Soustraction : -
Multiplication : *
Division : /
Modulo (reste) : %
Exponentiation : **

Manipulation des dictionnaires (objets)
````javascript
let objet = {
  cle: "valeur",
  nombre: 42
};

console.log(objet.cle); // "valeur"
objet.nouvelleCle = "nouvelle valeur";
````

Comment importer un fichier JavaScript

En HTML avec la balise <script src="fichier.js"></script>.
En Node.js avec require() ou, en module ES6, avec import :

import { maFonction } from './monModule.js';
