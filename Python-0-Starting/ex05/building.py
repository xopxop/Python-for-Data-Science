import sys
import string


def result(text: str) -> str:
    strlen = len(text)
    uppercaseCount = sum(1 for char in text if char.isupper())
    lowercaseCount = sum(1 for char in text if char.islower())
    punctuationCount = sum(1 for char in text if char in string.punctuation)
    digitCount = sum(1 for char in text if char.isdigit())
    spaceCount = sum(1 for char in text if char.isspace())

    return (
        f"The text contains {strlen} characters:\n"
        f"{uppercaseCount } uppercase letters\n"
        f"{lowercaseCount} lowercase letters\n"
        f"{punctuationCount} punctuation marks\n"
        f"{spaceCount} spaces\n"
        f"{digitCount} digits"
            )


def main():
    argv = sys.argv
    argc = len(argv)

    if argc == 1:
        print("What is the text to count?")
        text = sys.stdin.read()
    elif argc == 2:
        text = sys.argv[1]
    else:
        print("Assertion Error: more than one argument is provided")
        exit(1)
    print(result(text))
    exit(0)


if __name__ == "__main__":
    main()
