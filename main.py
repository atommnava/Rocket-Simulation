import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1600,1200
window = pygame.display_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot")

# Constants
PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100

image1 = "background.jpg"
image2 = "jupiter.png"
BACKGROUND = pygame.image.load(image1)
PLANET = pygame.image.load(image2)
