"""
Advent of Code 2025 - Day 5
"""

from heapq import merge
from pathlib import Path
from aoc_template import BaseSolution, parse_blocks


def merge_ranges(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []

    for s, e in ranges:
        # start a new merged intervval of extend last one
        if not merged or s > merged[-1][1] + 1:
            merged.append((s, e))
        else:
            last_s, last_e = merged[-1]
            merged[-1] = (last_s, max(last_e, e))

    return merged


class Solution(BaseSolution):
    """Solution for Day 5."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        blocks = parse_blocks(input_text)

        ranges_block, nums_block = blocks

        # ranges = []

        # for line in ranges_block.splitlines(): # ["3-5", "10-14", "16-20", "12-18"]
        #     if not line.strip():
        #         continue # skip empty lines
        #     left, right = line.split("-")  # "3", "5"
        #     left = int(left)
        #     right = int(right)

        #     ranges.append([left, right])

        ranges = [
            tuple(map(int, line.split("-")))
            for line in ranges_block.splitlines()
            if line.strip()
        ]
        nums = [int(line) for line in nums_block.splitlines() if line.strip()]

        return (ranges, nums)

    def part1(self):
        """Solve part 1."""
        count = 0
        ranges, nums = self.data

        merged_ranges = merge_ranges(ranges)

        for num in nums:
            for start, end in merged_ranges:
                if start > num:
                    break
                if start <= num <= end:
                    count += 1
                    break

        return count

    def part2(self):
        """Solve part 2."""
        # TODO: Implement part 2
        pass


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
