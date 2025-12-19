"""
Advent of Code 2025 - Day 6
"""

import math
from pathlib import Path
from aoc_template import BaseSolution


class Solution(BaseSolution):
    """Solution for Day 6."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        rows = input_text.splitlines()
        W = max(len(r) for r in rows)
        # build a 2D grid from each row, by addding some padding to the right (making everything left justified)
        grid = [row.ljust(W, " ") for row in rows]

        # compute which character columns are "separators"
        separator = [True] * W
        for c in range(W):
            for r in range(len(grid)):
                if grid[r][c] != " ":
                    separator[c] = False
                    break

        # compute the ranges that contain non-separators
        spans = []
        c = 0
        while c < W:
            while c < W and separator[c] == True:
                c += 1
            if c == W:
                break
            start = c
            while c < W and separator[c] == False:
                c += 1
            end = c
            spans.append((start, end))

        # for each span, extract continguous digits from a string (ignoring spaces)
        problems = []
        for start, end in spans:  # loop through the ranges in spans
            chunk_rows = [
                row[start:end] for row in grid
            ]  # build an array taking slice of each range of non-separactor chunks in each row of the grid

            op_row = chunk_rows[
                -1
            ]  # extract the operator character from the last row (no spaces)
            op = op_row.strip()

            nums = []  # loop through each of these chunk rows except for the last row to extract out the list of problem numbers (without the operator)
            for row in chunk_rows[0:-1]:
                token = row.strip()
                if token:
                    nums.append(int(token))

            problems.append((nums, op))

        return problems

    def part1(self):
        """Solve part 1."""
        problem_sets = self.data
        total = 0

        for nums, op in problem_sets:
            if op == "+":
                total += sum(nums)
            elif op == "*":
                total += math.prod(nums)
            else:
                raise ValueError(f"Unknown operator: {op}")

        return total

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
