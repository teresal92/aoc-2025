"""Tests for Day 2 solution."""
import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day02 import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution, example_input):
    """Test input parsing."""
    expected = ["11-22","95-115","998-1012","1188511880-1188511890","222220-222224","1698522-1698528","446443-446449","38593856-38593862","565653-565659","824824821-824824827","2121212118-2121212124"]
    assert solution.parse_input(example_input) == expected


def test_part1(solution):
    """Test part 1 solution."""
    # TODO: Add part 1 tests
    expected = None  # Replace with expected value
    # assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    # TODO: Add part 2 tests
    expected = None  # Replace with expected value
    # assert solution.part2() == expected
