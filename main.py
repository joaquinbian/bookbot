print("hello world")


def main():
    frankensteinPath = "books/frankenstein.txt"
    res = readBook(frankensteinPath)
    wordsCount = countWords(res)
    print(f"Frankenstein book has {wordsCount} words")
    letterCount = getLetterCount(res)
    print(f"letters count in frankenstein {letterCount}")
    


def readBook(path):
        with open(path) as file:
            res = file.read()
            return res


def countWords(text = " "):
    textArr = text.split()
    textLen = len(textArr)
    return textLen


def getLetterCount(text = ""):
    lettersCount = {}
    for i in range(len(text)):
        letter = text[i].lower()
        if(letter in lettersCount):
            lettersCount[letter] += 1 
        else:
            lettersCount[letter] = 1
    
    return lettersCount


main()
