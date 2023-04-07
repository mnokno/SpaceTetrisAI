from src.agents.agent import Agent
from random import randint


class RandomAgent(Agent):

    def __init__(self, noise: int = 1000):
        """
        Creates a new random agents that randomly guesses +- noise

        :param noise: Determines the guessing range
        """

        self.__noise = noise
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
        return randint(-self.__noise, self.__noise)
