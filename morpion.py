"""
Morpion NGASSAM Franck-Enrick (Tic-Tac-Toe) - Jeu en ligne de commande
"""


def creer_grille():
    """Crée une grille de jeu vide (3x3)."""
    return [[" " for _ in range(3)] for _ in range(3)]


def afficher_grille(grille):
    """Affiche la grille de jeu dans le terminal."""
    print("\n  1   2   3")
    for i, ligne in enumerate(grille):
        print(f"{i + 1} {' | '.join(ligne)}")
        if i < 2:
            print("  ---------")
    print()


def verifier_victoire(grille, joueur):
    """Vérifie si le joueur donné a gagné."""
    # Lignes et colonnes
    for i in range(3):
        if all(grille[i][j] == joueur for j in range(3)):
            return True
        if all(grille[j][i] == joueur for j in range(3)):
            return True

    # Diagonales
    if all(grille[i][i] == joueur for i in range(3)):
        return True
    if all(grille[i][2 - i] == joueur for i in range(3)):
        return True

    return False


def verifier_egalite(grille):
    """Vérifie si la grille est pleine (match nul)."""
    return all(grille[i][j] != " " for i in range(3) for j in range(3))


def obtenir_coup(grille, joueur):
    """Demande au joueur de saisir un coup valide."""
    while True:
        try:
            saisie = input(f"Joueur {joueur}, entrez votre coup (ligne colonne, ex: 1 2) : ")
            parts = saisie.strip().split()
            if len(parts) != 2:
                raise ValueError
            ligne, col = int(parts[0]) - 1, int(parts[1]) - 1
            if not (0 <= ligne <= 2 and 0 <= col <= 2):
                print(" Position hors de la grille. Choisissez entre 1 et 3.")
                continue
            if grille[ligne][col] != " ":
                print(" Cette case est déjà occupée. Choisissez une autre.")
                continue
            return ligne, col
        except (ValueError, IndexError):
            print(" Saisie invalide. Entrez deux chiffres séparés par un espace (ex: 1 2).")


def jouer_partie():
    """Lance et gère une partie complète."""
    grille = creer_grille()
    joueurs = ["X", "O"]
    tour = 0

    print("\n Bienvenue au Morpion !")
    print("Les cases sont numérotées : ligne (1-3) puis colonne (1-3).\n")

    while True:
        joueur = joueurs[tour % 2]
        afficher_grille(grille)

        ligne, col = obtenir_coup(grille, joueur)
        grille[ligne][col] = joueur

        if verifier_victoire(grille, joueur):
            afficher_grille(grille)
            print(f" Bravo ! Le joueur {joueur} a gagné !\n")
            return joueur

        if verifier_egalite(grille):
            afficher_grille(grille)
            print(" Match nul ! Bonne partie !\n")
            return None

        tour += 1


def main():
    """Point d'entrée principal du jeu."""
    scores = {"X": 0, "O": 0, "Nul": 0}

    while True:
        gagnant = jouer_partie()

        if gagnant:
            scores[gagnant] += 1
        else:
            scores["Nul"] += 1

        print(f" Scores — X : {scores['X']} | O : {scores['O']} | Nuls : {scores['Nul']}")

        rejouer = input("Voulez-vous rejouer ? (o/n) : ").strip().lower()
        if rejouer not in ("o", "oui", "y", "yes"):
            print("\nMerci d'avoir joué ! À bientôt ")
            break


if __name__ == "__main__":
    main()
