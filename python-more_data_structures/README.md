# Sets et Dictionnaires en Python

## Qu'est-ce qu'un set et comment les utiliser ?

En Python, un **set** est une collection non ordonnée d'éléments uniques. Contrairement aux listes et aux tuples, les sets ne contiennent pas d'éléments dupliqués et n'ont pas d'ordre spécifique.

### Comment utiliser un set ?
- Pour créer un set : `mon_set = {1, 2, 3}`
- Pour ajouter un élément : `mon_set.add(4)`
- Pour supprimer un élément : `mon_set.remove(3)` (lève une erreur si l'élément n'existe pas) ou `mon_set.discard(3)` (ne lève pas d'erreur)
- Pour vérifier si un élément existe : `3 in mon_set` (retourne `True` ou `False`)

## Les méthodes les plus courantes des sets et comment les utiliser

Voici quelques méthodes courantes pour manipuler les sets :

- `add(x)` : Ajoute l'élément `x` au set.
- `remove(x)` : Supprime l'élément `x` du set. Lève une erreur si l'élément n'existe pas.
- `discard(x)` : Supprime l'élément `x` du set sans lever d'erreur si l'élément n'existe pas.
- `pop()` : Supprime et renvoie un élément arbitraire du set.
- `clear()` : Supprime tous les éléments du set.
- `union(set)` : Retourne l'union de deux sets.
- `intersection(set)` : Retourne l'intersection de deux sets.
- `difference(set)` : Retourne la différence entre deux sets.

## Quand utiliser les sets plutôt que les listes ?

Les sets doivent être utilisés quand vous avez besoin :
- D'une collection d'éléments uniques.
- D'un test d'appartenance rapide (`in` est plus rapide dans un set que dans une liste).
- D'opérations d'union, d'intersection ou de différence.

Les listes, quant à elles, sont plus adaptées quand :
- L'ordre des éléments est important.
- Vous devez accéder à des éléments par un indice.
- Les éléments peuvent être dupliqués.

## Comment itérer sur un set ?

Pour itérer sur un set, vous pouvez utiliser une boucle `for`. Exemple :

```python
mon_set = {1, 2, 3, 4}
for element in mon_set:
    print(element)
```