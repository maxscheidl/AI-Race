import pygame
from segments.block import Block, Start, NarrowBlock, ZicZacBlock
from segments.curve import BlockCurve, SmoothCurve


class Road:

    def __init__(self):

        self.segments = []
        self.width = 70

        self.init_road_one()

    def draw(self, canvas):

        for segment in self.segments:
            segment.draw(canvas)

    def init_road_zero(self):

        self.segments.append(Start((60, 300), (0,-1), self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(BlockCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 200))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 370))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))

    def init_road_one(self):

        self.segments.append(Start((60, 400), (0,-1), self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.7))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "left", 0.8))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20, "right", 0.8))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 50))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "center", 0.9))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "center", 1))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "left", 0.6))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.6))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "left", 0.7))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "left", 0.7))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "center", 0.9))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.7))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.7))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "left", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "right", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "left", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "right", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "center", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 70, "left", 0.9))
        self.segments.append(Block(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20))
        self.segments.append(BlockCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.9))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 20, "left", 0.9))
        self.segments.append(SmoothCurve("left", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(SmoothCurve("right", self.segments[-1].end, self.segments[-1].next_direction, self.width))
        self.segments.append(ZicZacBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 100, "right", 0.7))
        self.segments.append(NarrowBlock(self.segments[-1].end, self.segments[-1].next_direction, self.width, 80, "right", 0.9))




