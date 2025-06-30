# Librarys
import pygame
import math
from models import *

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
PLANET = pygame.transform.scale(pygame.image.load(image2), (PLANET_SIZE * 2, PLANET_SIZE * 2))


WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)

def create_ship(Location, mouse):
    t_x, t_y = Location
    m_x, m_y = mouse
    vel_x = (m_x - t_x) / VEL_SCALE
    vel_y = (m_y - t_y) / VEL_SCALE
    object = Spacecraft(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return object

def main() -> None:
    running = True
    clock = pygame.time.Clock()

    planet = Planet(WIDTH // 2, HEIGHT // 2, PLANET_MASS)
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

                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos

        window.blit(BACKGROUND, (0,0))

        if temp_obj_pos :
            pygame.draw.line(window, RED, temp_obj_pos, mouse_pos, 2)
            pygame.draw.circle(window, RED, temp_obj_pos, OBJ_SIZE)

        for obj in objects[:]:
            obj.draw()
            obj.move()
            off_screen = obj.x < 0 or obj.x > WIDTH or obj.y < 0 or obj.y > HEIGHT
            # Pitágoras c^2=a^2+b^2
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= PLANET_SIZE
            if off_screen or collided:
                objects.remove(obj)

        planet.draw()

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()


