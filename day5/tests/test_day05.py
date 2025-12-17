"""Tests for Day 5 solution."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day05 import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """3-5
10-14
16-20
12-18

1
5
8
11
17
32
    """


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution, example_input):
    """Test input parsing."""
    expected = ([[3, 5], [10, 14], [16, 20], [12, 18]], [1, 5, 8, 11, 17, 32])
    assert solution.parse_input(example_input) == expected


def test_part1(solution):
    """Test part 1 solution."""
    expected = 3
    assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    # TODO: Add part 2 tests
    expected = None  # Replace with expected value
    # assert solution.part2() == expected
