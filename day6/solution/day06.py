"""
Advent of Code 2025 - Day 6
"""

from dataclasses import dataclass
import math
from pathlib import Path
from aoc_template import BaseSolution


def apply_op(op: str, nums: list[int]) -> int:
    return sum(nums) if op == "+" else math.prod(nums)


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

        problems = []
        for start, end in spans:  # loop through the ranges in spans
            chunk_rows = [row[start:end] for row in grid]

            op_row = chunk_rows[-1]
            ops = [ch for ch in op_row if ch in "+*"]
            if len(ops) != 1:
                raise ValueError(f"Expected exactly one operator, got {ops}")
            op = ops[0]

            number_rows = chunk_rows[:-1]

            problems.append((number_rows, op))

        return problems

    def part1(self):
        """Solve part 1."""
        problem_sets = self.data
        total = 0

        for numbers_row, op in problem_sets:
            nums = []
            # remove white spaces from digits and convert from str to int
            for row in numbers_row:
                token = row.strip()
                if token:
                    nums.append(int(token))
            total += apply_op(op, nums)

        return total

    def part2(self):
        """Solve part 2."""
        problem_sets = self.data
        total = 0

        for number_rows, op in problem_sets:
            H = len(number_rows)
            W = len(number_rows[0]) if H else 0  # of columns

            nums = []

            # scan right-to-left
            for c in range(W - 1, -1, -1):
                digits = []
                # read top-to-bottom within the column
                for r in range(H):
                    ch = number_rows[r][c]
                    if ch.isdigit():
                        digits.append(ch)

                if digits:
                    s = "".join(digits).strip()
                    nums.append(int(s))

            total += apply_op(op, nums)

        return total


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
