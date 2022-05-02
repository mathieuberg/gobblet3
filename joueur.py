"""Module Joueur

Functions:
    * Joueur - Classe représentant un joueur de Gobblet.
"""

from gobblet import Gobblet, GobbletError
from plateau import Plateau
import numpy as np

class Joueur:
    """
    Joueur de Gobblet.
    """

    def __init__(self, nom, no_joueur, gobelets):
        '       '
        self.nom, self.no_joueur, self.piles = self.valider_joueur(nom, no_joueur, gobelets)

    def valider_joueur(self, nom, no_joueur, gobelets):
        '   dasasf    '
        if not isinstance(nom, str) and nom:
            raise GobbletError('Le nom du joueur doit être une chaine de caractères non vide.')
        if no_joueur != 1 and no_joueur != 2:
            raise GobbletError('Le numéro du joueur doit être 1 ou 2.')
        if not isinstance(gobelets, list):
            raise GobbletError("Les piles de gobelets doivent être spécifiés sous la forme d'une liste.")
        if len(gobelets) != 3:
            raise GobbletError('Le joueur doit possèder 3 piles.')
        for i in gobelets:
            if not isinstance(i, list):
                raise GobbletError('Une pile doit être une liste de deux entiers ou une liste vide.')
            #elif i or len(i) != 2 and not isinstance(i[0], int) and not isinstance(i[1], int):
            elif not ((len(i) == 2 and isinstance(i[0], int) and isinstance(i[1], int)) or not i):
                raise GobbletError('Une pile doit être une liste de deux entiers ou une liste vide.')
        return nom, no_joueur, [(Gobblet(i[1], i[0]) if i else None) for i in gobelets]


    def __str__(self):
        "    fas   "
        liste = []
        for gobblet in self.piles:
            liste.append(str(gobblet) if gobblet else '   ')
        return f'{self.nom}: {" ".join(liste)}'

    def retirer_gobblet(self, no_pile):
        "    asf     "
        if isinstance(no_pile, int) is False:
            raise GobbletError('Le numéro de la pile doit être un entier.')
        if no_pile not in (0, 1, 2):
            raise GobbletError('Le numéro de la pile doit être 0, 1 ou 2.')
        if not self.piles[no_pile]:
            raise GobbletError('Le joueur ne possède pas de gobelet pour la pile demandée.')
        return self.piles[no_pile]


    def placer_gobblet(self, no_pile, gobelets):
        " adsdas"
        if not isinstance(no_pile, int):
            raise GobbletError('Le numéro de la pile doit être un entier.')
        if no_pile not in (0, 1, 2):
            raise GobbletError('Le numéro de la pile doit être 0, 1 ou 2.')
        if gobelets.no_joueur != self.no_joueur:
            raise GobbletError('Le gobelet doit appartenir au joueur.')
        if self.piles[no_pile]:
            raise GobbletError('Vous ne pouvez pas placer un gobelet à cet emplacement.')
        self.piles[no_pile] = gobelets

    def récupérer_le_coup(self, plateau):
        '   fas      '
        print('Quel gobelet voulez-vous déplacer:')
        ori = input('Donnez le numéro de la pile (p) ou la position sur le plateau (x,y): ').split(',')
        dest = input('Où voulez-vous placer votre gobelet (x,y): ').split(',')

        ori, dest = self.valider_coup(ori, dest, plateau)
        try:
            ori = list(map(int, ori))
        except:
            raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")
        try:
            dest = list(map(int, dest))
        except:
            raise GobbletError("La destination doit être une liste de 2 entiers.")

        if len(dest) != 2:
            raise GobbletError("La destination doit être une liste de 2 entiers.")
        j_dest, i_dest = dest

        if i_dest not in (0, 1, 2, 3) or j_dest not in (0, 1, 2, 3):
            raise GobbletError("La destination n'est pas une case valide du plateau.")

        # Gobblet pris de la pile
        if len(ori) == 1:
            pile = ori[0]
            plateau.placer_gobblet(j_dest, i_dest, self.piles[pile].pop())
        # Goblet pris du plateau
        else:
            j_ori, i_ori = ori
            plateau.placer_gobblet(j_dest, i_dest, plateau.plateau[i_ori][j_ori].pop())

    def état_joueur(self):
        '  fsa  '
        liste = []
        for gobblet in self.piles:
            liste.append([gobblet.no_joueur, gobblet.grosseur])
        return {'nom': self.nom, 'piles': liste}

    def valider_coup(self, ori, dest, plateau):
        'das'
        try:
            ori = list(map(int, ori))
        except:
            raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")
        try:
            dest = list(map(int, dest))
        except:
            raise GobbletError("La destination doit être une liste de 2 entiers.")
        if len(dest) != 2:
            raise GobbletError("La destination doit être une liste de 2 entiers.")
        j_dest, i_dest = dest
        if i_dest not in (0, 1, 2, 3) or j_dest not in (0, 1, 2, 3):
            raise GobbletError("La destination n'est pas une case valide du plateau.")
        # Gobblet pris de la pile
        if len(ori) == 1:
            pile = ori[0]
            if pile not in (0, 1, 2):
                raise GobbletError("L'origine n'est pas une pile valide.")
            if len(self.piles[pile]) == 0:
                raise GobbletError("L'origine ne possède pas de gobelet.")
            gobblet = self.piles[pile][-1]
            if len(plateau.plateau[i_dest][j_dest]) > 0 and plateau.plateau[i_dest][j_dest][-1].grosseur >= gobblet.grosseur:
                raise GobbletError("La destination n'est pas une case valide du plateau")
        # Goblet pris du plateau
        else:
            if len(ori) != 2:
                raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")
            j_ori, i_ori = ori
            if i_ori not in (0, 1, 2, 3) or j_ori not in (0, 1, 2, 3):
                raise GobbletError("L'origine n'est pas une case valide du plateau.")
            if plateau.plateau[i_ori][j_ori].grosseur < plateau.plateau[i_ori][j_ori].grosseur:
                raise GobbletError("La destination n'est pas une case valide du plateau.")
            if not plateau.plateau[i_ori][j_ori]:
                raise GobbletError("L'origine ne possède pas de gobelet.")
            if self.no_joueur != plateau.plateau[i_ori][j_ori].no_joueur:
                raise GobbletError("Le gobelet d'origine n'appartient pas au joueur.")
        return ori, dest
  

class Automate(Joueur):
    'dasads'
    def récupérer_le_coup(self, plateau):
        '   fas      '
        liste = [3, 2, 1, 0]
        for ori in range(0,1):
            ori = np.random.choice(range(0, 3), size=np.random.choice(range(2), 1), replace=False)
        for dest in range(0,1):
            dest = int(np.random.choice(range(0, 3), 1))
        try:
            ori = list(map(int, ori))
        except:
            raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")


        try:
            dest = list(map(int, dest))
        except:
            raise GobbletError("La destination doit être une liste de 2 entiers.")

        if len(dest) != 2:
            raise GobbletError("La destination doit être une liste de 2 entiers.")
        i, j = dest
        if i not in (0, 1, 2, 3) or j not in (0, 1, 2, 3):
            raise GobbletError("La destination n'est pas une case valide du plateau.")

        if len(ori) == 1:
            if ori[0] not in (0, 1, 2):
                raise GobbletError("L'origine n'est pas une pile valide.")
            if not self.piles[ori[0]]:
                raise GobbletError("L'origine ne possède pas de gobelet.")

            gob = self.piles[ori[0]]
            if gob.grosseur < plateau[liste[j]][i].grosseur:
                raise GobbletError("La destination n'est pas une case valide du plateau.")
        else:
            if gob.grosseur > plateau[liste[j]][i].grosseur:
                plateau[j][i].append()
