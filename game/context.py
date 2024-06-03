import random

from utils.card import *
from utils.exceptions import *
from utils.util import *
from state import State


class Context:
    """
    A Context is a snapshot of the current game. It acts as an interface between State and Game.
    Most game-based information is stored in the Context, but no high-level player information (only player ids).
    As a result, the Context contains all the game logic and will drive the game forward.
    Players do not have access to Context.
    """

    def __init__(self):
        self.round = 1
        self.players = []  # players are added to the list in a clockwise fashion
        self.next_player = None

        self.current_state = State()
        self.past_states = []

    def init(self, players: list) -> None:
        """
        initializes the game, shuffles cards, deals cards
        """
        self.players = players
        deck = all_cards
        random.shuffle(deck)

        for i in range(4):
            players[i].deal(deck[i * 13: (i + 1) * 13])

    def execute_pass(self, direction: int) -> None:
        """
        The direction integer is as follows:
        -1 for passing right
        1 for passing left
        2 for passing across

        The reason being is (i + direction) % 4 is always the desired end index
        """
        passes = []
        for i in self.players:
            _pass = i.get_pass()

            # Validity Check
            if len(_pass) != 3:
                raise InvalidPassException("The length of the pass is not 3")
            if not [_ for _ in _pass if valid_card(_)]:
                raise InvalidCardException("There is an invalid card being passed")

            passes.append(_pass)
        for i in range(4):
            self.players[(i + direction) % 4].receive_pass(passes[i])
        self.next_player = [i for i in self.players if club_3 in i.hand][0]

    def update(self, card: int, player: int) -> None:
        """
        Updates the Context
        """
        if not valid_card(card):
            raise InvalidCardException("There is an invalid card being played")

        # similar to State.update, but with more game logic
        self.next_player = (self.players.index(player) + 1) % 4  # clockwise is +1

        # update states
        self.current_state.update(card, player)

        if self.current_state.length() == 4:
            self.next_player = self.current_state.current_taker()

            self.past_states.append(self.current_state)
            self.current_state = State()
            self.round += 1
        for i in self.players:
            i.update(self.current_state)
