from src.agents.agent import Agent


class NullAgent(Agent):

    def score(self, board: [int], left_piece: [int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return objective_score
