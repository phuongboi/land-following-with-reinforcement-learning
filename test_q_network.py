import numpy as np
from collections import deque
import random
import torch
from torch import nn
import os
from env import VrepEnvironment
import params
from matplotlib import pyplot as plt
from IPython.display import clear_output

class Network(nn.Module):
    def __init__(self, input_shape, num_actions):
        super().__init__()

        self.linear_relu_stack = nn.Sequential(
            nn.Linear(input_shape, 256),
            nn.ReLU(),
            nn.Linear(256, num_actions)
        )

    def forward(self, x):
        x = self.linear_relu_stack(x)
        return x

def make_model():
    model = Network(512, 3)
    return model
