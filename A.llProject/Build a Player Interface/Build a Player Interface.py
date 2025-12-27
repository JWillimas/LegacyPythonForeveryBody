import random
from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self):
        self.moves = []                 # empty list
        self.position = (0, 0)           # starting position
        self.path = [self.position]      # path starts with initial position

    def make_move(self):
        move = random.choice(self.moves)     # pick random move
        x, y = self.position
        dx, dy = move

        self.position = (x + dx, y + dy)     # update position
        self.path.append(self.position)      # record path

        return self.position

    @abstractmethod
    def level_up(self):
        pass


class Pawn(Player):
    def __init__(self):
        super().__init__()   # call Player.__init__

        # basic moves: up, down, left, right
        self.moves = [
            (0, 1),    # up
            (0, -1),   # down
            (-1, 0),   # left
            (1, 0)     # right
        ]

    def level_up(self):
        # add diagonal moves
        self.moves.extend([
            (1, 1),     # up-right
            (1, -1),    # down-right
            (-1, 1),    # up-left
            (-1, -1)    # down-left
        ])

