import pygame
from point import Point


class Checkpoint:

    def __init__(self, point1, point2):

        self.start = point1
        self.end = point2

    def get_middle(self):

        return Point((self.start.x + self.end.x) / 2, (self.start.y + self.end.y) / 2)

    def draw(self, canvas):

        pygame.draw.line(canvas, "white", (self.start.x, self.start.y), (self.end.x, self.end.y), width=1)
        #middle = self.get_middle()
        #pygame.draw.circle(canvas, "white", (middle.x, middle.y), 2)

    def as_list(self):

        return [self.start, self.end]
