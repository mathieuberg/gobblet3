"""Module Joueur

Functions:
    * Joueur - Classe représentant un joueur de Gobblet.
"""

from gobblet import Gobblet, GobbletError
from plateau import Plateau


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
        liste = [3, 2, 1, 0]


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

            return ori[0], dest

        else:
            x, y = ori
            if len(ori) != 2:
                raise GobbletError("L'origine doit être un entier ou une liste de 2 entiers.")
            if x not in (0, 1, 2, 3) or y not in (0, 1, 2, 3):
                raise GobbletError("L'origine n'est pas une case valide du plateau.")
            if plateau[liste[y]][x].grosseur < plateau[liste[j]][i].grosseur:
                raise GobbletError("La destination n'est pas une case valide du plateau.")
            if not plateau[liste[y]][x]:
                raise GobbletError("L'origine ne possède pas de gobelet.")
            if self.no_joueur != plateau[liste[y]][x].no_joueur:
                raise GobbletError("Le gobelet d'origine n'appartient pas au joueur.")
            return ori, dest

    def état_joueur(self):
        '  fsa  '
        liste = []
        for gobblet in self.piles:
            liste.append([gobblet.no_joueur, gobblet.grosseur])
        return {'nom': self.nom, 'piles': liste}
