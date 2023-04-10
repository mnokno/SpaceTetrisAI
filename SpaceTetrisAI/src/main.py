from environment import *
from agents import *


if __name__ == '__main__':
    agentR: Agent = RandomAgent()
    agentNN: Agent = NoiseNullAgent(noise=10)
    agentN: Agent = NullAgent()
    agentS: Agent = SmartAgent()
    agentDNN: Agent = DNNAgent()
    agentSR: Agent = SmarterAgent()
    agentH: Agent = HybridAgent()

    agentR_score = 0
    agentNN_score = 0
    agentN_score = 0
    agentS_score = 0
    agentDNN_score = 0
    agentSR_score = 0
    agentH_score = 0

    test_game = 1000
    for i in range(test_game):
        pg: PieceGenerator = PieceGenerator(i)
        pg.get_piece(500)

        agentR_score += score_agent(agentR, Game(PieceGenerator(history=pg.get_history())))
        agentNN_score += score_agent(agentNN, Game(PieceGenerator(history=pg.get_history())))
        agentN_score += score_agent(agentN, Game(PieceGenerator(history=pg.get_history())))
        agentS_score += score_agent(agentS, Game(PieceGenerator(history=pg.get_history())))
        agentDNN_score += score_agent(agentDNN, Game(PieceGenerator(history=pg.get_history())))
        agentSR_score += score_agent(agentSR, Game(PieceGenerator(history=pg.get_history())))
        agentH_score += score_agent(agentH, Game(PieceGenerator(history=pg.get_history())))

    print("Average scores over " + str(test_game) + " games")
    print("Random agent:\t\t", float(agentR_score) / float(test_game))
    print("Noise Null agent:\t", float(agentNN_score) / float(test_game))
    print("Null agent:\t\t\t", float(agentN_score) / float(test_game))
    print("Smart agent:\t\t", float(agentS_score) / float(test_game))
    print("DNN agent:\t\t\t", float(agentDNN_score) / float(test_game))
    print("Smarter agent:\t\t", float(agentSR_score) / float(test_game))
    print("Hybrid agent:\t\t", float(agentH_score) / float(test_game))
