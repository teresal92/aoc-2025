"""Tests for Day 1 solution."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day01 import Solution


@pytest.fixture
def example_input():
    """Example input for testing."""
    return """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    expected = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    assert solution.parse_input(solution.input_text) == expected


def test_part1(solution):
    """Test part 1 solution."""
    expected = 3
    assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    expected = 6
    assert solution.part2() == expected
