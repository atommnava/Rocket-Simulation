# Librarys
import pygame
import math
from Spacecraft import *

pygame.init()

WIDTH, HEIGHT = 800,600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gravitational Slingshot")

# Constants
PLANET_MASS = 100
SHIP_MASS = 5
G = 5
FPS = 60
PLANET_SIZE = 50
OBJ_SIZE = 5
VEL_SCALE = 100

# Images
image1 = "background.jpg"
image2 = "jupiter.png"
BACKGROUND = pygame.transform.scale(pygame.image.load(image1), (WIDTH, HEIGHT))
PLANET = pygame.transform.scale(pygame.image.load(image2), (PLANET_SIZE * 2, PLANET_MASS * 2))

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

def main() -> None:
    running = True
    clock = pygame.time.Clock()

    objects = []
    temp_obj_pos = None
    while running:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    t_x, t_y = temp_obj_pos
                    obj = Spacecraft(t_x, t_y, 0, 0, SHIP_MASS)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        window.blit(BACKGROUND, (0,0))

        if temp_obj_pos :
            pygame.draw.line(window, RED, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(window, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects:
            obj.draw()
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()


