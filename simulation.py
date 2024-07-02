import turtle
import time
from lind_systems import *
from typing import Tuple
GENS = 100
class Simulation:
    def __init__(self, win_width, win_height, bug, step_size):
        self.win_width = win_width
        self.win_height = win_height
        self.bug = bug
        self.step_size = step_size

    def run_system(self, L_sys: object):
        self.bug.speed(0)
        turtle.mode("logo")
        if L_sys.name == "fractal_tree":
            LEFT_ANGLE: int = 45
            RIGHT_ANGLE: int = 45
            pos_angles: List[Tuple[Tuple[int, int], int]] = []
            def generate(char: str):
                #time.sleep(1)
                nonlocal pos_angles
                if char == '1':
                    self.bug.forward(self.step_size)
                elif char == '0':
                    self.bug.color('green')
                    self.bug.forward(self.step_size)
                    self.bug.color('black')
                elif char == '[':
                    pos_angles.append((self.bug.pos(), self.bug.heading()))
                    self.bug.left(LEFT_ANGLE)
                elif char == ']':
                    pos, angle = pos_angles.pop()
                    self.bug.penup()
                    self.bug.goto(pos)
                    self.bug.setheading(angle)
                    self.bug.pendown()
                    self.bug.right(RIGHT_ANGLE)

            for _ in range(7):
                self.bug.pendown()
                for char in L_sys.string:
                    generate(char)

                L_sys.crawl()
                self.bug.penup()
                self.bug.home()

        elif L_sys.name == "algae":
            L_sys.crawl()
            print(L_sys.string)
        turtle.done()


    def reset(self, L_sys):
        L_sys.reset()
        print(L_sys.string)

