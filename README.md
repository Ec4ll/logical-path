# Pathfinding with Propositional Logic

This project models a pathfinding algorithm in propositional logic.

## Structure

-   `documents`: Contains folders for the draft and final submissions.
-   `run.py`: The main driver for the project.
-   `settings.py`: The file where the user can specify the grid size, starting square, ending square, and inaccessible squares.
-   `setup.py`: Checks that the user input in `settings.py` is valid, and generates the variables used in the model.
-   `pathfinder.py`: Generates a single path for the grid using complex constraints.
-   `all_paths.py`: Generates all of the unique paths for the grid. Note: large grids with few inaccessible squares will error out due to recursion depth limits.
-   `display.py`: A module with helper functions to display the grid and paths to the console.
-   `test.py`: Confirms the submission has everything required.
