"""Tests for Day 2 solution."""
import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day02 import Solution


@pytest.fixture
def example_input():
    # """Example input for testing."""
    return """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    assert len(solution.data) == 11
    assert solution.data[0] == "11-22"


def test_part1(solution):
    """Test part 1 solution."""
    expected = 1227775554  
    actual = solution.part1()
    assert actual == expected


def test_part2(solution):
    """Test part 2 solution."""
    expected = 4174379265  
    actual = solution.part2()
    assert actual == expected
