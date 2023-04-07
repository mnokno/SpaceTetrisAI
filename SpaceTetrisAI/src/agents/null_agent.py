from src.agents.agent import Agent


class NullAgent(Agent):

    def score(self, board: [int], left_piece: [int], multiplier: [int]) -> int:
        """
        Always scores 0
        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return 0
