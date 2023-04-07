import torch.nn as nn
from torch import Tensor


class SimpleNet(nn.Module):

    def __init__(self):
        super(SimpleNet, self).__init__()

        self.sequential = nn.Sequential(
            # board5x5=25 piece3x3=9 total=34
            nn.Linear(in_features=34, out_features=1000),
            nn.BatchNorm1d(1000),
            nn.Tanh(),
            nn.Dropout(0.2),

            nn.Linear(in_features=1000, out_features=10000),
            nn.BatchNorm1d(10000),
            nn.Tanh(),
            nn.Dropout(0.2),

            nn.Linear(in_features=10000, out_features=1000),
            nn.BatchNorm1d(1000),
            nn.ReLU(),
            nn.Dropout(0.2),

            nn.Linear(in_features=1000, out_features=1),
            nn.Sigmoid()
        )

    def forward(self, x: Tensor) -> Tensor:
        return self.sequential(x)
