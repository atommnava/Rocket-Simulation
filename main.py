# Librarys
import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1600,1200
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
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        window.blit(BACKGROUND, (0,0))
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()


