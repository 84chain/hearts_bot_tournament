import random

from utils.card import *
from utils.util import *
from context import Context


class Game:
    def __init__(self, players):
        self.players = players
        self.context = Context()
        self.context.init(self.players)
        random.shuffle(team_cards)
        for i in range(4):
            self.players[i].assign_team(team_cards[i])

    def _pass(self, direction):
        self.context.execute_pass(direction)

    def play(self):
        for _ in range(13):
            order = get_order(self.context.next_player, self.players)
            for p in order:
                self.context.update(p.play(self.context.current_state), p.id)
        return self.context
