import random
from random import randint


class PieceGenerator:
    """
    Piece generator can be used to generate random pieces and ensures that upcoming
    pieces do not change after backtracking
    """

    def __init__(self, seed: int = None, history: [(int, int)] = None):
        """
        Creates a new random piece generator
        :param seed: Optional parameter, seed to be set to random, WARNING random uses a shared instance so seed
        does not guarantee an output, set history to guarantee an output
        :param history: a history to be used by this piece generator
        """

        self.__history: [(int, int)] = []
        """                               
        Stores previously generated pieces
        """

        if seed is not None:
            random.seed(seed)
        if history is not None:
            for e in history:
                self.__history.append(e)

    def get_piece(self, time_stamp: int) -> (int, int):
        """
        Returns a new piece mask repointing to the given time_stamp

        :param time_stamp: How many piece where played in the game
        :return: return new piece maks
        """

        while not time_stamp < len(self.__history):
            self.__history.append((randint(0, 14), randint(0, 3)))

        if time_stamp < len(self.__history):
            return self.__history[time_stamp]

    def get_history(self) -> [(int, int)]:
        """
        Getter for history
        :return: History stack
        """
        return self.__history
    