import sys


def main():
    av = sys.argv
    ac = len(av)
    validInput = lambda arg1, arg2: (  # noqa: E731
        all(char.isalpha() or char == ' ' for char in arg1) and
        arg2.isnumeric()
    )
    filteredList = lambda text, maxlen: [  # noqa: E731
        word for word in text.split() if len(word) > maxlen
    ]

    if ac != 3 or not validInput(av[1], av[2]):
        print("Assertion Error: the arguments are bad")
        exit(1)
    print(filteredList(av[1], int(av[2])))
    return 0


if __name__ == "__main__":
    main()
