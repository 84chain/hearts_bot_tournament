from utils.card import *


class State:
    """
    A State is a representation of a single round in hearts. A State starts empty and will inaccessible once full.
    Cards are played into the State via State.update(card, player).
    Context will roll over a new State once the current one is deemed over.
    Getters and other utility functions have been provided.
    """

    def __init__(self):
        # cards played in the round, added as a card is played
        self.cards = []

        # players in the round, added as a player plays
        self.players = []

        # start off None but is set to 1 of 4 suits once self.cards has at least 1 entry
        self.suit = None

    def update(self, card: int, player: int) -> None:
        # takes a card and the player id who played it and updates the state

        if not self.cards:  # to update suit
            self.suit = card >> 13

        # updating
        self.cards.append(card)
        self.players.append(player)

    # getters
    def length(self):
        return len(self.cards)

    # other
    def highest(self):
        # returns the current highest card, else None
        try:
            return max([i for i in self.cards if i >> 13 == self.suit])
        except:
            return

    def current_taker(self):
        # returns the player id of the currently taking player
        if not len(self.players): return
        return self.players[self.cards.index(State.highest(self))]

    def points(self):
        # returns the current point count of the round
        points = sum([all_points[i] for i in self.cards])
        return points if club_10 not in self.cards else points * 2
