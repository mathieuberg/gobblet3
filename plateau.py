"""Module Joueur

Functions:
    * Plateau - Classe représentant un Plateau.
"""

from http.client import GONE
from gobblet import Gobblet, GobbletError


class Plateau:
    """
    Plateau
    """

    def __init__(self, plateau):
        """Constructeur de Plateau

        Vous ne devez PAS modifier cette méthode

        Args:
            plateau (list): Plateau à construire tel que représenté dans l'énoncé
        """
        self.plateau = self.valider_plateau(plateau)

    def valider_plateau(self, plateau):
        """Validateur de Plateau

        Args:
            plateau (list): Plateau tel que représenté dans l'énoncé

        Returns:
            list: Plateau composé de liste de Gobblets ou None pour l'absence de Gobblet

        Raises:
            GobbletError: Le plateau doit être une liste
            GobbletError: Le plateau ne possède pas le bon nombre de ligne
            GobbletError: Le plateau ne possède pas le bon nombre de colonne dans les lignes
            GobbletError: Les Gobblets doivent être des listes de paires ou une liste vide
        """
        if not isinstance(plateau, list):
            raise GobbletError("Le plateau doit être une liste")
        if len(plateau) != 4:
            raise GobbletError("Le plateau ne possède pas le bon nombre de ligne")
        if len(plateau[0]) != 4:
            raise GobbletError('Le plateau ne possède pas le bon nombre de colonne dans les lignes')
        for listes in plateau:
            for car in listes:
                if len(car) not in [0, 2]:
                    raise GobbletError('Les Gobblets doivent être des listes de paires ou une liste vide')
        return plateau

    def __str__(self):
        plateau = self.plateau
        "Une méthode de conversion en chaîne de caractères,"
        "où la chaîne produite est une représentation textuelle "
        "du plateau, en utilisant le même format que pour "
        "la phase 1 du projet."        


    def retirer_gobblet(self, no_colonne, no_ligne): 
        no_colonne = self.no_colonne
        no_ligne = self.no_ligne
        if not isinstance(int,no_colonne) or not isinstance(int,no_ligne):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if not isinstance(int,no_colonne) and not isinstance(int,no_ligne):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if int(no_ligne)< 0 or int(no_ligne)>3:
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if int(no_colonne)< 0 or int(no_colonne)>3:
                raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        else:
            return self.plateau[no_colonne][no_ligne]

    "Une méthode retirer_gobblet qui accepte en argument le numéro de colonne et le numéro de ligne de la case pour laquelle nous"
    "voulons retirer un gobelet et retourne le Gobblet retiré du plateau si l'argument est valide. En cas d'erreur, cette "
    "méthode soulève une exception de type GobbletError avec les messages spécifiés en docstring."


    def placer_gobblet(self, no_colonne, no_ligne, gobblet):

        if not isinstance(int,no_colonne) or not isinstance(int,no_ligne):
             raise GobbletError('Ligne et colonne doivent être des entiers')
        if int(no_ligne)< 0 or int(no_ligne)>3:
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if int(no_colonne)< 0 or int(no_colonne)>3:
                raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        else:
            gobbelet = self.plateau[no_colonne][no_ligne]
            return gobbelet
    
    "Une méthode placer_gobblet qui accepte en argument le numéro de colonne et "
    "le numéro de ligne représentant la case pour laquelle nous voulons placer un Gobblet et le Gobblet à placer "
    "si les arguments sont valides. En cas d'erreur, cette méthode soulève une exception de type GobbletError avec les" 
    "messages spécifiés en docstring."

    def état_plateau(self):
        if self.plateau
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """
