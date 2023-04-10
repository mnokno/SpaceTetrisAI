from src.agents.agent import Agent
from src.agents.dnn_agent import DNNAgent
from src.agents.smarter_agent import SmarterAgent


class HybridAgent(Agent):

    def __init__(self):
        """
        Creates a new HybridAgent and initiates its components
        """
        self.smarter_agent = SmarterAgent()
        self.dnn_agent = DNNAgent()

    def score(self, board: list[int], left_piece: list[int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """
        return objective_score + self.smarter_agent.score(board, left_piece, objective_score, multiplier) + \
            int(self.dnn_agent.score(board, left_piece, objective_score, multiplier) * 0.1)
