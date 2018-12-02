"""Get the common letters between two correct IDs."""


def main():
    """Check for the common letters and remove them."""
    with open("day_2/input.txt") as file:
        file_input = file.readlines()

        for i, word in enumerate(iter(file_input)):
            for next_word in iter(file_input[i+1:]):
                common_word, ok = compare(word, next_word)
                if ok:
                    print(common_word)


def compare(word, next_word):
    """Compares 2 words and returns the word with 1 different character."""
    idx = -1
    if len(word) != len(next_word):
        return "", False

    for i, _ in enumerate(word):
        if word[i] == next_word[i]:
            continue

        if idx >= 0:
            return "", False
        idx = i

    return word[:idx] + word[idx+1:], True


if __name__ == "__main__":
    main()
