"""Get the ID of claims that do not overlap."""
import re
from collections import Counter

PATTERN = r"#(\d+)\s+@\s+(\d+),(\d+):\s+(\d+)x(\d+)"


def main():
    """Calculate which ID does not overlap given a list."""
    with open("day_3/input.txt") as file:
        claims = file.readlines()
    claimed = Counter()
    points = {}
    claim_ids = set({})
    for claim in iter(claims):
        match = re.match(PATTERN, claim)
        claim_id, left, top, width, height = (int(x) for x in match.groups())
        claim_ids.add(claim_id)
        claimed += create_claim(left, top, width, height)
        check_overlap(
            claim_id, left, top, (width, height), points, claim_ids)

    for _, ids_ in points.items():
        if len(ids_) > 1:
            for id_ in ids_:
                if id_ in claim_ids:
                    claim_ids.remove(id_)

    no_overlap = claim_ids.pop()
    print(no_overlap)


def create_claim(left, top, width, height):
    """Create a claim as it would appear on the fabric."""
    claimed = Counter()
    for i in range(width):
        for j in range(height):
            claim = (i+left, j+top)
            claimed[claim] += 1
    return claimed


def check_overlap(claim_id, left, top, dimensions, points, claim_ids):
    """Create a claim as it would appear on the fabric."""
    width, height = dimensions
    for i in range(width):
        removed = False
        for j in range(height):
            claim = (i+left, j+top)
            if claim not in points:
                points[claim] = [claim_id]
            else:
                points[claim].append(claim_id)
                if not removed:
                    for id2_ in points[claim]:
                        if id2_ in claim_ids:
                            claim_ids.remove(id2_)
                    removed = True


if __name__ == "__main__":
    main()
