"""Get the number of claims that overlap."""
import re
from collections import Counter
PATTERN = r"#\d+\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)"


def main():
    """Calculate which claims overlap given a list."""
    with open("day_3/input.txt") as file:
        claims = file.readlines()
    claimed = Counter()
    overlap = 0
    for claim in iter(claims):
        match = re.match(PATTERN, claim)
        left, top, width, height = (int(x) for x in match.groups())
        claimed += create_claim(left, top, width, height)

    for claim in claimed:
        if claimed[claim] > 1:
            overlap += 1

    print(overlap)


def create_claim(left, top, width, height):
    """Create a claim as it would appear on the fabric."""
    claimed = Counter()
    for i in range(width):
        for j in range(height):
            claim = (i+left, j+top)
            claimed[claim] += 1
    return claimed


if __name__ == "__main__":
    main()
