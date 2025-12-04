"""
Advent of Code 2025 - Day 2
"""

from pathlib import Path
from aoc_template import BaseSolution
import re


def is_invalid_id_part1(str_id: str) -> bool:
    id_length = len(str_id)
    if id_length % 2 != 0:
        return False
    mid = id_length // 2
    return str_id[:mid] == str_id[mid:]


def is_invalid_id_part2(str_id: str) -> bool:
    pattern = r"^(\d+)\1+$"
    if re.match(pattern, str_id):
        return True
    return False


class Solution(BaseSolution):
    """Solution for Day 2."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        ranges = input_text.strip().split(",")
        return [
            (int(start), int(end)) for start, end in (r.split("-") for r in ranges if r)
        ]

    def part1(self):
        """Solve part 1."""
        product_ids = self.data
        sum = 0

        for start, end in product_ids:
            for product_id in range(start, end + 1):
                str_id = str(product_id)
                if is_invalid_id_part1(str_id):
                    sum += int(str_id)

        return sum

    def part2(self):
        """Solve part 2."""
        product_ids = self.data
        sum = 0

        for start, end in product_ids:
            for product_id in range(start, end + 1):
                str_id = str(product_id)
                if is_invalid_id_part2(str_id):
                    sum += int(str_id)

        return sum


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
