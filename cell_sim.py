from visualiser import Visualiser
from model import CellPatch
from model import ObstaclePatch
from model import Cell
import random
from random import shuffle, choices, choice
import numpy as np

def cell_life(cell:Cell,age_limit,division_limit):
    '''Uses tick function to age cells. if the age_limit or division_limit is exceeded, the cell will die.'''
    cell.tick()
    if cell.age() > age_limit:
        cell.patch().remove_cell()
    elif cell.divisions() > division_limit:
        cell.patch().remove_cell()
    else:
        if cell.patch().toxicity() - cell.resistance() >= random.randint(0,10):
            cell.patch().remove_cell()

def check_for_cells(patch_list):
    '''Iterates over the entire patch list for cells. Returns true if there is a cell on the patch.'''
    for patch in patch_list:
        if patch.has_cell() == True:
            return True
    return False

def create_board(row:int, col:int, grid:np.array):
    patch_list = []
    for i in range(row):
        for j in range(col):
            if grid[i][j] == '%':
                obstacle_patch = ObstaclePatch(i, j)
                patch_list.append(obstacle_patch)
            else:
                toxic = int(grid[i][j])
                cell_patch = CellPatch(i, j,toxic)
                patch_list.append(cell_patch)
    return patch_list

def free_neighbors(patches, patch, row:int, col:int):
    '''Checks neighboring patches of each cell for vacant patches. Returns false with a list of vacant patches, if there are, true if not.'''
    neighbor_patches = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    (x,y) = patch.row(), patch.col()
    if_vacants = []
    if_not = [(x,y)]
    for (z,w) in neighbor_patches:
        row_pos = z + x
        col_pos = w + y
        (a,b) = (row_pos%row,col_pos%col)
        if_not.append((a,b))
        if not isinstance(patches[a][b], ObstaclePatch):
            if not patches[a][b].has_cell():
                if_vacants.append((a,b))
    return (False,if_vacants) if len(if_vacants)>0 else (True,if_vacants)

def rand(prob):
    result = choices([1,0],[prob,1-prob],k=1)[0]
    if result == 1:
        return True
    else:
        return False

def spread_cells(patches,patch,row,col,divisions_probability,cd):
    '''Function for cell division. If the square is overcrowded a random cell from that square dies,
    if not, the random function runs and a cell divides if it is succesful and has no cooldown period.'''
    (x,y) = (patch.row(),patch.col())
    overcrowd, poss = free_neighbors(patches, patch, row, col)
    if (divisions_probability - patch.cell().resistance()/20) <= random.random() and poss:
        if rand(divisions_probability):
            x_r, y_r = choice(poss)
            cell = patch.cell()
            if cell.divisions() <= cd:
                cell.divide(patches[x_r][y_r])

def initial_pop(row:int,col:int,intial_population:int,grid):
    init_pop = initial_population * [1] + (row * col - initial_population)*[0]
    shuffle(init_pop)
    board = create_board(row,col,grid)
    cellpatches = list(filter(lambda x: isinstance(x, CellPatch), board))
    for patches in cellpatches:
        if init_pop[0] == 1:
            Cell(patches,random.randrange(10))
        init_pop = init_pop[1:]
    return board, cellpatches

if __name__ == '__main__':
    grid = np.genfromtxt('grid_3.txt', dtype='str')
    row = len(grid)
    col = len(grid[0])
    initial_population = 2
    age_limit = 10
    division_limit = 7
    division_prob = 0.6
    division_cd = 1
    time_limit = 100
    tick = 0
    init_pop,cell_patches = initial_pop(row,col,initial_population,grid)
    vis = Visualiser(init_pop,row,col)
    while check_for_cells(cell_patches) and tick<time_limit:
        for patch in cell_patches:
            if patch.has_cell():
                cell = patch.cell()
                cell_life(cell,age_limit,division_limit)
        for patch in cell_patches:
            if patch.has_cell():
                spread_cells(vis._patches,patch,row,col,division_prob,division_cd)
        vis.update()
        tick += 1
