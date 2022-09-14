import pygame
from visualizer import Visualizer
import pickle


class Evolution:

    def __init__(self, canvas, cars):

        self.generation = 1
        self.cars_alive = len(cars)
        self.currentBest = cars[0]

        self.bestNetwork = cars[0].network
        self.bestScore = 0

        self.mutationRate = 0.1

        self.canvas = canvas
        self.visualizer = Visualizer(canvas)
        self.cars = cars

        self.load_best_network()

    def evolve(self, road):

        self.generation += 1

        for i, car in enumerate(self.cars):
            if i == 0:
                car.reset(road.segments[0].spawn[0], road.segments[0].spawn[1], self.currentBest.network)
            elif i < len(self.cars)*0.2:
                car.reset(road.segments[0].spawn[0], road.segments[0].spawn[1], self.currentBest.network.clone().mutate(self.mutationRate/2))
            elif i < len(self.cars)*0.8:
                car.reset(road.segments[0].spawn[0], road.segments[0].spawn[1], self.currentBest.network.clone().mutate(self.mutationRate))
            else:
                car.reset(road.segments[0].spawn[0], road.segments[0].spawn[1], self.currentBest.network.clone().mutate(self.mutationRate*2))

        self.currentBest = self.cars[0]

    def update(self):

        self.cars_alive = 0

        for car in self.cars:
            if not car.crashed:
                self.cars_alive += 1
            if car.score > self.currentBest.score:
                self.currentBest = car

        if self.currentBest.score > self.bestScore:
            self.bestScore = self.currentBest.score
            self.bestNetwork = self.currentBest.network

        self.cars[0].highlight(self.canvas, "lightblue")
        self.currentBest.highlight(self.canvas, "white")

        self.visualizer.draw(self.currentBest.network, self)

    def safe_network(self, number):

        with open('bestBrain' + str(number) + '.p', 'wb') as outp:
            pickle.dump(self.bestNetwork, outp, pickle.HIGHEST_PROTOCOL)

    def load_best_network(self):

        with open('bestBrain1.p', 'rb') as inp:
            self.bestNetwork = pickle.load(inp)

        for i, car in enumerate(self.cars):
            if i == 0:
                car.network = self.bestNetwork
            else:
                car.network = self.bestNetwork.clone().mutate(0.1)





