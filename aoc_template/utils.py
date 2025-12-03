import re
from typing import Callable


def parse_lines(text: str, strip: bool = True) -> list[str]:
    """
    Parse input into lines.

    Args:
        text: Raw input text
        strip: Whether to strip whitespace from each line

    Returns:
        List of lines
    """
    lines = text.strip().split("\n")
    return [line.strip() if strip else line for line in lines]


def parse_ints(text: str) -> list[int]:
    """
    Extract all integers from text.

    Args:
        text: Text containing integers

    Returns:
        List of integers found in text
    """
    return [int(x) for x in re.findall(r"-?\d+", text)]


def parse_grid(text: str, transform: Callable[[str], any] = None) -> list[list]:
    """
    Parse input into a 2D grid.

    Args:
        text: Raw input text with rows on separate lines
        transform: Optional function to transform each cell

    Returns:
        2D list representing the grid
    """
    lines = parse_lines(text)
    if transform:
        return [[transform(char) for char in line] for line in lines]
    return [list(line) for line in lines]


def parse_blocks(text: str, strip: bool = True) -> list[str]:
    """
    Parse input into blocks separated by blank lines.

    Args:
        text: Raw input text
        strip: Whether to strip whitespace from each block

    Returns:
        List of text blocks
    """
    blocks = text.strip().split("\n\n")
    return [block.strip() if strip else block for block in blocks]


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """
    Calculate Manhattan distance between two points.

    Args:
        p1: First point (x, y)
        p2: Second point (x, y)

    Returns:
        Manhattan distance
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def neighbors_4(x: int, y: int) -> list[tuple[int, int]]:
    """
    Get 4-directional neighbors (up, down, left, right).

    Args:
        x: X coordinate
        y: Y coordinate

    Returns:
        List of neighbor coordinates
    """
    return [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]


def neighbors_8(x: int, y: int) -> list[tuple[int, int]]:
    """
    Get 8-directional neighbors (including diagonals).

    Args:
        x: X coordinate
        y: Y coordinate

    Returns:
        List of neighbor coordinates
    """
    return [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
