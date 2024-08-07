def count_characters(inputString):
    dictionaryToBeReturned = {}
    for letter in inputString:
        if letter.lower() in dictionaryToBeReturned.keys():
            dictionaryToBeReturned[letter.lower()] = dictionaryToBeReturned[letter.lower()] + 1
        else:
            dictionaryToBeReturned[letter.lower()] = 1
    return dictionaryToBeReturned

def count_words(inputString):
    splitInputString = inputString.split()
    return len(splitInputString)


def main():
    book = open ("books/frankenstein.txt")
    file_content = book.read()
    book.close()

    print(count_characters(file_content))

if __name__ == "__main__":
    main()
