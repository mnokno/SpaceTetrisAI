from src.agents.agent import Agent
from random import randint


class RandomAgent(Agent):

    def __init__(self, upper_bound: int = 1000, lower_bound: int = -1000):
        """
        Creates a new random agents that randomly guesses between lower_bound and upper_bound

        :param upper_bound: Upper bound for a guess
        :param lower_bound: Lower bound for a guess
        """

        self.__upper_bound = upper_bound
        """
        Upper bound for a guess
        """
        self.__lower_bound = lower_bound
        """
        Lower bound for a guess
        """

    def score(self, board: [int], left_piece: [int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return randint(self.__lower_bound, self.__upper_bound)
