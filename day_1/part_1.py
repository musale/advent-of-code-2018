"""Day 1: Chronal Calibration."""


def main():
    """Read the input file and get the sum of the values."""
    frequency = 0
    with open("day_1/input.txt", "r") as file:
        for line in iter(file.readline, ''):
            frequency = frequency + int(line)
    print(frequency)

if __name__ == "__main__":
    main()
