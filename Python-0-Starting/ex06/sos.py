import sys

NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
}


def validInput(text: str) -> bool:
    return all(char.isalpha() and char != ' ' for char in text)


def getMORSEstr(text: str) -> str:
    return "".join(NESTED_MORSE[char.upper()] for char in text)


def main():
    argv = sys.argv
    argc = len(argv)

    if argc != 2 or not validInput(argv[1]):
        print("Assertion Error: the arguments are bad")
        exit(1)
    print(getMORSEstr(argv[1]))
    return 0


if __name__ == "__main__":
    main()
