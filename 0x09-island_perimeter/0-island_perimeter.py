#!/usr/bin/python3
"""
Calculate the perimeter of an island
"""


def island_perimeter(grid):
    """
    find the perimeter of an island represented by 2D matrix
    1 indicate land, 0 indicate water
    """
    max_height = len(grid)  # the total number of rows
    max_width = len(grid[0])  # the total number of columns

    cell_perimeter = 0
    # traverse through the grid
    for row in range(max_height):
        # every row with the given 2D grid
        for col in range(max_width):
            # every col in a row
            if grid[row][col] == 1:
                cell = 4
                # check adjacent cells, if cell == 1, reduce cell by 1
                # traverse vertically
                if row - 1 > 0 and grid[row - 1][col] == 1:
                    # adjacent above
                    cell -= 1
                if row + 1 < max_height and grid[row + 1][col] == 1:
                    # adjacent below
                    cell -= 1

                # traverse horizontal left
                if col - 1 > 0 and grid[row][col - 1] == 1:
                    cell -= 1
                # traverse horizontal right
                if col + 1 < max_width and grid[row][col + 1] == 1:
                    cell -= 1

                cell_perimeter += (1 * cell)
    return cell_perimeter
