from card import *
from utils.exceptions import *


def get_order(player, players):
    return [players[k] for k in [(j + [i.id for i in players].index(player.id)) % 4 for j in range(4)]]


def valid_card(card):
    return card in all_cards


def valid_player(player):
    try:
        if type(player.id) != int: raise InvalidPlayerException("The player id type must be an integer")
    except:
        raise InvalidPlayerException("The player id must exist")
    try:
        if type(player.hand) != list: raise InvalidPlayerException("The player hand type must be a list")
    except:
        raise InvalidPlayerException("The player hand must exist")
    try:
        if type(player.team) != int: raise InvalidPlayerException("The player team type must be an integer")
    except:
        raise InvalidPlayerException("The player team must exist")
    try:
        if not callable(player.assign_team): raise InvalidPlayerException(
            "The function assign_team must follow the original signature")
    except:
        raise InvalidPlayerException("The function assign_team must exist")
    try:
        if not callable(player.update): raise InvalidPlayerException(
            "The function update must follow the original signature")
    except:
        raise InvalidPlayerException("The function update must exist")
    try:
        if not callable(player.play): raise InvalidPlayerException(
            "The function play must follow the original signature")
    except:
        raise InvalidPlayerException("The function play must exist")
    try:
        if not callable(player.get_pass): raise InvalidPlayerException(
            "The function get_pass must follow the original signature")
    except:
        raise InvalidPlayerException("The function get_pass must exist")
    try:
        if not callable(player.receive_pass): raise InvalidPlayerException(
            "The function receive_pass must follow the original signature")
    except:
        raise InvalidPlayerException("The function receive_pass must exist")
