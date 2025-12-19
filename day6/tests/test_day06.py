"""Tests for Day 6 solution."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day06 import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """123 328  51 64
 45 64  387 23
  6 98  215 314
*   +   *   +  """


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    assert solution.data == [
        ([123, 45, 6], "*"),
        ([328, 64, 98], "+"),
        ([51, 387, 215], "*"),
        ([64, 23, 314], "+"),
    ]


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
