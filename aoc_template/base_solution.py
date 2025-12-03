from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseSolution(ABC):
    """Base class for Advent of Code solutions."""

    def __init__(self, input_text: str, description_path: Path | str | None = None):
        """
        Initialize solution with input text.

        Args:
            input_text: Raw input text from puzzle
            description_path: Optional path to description.txt file
        """
        self.input_text = input_text.strip()
        self.data = self.parse_input(input_text)
        self.description_path = Path(description_path) if description_path else None
        self._description = None

    @abstractmethod
    def parse_input(self, input_text: str) -> Any:
        """
        Parse raw input text into a usable format.

        Args:
            input_text: Raw input text

        Returns:
            Parsed data structure
        """
        pass

    @abstractmethod
    def part1(self) -> Any:
        """
        Solve part 1 of the puzzle.

        Returns:
            Solution to part 1
        """
        pass

    @abstractmethod
    def part2(self) -> Any:
        """
        Solve part 2 of the puzzle.

        Returns:
            Solution to part 2
        """
        pass

    def solve(self) -> tuple[Any, Any]:
        """
        Solve both parts of the puzzle.

        Returns:
            Tuple of (part1_answer, part2_answer)
        """
        return self.part1(), self.part2()

    @property
    def description(self) -> str | None:
        """
        Load and return the problem description.

        Returns:
            Problem description text or None if not available
        """
        if self._description is None and self.description_path:
            try:
                self._description = self.description_path.read_text()
            except FileNotFoundError:
                return None
        return self._description

    def display_description(self) -> None:
        """Display the problem description in a clean format."""
        if not self.description:
            print("No description available.")
            return

        print(self.description)
        print()

    @classmethod
    def from_file(
        cls, filepath: str | Path, description_path: str | Path | None = None
    ) -> "BaseSolution":
        """
        Create solution instance from input file.

        Args:
            filepath: Path to input file
            description_path: Optional path to description.txt file

        Returns:
            Solution instance
        """
        input_path = Path(filepath)

        # Auto-detect description.txt if not provided
        if description_path is None:
            # Look for description.txt in parent directory of input file
            # (assumes structure like day1/solution/input.txt and day1/description.txt)
            potential_desc = input_path.parent.parent / "description.txt"
            if potential_desc.exists():
                description_path = potential_desc

        return cls(input_path.read_text(), description_path)
