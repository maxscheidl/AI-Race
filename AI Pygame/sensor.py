import pygame
import math
import utils
from point import Point
from utils import get_intersection, find_min_offset


class Sensor:

    def __init__(self, car):
        self.car = car
        self.rayCount = 5
        self.rayLegth = 100
        self.raySpread = math.pi

        self.rays = []
        self.intersections = []


    # O(boarder * ray)
    def update_intersections(self, left_boarder, right_boarder):

        self.intersections = []

        for ray in self.rays:
            self.intersections.append(
                self.calc_intersections(ray, left_boarder, right_boarder)
            )

    # O(boarder)
    def calc_intersections(self, ray, left_boarder, right_boarder):

        intersections = []

        for i in range(len(left_boarder) - 1):

            intersection = get_intersection(
                ray[0], ray[1],
                left_boarder[i], left_boarder[i+1]
            )

            if len(intersection) != 0:
                intersections.append(intersection)

        for i in range(len(right_boarder) - 1):

            intersection = get_intersection(
                ray[0], ray[1],
                right_boarder[i], right_boarder[i+1]
            )

            if len(intersection) != 0:
                intersections.append(intersection)

        if len(intersections) != 0:
            return find_min_offset(intersections)
        else:
            return []

    # O(n)
    def update_rays(self, left_boarder, right_boarder):
        self.rays = []

        for i in range(self.rayCount):
            rayAngle = utils.lerp(self.raySpread / 2, -self.raySpread / 2,
                                  0.5 if self.rayCount == 1 else i / (self.rayCount - 1)) + self.car.angle

            rayLength = self.rayLegth * utils.ray_length_scale(self.rayCount, i)

            self.rays.append([
                Point(self.car.x,
                      self.car.y),
                Point(self.car.x - math.sin(rayAngle) * rayLength,
                      self.car.y - math.cos(rayAngle) * rayLength),
                rayLength
            ])

        self.update_intersections(left_boarder, right_boarder)

    # O(n)
    def draw(self, canvas):
        #for ray in self.rays:
        #    pygame.draw.line(canvas, "black", (ray[0].x, ray[0].y), (ray[1].x, ray[1].y))

        for intersection in self.intersections:

            if len(intersection) != 0:

                pygame.draw.line(canvas, utils.get_ray_color(intersection[1]),
                                 (self.car.x, self.car.y), (intersection[0].x, intersection[0].y), 1)

    def get_readings(self):

        readings = []

        for intersection in self.intersections:
            if len(intersection) != 0:
                readings.append(1 - intersection[1])
            else:
                readings.append(0)

        return readings

