import turtle
from sys import exit
from lind_systems import L_sysA, L_sysB
from simulation import Simulation

WIN_WIDTH = 800
WIN_HEIGHT = 800
FPS = 50
GENS = 10
bug = turtle.Turtle()
STEP_SIZE = 6
simulation = Simulation(WIN_WIDTH, WIN_HEIGHT, bug, STEP_SIZE)

algae = L_sysA("algae", ['A', 'B'], None, 'A', {
    'A': 'AB',
    'B': 'A'
})

fractal_tree = L_sysB("fractal_tree", ['1', '0'], ["[", "]"], '0', {
    '1': '11',
    '0': '1[0]0'
})

koch_curve = L_sysB("koch_curve", ['F'], ['+', '-'], 'F', {
    'F': 'F+F-F-F+F'
})

def main():
    simulation.run_system(fractal_tree)

if __name__ == "__main__":
    main()