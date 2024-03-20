print("hello world")


def main():
    frankensteinPath = "books/frankenstein.txt"
    res = readBook(frankensteinPath)
    wordsCount = countWords(res)
    print(f"Frankenstein book has {wordsCount} words")
    letterCount = getLetterCount(res)
    lettersCountList = lettersDictToList(letterCount)
    lettersCountList.sort(reverse=True, key=sortLettersOn)
    print(f"letters sorted {lettersCountList}") 
    


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


def lettersDictToList(dict = {}):
    lettersList = []
    lettersKeys = dict.keys()
    for letter in lettersKeys:
        if(letter.isalpha()):
            letterObj = {letter: letter, "count": dict[letter]}
            lettersList.append(letterObj)
    
    return lettersList


def sortLettersOn(dict):
    return dict["count"]

main()
