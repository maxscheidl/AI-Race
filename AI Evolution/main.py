import pygame
from car import Car
from road import Road
from evolution import Evolution


pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1400, 700
canvas = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Race")

canvas.fill("lightgreen")


def main():

    run = True
    clock = pygame.time.Clock()

    road = Road()

    cars = []

    ###################################################################################################################

    #cars.append(Car(road.segments[0].spawn[0], road.segments[0].spawn[1], "Manual"))

    for i in range(50):
        cars.append(Car(road.segments[0].spawn[0], road.segments[0].spawn[1], "AI"))

    ###################################################################################################################

    evolution = Evolution(canvas, cars)

    while run:

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.KEYUP):
                cars[0].controls.update(event)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_PLUS:
                    evolution.mutationRate += 0.01
                if event.key == pygame.K_MINUS:
                    evolution.mutationRate -= 0.01

                if event.key == pygame.K_1:
                    evolution.safe_network(1)
                if event.key == pygame.K_2:
                    evolution.safe_network(2)
                if event.key == pygame.K_3:
                    evolution.safe_network(3)

        pygame.draw.rect(canvas, "lightgreen", pygame.Rect(0, 0, 700, 700))

        road.draw(canvas)

        for car in cars:
            car.move(road.segments)

        for car in cars:
            if car.score < (evolution.currentBest.score - 100):
                car.crashed = True

            car.draw(canvas, True if car == evolution.currentBest else False)

        evolution.update()

        pygame.display.update()

        if all_cars_crashed(cars):
            evolution.evolve(road)

    pygame.quit()


def all_cars_crashed(cars):

    all_crashed = True
    for car in cars:
        if not car.crashed:
            all_crashed = False

    return all_crashed


if __name__ == "__main__":
    main()


