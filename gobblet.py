"""Module Gobblet

Attributes:
    GOBBLET_REPRÉSENTATION (dict): Constante représentant les gobelets des joueurs.

Functions:
    * Gobblet - Classe représentant un Gobblet.
    * GobbletError - Classe gérant les exceptions GobbletError.
    * interpréteur_de_commande - Génère un interpréteur de commande.
    * formater_jeu - Formater la représentation graphique d'un jeu.
    * formater_les_parties - Formater la liste des dernières parties.
"""

from argparse import ArgumentParser

# Voici la représentation des Gobblets, n'hésitez pas à l'utiliser.
# 1 pour le joueur 1, 2 pour le joueur 2.
GOBBLET_REPRÉSENTATION = {
    1: ["▫", "◇", "◯", "□"],
    2: ["▪", "◆", "●", "■"],
}

class Gobblet:
    """
    Gobblet
    """

    def __init__(self, grosseur, no_joueur):
        """Constructeur de gobelet.

        Ne PAS modifier cette méthode.

        Args:
            grosseur (int): Grosseur du Gobblet [0, 1, 2, 3].
            no_joueur (int): Numéro du joueur [1, 2].
        """
        self.grosseur, self.no_joueur = self.valider_gobblet(grosseur, no_joueur)

    def valider_gobblet(self, grosseur, no_joueur):
        "  sdas"
        if not isinstance(grosseur,int):
            raise GobbletError("La grosseur doit être un entier.")
        if grosseur < 0 or grosseur > 3:
            raise GobbletError("La grosseur doit être comprise entre 0 et 3.")
        if not isinstance(no_joueur,int):
            raise GobbletError("Le numéro du joueur doit être un entier.")
        if (int(no_joueur) <1  or int(no_joueur)> 2):
            raise GobbletError("Le numéro du joueur doit être 1 ou 2.")
        else:
            return (grosseur, no_joueur)

    def __str__(self):
        """Formater un gobelet.

        Returns:
            str: Représentation du gobelet pour le joueur.
        """
        if self.no_joueur == 1:
            if self.grosseur == 0:
                return "▫"
            if self.grosseur == 1:
                return "◇"
            if self.grosseur == 2:
                return "◯"
            if self.grosseur == 3:
                return "□"
        if self.no_joueur == 2:
            if self.grosseur == 0:
                return "▪"
            if self.grosseur == 1:
                return "◆"
            if self.grosseur == 2:
                return "●"
            if self.grosseur == 3:
                return "■"

    def __eq__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si les deux gobelets sont de même taille.
        """
        return self.grosseur == autre.grosseur

    def __gt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus gros que l'autre.
        """
        if self.grosseur < autre.grosseur:
            return True
        return False

    def __lt__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit que l'autre.
        """
        if self.grosseur > autre.grosseur:
            return True
        return False

    def __ne__(self, autre):
        """Comparer l'équivalence de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet n'est pas équivalent à l'autre.
        """
        if self.grosseur != autre.grosseur:
            return True
        return False

    def __ge__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus grand ou égal à l'autre.
        """
        if self.grosseur >= autre.grosseur:
            return True
        return False

    def __le__(self, autre):
        """Comparer la grosseur de deux gobelets.

        Args:
            autre (Gobblet | None): None ou Gobblet à comparer.

        Returns:
            bool: si ce gobelet est plus petit ou égal à l'autre.
        """
        if self.grosseur <= autre.grosseur:
            return True
        return False

    def état_gobblet(self):
        """Obtenir l'état du gobelet.

        Returns:
            list: la paire d'entiers représentant l'état du gobelet (numéro du joueur et grosseur du gobelet).
        """
        return [self.no_joueur, self.grosseur]


def interpréteur_de_commande():
    """Interpreteur de commande.

    Returns:
        Namespace: Un objet Namespace tel que retourné par parser.parse_args().
                   Cette objet aura l'attribut IDUL représentant l'idul du joueur
                   et l'attribut lister qui est un booléen True/False.
    """
    parser = ArgumentParser(description= 'gobblet')
    parser.add_argument('IDUL', help = 'IDUL du joueur')
    parser.add_argument('-l', '--lister', help = 'lister les parties existantes')

    # Complétez le code ici
    # vous pourriez aussi avoir à ajouter des arguments dans ArgumentParser(...)

    return parser.parse_args()

def formater_jeu(plateau, joueurs):
    """Formater un jeu.

    Args:
        plateau (Plateau): le plateau de jeu.
        joueurs (list): la liste des deux Joueurs.

    Returns:
        str: Représentation du jeu.
    """
    ncols = max(len(joueurs[0].nom), len(joueurs[1].nom)) + 13
    repjeu = (f"{' 0   1   2 ':>{ncols}}\n"
    f"{str(joueurs[0]):>{ncols}}\n"
    f"{str(joueurs[1]):>{ncols}}\n\n")
    return repjeu + str(plateau)


def formater_les_parties(parties):
    """Formater une liste de parties.

    L'ordre doit être exactement la même que ce qui est passé en paramètre.

    Args:
        parties (list): une liste des parties.

    Returns:
        str: Représentation des parties.
    """
    rep = []
    for i, partie in enumerate(parties, 1):
        if partie.get("gagnant", False):
            rep.append("{} : {}, {} vs {}, gagnant: {}".format(i, partie.get(
                "date"), partie.get("joueurs")[0], partie.get("joueurs")[1], partie.get("gagnant")))
        else:
            rep.append("{} : {}, {} vs {}".format(i, partie.get(
                "date"), partie.get("joueurs")[0], partie.get("joueurs")[1]))
    return "\n".join(rep)

class GobbletError(Exception):
    'dasads'
    def __str__(self):
        return f"{self.args}"
