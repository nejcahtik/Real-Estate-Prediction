import torch.optim as optim
import torch.nn as nn
import numpy as np
from torch.utils.data import Dataset
import pandas as pd
from Dataset import mins, maxs

import torch
from tqdm.notebook import tqdm

from Dataset import SegmentationDataset
from NeuralNetwork import NeuralNetwork
torch.set_grad_enabled(True)  # Context-manager

net = NeuralNetwork()
net.cuda()

# Define the loss function
criterion = nn.MSELoss()

optimizer = optim.Adam(net.parameters(), lr=0.0001)
epochs = 2

trainset = SegmentationDataset(train=True)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=4,
                                          shuffle=True, num_workers=2)

testset = SegmentationDataset(train=False)
testloader = torch.utils.data.DataLoader(testset, batch_size=4,
                                         shuffle=False, num_workers=2)

print(net.linear1.weight.dtype)

for epoch in range(epochs):  # loop over the dataset multiple times
    for batch_idx, (inputs, targets) in enumerate(trainloader):
        # get the inputs; data is a list of [inputs, labels]
        inputs = inputs.cuda()
        targets = targets.cuda()

        targets = targets.view(-1, 1)

        optimizer.zero_grad()

        # forward + backward + optimize
        outputs = net(inputs)
        a = outputs
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

        if (batch_idx + 1) % 10 == 0:
            print(
                f'Epoch [{epoch + 1}/{epochs}], Batch [{batch_idx + 1}/{len(trainloader)}], Loss: {loss.item()}')

net.eval()

df = pd.read_csv("./Data/transformed_test.csv")

data = []

for row in range(0, df.shape[0]):
    input = torch.tensor(df.iloc[row, :].values.astype(np.float32)).cuda()

    output = net(input).item()
    min = mins[trainset.length-1]
    max = maxs[trainset.length-1]
    output = output * (max - min) + min
    data.append([row, output])


new_df = pd.DataFrame(data, columns=["Id", "SalePrice"])

new_df.to_csv("./Data/end_results.csv")