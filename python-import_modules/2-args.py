#!/usr/bin/python3
if __name__ == "__main__":
    def args(argc, argv):
        if argc == 1:
            print("O arguments.")
        elif argc == 2:
            print("1 argument:")
        else:
            print("{} arguments".format(argc - 1))
            
        for n in range(1, argc):
            print(f"{n}: {argv[n]}")
