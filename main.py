print("hello world")


def main():
    frankensteinPath = "books/frankenstein.txt"
    res = readBook(frankensteinPath)
    wordsCount = countWords(res)
    print("Frankenstein has ", wordsCount," words")
    


def readBook(path):
        with open(path) as file:
            res = file.read()
            return res


def countWords(text = " "):
    textArr = text.split()
    textLen = len(textArr)
    return textLen


main()
