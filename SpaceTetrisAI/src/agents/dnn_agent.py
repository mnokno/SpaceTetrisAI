import os
import torch
from src.agents.agent import Agent
from src.agents.ml.architectures import SimpleNet


class DNNAgent(Agent):

    def __init__(self, brain: SimpleNet = None):
        """
        Creates a new DNNAgent with the given brain, if no brain is provided the pretrained brain will be loaded
        :param brain: Barin for the agent
        """
        if brain is None:
            self.__brain = torch.load(os.getcwd() + "\\src\\agents\\ml\\pre_trained.pt")
        else:
            self.__brain: SimpleNet = brain

    def score(self, board: list[int], left_piece: list[int], objective_score: int, multiplier: int) -> int:
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
        if next(self.__brain.parameters()).is_cuda:
            input_tensor.cuda()

        return self.__brain.forward(input_tensor) * 100

    def get_barin(self) -> SimpleNet:
        """
        Getter for agents barin
        :return: Agents brain
        """
        return self.__brain
