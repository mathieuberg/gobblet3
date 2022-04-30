# -*- coding: utf-8 -*-
"""Jeu Gobblet

Ce programme permet de joueur au jeu Gobblet.
"""
from api import débuter_partie, lister_parties
from gobblet import (
    formater_jeu,
    formater_les_parties,
    interpréteur_de_commande,
)
from joueur import Joueur
from plateau import Plateau

# Mettre ici votre secret récupérer depuis le site de PAX
SECRET = ""


if __name__ == "__main__":
    args = interpréteur_de_commande()
    if args.lister:
        parties = lister_parties(args.IDUL, SECRET)
        print(formater_les_parties(parties))
    else:
        id_partie, plateau, joueurs = débuter_partie(args.IDUL, SECRET)
        while True:
            # Implémentez votre boucle de jeu
            pass
