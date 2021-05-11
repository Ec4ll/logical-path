"""
The main driver for the project.
"""
from settings import *
from display import *
from setup import *
from pathfinder import *

if __name__ == "__main__":
    assign_accessibility()
    generate_path((coords[start_index][0], coords[start_index][1]), [])
    theory = e.compile()
    # e.introspect()
    sol = theory.solve()
    print(f"Theory: {theory}\n")
    print_grid()
    print(f"Solution: {sol}\n")
    path_sol = get_path(sol)  # type: ignore
    print(f"Path: {path_sol}")
    path_list = [(int(y.x), int(y.y)) for y in path_sol.keys()]
    print_grid(path_list)
