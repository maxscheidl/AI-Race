import pygame
from controls import Controls
from sensor import Sensor
from point import Point
from utils import polynom_intersection
from network import Network
import math


class Car:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 30

        self.speed = 0
        self.acceleration = 0.2
        self.maxSpeed = 2
        self.friction = 0.05
        self.angle = 0
        self.rotation = 0.05
        self.crashed = False
        self.positions = []

        self.nextCheckpoint = 0
        self.score = 0

        self.controls = Controls()
        self.sensor = Sensor(self)

        self.manual = False if type == "AI" else True
        self.network = Network([self.sensor.rayCount, 6, 4])

    def draw(self, canvas, sensors):

        if sensors:
            self.sensor.draw(canvas)

        pygame.draw.polygon(canvas, "lightgray" if self.crashed else "red",
                            [(self.positions[0].x, self.positions[0].y),(self.positions[1].x, self.positions[1].y),
                             (self.positions[2].x, self.positions[2].y),(self.positions[3].x, self.positions[3].y)])

        pygame.draw.line(canvas, "black", (self.positions[0].x, self.positions[0].y), (self.positions[1].x, self.positions[1].y), 3)

    def asses_damage(self, left_boarder, right_boarder):

        if polynom_intersection(self.positions, left_boarder) or polynom_intersection(self.positions, right_boarder):
            self.crashed = True

    # O(1)
    def calculate_positions(self):
        points = []
        rad = math.hypot(self.width, self.height)/2
        alpha = math.atan2(self.width, self.height)

        points.append(
            Point(self.x - math.sin(self.angle - alpha) * rad,
                  self.y - math.cos(self.angle - alpha) * rad)
        )
        points.append(
            Point(self.x - math.sin(self.angle + alpha) * rad,
                  self.y - math.cos(self.angle + alpha) * rad)
        )
        points.append(
            Point(self.x - math.sin(math.pi + self.angle - alpha) * rad,
                  self.y - math.cos(math.pi + self.angle - alpha) * rad)
        )
        points.append(
            Point(self.x - math.sin(math.pi + self.angle + alpha) * rad,
                  self.y - math.cos(math.pi + self.angle + alpha) * rad)
        )
        return points

    def move(self, left_boarder, right_boarder, checkpoints):

        if not self.crashed:

            if self.controls.forward:
                self.speed += self.acceleration

            if self.controls.reverse:
                self.speed -= self.acceleration

            if self.speed > self.maxSpeed:
                self.speed = self.maxSpeed

            if self.speed < -self.maxSpeed/2:
                self.speed = -self.maxSpeed/2

            if self.speed > 0:
                self.speed -= self.friction

            if self.speed < 0:
                self.speed += self.friction

            if math.fabs(self.speed) < self.friction:
                self.speed = 0

            if self.speed != 0:
                flip = 1 if self.speed > 0 else -1

                if self.controls.left:
                    self.angle += flip * self.rotation  #* (self.rotation - 0.03 * (self.speed / self.maxSpeed))

                if self.controls.right:
                    self.angle -= flip * self.rotation  #* (self.rotation - 0.03 * (self.speed / self.maxSpeed))

            self.x -= math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed

            self.positions = self.calculate_positions()  # O(1)
            self.asses_damage(left_boarder, right_boarder)  # Problem
            self.update_score(checkpoints)
            self.sensor.update_rays(left_boarder, right_boarder)  # Problem

            if not self.manual:
                outputs = self.network.feed_forward(self.sensor.get_readings())
                self.controls.set(outputs)

    def update_score(self, checkpoints):

        intersection = polynom_intersection(self.positions, checkpoints[self.nextCheckpoint].as_list())

        if intersection:
            self.score += 5
            self.nextCheckpoint = (self.nextCheckpoint + 1) % len(checkpoints)

    def reset(self, x, y, network):
        self.x = x
        self.y = y

        self.speed = 0
        self.angle = 0
        self.crashed = False
        self.positions = []

        self.nextCheckpoint = 0
        self.score = 0

        self.network = network

    def highlight(self, canvas, color):
        pygame.draw.circle(canvas, color, (self.x, self.y), 5)

