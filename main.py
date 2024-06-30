import pygame
from sys import exit
from lind_systems import L_sysA, FractalTree
from simulation import Simulation
pygame.init()

WIN_WIDTH = 800
WIN_HEIGHT = 800
FPS = 50

window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("L Systems")

clock = pygame.time.Clock()
simulation = Simulation(WIN_WIDTH, WIN_HEIGHT)

def main():
    algae = L_sysA(['A', 'B'], None, 'A', {
        'A': 'AB',
        'B': 'A'
    })

    fractal_tree = FractalTree(['1', '0'], ["[", "]"], '0', {
        '1': '11',
        '0': '1[0]0'
    })

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulation.crawl_system(fractal_tree)
                if event.key == pygame.K_r:
                    simulation.reset(fractal_tree)

        pygame.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    main()