from main import *
import pygame.draw


class Spacecraft:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass

    def draw(self):
        pygame.draw.circle(window, RED, (int(self.x), int(self.y)), OBJ_SIZE)

    def move(self, planet=None):
        self.x += self.vel_x
        self.y += self.vel_y
