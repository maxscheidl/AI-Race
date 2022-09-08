import pygame
from point import Point
from checkpoint import Checkpoint

# O(n)
def coordinates_as_points(x_coords, y_coords):
    boarder = []

    for i in range(len(x_coords)):
        boarder.append(
            Point(x_coords[i], y_coords[i])
        )

    return boarder

# O(n)
def coordinates_as_tuples(x_coords, y_coords):
    boarder = []

    for i in range(len(x_coords)):
        boarder.append((x_coords[i], y_coords[i]))

    return boarder


class Road:

    def __init__(self):
        self.left_boarder_x = []
        self.left_boarder_y = []
        self.left_boarder = []

        self.right_boarder_x = []
        self.right_boarder_y = []
        self.right_boarder = []

        self.checkpoints = []

        self.init_road_five()

    # O(1)
    def draw(self, canvas):
        pygame.draw.polygon(canvas, "gray", coordinates_as_tuples(self.left_boarder_x, self.left_boarder_y))
        pygame.draw.polygon(canvas, "lightgreen", coordinates_as_tuples(self.right_boarder_x, self.right_boarder_y))

        for checkpoint in self.checkpoints:
            checkpoint.draw(canvas)

        pygame.draw.line(canvas, "white", (30, 165), (100, 165), 2)
        pygame.draw.line(canvas, "white", (30, 170), (100, 170), 2)
        pygame.draw.line(canvas, "white", (30, 160), (100, 160), 2)
        pygame.draw.line(canvas, "white", (30, 150), (100, 150), 2)
        pygame.draw.line(canvas, "white", (30, 155), (100, 155), 2)

    def init_road_zero(self):
        self.left_boarder_x = [30, 670, 670, 30]
        self.left_boarder_y = [30, 30,  670,  670]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [100, 600,  600,  100]
        self.right_boarder_y = [100, 100,  600,  600]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.checkpoints = [Checkpoint(Point(30, 120), Point(100, 120))]

    # O(1)
    def init_road_one(self):
        self.left_boarder_x = [60, 630, 650, 670, 670, 650, 630, 70,  40,  30, 30, 40, 60]
        self.left_boarder_y = [30, 30,  40,  70,  630, 660, 670, 670, 650, 630, 70, 40, 30]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [120, 580,  590,  600,  600, 595, 580, 120, 105, 100, 100, 105, 120]
        self.right_boarder_y = [100, 100,  105,  120,  580, 590, 600, 600, 595, 580, 120, 105, 100]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.checkpoints = [Checkpoint(Point(30, 120), Point(100, 120))]

    # O(1)
    def init_road_two(self):
        self.left_boarder_x = [30,40,70,   190,215,230,   230,240,250,   630,650,670,   670,655,630,    340,310,300,    300,290,280,    70,40,30,    30]
        self.left_boarder_y = [70,45,30,   30,40,70,      250,265,270,   270,280,310,   630,660,670,    670,655,630,    520,505,500,    500,485,460,   70]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [100,110,120,    140,150,160,     160,180,200,   350, 370, 470, 500,   580,590,600,  600, 605,   600,590,580,      390,380,370,    370,355,330,    120,110,100,    100]
        self.right_boarder_y = [120,105,100,    100,105,120,     300,330,340,   340, 330, 330, 340,   340,345,360,  450, 450,   580,595,600,      600,595,580,    470,440,430,    430,425,410,    120]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.checkpoints = [Checkpoint(Point(30, 120), Point(100, 120)), Checkpoint(Point(130, 30), Point(130, 100)),
                            Checkpoint(Point(160, 120), Point(230, 120)), Checkpoint(Point(230, 250), Point(160, 250)),
                            Checkpoint(Point(250, 270), Point(250, 340)), Checkpoint(Point(420, 340), Point(420, 270)),
                            Checkpoint(Point(580, 340), Point(580, 270)), Checkpoint(Point(600, 360), Point(670, 360)),
                            Checkpoint(Point(600, 580), Point(670, 580)), Checkpoint(Point(580, 600), Point(580, 670)),
                            Checkpoint(Point(390, 600), Point(390, 670)), Checkpoint(Point(370, 580), Point(300, 580)),
                            Checkpoint(Point(300, 520), Point(370, 520)), Checkpoint(Point(280, 500), Point(280, 430)),
                            Checkpoint(Point(120, 430), Point(120, 500)), Checkpoint(Point(100, 410), Point(30, 410)),
                            Checkpoint(Point(30, 270), Point(100, 270))]

    # O(n)
    def init_road_three(self):
        self.left_boarder_x = [30,   230,  230,   300,   300,   670,  670,  470,   470,    670,   670,  300, 300,  30,   30]
        self.left_boarder_y = [30,   30,   270,   270,   100,   100,  270,  270,   430,    430,   670,  670, 470,  470,  30]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [100,   160,   160,   370,   370,   600,   600,   400,   400,   600,   600, 370, 370,  100,   100]
        self.right_boarder_y = [100,   100,   340,   340,   170,   170,   200,   200,   500,   500,   600, 600, 400,  400,   100]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.create_checkpoints(Checkpoint(Point(30, 120), Point(100, 120)))

    # O(n)
    def init_road_four(self):
        self.left_boarder_x = [30,   230,  230,   300,   300,   670,  670,  470,   470, 540, 540,    670,   670,  30,  30,   300, 300, 30,  30]
        self.left_boarder_y = [30,   30,   270,   270,   100,   100,  270,  270,   360, 360, 430,  430,   670,  670, 500,  500, 470, 470, 30]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [100,   160,   160,   370,   370,   600,   600,   400,   400, 470, 470, 600,   600, 100, 100,  370, 370, 100, 100]
        self.right_boarder_y = [100,   100,   340,   340,   170,   170,   200,   200,   430, 430, 500, 500,   600, 600, 570,  570, 400, 400, 100]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.create_checkpoints(Checkpoint(Point(30, 150), Point(100, 150)))

    def init_road_five(self):
        self.left_boarder_x = [30,70,   190,230,  230,190,190,   230,250,  350,370,470,500,   630,670,    670, 635,     670,630,    450,450,430,430,  340,300,    300,280,  250,250,150,150,  70,30,    30]
        self.left_boarder_y = [70,30,   30,70,    200,220,250,    250,270,  270,280,280,270,   270,310,    450, 450,     630,670,   670,630,630,670,   670,630,    520,500, 500,460,460,500,   500,460,   70]

        self.left_boarder = coordinates_as_points(self.left_boarder_x, self.left_boarder_y)

        self.right_boarder_x = [100,120,    140,160,  160,200,200,160,   160,200,   350,370,470,500,   580,600,     600, 615,    600,580, 550,550,530,530,   390,370,    370,330,    120,100,    100]
        self.right_boarder_y = [120,100,    100,120,  150,150,170,170,   300,340,   340,330,330,340,   340,360,     500,550,    580,600,  600,645,645,600,  600,580,    470,430,    430,410,    120]

        self.right_boarder = coordinates_as_points(self.right_boarder_x, self.right_boarder_y)

        self.checkpoints = [Checkpoint(Point(30, 120), Point(100, 120)), Checkpoint(Point(130, 30), Point(130, 100)),
                            Checkpoint(Point(160, 120), Point(230, 120)), Checkpoint(Point(230, 250), Point(160, 250)),
                            Checkpoint(Point(250, 270), Point(250, 340)), Checkpoint(Point(420, 340), Point(420, 270)),
                            Checkpoint(Point(580, 340), Point(580, 270)), Checkpoint(Point(600, 360), Point(670, 360)),
                            Checkpoint(Point(600, 580), Point(670, 580)), Checkpoint(Point(580, 600), Point(580, 670)),
                            Checkpoint(Point(390, 600), Point(390, 670)), Checkpoint(Point(370, 580), Point(300, 580)),
                            Checkpoint(Point(300, 520), Point(370, 520)), Checkpoint(Point(280, 500), Point(280, 430)),
                            Checkpoint(Point(120, 430), Point(120, 500)), Checkpoint(Point(100, 410), Point(30, 410)),
                            Checkpoint(Point(30, 270), Point(100, 270))]

    # O()
    def create_checkpoints(self, start):

        self.checkpoints.append(start)

        for i in range(len(self.left_boarder)-1):

            point1 = self.left_boarder[i]
            point2 = self.right_boarder[i]

            prevCheckpoint = self.checkpoints[len(self.checkpoints)-1].get_middle()

            endpoint1 = Point(point2.x, point1.y)
            endpoint2 = Point(point1.x, point2.y)

            if point1.distance_to(prevCheckpoint) < point2.distance_to(prevCheckpoint):
                if endpoint1.distance_to(prevCheckpoint) < endpoint2.distance_to(prevCheckpoint):
                    self.checkpoints.append(Checkpoint(Point(point1.x, point1.y), endpoint1))
                    self.checkpoints.append(Checkpoint(Point(point1.x, point1.y), endpoint2))
                else:
                    self.checkpoints.append(Checkpoint(Point(point1.x, point1.y), endpoint2))
                    self.checkpoints.append(Checkpoint(Point(point1.x, point1.y), endpoint1))
            else:
                if endpoint1.distance_to(prevCheckpoint) < endpoint2.distance_to(prevCheckpoint):
                    self.checkpoints.append(Checkpoint(Point(point2.x, point2.y), endpoint1))
                    self.checkpoints.append(Checkpoint(Point(point2.x, point2.y), endpoint2))
                else:
                    self.checkpoints.append(Checkpoint(Point(point2.x, point2.y), endpoint2))
                    self.checkpoints.append(Checkpoint(Point(point2.x, point2.y), endpoint1))

