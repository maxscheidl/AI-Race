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
        self.forward = True if directions[0] > 0 else False
        self.reverse = True if directions[1] > 0 else False
        self.left = True if directions[2] > 0 else False
        self.right = True if directions[3] > 0 else False

    def reset(self):
        self.forward = False
        self.left = False
        self.right = False
        self.reverse = False
