#!/usr/bin/env python3
import os
import time
import random
from figures import FIGURES

# world size - designed for standard unix 80x24 console
WIDTH = 79
HEIGHT = 22


def normalize(y, x):
    """ makes sure that y,x coordinates is in the world possible coordinates """
    return y % HEIGHT, x % WIDTH


def draw_world(world):
    """prints world to console"""
    os.system('clear')
    for line in world:
        print(''.join(line))


def count_neighbors(world, cell_y, cell_x):
    neighbors = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == j == 0: continue
            y = cell_y + i
            x = cell_x + j
            y, x = normalize(y, x)
            if world[y][x] == 'O':
                neighbors += 1
    return neighbors


def make_next_generation(world):
    new_world = []
    for y in range(HEIGHT):
        new_line = []
        for x in range(WIDTH):
            cell = world[y][x]
            neighbors = count_neighbors(world, y, x)

            # main Convay's Game of Life rules:
            if cell == ' ' and neighbors == 3:
                new_line.append('O')
            elif cell == 'O' and (2 <= neighbors <= 3):
                new_line.append('O')
            else:
                new_line.append(' ')

        new_world.append(new_line[:])
    return new_world


def make_random_world(probability=0.1):
    """
    'world' is just dicts[x-coord] inserted in dict[y-coord]
    alive cell is 'O'
    dead cell is  ' '
    """
    return [
        ['O' if random.random() < probability else ' ' for x in range(WIDTH)]
        for y in range(HEIGHT)
    ]


def add_random_figure(world):
    """    adds some known figures into random place in the world    """
    figure = random.choice(FIGURES)
    pos_x = random.randint(5, WIDTH-5)
    pos_y = random.randint(5, HEIGHT-5)

    for coord in figure:
        y = pos_y + coord[0]
        x = pos_x + coord[1]
        y, x = normalize(y, x)
        world[y][x] = 'O'
    return world


if __name__ == '__main__':
    world = make_random_world(0.2)
    while True:
        world = make_next_generation(world)
        if random.random() < 0.01:
            world = add_random_figure(world)
        draw_world(world)
        time.sleep(0.1)