"""
Advent of Code 2025 - Day 3
"""

from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 3."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)

    def part1(self):
        """Solve part 1."""
        total = 0
        banks = self.data
        for bank in banks:
            string_digits = list(bank)
            digits = list(map(int, string_digits))
            best_pair = None
            best_right_digit = digits[len(digits) - 1]

            for i in range(len(digits) - 2, -1, -1):
                candidate = 10 * digits[i] + best_right_digit
                if best_pair is None or candidate > best_pair:
                    best_pair = candidate

                best_right_digit = max(best_right_digit, digits[i])

            total += best_pair
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
