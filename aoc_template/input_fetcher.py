import os
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()


def fetch_input(year: int, day: int, session_cookie: str | None = None) -> str:
    """
    Fetch input from Advent of Code website.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)
        session_cookie: AoC session cookie (can also be set via AOC_SESSION env var)

    Returns:
        Raw input text from the puzzle

    Raises:
        ValueError: If session cookie is not provided
        requests.HTTPError: If request fails
    """
    session = session_cookie or os.getenv("AOC_SESSION")
    if not session:
        raise ValueError(
            "Session cookie required. Set AOC_SESSION environment variable "
            "or pass session_cookie parameter"
        )

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": session}

    response = requests.get(url, cookies=cookies, timeout=10)
    response.raise_for_status()

    return response.text


def load_input(year: int, day: int, cache_dir: Path | None = None) -> str:
    """
    Load input, fetching from web if not cached locally.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)
        cache_dir: Directory to cache inputs (defaults to ./inputs)

    Returns:
        Raw input text from the puzzle
    """
    if cache_dir is None:
        cache_dir = Path("inputs")

    cache_dir.mkdir(exist_ok=True)
    cache_file = cache_dir / f"{year}_day{day:02d}.txt"

    if cache_file.exists():
        return cache_file.read_text()

    input_text = fetch_input(year, day)
    cache_file.write_text(input_text)

    return input_text
