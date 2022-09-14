import pygame
import math


def rotate(vector, angle):

    return (vector[0] * math.cos(angle) - vector[1] * math.sin(angle),
            vector[0] * math.sin(angle) + vector[1] * math.cos(angle))


class Block:

    def __init__(self, start, direction, width, length):

        directionLength = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
        self.direction = (direction[0] / directionLength, direction[1] / directionLength)

        self.start = start
        self.end = (start[0] + self.direction[0] * length, start[1] + self.direction[1] * length)
        self.next_direction = self.direction

        self.left_boarder = []
        self.right_boarder = []
        self.boarder = []

        self.width = width
        self.length = length

        self.calculate_boarders()

    def calculate_boarders(self):

        start = self.start
        direction = self.direction
        left = self.left_boarder
        right = self.right_boarder

        left.append((start[0] + direction[1] * self.width / 2, start[1] + (-direction[0]) * self.width / 2))
        left.append((left[0][0] + direction[0] * self.length, left[0][1] + direction[1] * self.length))

        right.append((start[0] + (-direction[1]) * self.width / 2, start[1] + direction[0] * self.width / 2))
        right.append((right[0][0] + direction[0] * self.length, right[0][1] + direction[1] * self.length))

        self.boarder = self.left_boarder.copy()
        self.boarder.extend(reversed(self.right_boarder))

    def draw(self, canvas):

        pygame.draw.polygon(canvas, "gray", self.boarder)
        pygame.draw.circle(canvas, "blue", self.start, 2)
        pygame.draw.circle(canvas, "red", self.end, 3)


class Start(Block):

    def __init__(self, start, direction, width):

        super().__init__(start, direction, width, width)

        self.spawn = (start[0] + self.direction[0] * width / 2, start[1] + self.direction[1] * width / 2)

    def draw(self, canvas):

        super().draw(canvas)
        pygame.draw.circle(canvas, "white", self.spawn, 6)


class NarrowBlock(Block):

    def __init__(self, start, direction, width, length, type="center", tightness=0.5):

        self.tightness = tightness
        self.type = type

        super().__init__(start, direction, width, length)

    def calculate_boarders(self):

        start = self.start
        direction = self.direction
        left = self.left_boarder
        right = self.right_boarder

        left.append((start[0] + direction[1] * self.width / 2, start[1] + (-direction[0]) * self.width / 2))
        right.append((start[0] + (-direction[1]) * self.width / 2, start[1] + direction[0] * self.width / 2))

        if self.type == "center":
            left.append((left[0][0] + direction[0] * self.length / 10 + -direction[1] * self.width / 3 * self.tightness,
                         left[0][1] + direction[1] * self.length / 10 + direction[0] * self.width / 3 * self.tightness))
            left.append((left[1][0] + direction[0] * 8 * self.length / 10, left[1][1] + direction[1] * 8 * self.length / 10))

            right.append((right[0][0] + direction[0] * self.length / 10 + direction[1] * self.width / 3 * self.tightness,
                          right[0][1] + direction[1] * self.length / 10 - direction[0] * self.width / 3 * self.tightness))
            right.append((right[1][0] + direction[0] * 8 * self.length / 10, right[1][1] + direction[1] * 8 * self.length / 10))

        elif self.type == "right":
            right.append((right[0][0] + direction[0] * self.length / 10 + direction[1] * 2 * self.width / 3 * self.tightness,
                          right[0][1] + direction[1] * self.length / 10 - direction[0] * 2 * self.width / 3 * self.tightness))
            right.append((right[1][0] + direction[0] * 8 * self.length / 10, right[1][1] + direction[1] * 8 * self.length / 10))

        elif self.type == "left":
            left.append((left[0][0] + direction[0] * self.length / 10 + -direction[1] * 2 * self.width / 3 * self.tightness,
                         left[0][1] + direction[1] * self.length / 10 + direction[0] * 2 * self.width / 3 * self.tightness))
            left.append((left[1][0] + direction[0] * 8 * self.length / 10, left[1][1] + direction[1] * 8 * self.length / 10))

        else:
            raise "wrong type"

        left.append((left[0][0] + direction[0] * self.length, left[0][1] + direction[1] * self.length))
        right.append((right[0][0] + direction[0] * self.length, right[0][1] + direction[1] * self.length))

        self.boarder = self.left_boarder.copy()
        self.boarder.extend(reversed(self.right_boarder))


class ZicZacBlock(Block):

    def __init__(self, start, direction, width, length, side, tightness=0.5):

        self.tightness = tightness
        self.side = side

        super().__init__(start, direction, width, length)

    def calculate_boarders(self):

        start = self.start
        direction = self.direction
        left = self.left_boarder
        right = self.right_boarder

        left.append((start[0] + direction[1] * self.width / 2, start[1] + (-direction[0]) * self.width / 2))
        right.append((start[0] + (-direction[1]) * self.width / 2, start[1] + direction[0] * self.width / 2))

        if self.side == "right":
            left.append((left[0][0] + direction[0] * 7 * self.length / 10, left[0][1] + direction[1] * 7 * self.length / 10))
            left.append((left[1][0] + -direction[1] * 2 * self.width / 3 * self.tightness, left[1][1] + direction[0] * 2 * self.width / 3 * self.tightness))
            left.append((left[2][0] + direction[0] * self.length / 10, left[2][1] + direction[1] * self.length / 10))
            left.append((left[1][0] + direction[0] * self.length / 10, left[1][1] + direction[1] * self.length / 10))

            right.append((right[0][0] + direction[0] * 2 * self.length / 10, right[0][1] + direction[1] * 2 * self.length / 10))
            right.append((right[1][0] + direction[1] * 2 * self.width / 3 * self.tightness, right[1][1] + -direction[0] * 2 * self.width / 3 * self.tightness))
            right.append((right[2][0] + direction[0] * self.length / 10, right[2][1] + direction[1] * self.length / 10))
            right.append((right[1][0] + direction[0] * self.length / 10, right[1][1] + direction[1] * self.length / 10))
        elif self.side == "left":
            left.append((left[0][0] + direction[0] * 2 * self.length / 10, left[0][1] + direction[1] * 2 * self.length / 10))
            left.append((left[1][0] + -direction[1] * 2 * self.width / 3 * self.tightness, left[1][1] + direction[0] * 2 * self.width / 3 * self.tightness))
            left.append((left[2][0] + direction[0] * self.length / 10, left[2][1] + direction[1] * self.length / 10))
            left.append((left[1][0] + direction[0] * self.length / 10, left[1][1] + direction[1] * self.length / 10))

            right.append((right[0][0] + direction[0] * 7 * self.length / 10, right[0][1] + direction[1] * 7 * self.length / 10))
            right.append((right[1][0] + direction[1] * 2 * self.width / 3 * self.tightness, right[1][1] + -direction[0] * 2 * self.width / 3 * self.tightness))
            right.append((right[2][0] + direction[0] * self.length / 10, right[2][1] + direction[1] * self.length / 10))
            right.append((right[1][0] + direction[0] * self.length / 10, right[1][1] + direction[1] * self.length / 10))

        else:
            raise "wrong type"

        left.append((left[0][0] + direction[0] * self.length, left[0][1] + direction[1] * self.length))
        right.append((right[0][0] + direction[0] * self.length, right[0][1] + direction[1] * self.length))

        self.boarder = self.left_boarder.copy()
        self.boarder.extend(reversed(self.right_boarder))





