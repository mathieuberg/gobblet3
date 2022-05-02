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
        "Une méthode de conversion en chaîne de caractères,"
        "où la chaîne produite est une représentation textuelle "
        "du plateau, en utilisant le même format que pour "
        "la phase 1 du projet."
        return self.formater_plateau(self.plateau)


    def retirer_gobblet(self, no_colonne, no_ligne): 
        "Une méthode retirer_gobblet qui accepte en argument le numéro de colonne et le numéro de ligne de la case pour laquelle nous"
        "voulons retirer un gobelet et retourne le Gobblet retiré du plateau si l'argument est valide. En cas d'erreur, cette "
        "méthode soulève une exception de type GobbletError avec les messages spécifiés en docstring."
        no_colonne = self.no_colonne
        no_ligne = self.no_ligne
        if not isinstance(int, no_colonne) or not isinstance(int, no_ligne):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if not isinstance(int, no_colonne) and not isinstance(int, no_ligne):
            raise GobbletError("Ligne et colonne doivent être des entiers")
        if int(no_ligne) < 0 or int(no_ligne) > 3:
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if int(no_colonne) < 0 or int(no_colonne) > 3:
                raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        else:
            return self.plateau[no_ligne][no_colonne].pop()


    def placer_gobblet(self, no_colonne, no_ligne, gobblet):
        "Une méthode placer_gobblet qui accepte en argument le numéro de colonne et "
        "le numéro de ligne représentant la case pour laquelle nous voulons placer un Gobblet et le Gobblet à placer "
        "si les arguments sont valides. En cas d'erreur, cette méthode soulève une exception de type GobbletError avec les" 
        "messages spécifiés en docstring."

        if not isinstance(int,no_colonne) or not isinstance(int,no_ligne):
             raise GobbletError('Ligne et colonne doivent être des entiers')
        if int(no_ligne) < 0 or int(no_ligne) > 3:
            raise GobbletError('Le numéro de la ligne doit être 0, 1, 2 ou 3')
        if int(no_colonne) < 0 or int(no_colonne) > 3:
                raise GobbletError('Le numéro de la colonne doit être 0, 1, 2 ou 3')
        else:
            self.plateau[no_ligne][no_colonne].append(gobblet)


    def état_plateau(self):
        """Obtenir l'état du plateau

        Returns:
            list: Liste contenant l'état du plateau tel que représenté dans l'énoncé
        """
        return self.plateau


    def formater_un_gobblet(gobblet):
        """Formater un Gobblet

        Args:
            gobblet (list): liste vide ou de 2 entier [x, y] représentant le Gobblet

        Returns:
            str: Représentation du Gobblet pour le bon joueur
        """
        if gobblet == []:
            car = ' '
            return car
        if gobblet[0] == 1:
            x = gobblet[1]
            if x == 0:
                car = "▫"
            if x == 1:
                car = "◇"
            if x == 2:
                car = "◯"
            if x == 3:
                car = "□"
        if gobblet[0] == 2:
            x = gobblet[1]
            if x == 0:
                car = "▪"
            if x == 1:
                car = "◆"
            if x == 2:
                car = "●"
            if x == 3:
                car = "■"
        return car


    def formater_plateau(self):
        """Formater un plateau
        plateau = [
        [[], [], [], []],
        [[], [], [], []],
        [[], [], [], []],
        [[[Gobblet(1, 1), Gobblet(2, 2)]]], [], [], []]
        ]
        Args:
            plateau (list): plateau de jeu 4 x 4

        Returns:
            str: Représentation du plateau avec ses Gobblet
        """
        car = list(range(16))
        for i in range(4):
            for j in range(4):
                if len(self.plateau[i][j]) > 0:
                    car[i][j] = self.formater_un_gobblet([self.plateau[i][j][-1].joueur, self.plateau[i][j][-1].grosseur])
                else: 
                    car[i][j] = self.formater_un_gobblet([])
            
        ligne1 = ('3 ' + car[0] +' | ' + car[1] + ' | ' + car[2] + ' | ' + car[3]) + '\n'
        ligne2 = (' ───┼───┼───┼───') + '\n'
        ligne3 = ('2 ' + car[4] +' | ' + car[5] + ' | ' + car[6] + ' | ' + car[7]) + '\n'
        ligne4 = (' ───┼───┼───┼───') + '\n'
        ligne5 = ('1 ' + car[8] +' | ' + car[9] + ' | ' + car[10] + ' | ' + car[11]) + '\n'
        ligne6 = (' ───┼───┼───┼───') + '\n'
        ligne7 = ('0 ' + car[12] +' | ' + car[13] + ' | ' + car[14] + ' | ' + car[15]) + '\n'
        ligne8 = ('  0   1   2   3')
        tableau = ligne1 + ligne2 + ligne3 + ligne4 + ligne5 + ligne6 + ligne7 + ligne8

        return tableau