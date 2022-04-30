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
        for liste in plateau:
            for car in plateau:

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

    def placer_gobblet(self, no_colonne, no_ligne, gobblet):

        if not isinstance(int,no_colonne) or not isinstance(int,no_ligne):
             raise GobbletError('Ligne et colonne doivent être des entiers')
        if int(no_ligne)< 0 or int(no_ligne)>3:
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if int(no_colonne)< 0 or int(no_colonne)>3:
                raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        """Placer un Gobblet dans le plateau

        Args:
            no_colonne (int): Numéro de la colonne (0, 1, 2 ou 3)
            no_ligne (int): Numéro de la ligne (0, 1, 2 ou 3)
            gobblet (Gobblet): Gobblet à placer dans le plateau

        Raises:
            GobbletError: Ligne et colonne doivent être des entiers
            GobbletError: Le numéro de la ligne doit être 0, 1, 2 ou 3
            GobbletError: Le numéro de la colonne doit être 0, 1, 2 ou 3
            GobbletError: Le Gobblet ne peut pas être placé sur la case demandée
        """
    
    
    def état_plateau(self):
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """
