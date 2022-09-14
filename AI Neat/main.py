import pygame
import pickle
import neat
import os
from car import Car
from road import Road


pygame.init()

WIDTH, HEIGHT = 1400, 700
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Race")

canvas.fill("lightgreen")

road = Road()


def main(genomes, config):

    nets = []
    cars = []
    ge = []

    for genome_id, genome in genomes:
        genome.fitness = 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        cars.append(Car(road.segments[0].spawn[0], road.segments[0].spawn[1], "AI"))
        ge.append(genome)

    global best
    best = cars[0]

    run = True
    clock = pygame.time.Clock()

    while run:

        #start = time.perf_counter()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                break
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
                cars[0].controls.update(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    print(best.score)

        canvas.fill("lightgreen")

        road.draw(canvas)

        for i, car in enumerate(cars):
            ge[i].fitness = car.score
            car.move(road.segments, nets[i])

        best = find_best_car(cars)

        for car in cars:
            if car.score < (best.score - 50):
                car.crashed = True
            car.draw(canvas, True if car == best else False)

        best.highlight(canvas, "white")
        cars[0].highlight(canvas, "lightblue")

        if all_cars_crashed(cars):
            run = False

        pygame.display.update()

        #end = time.perf_counter()
        #print((end-start)*1000)


def find_best_car(cars):

    global best

    for car in cars:
        if car.score > best.score:
            best = car
        elif car.score == best.score and best.crashed:
            best = car

    return best


def safe(network):

    with open('bestBrain.p', 'wb') as outp:
        pickle.dump(network, outp, pickle.HIGHEST_PROTOCOL)


def all_cars_crashed(cars):

    all_crashed = True
    for car in cars:
        if not car.crashed:
            all_crashed = False

    return all_crashed


#NEAT function
def run(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats =neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(main, 1000)

    safe(winner)


if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config_file.txt")
    run(config_path)

