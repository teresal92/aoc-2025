"""
Advent of Code 2025 - Day 2
"""
from pathlib import Path
from aoc_template import BaseSolution, parse_lines


class Solution(BaseSolution):
    """Solution for Day 2."""

    def parse_input(self, input_text: str):
        """Parse the input."""
        return parse_lines(input_text)[0].split(',')

    def part1(self):
        """Solve part 1."""
        total = 0
        for num_range in self.data:
            values = num_range.split('-')
            beg, end = int(values[0]), int(values[1])
            for i in range(beg, end + 1):
                num_str = str(i)
                str_len = len(num_str)
                midway = str_len // 2
                if str_len % 2 == 0 and num_str[0:midway] == num_str[midway:]:
                    total += i
        return total
                

    def part2(self):
        """Solve part 2."""
        total = 0
        added_nums = []
        for num_range in self.data:
            values = num_range.split('-')
            beg, end = int(values[0]), int(values[1])
            for i in range(beg, end + 1):
                num_str = str(i)
                str_len = len(num_str)
                midway = str_len // 2
                for j in range(1, midway + 1):
                   sequences = [num_str[k:k+j] for k in range(0, str_len, j)] 
                   if(len(set(sequences)) == 1 and i not in added_nums):
                       total += i
                       added_nums.append(i)
        return total
                



if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
