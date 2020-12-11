"""
Generates all of the unique paths for the grid. 
Note: large grids with few inaccessible squares will error out due to 
        recursion depth limits.
"""

from lib204 import Encoding
from setup import *
from pathfinder import assign_accessibility, is_valid


paths = list()


def neighbours(sq):
    """A utility function to find the valid squares adjacent to a square."""
    row = sq[0]
    col = sq[1]

    # The 4 possible adjacent squares
    potential = [(row-1, col),
                 (row+1, col),
                 (row, col-1),
                 (row, col+1)]

    return [n for n in potential if is_valid(n)]


def all_paths(path, sq):
    """Recursively generates all of the paths from sq to the ending square."""
    i = coords.index(sq)
    x = grid_vars[i]
    y = path_vars[i]

    # Base case
    # If the end has been reached, add the current path to the list of paths
    if sq == end_coords:
        path.append(y)
        paths.append([p for p in path])
        return True

    # Recursive case
    # Find a path to the end from each of the current squares neighbours
    valid = False
    if not x in inaccessible and not y in path:
        for sq2 in neighbours(sq):
            path.append(y)
            valid = all_paths(path, sq2) or valid
            path.remove(y)

    return valid


def constrain_path(current: list):
    """Recursively calculate the conjuntion of the variables in a path list."""
    sq = current.pop(0)
    if len(current) == 0:
        return sq
    return constrain_path(current) & sq


def constrain_paths(current: list):
    """Recursively calculate the disjunction of the paths in the paths list."""
    path = current.pop(0)
    if len(current) == 0:
        return constrain_path([y for y in path])
    return constrain_paths(current) | constrain_path([y for y in path])


def all_paths_theory():
    """Creates a model for the grid and possible paths."""
    E = Encoding()
    E.add_constraint(assign_accessibility([x for x in grid_vars]))
    all_paths([], start_coords)
    E.add_constraint(constrain_paths([path for path in paths]))

    # Negate any path variables that are never used in a path
    for y in path_vars:
        if not y in list(set(sum(paths, []))):
            E.add_constraint(~y)

    # Return the model and the path list with duplicate squares in each path
    # filtered out
    return E, [list(set(path)) for path in paths]
