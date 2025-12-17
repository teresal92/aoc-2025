"""Tests for Day 4 solution."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day04 import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution, example_input):
    """Test input parsing."""
    expected = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]
    assert solution.parse_input(example_input) == expected


def test_part1(solution):
    """Test part 1 solution."""
    expected = 13
    assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    expected = 43
    assert solution.part2() == expected
