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

            if op == "+":
                total += sum(nums)
            elif op == "*":
                total += math.prod(nums)
            else:
                raise ValueError(f"Unknown operator: {op}")

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

            if op == "+":
                total += sum(nums)
            elif op == "*":
                total += math.prod(nums)
            else:
                raise ValueError(f"Unknown operator: {op}")

        return total


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")


#   0       1      2              0      1      2       3
# 0 ['123', ' 45', '  6']    0 ["123", "328", " 51", "64 "]
# 1 ['328', '64 ', '98 ']    1 [" 45", "64 ", "387", "23 "]
# 2 [' 51', '387', '215']    2 ["  6", "98 ", "215", "314"]
# 3 ['64 ', '23 ', '314']                             012


# flip the rows and columns

# 0, 0 -> '123' 0, 0 -> '123'
# 0, 1 -> ' 45' 1, 0 -> ' 45'
# 0, 2 -> '  6' 2, 0 -> '  6'
# 1, 0 "328" -> 0, 1


# R2,C3,W2 => "4"
# R1,C3,W2 => ""
# R0,C3,W2 => ""

# R2,C2,W2 => "1"
# ...
