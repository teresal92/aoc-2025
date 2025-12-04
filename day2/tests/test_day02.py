"""Tests for Day 2 solution."""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import solution
sys.path.insert(0, str(Path(__file__).parent.parent / "solution"))
from day02 import Solution, is_invalid_id_part1, is_invalid_id_part2


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
    expected = [
        (11, 22),
        (95, 115),
        (998, 1012),
        (1188511880, 1188511890),
        (222220, 222224),
        (1698522, 1698528),
        (446443, 446449),
        (38593856, 38593862),
        (565653, 565659),
        (824824821, 824824827),
        (2121212118, 2121212124),
    ]
    assert solution.parse_input(example_input) == expected


def test_part1(solution):
    """Test part 1 solution."""
    expected = 1227775554
    assert solution.part1() == expected


def test_part2(solution):
    """Test part 2 solution."""
    expected = 4174379265
    assert solution.part2() == expected


def test_is_invalid_id_1_success():
    expected = True
    assert is_invalid_id_part1("99") == expected


def test_is_invalid_id_1_false():
    expected = False
    assert is_invalid_id_part1("995") == expected


def test_is_invalid_id_2_success():
    expected = True
    assert is_invalid_id_part2("131313") == expected


def test_is_invalid_id_2_false():
    expected = False
    assert is_invalid_id_part2("112") == expected
