import torch.nn as nn
from torch import Tensor


class SimpleNet(nn.Module):

    def __init__(self):
        super(SimpleNet, self).__init__()

        self.sequential = nn.Sequential(
            # board5x5=25 piece3x3=9 total=34
            nn.Linear(in_features=34, out_features=50),
            nn.Tanh(),

            nn.Linear(in_features=50, out_features=100),
            nn.Tanh(),

            nn.Linear(in_features=100, out_features=50),
            nn.Tanh(),

            nn.Linear(in_features=50, out_features=1)
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.sequential(x)
