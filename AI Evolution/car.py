import pygame
from controls import Controls
from sensor import Sensor
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

        self.currentSector = []
        self.nextSegment = 1
        self.relDistanceToNext = 0

        self.controlLine = []
        self.tempScore = 0
        self.score = 0
        self.time = 0
        self.lastScored = 0

        self.controls = Controls()
        self.sensor = Sensor(self)

        self.manual = False if type == "AI" else True
        self.network = Network([self.sensor.rayCount, 6, 4])

    def draw(self, canvas, best):

        if best:
            self.sensor.draw(canvas)
            #pygame.draw.polygon(canvas, "red", self.currentSector, 1)

        pygame.draw.polygon(canvas, "lightgray" if self.crashed else "red", self.positions)
        pygame.draw.line(canvas, "black", self.positions[0], self.positions[1])
        #pygame.draw.line(canvas, "black", self.controlLine[0], self.controlLine[1])

    def asses_damage(self, segments):
        if len(self.currentSector) == 0:
            self.update_sector(segments)

        if polynom_intersection(self.positions, self.currentSector):
            self.crashed = True

    def calculate_positions(self):
        points = []
        rad = math.hypot(self.width, self.height)/2
        alpha = math.atan2(self.width, self.height)

        points.append(
            (self.x - math.sin(self.angle - alpha) * rad, self.y - math.cos(self.angle - alpha) * rad)
        )
        points.append(
            (self.x - math.sin(self.angle + alpha) * rad, self.y - math.cos(self.angle + alpha) * rad)
        )
        points.append(
            (self.x - math.sin(math.pi + self.angle - alpha) * rad, self.y - math.cos(math.pi + self.angle - alpha) * rad)
        )
        points.append(
            (self.x - math.sin(math.pi + self.angle + alpha) * rad, self.y - math.cos(math.pi + self.angle + alpha) * rad)
        )
        return points

    def move(self, segments):

        if not self.crashed:

            self.time += 0.1

            if ((self.time - self.lastScored) > 10):
                self.crashed = True

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

            self.positions = self.calculate_positions()
            self.asses_damage(segments)
            self.update_score(segments)
            self.sensor.update_rays(self.currentSector)

            if not self.manual:
                readings = self.sensor.get_readings()
                #readings.append(self.speed/self.maxSpeed)
                outputs = self.network.feed_forward(readings)
                self.controls.set(outputs)

    def update_score(self, segments):

        segment = segments[self.nextSegment]

        vector = (-(self.positions[3][1] - self.positions[2][1]), self.positions[3][0] - self.positions[2][0])

        self.controlLine = [(self.x, self.y), (self.x + vector[0], self.y + vector[1])]

        intersection = polynom_intersection(self.controlLine, [segment.left_boarder[0], segment.right_boarder[0]])

        distance_vector = (segment.start[0] - self.x, segment.start[1] - self.y)
        self.relDistanceToNext = math.sqrt(math.pow(distance_vector[0], 2) + math.pow(distance_vector[1], 2)) / segment.length
        self.score = self.tempScore + (1-self.relDistanceToNext) * 10

        if intersection:
            self.tempScore += 10
            self.nextSegment = (self.nextSegment + 1) % len(segments)
            self.lastScored = self.time
            self.update_sector(segments)

    def reset(self, x, y, network):
        self.x = x
        self.y = y

        self.speed = 0
        self.angle = 0
        self.crashed = False
        self.positions = []

        self.currentSector = []
        self.nextSegment = 1
        self.relDistanceToNext = 0

        self.controlLine = []
        self.tempScore = 0
        self.score = 0
        self.time = 0
        self.lastScored = 0

        self.network = network

        self.controls.reset()

    def highlight(self, canvas, color):
        pygame.draw.circle(canvas, color, (self.x, self.y), 5)

    def update_sector(self, segments):
        sub_sectors = [(self.nextSegment - 2) % len(segments), (self.nextSegment - 1) % len(segments),
                       self.nextSegment, (self.nextSegment + 1) % len(segments)]

        sector = []
        sector.extend(segments[sub_sectors[0]].left_boarder)
        sector.extend(segments[sub_sectors[1]].left_boarder[1:-1])
        sector.extend(segments[sub_sectors[2]].left_boarder[0:-1])
        sector.extend(segments[sub_sectors[3]].left_boarder)
        sector.extend(reversed(segments[sub_sectors[3]].right_boarder))
        sector.extend(reversed(segments[sub_sectors[2]].right_boarder[0:-1]))
        sector.extend(reversed(segments[sub_sectors[1]].right_boarder[1:-1]))
        sector.extend(reversed(segments[sub_sectors[0]].right_boarder))

        self.currentSector = sector


