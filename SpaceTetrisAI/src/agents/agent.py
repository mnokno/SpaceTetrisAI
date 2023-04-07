import abc


class Agent:
    """
    Agent interface, used as a template for other agents.
    """

    @abc.abstractmethod
    def score(self, board: [int], left_piece: [int], multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple
        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param multiplier: Multiplier
        :return: Score for this position
        """
        pass
