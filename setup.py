from bauhaus import Encoding, proposition
from settings import *


# Check the settings are all valid
assert (start_coords[0] < GRID_SIZE and start_coords[1]
        < GRID_SIZE), f"Invalid starting square. Must be between (0,0) and ({GRID_SIZE-1},{GRID_SIZE-1})"
assert (end_coords[0] < GRID_SIZE and end_coords[1]
        < GRID_SIZE), f"Invalid ending square. Must be between (0,0) and ({GRID_SIZE-1},{GRID_SIZE-1})"
assert (all(c[0] < GRID_SIZE for c in inaccessible_coords) and all(c[1] < GRID_SIZE for c in inaccessible_coords)
        ), f"One or more of the user defined inaccessible squares are outside of the grid."

# Setup
e = Encoding()

@proposition(e)
class GridSquare(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Grid({self.x},{self.y})"

@proposition(e)
class PathSquare(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Path({self.x},{self.y})"


# [x00,x01,...,x0N,x10,...,xNN]
# grid is a list of variables representing the squares of the grid
# True: accessible
# False: inaccessible
grid_vars = list()

# [y00,y01,..., y0N,y10,...,yNN]
# path is a list of variables representing the squares in the grid
# True: square is used in the path
# False: square is not in the path
path_vars = list()

# [(0,0),(0,1),...,(0,N),(1,0),...,(N,N)]
# The coordinates of the square at a given index
coords = list()

# Generate the above lists based on the size of the grid
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        grid_vars.append(GridSquare(i,j))
        path_vars.append(PathSquare(i,j))
        coords.append((i,j))


start_index = coords.index(start_coords)
start = grid_vars[start_index]

end_index = coords.index(end_coords)
end = grid_vars[end_index]

inaccessible = [grid_vars[coords.index(b)] for b in inaccessible_coords]
