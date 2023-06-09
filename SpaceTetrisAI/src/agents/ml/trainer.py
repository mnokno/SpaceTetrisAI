import copy
import os
import torch
from src.agents import DNNAgent
from src.environment import *
from src.agents.ml import *


def train_agent(initial_barin: SimpleNet) -> None:
    """
    Trains the given barin
    :param initial_barin: Initial state of the brain
    """
    if not os.path.exists(os.getcwd() + "\\checkpoints"):
        os.makedirs(os.getcwd() + "\\checkpoints")

    population_size = 100
    parents = 5
    training_rounds = 250
    num_test_game = 100

    agents: list[DNNAgent] = []
    agent_scores: list[int] = []

    agents.clear()
    agents.append(DNNAgent(brain=initial_barin))
    for i in range(population_size - 1):
        agents.append(DNNAgent(get_mutated_brain(brain=initial_barin)))

    # Trains agents
    for i in range(training_rounds):
        # Initializes agent_score list
        agent_scores.clear()
        for _ in range(population_size):
            agent_scores.append(0)

        for game_id in range(num_test_game):
            pg: PieceGenerator = PieceGenerator()
            pg.get_piece(500)
            for agent_id in range(population_size):
                agent_scores[agent_id] += \
                    score_agent(agents[agent_id], Game(PieceGenerator(history=pg.get_history()))) / float(num_test_game)

        agent_scores_tuples = list(zip(agents, agent_scores))
        sorted_agents = sorted(agent_scores_tuples, key=lambda _x: _x[1], reverse=True)
        top_x_agents = sorted_agents[:parents]

        print("----------------------------------------------------------------------------------------")
        for x in range(len(top_x_agents)):
            torch.save(top_x_agents[x][0].get_barin(), f"checkpoints/gen_{i}_top_{x + 1}.pt")
            print(f"Top {x + 1} score: {top_x_agents[x][1]} over {num_test_game} test_games")
        print("----------------------------------------------------------------------------------------")

        agents.clear()
        for x in range(len(top_x_agents)):
            agents.append(DNNAgent(brain=top_x_agents[x][0].get_barin()))
            for _ in range(int(population_size / len(top_x_agents)) - 1):
                agents.append(DNNAgent(brain=get_mutated_brain(top_x_agents[x][0].get_barin())))


def get_mutated_brain(brain: SimpleNet) -> SimpleNet:
    """
    Crates a mutated copy of the given barin
    :param brain: Brain to mutate
    :return: Mutated brain
    """
    brain_copy = copy.deepcopy(brain)

    for param in brain_copy.parameters():
        noise = torch.randn(param.size()) * 0.01  # generate random noise
        param.data.add_(noise)  # add the noise to the parameter

    return brain_copy
