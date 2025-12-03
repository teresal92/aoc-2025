# Advent of Code 2025 - Python Template

Welcome to Brian's Advent of Code 2025!

## Goals

- Consistent coding
- Mastery of pythonic python
- Template for other AOC coders looking to understand Python
- Fun

## Ethos

- Try not to use AI for the AOC problems itself
- AI can be used for template updates and other boilerplate items
- Code should be readable and Pythonic when possible. That means using libraries when possible
- Performance comes after being right

## Features

This template automates common Advent of Code boilerplate:

- **Automatic input fetching** from adventofcode.com with local caching
- **Base solution class** with standardized structure
- **Parsing utilities** for common input formats
- **Pytest integration** with test templates
- **CLI tool** for generating new day solutions
- **Modern Python tooling** with `uv` for fast dependency management

## Quick Start

### 1. Install dependencies

```bash
# Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install project dependencies
uv sync
```

### 2. Set up your session cookie

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your session cookie
# Get it from: Browser DevTools > Application > Cookies > session
```

To get your session cookie:

1. Log in to [adventofcode.com](https://adventofcode.com)
2. Open browser DevTools (F12)
3. Go to Application/Storage tab > Cookies
4. Copy the value of the `session` cookie
5. Paste it in `.env` file

### 3. Create a new day solution

```bash
# Generate files for day 1
uv run aoc create 1

# Or for a specific year
uv run aoc create 5 --year 2024
```

This creates:

- `dayX/solution/dayXX.py` - Solution template
- `dayX/tests/test_dayXX.py` - Test template

### 4. Implement your solution

Edit `dayX/solution/dayXX.py`:

```python
from aoc_template import BaseSolution, parse_lines

class Solution(BaseSolution):
    def parse_input(self, input_text: str):
        # Parse your input
        return parse_lines(input_text)

    def part1(self):
        # Solve part 1
        return sum(len(line) for line in self.data)

    def part2(self):
        # Solve part 2
        return len(self.data)
```

### 5. Write tests

Edit `dayX/tests/test_dayXX.py` with the example input from the puzzle:

```python
@pytest.fixture
def example_input():
    return """paste
example
input
here"""

def test_part1(solution):
    assert solution.part1() == expected_value
```

### 6. Run tests

```bash
# Run tests for a specific day
uv run pytest day1/tests/test_day01.py

# Run all tests
uv run pytest

# Run with verbose output
uv run pytest -v
```

### 7. Run your solution

```bash
# Run directly (will fetch/cache input automatically)
uv run python day1/solution/day01.py
```

## Available Utilities

### Input Fetching

```python
from aoc_template import load_input, fetch_input

# Load with caching (recommended)
input_text = load_input(year=2025, day=1)

# Fetch directly from web
input_text = fetch_input(year=2025, day=1)
```

### Parsing Helpers

```python
from aoc_template import parse_lines, parse_ints, parse_grid, parse_blocks
from aoc_template.utils import manhattan_distance, neighbors_4, neighbors_8

# Parse into lines
lines = parse_lines(input_text)

# Extract all integers from text
numbers = parse_ints("abc 123 def -456")  # [123, -456]

# Parse 2D grid
grid = parse_grid(input_text)
grid_of_ints = parse_grid(input_text, transform=int)

# Split on blank lines
blocks = parse_blocks(input_text)

# Grid utilities
dist = manhattan_distance((0, 0), (3, 4))  # 7
adjacent = neighbors_4(x, y)  # 4 directions
all_neighbors = neighbors_8(x, y)  # 8 directions
```

### Base Solution Class

```python
from aoc_template import BaseSolution

class Solution(BaseSolution):
    def parse_input(self, input_text: str):
        # Required: Parse input into self.data
        return parse_lines(input_text)

    def part1(self):
        # Required: Return part 1 answer
        pass

    def part2(self):
        # Required: Return part 2 answer
        pass

# Usage
solution = Solution(input_text)
part1_answer = solution.part1()
part2_answer = solution.part2()
both = solution.solve()  # Returns (part1, part2)

# Load from file
solution = Solution.from_file("inputs/2025_day01.txt")
```

## Project Structure

```
.
├── aoc_template/          # Core utilities
│   ├── __init__.py
│   ├── base_solution.py   # BaseSolution class
│   ├── cli.py             # CLI tool
│   ├── input_fetcher.py   # Input fetching/caching
│   └── utils.py           # Parsing utilities
├── day1/                  # Day 1 directory
│   ├── solution/          # Solution files
│   │   └── day01.py
│   └── tests/             # Test files
│       └── test_day01.py
├── day2/                  # Day 2 directory
│   ├── solution/
│   │   └── day02.py
│   └── tests/
│       └── test_day02.py
├── inputs/                # Cached inputs (gitignored)
├── pyproject.toml         # Project config
├── .env                   # Session cookie (gitignored)
└── README.md
```

## Tips

- **Start with tests**: Add the example input to your test file first
- **Incremental development**: Get part 1 working before starting part 2
- **Use the utilities**: Check `aoc_template/utils.py` for helpful functions
- **Keep it simple**: Don't over-engineer, focus on correctness first
- **Cache is your friend**: Inputs are automatically cached in `inputs/`

## CLI Commands

```bash
# Create new day
uv run aoc create <day> [--year YEAR] [--force]

# Examples
uv run aoc create 1              # Create day 1 for 2025
uv run aoc create 5 --year 2024  # Create day 5 for 2024
uv run aoc create 1 --force      # Overwrite existing files
```

## Commit & Branching Guidelines

To keep this repo consistent and easy to review, each Advent of Code day follows a predictable commit pattern:

1. `chore(dayXX): add input + scaffold`
2. `feat(dayXX): implement parser`
3. `feat(dayXX): solve part 1`
4. `feat(dayXX): solve part 2`
5. `refactor(dayXX): clean helpers`
6. (optional) `test(dayXX): add edge-case tests`

Branches follow the naming pattern:
`aoc-2025-dayXX[-partX]`.

Happy coding!
