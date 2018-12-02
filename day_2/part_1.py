"""Get the checksum of the list of IDs."""
from collections import Counter


def main():
    """Gets the checksum of the input IDs."""
    counters = []
    with open("day_2/input.txt") as file:
        file_input = file.readlines()

        for input_ in iter(file_input):
            counter = Counter(x for x in input_ if x != "\n")
            counters.append(counter)
    two_three = Counter({2: 0, 3: 0})
    step_has_acct = {}
    for i, counter in enumerate(counters):
        for value in counter:
            count = counter[value]
            has_2 = "{0}_2".format(i)
            has_3 = "{0}_3".format(i)
            if count == 2 and not step_has_acct.get(has_2, None):
                two_three[2] += 1
                step_has_acct[has_2] = True
            if count == 3 and not step_has_acct.get(has_3, None):
                two_three[3] += 1
                step_has_acct[has_3] = True

    checksum = two_three[2] * two_three[3]
    print(checksum)


if __name__ == "__main__":
    main()
