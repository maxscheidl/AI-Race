import pygame
import pickle
from car import Car
from road import Road
from network import Network
from visualizer import Visualizer
import time


pygame.init()

WIDTH, HEIGHT = 1400, 700
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Race")

canvas.fill("lightgreen")

road = Road()

cars = []

for i in range(30):
    cars.append(Car(65, 200, "AI"))

#cars.append(Car(65, 200, "Manual"))

best = cars[0]

visualizer = Visualizer(canvas)

def main():

    global best
    run = True
    clock = pygame.time.Clock()

    load_best_network()

    while run:

        #start = time.perf_counter()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
                cars[1].controls.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset()
                if event.key == pygame.K_s:
                    safe_brain()
                if event.key == pygame.K_p:
                    print(best.score)

        canvas.fill("lightgreen")

        road.draw(canvas)

        for car in cars:
            car.move(road.left_boarder, road.right_boarder, road.checkpoints)

        for car in cars:
            car.draw(canvas, True if car == best else False)

        best = find_best_car()
        best.highlight(canvas, "white")
        cars[0].highlight(canvas, "lightblue")
        visualizer.draw(best.network)

        pygame.display.update()

        #end = time.perf_counter()
        #print((end-start)*1000)

    pygame.quit()


def find_best_car():

    global best
    #best = cars[0]

    for car in cars:
        if car.score > best.score:
            best = car
        elif car.score == best.score and best.crashed:
            best = car

    return best


def reset():

    for i, car in enumerate(cars):
        if i == 0:
            car.reset(65, 200, best.network.clone())
        elif i < 20:
            car.reset(65, 200, best.network.clone().mutate(0.1))
        elif i < 25:
            car.reset(65, 200, best.network.clone().mutate(0.2))
        else:
            car.reset(65, 200, best.network.clone().mutate(0.5))


def safe_brain():

    with open('bestBrain.p', 'wb') as outp:
        pickle.dump(best.network, outp, pickle.HIGHEST_PROTOCOL)


def load_best_network():

    with open('bestBrain.p', 'rb') as inp:
        bestNetwork = pickle.load(inp)

    for i, car in enumerate(cars):
        if i == 0:
            car.network = bestNetwork
        else:
            car.network = bestNetwork.clone().mutate(0.1)


main()


