import sys

argv = sys.argv
argc = len(argv)

if argc > 1:
    if (argc == 2):
        if argv[1].isnumeric():
            numbr = int(argv[1])
            if (numbr % 2) == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        else:
            print("AssertionError: argument is not an integer")
            exit(1)
    else:
        print("AssertionError: more than one argument is provided")
        exit(1)

