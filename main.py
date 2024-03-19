print("hello world")


def main():
    with open("books/frankenstein.txt") as file:
        res = file.read()
        print(res)


main()
