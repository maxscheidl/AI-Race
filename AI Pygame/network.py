from random import random
from utils import lerp
import copy


class Network:

    def __init__(self, neuronCounts):

        self.levels = []

        for i in range(len(neuronCounts) - 1):
            self.levels.append(Level(neuronCounts[i], neuronCounts[i+1]))

    def feed_forward(self, inputs):
        outputs = inputs

        for level in self.levels:
            outputs = level.feed_forward(outputs)

        return outputs

    def mutate(self, intensity):
        for level in self.levels:
            level.mutate(intensity)

        return self

    def clone(self):
        return copy.deepcopy(self)


class Level:

    def __init__(self, inputCount, outputCount):

        self.inputs = []
        self.outputs = []
        self.biases = []
        self.weights = []

        self.inputCount = inputCount
        self.outputCount = outputCount

        self.init_random()

    def init_random(self):

        for i in range(self.inputCount):
            weights = []
            for j in range(self.outputCount):
                weights.append(random() * 2 - 1)

            self.weights.append(weights)

        for i in range(self.outputCount):
            self.biases.append(random() * 2 - 1)

    def feed_forward(self, inputs):

        self.inputs = inputs
        self.outputs = []

        for i in range(self.outputCount):
            sum = 0

            for j in range(self.inputCount):
                sum += inputs[j] * self.weights[j][i]

            if sum > self.biases[i]:
                self.outputs.append(1)
            else:
                self.outputs.append(0)

        return self.outputs

    def mutate(self, intensity):

        for i, weights in enumerate(self.weights):
            for j, weight in enumerate(weights):
                weights[j] = lerp(weight, random() * 2 - 1, intensity)

        for i, bias in enumerate(self.biases):
            self.biases[i] = lerp(bias, random() * 2 - 1, intensity)



