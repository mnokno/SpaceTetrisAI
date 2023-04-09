from src.agents.ml.architectures import SimpleNet
from src.agents.ml.trainer import train_agent

if __name__ == '__main__':
    model = SimpleNet()
    model.requires_grad_(False)
    train_agent(model)
