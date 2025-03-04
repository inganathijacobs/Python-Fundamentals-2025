# import f1  ## runs everything in f1 (entire file) (runs first)
from f1 import add


def main():
    print("Hello, from f2")
    #
    print(add(10, 100))


if __name__ == "__main__":
    main()


## Summary
# 1. Import entire file
# 2. Import only the required function or values (Preferred)
