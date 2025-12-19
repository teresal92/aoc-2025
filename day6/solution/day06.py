"""
Advent of Code 2025 - Day 6
"""

from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 6."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        rows = input_text.splitlines()

        # normalized width of each row
        W = max(len(r) for r in rows)
        grid = [row.ljust(W, " ") for row in rows]

        separator = [True] * W
        for c in range(W):
            for r in range(len(grid)):
                if grid[r][c] != " ":
                    separator[c] = False
                    break

        # convert separators into problem column-spans
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
            end = c  # slice end (exclusive)
            spans.append((start, end))

        # for each span, slice out the rectangular chunks and extract tokens
        problems = []
        for start, end in spans:
            chunk_rows = [row[start:end] for row in grid]

            op_row = chunk_rows[-1]
            op = op_row.strip()

            nums = []
            for row in chunk_rows[0:-1]:
                token = row.strip()
                if token:
                    nums.append(int(token))

            problems.append((nums, op))

        return problems

    def part1(self):
        """Solve part 1."""
        # TODO: Implement part 1
        pass

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
