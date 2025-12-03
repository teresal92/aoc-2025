"""
Advent of Code 2025 - Day 2
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 2."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        ranges = input_text.strip().split(",")
        return [ (int(start), int(end)) for start, end in (r.split("-") for r in ranges if r)]

    def part1(self):
        """Solve part 1."""



        # loop through list of strings ranges
          # parse each range by splitting


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
