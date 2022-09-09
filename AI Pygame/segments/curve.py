import pygame
import math


def rotate(vector, angle):

    return (vector[0] * math.cos(angle) - vector[1] * math.sin(angle),
            vector[0] * math.sin(angle) + vector[1] * math.cos(angle))


class BlockCurve:

    def __init__(self, type, start, direction, width):

        directionLength = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
        self.direction = (direction[0] / directionLength, direction[1] / directionLength)

        self.start = start
        self.end = ()
        self.next_direction = ()

        self.left_boarder = []
        self.right_boarder = []
        self.boarder = []

        self.width = width
        self.offset = width/7

        self.calculate_boarders(type)

    def calculate_boarders(self, type):

        start = self.start
        direction = self.direction
        left = self.left_boarder
        right = self.right_boarder
        offset = self.offset

        left.append((start[0] + direction[1] * self.width / 2, start[1] + -direction[0] * self.width / 2))
        right.append((start[0] + -direction[1] * self.width / 2, start[1] + direction[0] * self.width / 2))

        if type == "right":
            left.append((left[0][0] + direction[0] * (self.width + offset), left[0][1] + direction[1] * (self.width + offset)))
            left.append((left[1][0] + -direction[1] * (self.width + offset), left[1][1] + direction[0] * (self.width + offset)))
            right.append((right[0][0] + direction[0] * offset, right[0][1] + direction[1] * offset))
            right.append((right[1][0] + -direction[1] * offset, right[1][1] + direction[0] * offset))
            self.end = (right[2][0] + direction[0] * self.width / 2, right[2][1] + direction[1] * self.width / 2)
            self.next_direction = (-direction[1], direction[0])

        elif type == "left":
            right.append((right[0][0] + direction[0] * (self.width + offset), right[0][1] + direction[1] * (self.width + offset)))
            right.append((right[1][0] + direction[1] * (self.width + offset), right[1][1] + -direction[0] * (self.width + offset)))
            left.append((left[0][0] + direction[0] * offset, left[0][1] + direction[1] * offset))
            left.append((left[1][0] + direction[1] * offset, left[1][1] + -direction[0] * offset))
            self.end = (left[2][0] + direction[0] * self.width / 2, left[2][1] + direction[1] * self.width / 2)
            self.next_direction = (direction[1], -direction[0])

        self.boarder = self.left_boarder.copy()
        self.boarder.extend(reversed(self.right_boarder))

    def draw(self, canvas):

        pygame.draw.polygon(canvas, "gray", self.boarder)
        pygame.draw.circle(canvas, "blue", self.start, 2)
        pygame.draw.circle(canvas, "red", self.end, 3)

class SmoothCurve(BlockCurve):

    def __init__(self, type, start, direction, width):

        super().__init__(type, start, direction, width)

    def calculate_boarders(self, type):

        start = self.start
        direction = self.direction
        left = self.left_boarder
        right = self.right_boarder
        offset = self.offset

        left.append((start[0] + direction[1] * self.width / 2, start[1] + -direction[0] * self.width / 2))
        right.append((start[0] + -direction[1] * self.width / 2, start[1] + direction[0] * self.width / 2))

        if type == "right":
            temp = rotate(direction, 0.125*math.pi)
            left.append((left[0][0] + direction[0] * (self.width - 2*offset), left[0][1] + direction[1] * (self.width - 2*offset)))
            left.append((left[1][0] + temp[0] * 2*offset, left[1][1] + temp[1] * 2*offset))
            left.append((left[1][0] + (-direction[1] + direction[0]) * (3*offset), left[1][1] + (direction[1] + direction[0]) * (3*offset)))
            left.append((left[0][0] + (-direction[1] + direction[0]) * (self.width + offset), left[0][1] + (direction[1] + direction[0]) * (self.width + offset)))

            right.append((right[0][0] + temp[0] * 2*offset/3, right[0][1] + temp[1] * 2*offset/3))
            right.append((right[0][0] + (direction[0] - direction[1]) * offset, right[0][1] + (direction[1] + direction[0]) * offset))
            self.end = (right[2][0] + direction[0] * self.width / 2, right[2][1] + direction[1] * self.width / 2)
            self.next_direction = (-direction[1], direction[0])

        elif type == "left":
            temp = rotate(direction, 1.875*math.pi)
            right.append((right[0][0] + direction[0] * (self.width - 2*offset), right[0][1] + direction[1] * (self.width - 2*offset)))
            right.append((right[1][0] + temp[0] * 2*offset, right[1][1] + temp[1] * 2*offset))
            right.append((right[1][0] + (direction[1] + direction[0]) * (3*offset), right[1][1] + (direction[1] - direction[0]) * (3*offset)))
            right.append((right[0][0] + (direction[1] + direction[0]) * (self.width + offset), right[0][1] + (direction[1] - direction[0]) * (self.width + offset)))

            left.append((left[0][0] + temp[0] * 2*offset/3, left[0][1] + temp[1] * 2*offset/3))
            left.append((left[0][0] + (direction[0] + direction[1]) * offset, left[0][1] + (direction[1] + -direction[0]) * offset))
            self.end = (left[2][0] + direction[0] * self.width / 2, left[2][1] + direction[1] * self.width / 2)
            self.next_direction = (direction[1], -direction[0])

        self.boarder = self.left_boarder.copy()
        self.boarder.extend(reversed(self.right_boarder))