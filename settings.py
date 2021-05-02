"""
Use this file to specify the grid size, starting square, ending square,
and inaccessible squares.

NOTE
If the search space (total accessible squares) is too large
the program may not run due to recursion depth limits in python.
"""

# Set the size of the grid
# referenced as N in comments
GRID_SIZE = 4

# Set the starting square
start_coords = (0, 0)

# Set the ending square
end_coords = (3, 3)

# Set the inaccessible squares
inaccessible_coords = [(0, 1), (1, 1), (3, 2), (1,2), (1,3)]
