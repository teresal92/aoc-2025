"""
Advent of Code 2025 - Day 1
"""

import math
from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 1."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)

    def part1(self):
        """Solve part 1."""
        combos = self.data
        count = 0
        position = 50

        for combo in combos:
            direction = combo[0]
            distance = int(combo[1:])

            if direction == "L":
                position = position - distance
                while position < 0:
                    position = 100 + position
            else:
                position = position + distance
                while position >= 100:
                    if position == 100:
                        position = 0
                    else:
                        position = position - 100
            if position == 0:
                count += 1

        return count

    def part2(self):
        """Solve part 2."""
        combos = self.data
        count = 0
        position = 50

        for combo in combos:
            direction = combo[0]
            distance = int(combo[1:])

            start = position
            if direction == "L":
                end = start - distance
                hits = math.ceil(start / 100) - math.ceil(end / 100)

            else:
                end = start + distance
                hits = math.floor(end / 100) - math.floor(start / 100)

            count += hits
            position = end % 100
        return count


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
