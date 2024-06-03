from state import State


class Player:
    def __init__(self, id):
        self.id = id  # DO NOT CHANGE
        self.hand = []  # DO NOT CHANGE
        self.team = 0  # DO NOT CHANGE

    def get_pass(self):
        """
        Passes 3 cards
        """
        _pass = []
        self.hand = [i for i in self.hand if i not in _pass]  # DO NOT CHANGE

    def receive_pass(self, _pass):
        """
        Receives the pass into hand
        """
        self.hand += _pass  # DO NOT CHANGE

    def assign_team(self, card):
        self.team = card  # DO NOT CHANGE

    def play(self, state: State) -> int:
        """
        Takes a State and returns a valid card
        """
        card = 0

        return card  # DO NOT CHANGE

    def update(self, state: State) -> None:
        """
        Takes a State and updates player information (however you like)
        This is your only way to gather information about the game and other players
        """
