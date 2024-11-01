def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    print(text)
    countWords(text)
    countChars(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def countWords(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return print(f"The book has {counter} words.")
    
def countChars(text):
    lowered_string = text.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    chars = {char: 0 for char in letters}
    
    for char in lowered_string:
        if char in chars:
            chars[char] += 1
    return print(f"The book has characters: {chars}.")

main()