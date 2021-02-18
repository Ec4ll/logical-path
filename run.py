"""
The main driver for the project.
"""

from time import sleep
from setup import *
from pathfinder import *
from display import *
from all_paths import *


def var_to_coords(var_list: list):
    """Helper function to convert a var into its coordinates."""
    return [(int(str(y)[1]), int(str(y)[2])) for y in var_list]


# For the tests
example_theory = single_path_theory

if __name__ == "__main__":
    print("To customize the grid, edit settings.py")
    sleep(1)
    # Print the grid
    print("\nGrid:")
    print_grid()

    # Look for a path with the single path theory (the most logically complex path)
    C = single_path_theory()
    if C.is_satisfiable():
        print("There is a valid path.")
    else:
        print("There is no valid path.")

    # Print the full solution
    sol = C.solve()
    print(f"Solution: {sol}", end="\n\n")

    # Print the path variables
    path_sol = get_path(sol)
    print(f"Path: {path_sol}")

    if path_sol != None:
        # Print the complex path on the grid
        path_list = [(int(y[1]), int(y[2])) for y in path_sol.keys()]
        print_grid(path_list)

        # Find all paths
        A, paths = all_paths_theory()
        # Print the shortest path
        print("Shortest path:")
        print_grid(var_to_coords(min(paths, key=len)))
        # Ask the user if they want to see all the paths
        show_all = ""
        while not show_all.lower() in ["y", "n"]:
            show_all = input("Compute all paths? (y/n): ")

        if show_all.lower() == "y":
            all_solutions = A.solve()
            print(f"Solutions: {A.count_solutions()}")
            print(f"Unique solutions: {len(paths)}")
            print(
                "\n\tNote: some solutions may use the same squares but in a different order.", end="\n\n")

            print("Paths:")
            for path in paths:
                # Print all the unique paths
                path_list = var_to_coords(path)
                print_grid(path_list)

        # Ask the user if they want to see the path variable likelihoods
        show_likelihoods = ""
        while not show_likelihoods.lower() in ["y", "n"]:
            show_likelihoods = input(
                "Compute path variable likelihoods? (y/n): ")

        if show_likelihoods.lower() == "y":
            print("\nPath variable likelihoods:")
            var_strings = [str(var) for var in path_vars]
            for v, vn in zip(path_vars, var_strings):
                print(f" {vn}: {A.likelihood(v) * 100:.2f}%")
