"""Fetch and parse Advent of Code puzzle descriptions."""
import os
from pathlib import Path
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


def fetch_description_html(year: int, day: int, session_cookie: str | None = None) -> str:
    """
    Fetch the HTML content of the puzzle page.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)
        session_cookie: AoC session cookie (optional, but required for personalized content)

    Returns:
        Raw HTML content of the puzzle page

    Raises:
        requests.HTTPError: If request fails
    """
    url = f"https://adventofcode.com/{year}/day/{day}"

    # Session cookie is optional for fetching description, but recommended
    cookies = {}
    session = session_cookie or os.getenv("AOC_SESSION")
    if session:
        cookies = {"session": session}

    response = requests.get(url, cookies=cookies, timeout=10)
    response.raise_for_status()

    return response.text


def parse_description(html_content: str) -> str:
    """
    Parse the puzzle description from HTML content.

    Args:
        html_content: Raw HTML content of the puzzle page

    Returns:
        Formatted text description of the puzzle
    """
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main article elements (puzzle description)
    articles = soup.find_all('article', class_='day-desc')

    if not articles:
        return "No puzzle description found."

    description_parts = []

    for article in articles:
        # Extract the title (h2)
        title = article.find('h2')
        if title:
            description_parts.append(title.get_text().strip())
            description_parts.append("=" * 60)

        # Extract all paragraphs and code blocks
        for element in article.children:
            if element.name == 'p':
                text = element.get_text().strip()
                if text:
                    description_parts.append(text)
                    description_parts.append("")  # Add blank line after paragraph

            elif element.name == 'pre':
                # Code blocks
                code = element.get_text().strip()
                if code:
                    description_parts.append("```")
                    description_parts.append(code)
                    description_parts.append("```")
                    description_parts.append("")

            elif element.name in ['ul', 'ol']:
                # Lists
                for li in element.find_all('li'):
                    text = li.get_text().strip()
                    if text:
                        description_parts.append(f"  - {text}")
                description_parts.append("")

        description_parts.append("\n" + "-" * 60 + "\n")

    return "\n".join(description_parts)


def save_description(year: int, day: int, output_path: Path | None = None) -> Path:
    """
    Fetch puzzle description and save it to a file.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)
        output_path: Path to save the description (defaults to day{day}/description.txt)

    Returns:
        Path to the saved description file
    """
    if output_path is None:
        day_dir = Path(f"day{day}")
        day_dir.mkdir(exist_ok=True)
        output_path = day_dir / "description.txt"

    # Fetch and parse
    html_content = fetch_description_html(year, day)
    description = parse_description(html_content)

    # Save to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(description)

    return output_path


def fetch_and_display(year: int, day: int) -> str:
    """
    Fetch and return the puzzle description without saving.

    Args:
        year: Year of the puzzle
        day: Day of the puzzle (1-25)

    Returns:
        Formatted text description of the puzzle
    """
    html_content = fetch_description_html(year, day)
    return parse_description(html_content)
