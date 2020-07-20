# https://leetcode.com/problems/number-of-islands/


def num_islands(grid):
    # How islands are connected.
    connections = ((0, 1), (0, -1), (1, 0), (-1, 0))
    island_count = 0  # The number of islands we have found so far.
    visited = set()  # Set of index tuples we have looked at.

    def claim_connected_land(row_index, column_index):
        if row_index < 0 or column_index < 0:
            # Negative indexes are valid in Python so have to check.
            return

        if (row_index, column_index) in visited:
            return

        visited.add((row_index, column_index))
        try:
            value = grid[row_index][column_index]

        except IndexError:
            # Outside the grid.
            # Checking bounds might be faster,
            # but this easily allows any shape grid.
            return

        if value == 1:
            # Claim the land for the current island.
            grid[row_index][column_index] = str(island_count)

            # Continue to claim connected land.
            for row_delta, column_delta in connections:
                claim_connected_land(
                    row_index + row_delta,
                    column_index + column_delta
                )

    for row_index, row in enumerate(grid):
        for column_index, value in enumerate(row):
            if (row_index, column_index) in visited:
                continue

            if value == 1:
                island_count += 1
                claim_connected_land(row_index, column_index)

            else:
                visited.add((row_index, column_index))

    return island_count
