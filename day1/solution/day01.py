"""
Advent of Code - Day 1 Example
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines 
import math


class Solution(BaseSolution):
    """Example solution for Day 1."""

    def parse_input(self, input_text: str) -> list[str]:
        """Parse input into lines."""
        return parse_lines(input_text)

    def part1(self) -> int:
        counter, dial, sign  = 0, 50, {'R': 1, 'L': -1}

        for line in self.data:
            direction, value  = line[0], int(line[1:])
            dial += sign[direction] * value
            dial %= 100 # #'s range 0-99 on lock
            counter += not dial
        return counter
                

    def part2(self) -> int:
        counter, dial, sign  = 0, 50, {'R': 1, 'L': -1}

        for line in self.data:
            direction, value = line[0], int(line[1:])
            new_dial = dial + sign[direction] * value

            # Count multiples of 100 in the range, excluding start position, including end position
            if new_dial > dial:
                # Moving right: count multiples in (dial, new_dial]
                counter += new_dial // 100 - dial // 100
            elif new_dial < dial:
                # Moving left: count multiples in [new_dial, dial)
                counter += math.ceil(dial / 100) - math.ceil(new_dial / 100)

            dial = new_dial % 100
        return counter


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / 'input.txt')
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
