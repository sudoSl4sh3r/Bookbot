def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)
    printReport(path, text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return counter
    
def countChars(text):
    lowered_string = text.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    chars = {char: 0 for char in letters}
    
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
    return chars

def sort_on(dict_item):
    return dict_item["num"]

def sortCharsDict(dict):
    list_of_dict = []
    for key, value in dict.items():
        if key.isalpha():
            list_of_dict.append({"char": key, "num": value})
    list_of_dict.sort(key=sort_on, reverse=True)
    return list_of_dict

def printReport(path, text):
    print(f"=== Report of {path} ===")
    print(f"The book has {countWords(text)} number of words.")
    chars_dict = countChars(text)
    sorted_list = sortCharsDict(chars_dict)
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times.")
    print("=== End of report ===")

main()