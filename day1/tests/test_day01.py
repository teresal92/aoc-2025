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
    return """
        L68
        L30
        R48
        L5
        R60
        L55
        L1
        L99
        R14
        L82
    """


@pytest.fixture
def solution(example_input):
    """Create solution instance with example input."""
    return Solution(example_input)


def test_parse_input(solution):
    """Test input parsing."""
    assert len(solution.data) == 10
    assert solution.data[0] == "L68"


def test_part1(solution):
    """Test part 1 solution."""
    assert solution.part1() == 3


def test_part2(solution):
    """Test part 2 solution."""
    assert solution.part2() == 6


def test_solve(solution):
    """Test solving both parts."""
    part1, part2 = solution.solve()
    assert part1 == 3
    assert part2 == 6
