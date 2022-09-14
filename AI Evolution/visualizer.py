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

        self.x = 1040
        self.y = 340
        self.width = 300
        self.height = 300

        self.display_static_info()

    def draw(self, network, evolution):

        self.display_infos(evolution)

        arrows = get_arrows()

        pygame.draw.rect(self.canvas, "lightgreen", pygame.Rect(self.x - 20, self.y - 20, self.width + 40, self.height + 40))

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

    def display_infos(self, evolution):

        color = (109, 132, 140)
        text = pygame.font.SysFont('Helvetica', 20)

        pygame.draw.rect(self.canvas, color, pygame.Rect(750, 100, 600, 180), border_radius=10)

        text_surface = text.render('Generation: ' + str(evolution.generation), False, "white")
        self.canvas.blit(text_surface, (780, 120))
        text_surface = text.render('Population: ' + str(len(evolution.cars)), False, "white")
        self.canvas.blit(text_surface, (780, 150))
        text_surface = text.render('Cars alive: ' + str(evolution.cars_alive), False, "white")
        self.canvas.blit(text_surface, (780, 180))
        text_surface = text.render('Best score: ' + str(int(evolution.bestScore)), False, "white")
        self.canvas.blit(text_surface, (780, 210))
        text_surface = text.render('Current best score: ' + str(int(evolution.currentBest.score)), False, "white")
        self.canvas.blit(text_surface, (780, 240))

        text_surface = text.render('Mutation rate: ' + str(round(evolution.mutationRate, 2)), False, "white")
        self.canvas.blit(text_surface, (980, 120))

    def display_static_info(self):
        color = (109, 132, 140)
        heading = pygame.font.SysFont('Helvetica', 40)
        text = pygame.font.SysFont('Helvetica', 20)

        heading_surface = heading.render('Evolution of AI', False, "white")

        pygame.draw.rect(self.canvas, color, pygame.Rect(850, 30, 400, 50), border_radius=10)
        self.canvas.blit(heading_surface, (950, 30))

        pygame.draw.rect(self.canvas, color, pygame.Rect(750, 300, 250, 370), border_radius=10)
        pygame.draw.rect(self.canvas, "red", pygame.Rect(770, 320, 50, 100))
        pygame.draw.line(self.canvas, "black", (770, 320), (820, 320), width=6)
        pygame.draw.circle(self.canvas, "white", (795, 370), 15)
        pygame.draw.rect(self.canvas, "red", pygame.Rect(770, 450, 50, 100))
        pygame.draw.line(self.canvas, "black", (770, 450), (820, 450), width=6)
        pygame.draw.circle(self.canvas, "lightblue", (795, 500), 15)

        text_surface = text.render('Current best car', False, "white")
        self.canvas.blit(text_surface, (850, 360))
        text_surface = text.render('Previous best car', False, "white")
        self.canvas.blit(text_surface, (850, 490))

        text_surface = text.render('Best Network ===>', False, "white")
        self.canvas.blit(text_surface, (800, 600))


