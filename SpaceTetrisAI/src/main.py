from src.environment.piece_generator import PieceGenerator
from src.environment.piece import Piece
from src.environment.precalculated_data import PrecalculatedData
from src.environment.board import Board
from src.environment.game import Game
from src.environment.evaluator import score_agent
from src.agents.agent import Agent
from src.agents.null_agent import NullAgent
from src.agents.random_agent import RandomAgent
from src.agents.noise_null_agent import NoiseNullAgent
from src.agents.smart_agent import SmartAgent


def format_board(number):
    formatted = ""
    for i in range(1, 6):
        line = ""
        for j in range(1, 6):
            if (number & (1 << (j + i * 7))) == (1 << (j + i * 7)):
                line += "1"
            else:
                line += "0"
        formatted = line + "\n" + formatted
    return formatted


if __name__ == '__main__':
    Piece.init()
    PrecalculatedData.init()

    agentR: Agent = RandomAgent()
    agentNN: Agent = NoiseNullAgent(noise=10)
    agentN: Agent = NullAgent()
    agentS: Agent = SmartAgent()

    agentR_score = 0
    agentNN_score = 0
    agentN_score = 0
    agentS_score = 0

    test_game = 100
    for i in range(test_game):
        pg: PieceGenerator = PieceGenerator()
        pg.get_piece(500)

        agentR_score += score_agent(agentR, Game(PieceGenerator(history=pg.get_history())))
        agentNN_score += score_agent(agentNN, Game(PieceGenerator(history=pg.get_history())))
        agentN_score += score_agent(agentN, Game(PieceGenerator(history=pg.get_history())))
        agentS_score += score_agent(agentS, Game(PieceGenerator(history=pg.get_history())))

    print("Average scores over " + str(test_game) + " games")
    print("Random agent:\t\t", float(agentR_score) / float(test_game))
    print("Noise Null agent:\t", float(agentNN_score) / float(test_game))
    print("Null agent:\t\t\t", float(agentN_score) / float(test_game))
    print("Smart agent:\t\t", float(agentS_score) / float(test_game))
