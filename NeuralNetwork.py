import torch.nn as nn
import torch
from torchsummary import summary


class NeuralNetwork(nn.Module):

    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.linear1 = nn.Linear(363, 90)
        self.linear2 = nn.Linear(90, 70)
        self.linear3 = nn.Linear(70, 60)
        self.linear4 = nn.Linear(60, 50)
        self.linear5 = nn.Linear(50, 1)

        self.relu1 = nn.ReLU()
        self.relu2 = nn.ReLU()
        self.relu3 = nn.ReLU()
        self.relu4 = nn.ReLU()
        self.relu5 = nn.ReLU()


    def forward(self, x):

        x = self.linear1(x)
        x = self.relu1(x)

        x = self.linear2(x)
        x = self.relu2(x)

        x = self.linear3(x)
        x = self.relu3(x)

        x = self.linear4(x)
        x = self.relu4(x)

        x = self.linear5(x)
        x = self.relu5(x)

        return x