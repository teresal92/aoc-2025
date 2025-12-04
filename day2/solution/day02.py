"""
Advent of Code 2025 - Day 2
"""

from pathlib import Path
from aoc_template import BaseSolution
import math


def is_invalid_id(str_id: str) -> bool:
    id_length = len(str_id)
    # if len of str_id is odd do nothing so lets check for even len so we can apply some additional checks
    if id_length % 2 != 0:
        return False
    # calculate the mid index of the str_id
    mid = id_length // 2
    return str_id[:mid] == str_id[mid:]


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
        invalid_ids = []

        for start, end in product_ids:
            # go through each option in the range start to end (inclusive)
            for product_id in range(start, end + 1):
                # convert each option to str so we can do some str ops
                str_id = str(product_id)
                if is_invalid_id(str_id):
                    # convert back to int before appending to invalid_ids list
                    invalid_ids.append(int(str_id))

        # return the sum of all the product_ids in the list
        return sum(invalid_id for invalid_id in invalid_ids)

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
