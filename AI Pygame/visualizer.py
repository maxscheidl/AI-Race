import pygame
from network import *


def get_arrows():

    arrowImg = pygame.image.load("arrow_small.png")
    arrowImg = pygame.transform.scale(arrowImg, (20, 20))

    rotations = [90, 180, -90, 180]
    arrows = []

    for rotation in rotations:
        arrowImg = pygame.transform.rotate(arrowImg, rotation)
        arrows.append(arrowImg)

    return arrows


class Visualizer:

    def __init__(self, canvas):

        self.canvas = canvas

        self.x = 800
        self.y = 100
        self.width = 500
        self.height = 500

    def draw(self, network):

        arrows = get_arrows()

        #pygame.draw.rect(self.canvas, "white", pygame.Rect(725, 25, 650, 650))

        levels = len(network.levels)
        section = self.height / levels

        for i, level in enumerate(network.levels):

            neurons = level.inputCount
            gap = self.width / neurons

            for j in range(level.inputCount):

                position = (self.x + (gap / 2) + (j * gap), self.y + self.height - (i * section))

                neuronsOut = level.outputCount
                gapNext = self.width / neuronsOut

                for k in range(level.outputCount):
                    position2 = (self.x + (gapNext / 2) + (k * gapNext), self.y + self.height - ((i + 1) * section))
                    pygame.draw.line(self.canvas,
                                     "white" if level.weights[j][k] >= 0 else (89, 156, 129),
                                     position, position2)

                if i == 0:
                    pygame.draw.circle(self.canvas,
                                       "orange" if level.inputs[j] > 0 else "darkgray",
                                       position, 15)
                else:
                    pygame.draw.circle(self.canvas,
                                       (245, 66, 111) if level.inputs[j] > 0 else "darkgray",
                                    position, 15)

            if i == (len(network.levels) - 1):

                neurons = level.outputCount
                gap = self.width / neurons

                for j in range(level.outputCount):
                    position = (self.x + (gap / 2) + (j * gap), self.y + self.height - ((i + 1) * section))
                    pygame.draw.circle(self.canvas,
                                       (66, 155, 245) if level.outputs[j] > 0 else "darkgray",
                                       position, 15)

                    self.canvas.blit(arrows[j], (
                    position[0] - arrows[j].get_width() / 2, position[1] - arrows[j].get_height() / 2))
