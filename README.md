# Pathfinding with Propositional Logic

This project models a pathfinding algorithm in propositional logic.
The rules of a valid path are used as constraints, then the valid paths are found by a SAT solver.

## File Structure

-   `settings.py`: Here is where the user can specify everything about the grid.
-   `run.py`: The main driver for the project.
-   `setup.py`: Checks that the user input in `settings.py` is valid, and generates the variables used in the model.
-   `pathfinder.py`: Generates a single path for the grid using complex constraints.
-   `all_paths.py`: Generates all of the unique paths for the grid. Note: large grids with few inaccessible squares will error out due to recursion depth limits.
-   `display.py`: A module with helper functions to display the grid and paths to the console.
