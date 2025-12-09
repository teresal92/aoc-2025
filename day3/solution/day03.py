"""
Advent of Code 2025 - Day 3
"""

from pathlib import Path
from aoc_template import BaseSolution, parse_lines


def best_k_subsequence(digits, k=12):
    n = len(digits)
    result = []
    start = 0
    remaining_to_pick = k

    while remaining_to_pick > 0:
        last_start_index = n - remaining_to_pick
        max_digit = -1
        max_pos = -1

        for i in range(start, last_start_index + 1):
            if digits[i] > max_digit:
                max_digit = digits[i]
                max_pos = i

        result.append(
            str(max_digit)
        )  # convert to str so we can use join later on the result

        start = max_pos + 1

        remaining_to_pick -= 1
    return result


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
        total = 0
        banks = self.data
        for bank in banks:
            # convert line to list of digits
            string_digits = list(bank)
            digits = list(map(int, string_digits))

            # Get the best 12-digit subsequence
            best_digits = best_k_subsequence(digits, k=12)

            # convert to integer and add to total
            best_value = int("".join(best_digits))
            total += best_value

        return total


if __name__ == "__main__":
    solution = Solution.from_file(Path(__file__).parent / "input.txt")
    solution.display_description()
    print(f"Part 1: {solution.part1()}")
    print(f"Part 2: {solution.part2()}")
