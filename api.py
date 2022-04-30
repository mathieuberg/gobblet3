"""Module d'API du jeu Gobblet

Attributes:
    URL (str): Constante représentant le début de l'url du serveur de jeu.

Functions:
    * lister_parties - Récupérer la liste des parties reçus du serveur.
    * débuter_partie - Créer une nouvelle partie et retourne l'état de cette dernière.
    * récupérer_partie - Retrouver l'état d'une partie spécifique.
    * jouer_coup - Exécute un coup et retourne le nouvel état de jeu.
"""

import requests

URL = "https://pax.ulaval.ca/gobblet/api/"


def lister_parties(idul, secret):
    """Lister les parties

    Args:
        idul (str): idul du joueur
        secret (str): secret récupérer depuis le site de PAX

    Raises:
        PermissionError: Erreur levée lorsque le serveur retourne un code 401.
        RuntimeError: Erreur levée lorsque le serveur retourne un code 406.
        ConnectionError: Erreur levée lorsque le serveur retourne un code autre que 200, 401 ou 406

    Returns:
        list: Liste des parties reçues du serveur,
             après avoir décodé le json de sa réponse.
    """
    rep = requests.get(URL + 'parties',auth =(idul, secret))
    if rep.status_code == 200:
        rep = rep.json()
        return rep.get('parties')
    if rep.status_code == 406:
        rep = rep.json()
        raise RuntimeError(rep.get('message'))
    if rep.status_code == 401:
        rep = rep.json()
        raise PermissionError(rep.get('message'))
    else:
        raise ConnectionError('erreur')


def débuter_partie(idul, secret):
    '     asd  '
    rep2 = requests.post(URL + 'partie', auth = (idul, secret))
    if rep2.status_code == 200:
        rep2 = rep2.json()
        return (rep2.get('id'), rep2.get('plateau'), rep2.get('joueurs'))
    if rep2.status_code == 401:
        raise PermissionError(rep2.get('message'))
    if rep2.status_code == 406:
        raise RuntimeError(rep2.get('message'))
    else:
        raise ConnectionError("erreur")


def récupérer_partie(id_partie, idul, secret):
    '  dasasdasd   '
    URL3 = "https://pax.ulaval.ca/gobblet/api/partie/" +id_partie
    rep3 = requests.get(URL3, auth = ( idul, secret))
    if rep3.status_code == 200:
        rep3 = rep3.json()
        return (rep3.get('id'), rep3.get('plateau'), rep3.get('joueurs'))
    if rep3.status_code == 401:
        raise PermissionError(rep3.get('message'))
    if rep3.status_code == 406:
        raise RuntimeError(rep3.get('message'))
    else:
        raise ConnectionError("erreur")


def jouer_coup(id_partie, origine, destination, idul, secret):
    ' adsa '
    rep = requests.put(
        URL + 'jouer',
        auth = (idul, secret),
        json={
        "id": id_partie,
        "destination": destination,
        "origine": origine,
    }
    )
    dico = rep.json()

    if rep.status_code == 200:
        return dico['id'], dico['plateau'], dico['joueurs']

    if rep.status_code == 401:
        raise PermissionError(dico['message'])
    if rep.status_code == 406:
        raise RuntimeError(dico['message'])
    if rep.status_code != 200 and rep.status_code != 401 and rep.statuscode != 406:
        raise ConnectionError
    if dico['gagnant'] is not None:
        raise StopIteration(dico['gagnant'])
