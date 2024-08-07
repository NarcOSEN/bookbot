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

def sorted_on_value(dict):
    return dict["count"]


def main():
    book = open ("books/frankenstein.txt")
    file_content = book.read()
    book.close()

    word_count_dictionary = count_characters(file_content)
    tiny_dict = {}
    list_of_dict = []
    for i in word_count_dictionary:
        if i.isalpha() is True:
            tiny_dict = {"character": i, "count": word_count_dictionary[i]}
            #print(tiny_dict)
            list_of_dict.append(tiny_dict)

    list_of_dict.sort(reverse=True, key = sorted_on_value)
    #print(list_of_dict)

    print(f"""--- Begin report of books/frankenstein.txt ---
            {count_words(file_content)} words found in the document""")
    for item in list_of_dict:
        a = item["character"]
        b = item["count"]
        print(f"The '{a}' character was found '{b}' times")
    
    print("--- End report ---")
if __name__ == "__main__":
    main()
