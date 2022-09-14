import pygame


class Controls:

    def __init__(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False

    def update(self, event):
        if event.key == pygame.K_LEFT:
            self.left = not self.left

        if event.key == pygame.K_RIGHT:
            self.right = not self.right

        if event.key == pygame.K_DOWN:
            self.reverse = not self.reverse

        if event.key == pygame.K_UP:
            self.forward = not self.forward

    def set(self, directions):
        self.forward = directions[0]
        self.reverse = directions[1]
        self.left = directions[2]
        self.right = directions[3]

    def reset(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
