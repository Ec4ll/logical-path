"""
Generates a single path for the grid using complex constraints.
"""

from bauhaus import constraint
from setup import *


def assign_accessibility():
    for sq in grid_vars:
        if sq in inaccessible:
            constraint.add_at_most_one(e, sq, start)  # type: ignore
        else:
            constraint.add_at_least_one(e, sq)  # type: ignore


def is_valid(sq: tuple):
    """Checks if a pair of coordinates is in the grid."""
    return not (sq[0] >= GRID_SIZE or sq[0] < 0 or sq[1] < 0 or sq[1] >= GRID_SIZE)


def generate_path(sq: tuple, visited: list):
    """Recursively generate a path from sq to the ending square."""
    i = coords.index(sq)
    x = grid_vars[i]
    y = path_vars[i]

    row = sq[0]
    col = sq[1]

    # Base case
    # If the end has been reached, add it as a constraint
    if x == end and not x in inaccessible:
        constraint.add_exactly_one(e, y)  # type: ignore
        return True, y
    if visited is None:
        return True, y

    # Recursive case
    visited.append(sq)
    if not x in inaccessible:
        # Calculate each possible next square and the corresponding visited list
        left = (row - 1, col)
        v_left = visited.copy().append(left)
        right = (row + 1, col)
        v_right = visited.copy().append(right)
        up = (row, col - 1)
        v_up = visited.copy().append(up)
        down = (row, col + 1)
        v_down = visited.copy().append(down)

        # Look for a path to the end by moving in a valid direction and adding that
        # square to the path, or move back a square and look for a path to the end.
        if is_valid(left) and not left in visited and generate_path(left, visited)[0]:
            constraint.add_exactly_one(e, generate_path(sq, v_left)[1], y)  # type: ignore
            # E.add_constraint(
            #     (generate_path(E, sq, v_left)[1] | y) & (y | ~y)) # type: ignore
            return True, y

        if (
            is_valid(right)
            and not right in visited
            and generate_path(right, visited)[0]
        ):
            constraint.add_exactly_one(e, generate_path(sq, v_right)[1], y)  # type: ignore
            # E.add_constraint(
            # (generate_path(E, sq, v_right)[1] | y) & (y | ~y)) # type: ignore
            return True, y

        if is_valid(up) and not up in visited and generate_path(up, visited)[0]:
            constraint.add_exactly_one(e, generate_path(sq, v_up)[1], y)  # type: ignore
            # E.add_constraint(
            #     (generate_path(E, sq, v_up)[1] | y) & (y | ~y)) # type: ignore
            return True, y

        if is_valid(down) and not down in visited and generate_path(down, visited)[0]:
            constraint.add_exactly_one(e, generate_path(sq, v_down)[1], y)  # type: ignore
            # E.add_constraint(
            #     (generate_path(E, sq, v_down)[1] | y) & (y | ~y)) # type: ignore
            return True, y

    return False, y
