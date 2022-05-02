'aads'
from plateau import *
from joueur import Joueur
from gobblet import Gobblet
class Jeu:
    "asdasd"
    def __init__(self, idul, secret, id_partie = None, automatique = False):
        "asdads"
        self.idul = idul
        self.secret = secret
        self.id_partie = id_partie
        self.automatique = automatique
        self.plateau = Plateau(
            [
                [[], [], [], []],
                [[], [], [], []],
                [[], [], [], []],
                [[], [], [], []]
            ]
        )


    def jouer(self, joueur_1, joueur_2):
        prochain_tour_joueur_1 = True
        if prochain_tour_joueur_1:
            joueur = self.joueur_1
            prochain_tour_joueur_1 = False
        else:
            joueur = self.joueur_2
            prochain_tour_joueur_1 = True
        joueur.recuperer_coup()
