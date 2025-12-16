"""
Advent of Code 2025 - Day 4
"""

from pathlib import Path
from aoc_template import BaseSolution, parse_lines


DIRECTIONS = [
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
    (1, 0),
    (0, 1),
    (1, 1),
    (-1, 1),
]


def check_neighbor(r: int, c: int, grid):
    # check if neighbor is in bounds
    if not (0 <= r < len(grid)):
        return 0
    if not (0 <= c < len(grid[r])):
        return 0
    # check if neighbor contains paper towel
    return 1 if grid[r][c] == "@" else 0


class Solution(BaseSolution):
    """Solution for Day 4."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)

    def part1(self):
        """Solve part 1."""
        grid = self.data
        total = 0
        # Traverse each position (r, c) on the graph
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                # if position does not contain paper towel continue
                if grid[r][c] != "@":
                    continue

                # check if neighbor is out of bounds or contains paper towel
                count = 0
                for dr, dc in DIRECTIONS:
                    count += check_neighbor(r + dr, c + dc, grid)

                # if count is less than 4, increment total
                if count < 4:
                    total += 1

        return total

    def part2(self):
        """Solve part 2."""
        grid = [list(row) for row in self.data]
        total = 0

        while True:
            # find all removal rolls
            to_remove = []

            for r in range(len(grid)):
                for c in range(len(grid[r])):
                    # if position does not contain paper towel (@) continue
                    if grid[r][c] != "@":
                        continue

                    # count neighbors that contain paper towels
                    count = 0
                    for dr, dc in DIRECTIONS:
                        count += check_neighbor(r + dr, c + dc, grid)

                    if count < 4:
                        to_remove.append((r, c))

            # keep looping until to_removed is 0
            if len(to_remove) == 0:
                break

            for (r,c) in to_remove:
                grid[r][c] = '.'
            total += len(to_remove)

        return total


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
