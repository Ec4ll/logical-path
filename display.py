"""
A module with helper functions to display the grid and paths to the console.
"""
from setup import *


def get_path(sol: dict):
    """Gets the path from the solution."""
    if sol == None:
        return sol

    path = dict()
    for key in sol.keys():
        if not key[0] == "x":
            path[key] = sol[key]
    if path == {}:
        return

    return path


def print_grid(path=[]):
    """Prints the grid to the console. If a path is supplied, prints the
    path on the grid. Otherwise just prints the grid."""
    for i in range(GRID_SIZE):
        # The top border
        print(" " + "-" * (GRID_SIZE * 5 - 1))
        for j in range(GRID_SIZE):
            if j == 0:
                # The left border
                print("|", end="")
            # Put a star in the square if it is in the path
            c = "*" if (i, j) in path else " "
            # Put an X in the square if it is inaccessible
            c = "X" if (i, j) in inaccessible_coords else c
            # Put an s in the starting square
            if (i, j) == start_coords:
                c = "s" if not (i, j) in inaccessible_coords else "sX"
            # Put an e in the ending square
            if (i, j) == end_coords:
                c = "e" if not (i, j) in inaccessible_coords else "eX"
            # Right side column dividers (and right border)
            end_str = "|\n" if j == GRID_SIZE - 1 else "|"
            print("{:^4}".format(c), end=end_str)
    # The bottom border
    print(" " + "-" * (GRID_SIZE * 5 - 1), end="\n\n")
