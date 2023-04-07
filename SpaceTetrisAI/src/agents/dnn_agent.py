import torch
from src.agents.agent import Agent
from src.agents.ml.architectures import SimpleNet
from torch import Tensor


class DNNAgent(Agent):

    def __init__(self, barin: SimpleNet):
        """
        Creates a new DNNAgent with the given brain
        :param barin: Barin for the agent
        """
        self.__barin: SimpleNet = barin

    def score(self, board: [int], left_piece: [int], objective_score: int, multiplier: int) -> int:
        """
        Scores the given board based on the board itself, other piece and multiple

        :param board: Board state in a flat vector
        :param left_piece: Piece left in  a flat vector
        :param objective_score: Current game score
        :param multiplier: Multiplier
        :return: Score for this position
        """

        # convert the board and left piece into a single tensor
        input_tensor = torch.tensor(board + left_piece, dtype=torch.float32).unsqueeze(0)

        return objective_score + self.__barin.forward(input_tensor) * 1000

    def get_barin(self) -> SimpleNet:
        """
        Getter for agents barin
        :return: Agents brain
        """
        return self.__barin
