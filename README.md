# 🎮 Morpion (Tic-Tac-Toe)

Un jeu de morpion en ligne de commande, écrit en Python.

## Fonctionnalités

- Partie à deux joueurs (X et O) sur le même ordinateur
- Détection automatique de victoire (lignes, colonnes, diagonales)
- Détection du match nul
- Suivi des scores entre les parties
- Validation des saisies avec messages d'erreur clairs

## Lancer le jeu

```bash
python morpion.py
```

## Exemple de partie

```
🎮 Bienvenue au Morpion !
Les cases sont numérotées : ligne (1-3) puis colonne (1-3).

  1   2   3
1   |   |  
  ---------
2   |   |  
  ---------
3   |   |  

Joueur X, entrez votre coup (ligne colonne, ex: 1 2) : 2 2

  1   2   3
1   |   |  
  ---------
2   | X |  
  ---------
3   |   |  
```

## Structure du projet

```
morpion/
├── morpion.py   # Logique principale du jeu
└── README.md    # Ce fichier
```

## Règles du jeu

1. Le joueur **X** commence toujours.
2. À chaque tour, le joueur saisit la **ligne** puis la **colonne** (de 1 à 3).
3. Le premier joueur à aligner **3 symboles** (ligne, colonne ou diagonale) gagne.
4. Si toutes les cases sont remplies sans gagnant, c'est un **match nul**.

## Auteur

NGASSAM Franck-Enrick
