from math import dist
import random
import numpy as np
import matplotlib.pyplot as plt
from random import choice
from random import randint
from numpy.typing import _16Bit

def maze_maker(dimensions):
    maze = np.zeros((dimensions, dimensions), dtype=np.uint8)
    for m, element in enumerate(maze):
        for i, element in enumerate(element):
            if m % 2 == 0:
                maze[m][i] = 1
            else:
                if i % 2 == 0:
                    maze[m][i] = 1
    return maze, dimensions

def find_neighbour(maze, cell):
    y = cell[0]
    x = cell[1]
    ne1 = [y + 2, x]
    ne2 = [y - 2, x]
    ne3 = [y, x + 2]
    ne4 = [y, x - 2]
    neighbour_cells = [ne1, ne2, ne3, ne4]
    shape = np.shape(maze)
    for i in neighbour_cells:
        for m in i:
            if m < 0 or m > shape[1] or m > shape[0]:
                neighbour_cells.pop(neighbour_cells.index(i))
    neighbour_cells = np.array(neighbour_cells)
    valid_neighbours = []
    n, m = maze.shape
    for (i, j) in neighbour_cells:
        if i >= 0 and i < n and j >= 0 and j < m:
            valid_neighbours.append((i,j))
    neighbour_cells = valid_neighbours
    return neighbour_cells


def find_close_cells(maze, cell):
    cell_1 = cell[0], cell[1] + 1
    cell_2 = cell[0], cell[1] - 1
    cell_3 = cell[0] + 1, cell[1]
    cell_4 = cell[0] - 1, cell[1]
    nbr_cells = [cell_1, cell_2, cell_3, cell_4]
    close_cells = []
    for cell in nbr_cells:
        if maze[cell] == 0:
            close_cells.append(cell)
    return close_cells

def calculate_dist(current_cell, destination):
    dist_vector = np.array([destination[0] - current_cell[0], destination[1] - current_cell[1]])
    dist = int(np.linalg.norm(dist_vector))
    return dist

def close_dist(current_cell, destination):
    close_cells = find_close_cells(maze, current_cell)
    close_distance = []
    for cell in close_cells:
        dist = calculate_dist(cell, destination)
        close_distance.append([dist, cell])
    return close_distance

def generate_maze_alb(maze):
    unvisited = np.argwhere(maze == 0)
    current_cell = choice(unvisited)
    first_cell = current_cell
    visited = np.zeros_like(maze)
    visited[current_cell[0], current_cell[-1]] = 1
    count_1 = len(np.argwhere(visited == 1))
    count_0 = int(((len(maze) / 2) - 0.5 ) * ((len(maze) / 2) - 0.5 ))
    count = count_0 - count_1
    while count > 0:
        chosen_neighbour = choice(find_neighbour(maze, current_cell))
        if visited[chosen_neighbour[0], chosen_neighbour[1]] == 0:
            wall = (current_cell + np.array(chosen_neighbour)) // 2
            maze[wall[0], wall[1]] = 0
            visited[chosen_neighbour[0], chosen_neighbour[-1]] = 1
        current_cell = chosen_neighbour
        count_1 = len(np.argwhere(visited == 1))
        count = count_0 - count_1
    last_cell = current_cell
    return maze, tuple(first_cell), tuple(last_cell)

def diekstras(maze, first_cell, last_cell):
    current_cell = first_cell
    dist_dic = {}
    dist = np.full(maze.shape, np.inf, dtype="float64")
    dist[first_cell] = 0
    unvisited_dist = dist.copy()
    visited = np.zeros_like(maze)

    finished = False
    
    while True: # not finished:
        new_dist = dist[current_cell] + 1
        close_cells = find_close_cells(maze, current_cell)
        for nbr_cell in close_cells:
            if not visited[nbr_cell]:
                dist[nbr_cell] = min(dist[nbr_cell], new_dist)
                unvisited_dist[nbr_cell] = min(unvisited_dist[nbr_cell], new_dist)

        visited[current_cell] = 1
        unvisited_dist[current_cell] = np.inf
        
        if visited[last_cell]:
            # finished = True
            break
        
        current_cell = np.unravel_index(unvisited_dist.argmin(), unvisited_dist.shape)

    visited_cells = []
    S = []
    while True:
        new_dist = dist[current_cell] - 1
        close_cells = find_close_cells(maze, current_cell)
        for nbr_cell in close_cells:
            if dist[nbr_cell] == new_dist:
                S.append(nbr_cell)
                current_cell = nbr_cell
                break
        if current_cell == first_cell:
            break
            
    return dist, S

maze_0, dimensions = maze_maker(101)
maze, first_cell, last_cell = generate_maze_alb(maze_0)
options = [(1, 1), (dimensions - 2, 1), (1, dimensions - 2), (dimensions - 2, dimensions - 2)]
last_cell = choice(options)
first_cell = tuple([int(dimensions / 2 - 1), int(dimensions / 2 - 1)])
empty = np.zeros_like(maze)
empty[first_cell[0], first_cell[1]] = 1
full = np.zeros_like(maze)
full[last_cell[0], last_cell[1]] = 1

dist, S = diekstras(maze, first_cell, last_cell)
shape = np.zeros_like(maze)
for i in S:
    shape[i] = 1

plt.imshow(maze, cmap='binary') # maze
plt.imshow(np.ma.masked_equal(dist, np.inf), cmap='plasma') # depth map
plt.imshow(np.ma.masked_equal(shape, 0), cmap='RdYlGn', vmax=1, vmin=0) # shortest path
plt.imshow(np.ma.masked_equal(empty, 0), cmap='bwr') # start
plt.imshow(np.ma.masked_equal(full, 0), cmap='autumn') # end
plt.show()
print(maze_0)

