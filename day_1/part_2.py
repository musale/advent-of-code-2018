"""First frequency reached twice first."""
from collections import Counter


def main():
    """Returns the first frequency reached twice first."""
    frequency = 0
    counter = Counter()
    found = False

    with open("day_1/input.txt", "r") as file:
        file_input = file.readlines()
        while not found:
            for line in iter(file_input):
                frequency = frequency + int(line)
                counter[frequency] += 1
                if counter[frequency] > 1:
                    print(frequency)
                    found = True
                    break


if __name__ == "__main__":
    main()
