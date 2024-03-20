
def main():
    print("--- Begin report of books/frankenstein.txt ---\n")
    frankensteinPath = "books/frankenstein.txt"
    res = readBook(frankensteinPath)
    wordsCount = countWords(res)
    print(f"{wordsCount} words was found in the Frankenstein document!\n")
    characterCount = getCharacterCount(res)
    charactersCountList = charactersDictToList(characterCount)
    charactersCountList.sort(reverse=True, key=sortCharactersOn)

    for character in charactersCountList:
        print(f"character {character["letter"]} was found {character["count"]} times")    
    


def readBook(path):
        with open(path) as file:
            res = file.read()
            return res


def countWords(text = " "):
    textArr = text.split()
    textLen = len(textArr)
    return textLen


def getCharacterCount(text = ""):
    characterCount = {}
    for i in range(len(text)):
        character = text[i].lower()
        if(character in characterCount):
            characterCount[character] += 1 
        else:
            characterCount[character] = 1
    
    return characterCount


def charactersDictToList(dict = {}):
    charDictList = []
    charsList = dict.keys()
    for character in charsList:
        if(character.isalpha()):
            charObj = {"letter": character, "count": dict[character]}
            charDictList.append(charObj)
    
    return charDictList


def sortCharactersOn(dict):
    return dict["count"]
    #return dict["character"]
    #lo de arriba haria que se ordenen en orden alfabetico
    #esta funcion, para el key de sort, devuelve una key para
    #que sort use sus valores en el obj. para ordenar la lista


main()
